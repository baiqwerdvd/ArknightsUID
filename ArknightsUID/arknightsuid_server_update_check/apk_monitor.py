import asyncio
import json
import re
import struct
import time
import zlib
from contextlib import asynccontextmanager
from dataclasses import dataclass, field
from enum import Enum
from pathlib import Path

import aiofiles
import aiohttp
from gsuid_core.data_store import get_res_path
from gsuid_core.logger import logger
from gsuid_core.sv import SV

CONFIG = {
    "LATEST_APK_URL": "https://ak.hypergryph.com/downloads/android_lastest",
    "CHECK_INTERVAL": 10,
    "REQUEST_TIMEOUT": 30,
    "RETRY_COUNT": 3,
    "RETRY_DELAY": 5,
    "MAX_TAIL_SIZE": 1024 * 1024,
    "INITIAL_TAIL_SIZE": 1024,
}

EOCD_SIGNATURE = 0x06054B50
CENTRAL_DIR_SIGNATURE = 0x02014B50
LOCAL_FILE_SIGNATURE = 0x04034B50

sv_apk_check = SV("明日方舟APK更新检查")
sv_apk_check_sub = SV("订阅明日方舟APK更新", pm=3)

TASK_NAME_APK_CHECK = "订阅明日方舟APK更新"


class CompressionMethod(Enum):
    """压缩方法枚举"""

    STORED = 0
    DEFLATED = 8
    UNSUPPORTED = -1

    @classmethod
    def from_value(cls, value: int) -> "CompressionMethod":
        for method in cls:
            if method.value == value:
                return method
        return cls.UNSUPPORTED


@dataclass
class ExtractConfig:
    file_patterns: list[str] = field(
        default_factory=lambda: [
            "AndroidManifest.xml",
            "hot_update_list.json",
            "arm64-v8a/libil2cpp.so",
            "global-metadata.dat",
        ]
    )
    chunk_size_mb: int = 10

    @property
    def chunk_size(self) -> int:
        return self.chunk_size_mb * 1024 * 1024


@dataclass
class ApkFileInfo:
    filename: str
    compressed_size: int
    uncompressed_size: int
    compression_method: CompressionMethod

    def size_human_readable(self) -> str:
        return human_readable_size(self.uncompressed_size)

    def compression_ratio(self) -> float:
        if self.uncompressed_size == 0:
            return 0.0
        return 1.0 - (self.compressed_size / self.uncompressed_size)


@dataclass
class ExtractResult:
    """提取结果"""

    extracted_files: list[str] = field(default_factory=list)
    failed_files: list[tuple[str, str]] = field(default_factory=list)  # (filename, error)
    total_time_ms: int = 0
    apk_url: str = ""
    apk_version: str = ""


@dataclass
class VersionInfo:
    version_code: int
    version_name: str
    version_id: str
    manifest_name: str
    manifest_version: str
    il2cpp_size: int
    il2cpp_crc32: int
    global_metadata_size: int
    global_metadata_crc32: int


@dataclass
class ApkUpdateInfo:
    apk_url: str
    version_info: VersionInfo
    update_time: float


class ApkExtractorError(Exception):
    pass


class ZipStructure:
    @dataclass
    class EndOfCentralDir:
        central_dir_size: int
        central_dir_offset: int
        total_entries: int

    @dataclass
    class CentralDirEntry:
        filename: str
        compressed_size: int
        uncompressed_size: int
        local_header_offset: int
        compression_method: CompressionMethod

    @dataclass
    class LocalFileHeader:
        compressed_size: int
        uncompressed_size: int
        filename_length: int
        extra_field_length: int
        compression_method: CompressionMethod


class ApkExtractor:
    def __init__(self, config: ExtractConfig):
        self.config = config
        self.session: aiohttp.ClientSession | None = None
        self.cache_dir = get_res_path("ArknightsUID") / "apk_cache"
        self.cache_dir.mkdir(parents=True, exist_ok=True)
        self.output_dir = get_res_path("ArknightsUID") / "apk_extracted"
        self.output_dir.mkdir(parents=True, exist_ok=True)

    @asynccontextmanager
    async def get_session(self):
        if self.session is None or self.session.closed:
            timeout = aiohttp.ClientTimeout(total=CONFIG["REQUEST_TIMEOUT"])
            self.session = aiohttp.ClientSession(timeout=timeout)
        yield self.session

    async def close(self):
        if self.session and not self.session.closed:
            await self.session.close()

    async def get_latest_apk_url(self) -> str:
        url = CONFIG["LATEST_APK_URL"]
        for attempt in range(CONFIG["RETRY_COUNT"]):
            try:
                async with self.get_session() as session:
                    async with session.get(url, allow_redirects=False) as response:
                        if response.status in (301, 302, 303, 307, 308):
                            location = response.headers.get("Location")
                            if not location:
                                raise ApkExtractorError(f"未获取到第一次Location，状态码: {response.status}")
                        else:
                            raise ApkExtractorError(f"无法获取第一次重定向链接，状态码: {response.status}")

                    async with session.get(location, allow_redirects=False) as response2:
                        if response2.status in (301, 302, 303, 307, 308):
                            final_location = response2.headers.get("Location")
                            if final_location:
                                return final_location
                            else:
                                raise ApkExtractorError(f"未获取到第二次Location，状态码: {response2.status}")
                        else:
                            raise ApkExtractorError(f"无法获取第二次重定向链接，状态码: {response2.status}")

            except Exception as e:
                if attempt == CONFIG["RETRY_COUNT"] - 1:
                    logger.error(f"获取APK下载链接失败: {e}")
                    raise ApkExtractorError(f"获取APK下载链接失败: {e}")
                await asyncio.sleep(CONFIG["RETRY_DELAY"])
        raise ApkExtractorError("获取APK下载链接失败，所有重试均未成功")

    async def get_remote_file_size(self, url: str) -> int:
        async with self.get_session() as session:
            async with session.head(url) as response:
                if not response.ok:
                    raise ApkExtractorError(f"无法获取文件大小，状态码: {response.status}")

                content_length = response.headers.get("content-length")
                if not content_length:
                    logger.error(response.headers)
                    raise ApkExtractorError("响应头中没有content-length")

                return int(content_length)

    async def download_range(self, url: str, start: int, end: int) -> bytes:
        async with self.get_session() as session:
            headers = {"Range": f"bytes={start}-{end}"}
            async with session.get(url, headers=headers) as response:
                if response.status not in (200, 206):
                    raise ApkExtractorError(f"范围下载失败，状态码: {response.status}")
                return await response.read()

    async def find_zip_structure(self, url: str, file_size: int) -> ZipStructure.EndOfCentralDir:
        tail_size = CONFIG["INITIAL_TAIL_SIZE"]
        max_tail_size = min(CONFIG["MAX_TAIL_SIZE"], file_size)

        while tail_size <= max_tail_size:
            tail_start = file_size - tail_size
            tail_data = await self.download_range(url, tail_start, file_size - 1)

            eocd = self._find_eocd(tail_data)
            if eocd:
                if eocd.central_dir_offset >= file_size:
                    raise ApkExtractorError(f"中央目录偏移量 ({eocd.central_dir_offset}) 超出文件大小 ({file_size})")
                return eocd

            tail_size *= 4

        raise ApkExtractorError("未找到ZIP中央目录结束记录")

    def _find_eocd(self, data: bytes) -> ZipStructure.EndOfCentralDir | None:
        """查找中央目录结束记录"""
        if len(data) < 22:
            return None

        for i in range(len(data) - 22, -1, -1):
            if self._read_u32_le(data, i) == EOCD_SIGNATURE:
                comment_length = self._read_u16_le(data, i + 20)
                if i + 22 + comment_length <= len(data):
                    return ZipStructure.EndOfCentralDir(
                        total_entries=self._read_u16_le(data, i + 10),
                        central_dir_size=self._read_u32_le(data, i + 12),
                        central_dir_offset=self._read_u32_le(data, i + 16),
                    )
        return None

    def _read_u32_le(self, data: bytes, offset: int) -> int:
        """读取小端序32位整数"""
        if offset + 4 > len(data):
            return 0
        return struct.unpack("<I", data[offset : offset + 4])[0]

    def _read_u16_le(self, data: bytes, offset: int) -> int:
        """读取小端序16位整数"""
        if offset + 2 > len(data):
            return 0
        return struct.unpack("<H", data[offset : offset + 2])[0]

    def _parse_central_dir_entries(self, data: bytes) -> list[ZipStructure.CentralDirEntry]:
        """解析中央目录条目"""
        entries = []
        offset = 0

        while offset + 46 <= len(data):
            if self._read_u32_le(data, offset) != CENTRAL_DIR_SIGNATURE:
                break

            filename_length = self._read_u16_le(data, offset + 28)
            extra_field_length = self._read_u16_le(data, offset + 30)
            comment_length = self._read_u16_le(data, offset + 32)

            total_length = 46 + filename_length + extra_field_length + comment_length
            if offset + total_length > len(data):
                break

            filename = data[offset + 46 : offset + 46 + filename_length].decode("utf-8", errors="ignore")

            entries.append(
                ZipStructure.CentralDirEntry(
                    filename=filename,
                    compression_method=CompressionMethod.from_value(self._read_u16_le(data, offset + 10)),
                    compressed_size=self._read_u32_le(data, offset + 20),
                    uncompressed_size=self._read_u32_le(data, offset + 24),
                    local_header_offset=self._read_u32_le(data, offset + 42),
                )
            )

            offset += total_length

        return entries

    def _parse_local_file_header(self, data: bytes) -> ZipStructure.LocalFileHeader | None:
        """解析本地文件头"""
        if len(data) < 30 or self._read_u32_le(data, 0) != LOCAL_FILE_SIGNATURE:
            return None

        return ZipStructure.LocalFileHeader(
            compression_method=CompressionMethod.from_value(self._read_u16_le(data, 8)),
            compressed_size=self._read_u32_le(data, 18),
            uncompressed_size=self._read_u32_le(data, 22),
            filename_length=self._read_u16_le(data, 26),
            extra_field_length=self._read_u16_le(data, 28),
        )

    def _matches_pattern(self, filename: str) -> bool:
        """检查文件名是否匹配模式"""
        for pattern in self.config.file_patterns:
            if pattern in filename or filename.endswith(pattern):
                return True
        return False

    def _decompress_data(self, data: bytes, method: CompressionMethod) -> bytes:
        """解压缩数据"""
        if method == CompressionMethod.STORED:
            return data
        elif method == CompressionMethod.DEFLATED:
            return zlib.decompress(data, -zlib.MAX_WBITS)
        else:
            raise ApkExtractorError(f"不支持的压缩方法: {method}")

    async def extract_from_url(self, url: str) -> ExtractResult:
        start_time = time.time()

        file_size = await self.get_remote_file_size(url)
        logger.info(f"APK文件大小: {human_readable_size(file_size)}")

        eocd = await self.find_zip_structure(url, file_size)
        logger.info(f"找到{eocd.total_entries}个文件条目")

        central_dir_data = await self.download_range(
            url, eocd.central_dir_offset, eocd.central_dir_offset + eocd.central_dir_size - 1
        )

        entries = self._parse_central_dir_entries(central_dir_data)

        matched_entries = [entry for entry in entries if self._matches_pattern(entry.filename)]

        if not matched_entries:
            logger.warning(f"未找到匹配的文件: {self.config.file_patterns}")
            return ExtractResult(total_time_ms=int((time.time() - start_time) * 1000), apk_url=url)

        logger.info(f"找到{len(matched_entries)}个匹配的文件")

        extracted_files = []
        failed_files = []

        for entry in matched_entries:
            try:
                filename = await self._download_single_file(url, entry)
                extracted_files.append(filename)
                logger.info(f"成功提取: {filename}")
            except Exception as e:
                failed_files.append((entry.filename, str(e)))
                logger.error(f"提取失败 {entry.filename}: {e}")

        total_time_ms = int((time.time() - start_time) * 1000)

        return ExtractResult(
            extracted_files=extracted_files, failed_files=failed_files, total_time_ms=total_time_ms, apk_url=url
        )

    async def _download_single_file(self, url: str, entry: ZipStructure.CentralDirEntry) -> str:
        header_data = await self.download_range(url, entry.local_header_offset, entry.local_header_offset + 64)

        local_header = self._parse_local_file_header(header_data)
        if not local_header:
            raise ApkExtractorError("无法解析本地文件头")

        data_offset = entry.local_header_offset + 30 + local_header.filename_length + local_header.extra_field_length

        data_size = entry.compressed_size
        downloaded = 0
        file_data = b""

        while downloaded < data_size:
            chunk_size = min(self.config.chunk_size, data_size - downloaded)
            chunk_start = data_offset + downloaded
            chunk_end = chunk_start + chunk_size - 1

            chunk_data = await self.download_range(url, chunk_start, chunk_end)
            file_data += chunk_data
            downloaded += chunk_size

        decompressed_data = self._decompress_data(file_data, local_header.compression_method)

        output_filename = Path(entry.filename).name
        output_path = Path(self.output_dir) / output_filename
        logger.info(f"保存提取的文件: {output_path}")

        output_path = self.output_dir / output_filename

        async with aiofiles.open(output_path, "wb") as f:
            await f.write(decompressed_data)

        return output_filename


class ApkMonitor:
    """APK监控器"""

    def __init__(self):
        self.config = ExtractConfig()
        self.extractor = ApkExtractor(self.config)
        self.cache_file = get_res_path("ArknightsUID") / "apk_update_cache.json"
        self.last_update_info: ApkUpdateInfo | None = None
        self.output_dir = get_res_path("ArknightsUID") / "apk_extracted"

    async def check_and_extract_apk(self) -> tuple[ApkUpdateInfo | None, bool]:
        """检查并提取APK信息"""
        try:
            apk_url = await self.extractor.get_latest_apk_url()

            cached_info = await self._load_cache()
            if cached_info and [info for info in cached_info if getattr(info, "apk_url", None) == apk_url]:
                logger.info("APK URL未变化，跳过检查")
                return max(
                    cached_info, key=lambda info: getattr(getattr(info, "version_info", None), "version_code", 0)
                ), False

            logger.info(f"检测到新的APK: {apk_url}")

            result = await self.extractor.extract_from_url(apk_url)

            if not result.extracted_files:
                logger.warning("未能提取到任何文件")
                return None, False

            update_info = await self._parse_extracted_files(result, apk_url)

            if not cached_info:
                cached_info = []
                cached_info.append(update_info)
            else:
                if not any(info.apk_url == apk_url for info in cached_info):
                    cached_info.append(update_info)
            await self._save_cache(cached_info)

            self.last_update_info = update_info
            return update_info, True

        except Exception as e:
            logger.error(f"检查APK更新失败: {e}")
            return None, False

    async def _parse_extracted_files(self, result: ExtractResult, apk_url: str) -> ApkUpdateInfo:
        """解析提取的文件"""
        version_info = VersionInfo(
            version_code=0,
            version_name="",
            version_id="",
            manifest_name="",
            manifest_version="",
            il2cpp_size=0,
            il2cpp_crc32=0,
            global_metadata_size=0,
            global_metadata_crc32=0,
        )
        hot_update_info = {}

        manifest_path = self.output_dir / "AndroidManifest.xml"
        if manifest_path.exists():
            try:
                from pyaxmlparser.axmlprinter import AXMLPrinter

                manifest_data = await self._read_file_async(manifest_path)
                xml_data = AXMLPrinter(manifest_data).get_xml(pretty=False)
                if isinstance(xml_data, bytes):
                    xml_data = xml_data.decode("utf-8", errors="ignore")

                version_name = re.search(r'android:versionName="([^"]+)"', xml_data)
                if version_name:
                    version_info.version_name = version_name.group(1)

                version_code = re.search(r'android:versionCode="(\d+)"', xml_data)
                if version_code:
                    version_info.version_code = int(version_code.group(1))
            except Exception as e:
                logger.error(f"解析AndroidManifest.xml失败: {e}")
        manifest_path.unlink(missing_ok=True)

        hot_update_path = self.output_dir / "hot_update_list.json"
        if hot_update_path.exists():
            try:
                hot_update_data = await self._read_file_async(hot_update_path)
                hot_update_info = json.loads(hot_update_data.decode("utf-8"))

                versionId = hot_update_info.get("versionId")
                manifestName = hot_update_info.get("manifestName")
                manifestVersion = hot_update_info.get("manifestVersion")

                version_info.version_id = versionId
                version_info.manifest_name = manifestName
                version_info.manifest_version = manifestVersion
            except Exception as e:
                logger.error(f"解析hot_update_list.json失败: {e}")
        hot_update_path.unlink(missing_ok=True)

        libil2cpp_path = self.output_dir / "libil2cpp.so"
        if libil2cpp_path.exists():
            try:
                libil2cpp_data = await self._read_file_async(libil2cpp_path)
                libil2cpp_size = Path(libil2cpp_path).stat().st_size
                libil2cpp_crc32 = zlib.crc32(libil2cpp_data)

                version_info.il2cpp_size = libil2cpp_size
                version_info.il2cpp_crc32 = libil2cpp_crc32
            except Exception as e:
                logger.error(f"解析libil2cpp.so失败: {e}")
        libil2cpp_path.unlink(missing_ok=True)

        global_metadata_path = self.output_dir / "global-metadata.dat"
        if global_metadata_path.exists():
            try:
                global_metadata_data = await self._read_file_async(global_metadata_path)
                global_metadata_size = Path(global_metadata_path).stat().st_size
                global_metadata_crc32 = zlib.crc32(global_metadata_data)

                version_info.global_metadata_size = global_metadata_size
                version_info.global_metadata_crc32 = global_metadata_crc32
            except Exception as e:
                logger.error(f"解析global-metadata.dat失败: {e}")
        global_metadata_path.unlink(missing_ok=True)

        return ApkUpdateInfo(
            apk_url=apk_url,
            version_info=version_info,
            update_time=time.time(),
        )

    async def _read_file_async(self, file_path: Path) -> bytes:
        async with aiofiles.open(file_path, "rb") as f:
            return await f.read()

    async def _load_cache(self) -> list[ApkUpdateInfo] | None:
        try:
            if not self.cache_file.exists():
                return None

            async with aiofiles.open(self.cache_file, encoding="utf-8") as f:
                data = json.loads(await f.read())
                return [ApkUpdateInfo(**item) for item in data]
        except Exception as e:
            logger.error(f"加载缓存失败: {e}")
            return None

    async def _save_cache(self, info: list[ApkUpdateInfo]):
        from dataclasses import asdict

        try:
            async with aiofiles.open(self.cache_file, "w", encoding="utf-8") as f:
                await f.write(json.dumps([asdict(item) for item in info], indent=2, ensure_ascii=False))

        except Exception as e:
            logger.error(f"保存缓存失败: {e}")

    async def close(self):
        await self.extractor.close()


def human_readable_size(size: int) -> str:
    if size < 0:
        return f"{size} bytes"

    units = ["bytes", "KB", "MB", "GB"]
    f_size = float(size)

    for unit in units:
        if f_size < 1024.0:
            return f"{f_size:.2f} {unit}"
        f_size /= 1024.0

    return f"{f_size:.2f} TB"


apk_monitor = ApkMonitor()
