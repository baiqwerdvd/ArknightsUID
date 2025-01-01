import asyncio
import json
import random

import aiohttp
from msgspec import Struct, convert

from gsuid_core.aps import scheduler
from gsuid_core.bot import Bot
from gsuid_core.data_store import get_res_path
from gsuid_core.logger import logger
from gsuid_core.models import Event
from gsuid_core.subscribe import gs_subscribe
from gsuid_core.sv import SV

from ..arknightsuid_config import PREFIX

sv_server_check = SV("明日方舟版本更新")
sv_server_check_sub = SV("订阅明日方舟版本更新", pm=3)

task_name_server_check = "订阅明日方舟版本更新"


class VersionModel(Struct):
    clientVersion: str
    resVersion: str


class UpdateCheckResult(Struct):
    version: VersionModel
    old_version: VersionModel | None
    client_updated: bool
    res_updated: bool


async def check_update() -> UpdateCheckResult:
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

    version_path = get_res_path("ArknightsUID") / "version.json"

    is_first = False if version_path.exists() else True
    if is_first:
        with open(version_path, "w", encoding="utf-8") as f:
            json.dump(data, f, indent=2)

        logger.info("First time checking version")
        return UpdateCheckResult(
            version=version, old_version=None, client_updated=False, res_updated=False
        )
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

    result = UpdateCheckResult(
        version=version,
        old_version=base_version,
        client_updated=False,
        res_updated=False,
    )

    if version.clientVersion != base_version.clientVersion:
        result.client_updated = True
    if version.resVersion != base_version.resVersion:
        result.res_updated = True

    return result


@sv_server_check.on_command("取明日方舟最新版本")
async def get_latest_version(bot: Bot, ev: Event):
    result = await check_update()
    await bot.send(
        f"clientVersion: {result.version.clientVersion}\nresVersion: {result.version.resVersion}"
    )


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


@scheduler.scheduled_job("interval", minutes=10, id="check update")
async def match_checker():
    logger.trace("Checking for Arknights client update")

    result = await check_update()
    if not result.res_updated and not result.client_updated:
        logger.trace("No update found")
        return

    datas = await gs_subscribe.get_subscribe(task_name_server_check)
    if not datas:
        logger.info("[明日方舟版本更新] 暂无群订阅")
        return

    for subscribe in datas:
        if result.client_updated:
            logger.warning("检测到明日方舟客户端版本更新")
            if result.old_version is None:
                await subscribe.send(
                    f"检测到明日方舟客户端版本更新\nclientVersion: {result.version.clientVersion}\nresVersion: {result.version.resVersion}",
                )
            else:
                await subscribe.send(
                    f"检测到明日方舟客户端版本更新\nclientVersion: {result.old_version.clientVersion} -> {result.version.clientVersion}\nresVersion: {result.old_version.resVersion} -> {result.version.resVersion}",
                )
            await asyncio.sleep(random.uniform(1, 3))
        elif result.res_updated:
            logger.warning("检测到明日方舟资源版本更新")
            if result.old_version is None:
                await subscribe.send(
                    f"检测到明日方舟资源版本更新\nclientVersion: {result.version.clientVersion}\nresVersion: {result.version.resVersion}",
                )
            else:
                await subscribe.send(
                    f"检测到明日方舟资源版本更新\nclientVersion: {result.version.clientVersion}\nresVersion: {result.old_version.resVersion} -> {result.version.resVersion}",
                )
            await asyncio.sleep(random.uniform(1, 3))
