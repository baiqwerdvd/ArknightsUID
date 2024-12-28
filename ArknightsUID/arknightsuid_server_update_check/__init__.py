import json
from typing import cast

import aiohttp
from gsuid_core.aps import scheduler
from gsuid_core.bot import Bot
from gsuid_core.data_store import get_res_path
from gsuid_core.logger import logger
from gsuid_core.models import Event
from gsuid_core.subscribe import gs_subscribe
from gsuid_core.sv import SV
from msgspec import Struct, convert

from ..arknightsuid_config import PREFIX

sv_server_check = SV("明日方舟版本更新")
sv_server_check_sub = SV("订阅明日方舟版本更新", pm=3)

task_name_server_check = "订阅明日方舟版本更新"


class VersionModel(Struct):
    clientVersion: str
    resVersion: str


async def check_update() -> tuple[VersionModel, bool, bool]:
    """
    check if there is an update

    Returns:
        tuple[VersionModel, bool, bool]:
            VersionModel: the current version
            bool: if the client version is updated
            bool: if the resource version is updated
    """
    async with aiohttp.ClientSession() as session:
        async with session.get(
            "https://ak-conf.hypergryph.com/config/prod/official/Android/version"
        ) as response:
            data = json.loads(await response.text())
            version = convert(data, VersionModel)

    return_data = [version, False, False]
    version_path = get_res_path("ArknightsUID") / "version.json"

    is_first = False if version_path.exists() else True

    if is_first:
        with open(version_path, "w", encoding="utf-8") as f:
            json.dump(data, f, indent=2)

        logger.info("First time checking version")
        return cast(tuple[VersionModel, bool, bool], tuple(return_data))
    else:
        with open(version_path, encoding="utf-8") as f:
            base_version_json = json.load(f)

    base_version = convert(base_version_json, VersionModel)

    if (
        version.clientVersion != base_version.clientVersion
        or version.resVersion != base_version.resVersion
    ):
        with open(version_path, "w", encoding="utf-8") as f:
            json.dump(data, f, indent=2)

    if version.clientVersion != base_version.clientVersion:
        return_data[1] = True
    if version.resVersion != base_version.resVersion:
        return_data[2] = True

    return cast(tuple[VersionModel, bool, bool], tuple(return_data))


@sv_server_check.on_command("取明日方舟最新版本")
async def get_latest_version(bot: Bot, ev: Event):
    version = await check_update()
    await bot.send(f"当前版本: {version[0].clientVersion}\n资源版本: {version[0].resVersion}")


@sv_server_check_sub.on_fullmatch(f"{PREFIX}订阅版本更新")
async def sub_ann_(bot: Bot, ev: Event):
    if ev.group_id is None:
        return await bot.send("请在群聊中订阅")
    data = await gs_subscribe.get_subscribe(task_name_server_check)
    if data:
        for subscribe in data:
            if subscribe.group_id == ev.group_id:
                return await bot.send("已经订阅了明日方舟版本更新！")

    await gs_subscribe.add_subscribe(
        "session",
        task_name=task_name_server_check,
        event=ev,
        extra_message="",
    )

    logger.info(data)
    await bot.send("成功订阅明日方舟版本更新!")


@scheduler.scheduled_job("interval", seconds=2, id="check update")
async def match_checker():
    logger.info("Checking for Arknights client update")

    version = await check_update()

    datas = await gs_subscribe.get_subscribe(task_name_server_check)
    if not datas:
        logger.info("[明日方舟版本更新] 暂无群订阅")
        return

    for subscribe in datas:
        if version[1]:
            logger.warning("检测到明日方舟客户端版本更新")
            await subscribe.send(
                f"检测到明日方舟客户端版本更新\n当前版本: {version[0].clientVersion}\n资源版本: {version[0].resVersion}",
            )
        elif version[2]:
            logger.warning("检测到明日方舟资源版本更新")
            await subscribe.send(
                f"检测到明日方舟资源版本更新\n当前版本: {version[0].clientVersion}\n资源版本: {version[0].resVersion}",
            )
