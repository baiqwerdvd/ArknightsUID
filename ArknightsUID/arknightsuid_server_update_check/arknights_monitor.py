import asyncio
import json
from contextlib import asynccontextmanager
from dataclasses import dataclass
from pathlib import Path
from typing import Any

import aiohttp
from gsuid_core.data_store import get_res_path
from gsuid_core.logger import logger
from msgspec import Struct, convert

CONFIG = {
    "VERSION_URL": "https://ak-conf.hypergryph.com/config/prod/official/Android/version",
    "SERVER_STATUS_URL": "https://ak-webview.hypergryph.com/api/gate/meta/Android",
    "CHECK_INTERVAL": 5,
    "REQUEST_TIMEOUT": 10,
    "RETRY_COUNT": 3,
    "RETRY_DELAY": 5,
}

SERVER_STATUS_MAP = {
    1: "Under Maintenance",
    2: "Active",
}


class VersionModel(Struct):
    clientVersion: str
    resVersion: str


@dataclass
class UpdateCheckResult:
    version: VersionModel
    old_version: VersionModel | None
    client_updated: bool
    res_updated: bool


@dataclass
class ServerStatusResult:
    current_status: int
    previous_status: int | None
    status_changed: bool


class ArknightsMonitor:
    def __init__(self):
        self.version_path = get_res_path("ArknightsUID") / "version.json"
        self.status_path = get_res_path("ArknightsUID") / "server_status.json"
        self.session: aiohttp.ClientSession | None = None

    @asynccontextmanager
    async def get_session(self):
        if self.session is None or self.session.closed:
            timeout = aiohttp.ClientTimeout(total=CONFIG["REQUEST_TIMEOUT"])
            self.session = aiohttp.ClientSession(timeout=timeout)
        yield self.session

    async def close(self):
        if self.session and not self.session.closed:
            await self.session.close()

    async def _make_request_with_retry(self, url: str) -> dict[str, Any]:
        for attempt in range(CONFIG["RETRY_COUNT"]):
            try:
                async with self.get_session() as session:
                    async with session.get(url) as response:
                        response.raise_for_status()
                        return json.loads(await response.text())
            except (TimeoutError, aiohttp.ClientError, json.JSONDecodeError) as e:
                if attempt == CONFIG["RETRY_COUNT"] - 1:
                    logger.error(f"请求失败，已重试{CONFIG['RETRY_COUNT']}次: {url}, 错误: {e}")
                    raise
                logger.warning(
                    f"请求失败，{CONFIG['RETRY_DELAY']}秒后重试 ({attempt + 1}/{CONFIG['RETRY_COUNT']}): {e}"
                )
                await asyncio.sleep(CONFIG["RETRY_DELAY"])
        raise RuntimeError("请求失败，所有重试均未成功")

    def _save_json_data(self, file_path: Path, data: dict[str, Any]) -> None:
        try:
            file_path.parent.mkdir(parents=True, exist_ok=True)
            with file_path.open("w", encoding="utf-8") as f:
                json.dump(data, f, indent=2, ensure_ascii=False)
        except Exception as e:
            logger.error(f"保存文件失败: {file_path}, 错误: {e}")
            raise

    def _load_json_data(self, file_path: Path) -> dict[str, Any] | None:
        try:
            if not file_path.exists():
                return None
            with file_path.open("r", encoding="utf-8") as f:
                return json.load(f)
        except Exception as e:
            logger.error(f"加载文件失败: {file_path}, 错误: {e}")
            return None

    async def check_version_update(self) -> UpdateCheckResult:
        try:
            data = await self._make_request_with_retry(CONFIG["VERSION_URL"])
            current_version = convert(data, VersionModel)

            old_data = self._load_json_data(self.version_path)
            if old_data is None:
                self._save_json_data(self.version_path, data)
                logger.info("首次检查版本")
                return UpdateCheckResult(
                    version=current_version, old_version=None, client_updated=False, res_updated=False
                )

            old_version = convert(old_data, VersionModel)

            client_updated = current_version.clientVersion != old_version.clientVersion
            res_updated = current_version.resVersion != old_version.resVersion

            if client_updated or res_updated:
                self._save_json_data(self.version_path, data)
                logger.info(f"版本更新: 客户端{'✓' if client_updated else '✗'}, 资源{'✓' if res_updated else '✗'}")

            return UpdateCheckResult(
                version=current_version, old_version=old_version, client_updated=client_updated, res_updated=res_updated
            )

        except Exception as e:
            logger.error(f"检查版本更新失败: {e}")
            raise

    async def check_server_status(self) -> ServerStatusResult:
        try:
            data = await self._make_request_with_retry(CONFIG["SERVER_STATUS_URL"])
            current_status = data.get("preAnnounceType", 2)

            old_data = self._load_json_data(self.status_path)
            if old_data is None:
                self._save_json_data(self.status_path, data)
                logger.info("首次检查服务器状态")
                return ServerStatusResult(current_status=current_status, previous_status=None, status_changed=False)

            previous_status = old_data.get("preAnnounceType", 2)
            status_changed = current_status != previous_status

            if status_changed:
                self._save_json_data(self.status_path, data)
                logger.info(f"服务器状态变更: {previous_status} -> {current_status}")

            return ServerStatusResult(
                current_status=current_status, previous_status=previous_status, status_changed=status_changed
            )

        except Exception as e:
            logger.error(f"检查服务器状态失败: {e}")
            raise

    def get_status_text(self, status_code: int) -> str:
        """获取状态文本"""
        return SERVER_STATUS_MAP.get(status_code, f"Unknown(preAnnounceType: {status_code})")


ark_monitor = ArknightsMonitor()
