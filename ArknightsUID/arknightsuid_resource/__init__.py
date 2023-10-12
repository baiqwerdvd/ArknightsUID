from pathlib import Path

from gsuid_core.bot import Bot
from gsuid_core.data_store import get_res_path
from gsuid_core.logger import logger
from gsuid_core.models import Event
from gsuid_core.sv import SV

from ..utils.resource.download_from_cos import check_use
from .constants import Excel
from .memoryStore import store

sv_download_config = SV("下载资源", pm=2)


@sv_download_config.on_fullmatch(("ark下载全部资源"))  # noqa: UP034
async def send_download_resource_msg(bot: Bot, ev: Event):
    await bot.send("正在开始下载~可能需要较久的时间!")
    im = await check_use()
    await bot.send(im)


async def startup():
    logger.info("[资源文件下载] 正在检查与下载缺失的资源文件, 可能需要较长时间, 请稍等")
    await check_use()
    logger.info("[资源文件下载] 检查完毕, 正在加载 gamedata")

    for file_path in Path(
        get_res_path(["ArknightsUID", "resource", "gamedata"])
    ).rglob("*.json"):
        await store.get_file(file_path)

    await Excel.preload_table()
