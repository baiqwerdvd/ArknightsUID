import asyncio
import os
from pathlib import Path

from aiohttp.client import ClientSession
from gsuid_core.logger import logger
from msgspec import json as msgjson

from .download_url import download_file
from .RESOURCE_PATH import RESOURCE_PATH

with open(
    Path(__file__).parent / 'resource_map.json', encoding='UTF-8'
) as f:
    resource_map = msgjson.decode(
        f.read(),
        type=dict[str, dict[str, dict[str, dict[str, int | str]]]],
    )


async def download_all_file_from_cos():
    async def _download(tasks: list[asyncio.Task]):
        failed_list.extend(
            list(filter(lambda x: x is not None, await asyncio.gather(*tasks)))
        )
        tasks.clear()
        logger.info('[cos]下载完成!')

    failed_list: list[tuple[str, str, str, str]] = []
    TASKS = []
    async with ClientSession() as sess:
        for res_type in ['resource']:
            logger.info('[cos]开始下载资源文件...')
            resource_type_list = [
                'character',
                'character_portrait',
                'character_preview',
                'consumable',
                'element',
                'light_cone',
                'relic',
                'skill',
            ]
            for resource_type in resource_type_list:
                file_dict = resource_map[res_type][resource_type]
                logger.info(
                    f'[cos]数据库[{resource_type}]中存在{len(file_dict)}个内容!'
                )
                temp_num = 0
                for file_name, file_info in file_dict.items():
                    name = file_name
                    size = file_info['size']
                    url = file_info['url']
                    if isinstance(url, int):
                        continue
                    path = Path(RESOURCE_PATH / resource_type / name)
                    if path.exists():
                        is_diff = size == os.stat(path).st_size
                    else:
                        is_diff = True
                    if (
                        not path.exists()
                        or not os.stat(path).st_size
                        or not is_diff
                    ):
                        logger.info(f'[cos]开始下载[{resource_type}]_[{name}]...')
                        temp_num += 1
                        TASKS.append(
                            asyncio.wait_for(
                                download_file(
                                    url, res_type, resource_type, name, sess
                                ),
                                timeout=60,
                            )
                        )
                        # await download_file(url, FILE_TO_PATH[file], name)
                        if len(TASKS) >= 10:
                            await _download(TASKS)
                else:
                    await _download(TASKS)
                if temp_num == 0:
                    im = f'[cos]数据库[{resource_type}]无需下载!'
                else:
                    im = f'[cos]数据库[{resource_type}]已下载{temp_num}个内容!'
                temp_num = 0
                logger.info(im)
    if failed_list:
        logger.info(f'[cos]开始重新下载失败的{len(failed_list)}个文件...')
        for url, res_type, resource_type, name in failed_list:
            TASKS.append(
                asyncio.wait_for(
                    download_file(url, res_type, resource_type, name, sess),
                    timeout=60,
                )
            )
            if len(TASKS) >= 10:
                await _download(TASKS)
        else:
            await _download(TASKS)
        if count := len(failed_list):
            logger.error(f'[cos]仍有{count}个文件未下载，请使用命令 `下载全部资源` 重新下载')
