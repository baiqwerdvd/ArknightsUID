import json
from pathlib import Path
from typing import cast

import aiohttp
from gsuid_core.data_store import get_res_path
from gsuid_core.logger import logger
from msgspec import convert
from msgspec import json as msgjson

from .model import BulletinData, BulletinMeta, BulletinTargetData, BulletinTargetDataItem


def read_json(file_path: Path) -> dict[str, object]:
    try:
        with Path.open(file_path, encoding="UTF-8") as file:
            return cast(dict[str, object], json.load(file))
    except FileNotFoundError as _:
        raise FileNotFoundError(f"Error reading JSON file: {file_path}")
    except json.JSONDecodeError as e:
        raise e


def write_json(data: object, file_path: Path) -> None:
    try:
        with Path.open(file_path, mode="w", encoding="UTF-8") as file:
            json.dump(data, file, sort_keys=False, indent=4, ensure_ascii=False)
    except FileNotFoundError as e:
        raise e


async def get_image(url: str) -> bytes:
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            return await response.read()


async def get_announcement(cid: str) -> BulletinData:
    url = f"https://ak-webview.hypergryph.com/api/game/bulletin/{cid}"
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            data = await response.json()
    data = convert(data.get("data", {}), BulletinData)
    return data


async def check_bulletin_update() -> dict[str, BulletinData]:
    bulletin_path = get_res_path(["ArknightsUID", "announce"]) / "bulletin.meta.json"
    logger.info("Checking for game bulletin...")

    bulletin_meta = convert(read_json(bulletin_path), BulletinMeta)

    android_data = None
    bilibili_data = None
    ios_data = None

    async with aiohttp.ClientSession() as session:
        for target in ["Android", "Bilibili", "IOS"]:
            async with session.get(
                f"https://ak-webview.hypergryph.com/api/game/bulletinList?target={target}"
            ) as response:
                cur_meta = await response.json()
                if cur_meta.get("code") == 0:
                    match target:
                        case "Android":
                            android_data = convert(cur_meta.get("data", {}), BulletinTargetData)
                            bulletin_meta.target.Android = android_data
                        case "Bilibili":
                            bilibili_data = convert(cur_meta.get("data", {}), BulletinTargetData)
                            bulletin_meta.target.Bilibili = bilibili_data
                        case "IOS":
                            ios_data = convert(cur_meta.get("data", {}), BulletinTargetData)
                            bulletin_meta.target.IOS = ios_data
        logger.info("The file 'bulletin.meta.json' has been successfully updated.")

    assert android_data is not None
    assert bilibili_data is not None
    assert ios_data is not None

    update_list = android_data.list_ + bilibili_data.list_ + ios_data.list_

    update_set: set[int] = set()
    update_list: list[BulletinTargetDataItem] = [
        x
        for x in update_list
        if x.updatedAt not in update_set and not update_set.add(x.updatedAt)
    ]
    update_list.sort(key=lambda x: x.updatedAt, reverse=True)

    new_ann: dict[str, BulletinData] = {}

    for item in update_list:
        for key, value in bulletin_meta.update.items():
            if value.cid == item.cid and value.updatedAt == item.updatedAt:
                break
            elif value.cid == item.cid and value.updatedAt != item.updatedAt:
                bulletin_meta.update.pop(key)
                if "_" in key:
                    new_key = f"{item.cid}_{int(key.split('_')[1]) + 1}"
                else:
                    new_key = f"{item.cid}_1"
                ann = await get_announcement(item.cid)
                bulletin_meta.update[new_key] = ann
                new_ann[item.cid] = ann
                logger.info(f"Bumped bulletin found: {item.cid}:{item.title}")
                break
            elif value.cid != item.cid:
                continue

        if item.cid not in bulletin_meta.data:
            ann = await get_announcement(item.cid)
            bulletin_meta.data[item.cid] = ann
            new_ann[item.cid] = ann
            logger.info(f"New bulletin found: {item.cid}:{item.title}")

    bulletin_meta.data = dict(sorted(bulletin_meta.data.items(), key=lambda x: int(x[0])))
    bulletin_meta.update = dict(
        sorted(bulletin_meta.update.items(), key=lambda x: x[1].cid, reverse=False)
    )

    data = msgjson.decode(msgjson.encode(bulletin_meta))
    write_json(data, bulletin_path)

    return new_ann