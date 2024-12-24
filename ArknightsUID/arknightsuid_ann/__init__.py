import asyncio
import random

from gsuid_core.aps import scheduler
from gsuid_core.bot import Bot
from gsuid_core.data_store import get_res_path
from gsuid_core.logger import logger
from gsuid_core.models import Event
from gsuid_core.segment import MessageSegment
from gsuid_core.subscribe import gs_subscribe
from gsuid_core.sv import SV
from msgspec import json as msgjson

from ..arknightsuid_config import PREFIX, ArkConfig
from .draw_img import get_ann_img
from .get_data import check_bulletin_update, get_announcement, write_json
from .model import BulletinMeta

sv_ann = SV("明日方舟公告")
sv_ann_sub = SV("订阅明日方舟公告", pm=3)

task_name_ann = "订阅明日方舟公告"
ann_minute_check: int = ArkConfig.get_config("AnnMinuteCheck").data


@sv_ann.on_command(f"{PREFIX}公告")
async def ann_(bot: Bot, ev: Event):
    cid = ev.text

    if not cid.isdigit():
        raise Exception("公告ID不正确")

    data = await get_announcement(cid)
    img = await get_ann_img(data)
    msg = [MessageSegment.text(f"[明日方舟公告] {data.title}\n"), MessageSegment.image(img)]
    await bot.send(msg)


@sv_ann_sub.on_fullmatch(f"{PREFIX}订阅公告")
async def sub_ann_(bot: Bot, ev: Event):
    if ev.group_id is None:
        return await bot.send("请在群聊中订阅")
    data = await gs_subscribe.get_subscribe(task_name_ann)
    if data:
        for subscribe in data:
            if subscribe.group_id == ev.group_id:
                return await bot.send("已经订阅了明日方舟公告！")

    await gs_subscribe.add_subscribe(
        "session",
        task_name=task_name_ann,
        event=ev,
        extra_message="",
    )

    logger.info(data)
    await bot.send("成功订阅明日方舟公告!")


@sv_ann_sub.on_fullmatch((f"{PREFIX}取消订阅公告", f"{PREFIX}取消公告", f"{PREFIX}退订公告"))
async def unsub_ann_(bot: Bot, ev: Event):
    if ev.group_id is None:
        return await bot.send("请在群聊中取消订阅")

    data = await gs_subscribe.get_subscribe(task_name_ann)
    if data:
        for subscribe in data:
            if subscribe.group_id == ev.group_id:
                await gs_subscribe.delete_subscribe("session", task_name_ann, ev)
                return await bot.send("成功取消订阅明日方舟公告!")

    return await bot.send("未曾订阅明日方舟公告！")


@scheduler.scheduled_job("interval", minutes=ann_minute_check)
async def check_ark_ann():
    await check_ark_ann_state()


async def check_ark_ann_state():
    logger.info("[明日方舟公告] 定时任务: 明日方舟公告查询..")

    bulletin_path = get_res_path(["ArknightsUID", "announce"]) / "bulletin.meta.json"
    logger.info("Checking for game bulletin...")

    if not bulletin_path.exists():
        data = msgjson.encode(BulletinMeta())
        write_json(data, bulletin_path)
        logger.info("[明日方舟公告] 初始成功, 将在下个轮询中更新.")
        return

    updates = await check_bulletin_update()

    datas = await gs_subscribe.get_subscribe(task_name_ann)
    if not datas:
        logger.info("[明日方舟公告] 暂无群订阅")
        return

    if len(updates) == 0:
        logger.info("[明日方舟公告] 没有最新公告")
        return

    for data in updates.values():
        try:
            img = await get_ann_img(data)
            msg = [
                MessageSegment.text(f"[明日方舟公告] {data.title}\n"),
                MessageSegment.image(img),
            ]

            if isinstance(img, str):
                continue
            for subscribe in datas:
                await subscribe.send(msg)
                await asyncio.sleep(random.uniform(1, 3))
        except Exception as e:
            logger.exception(e)

    logger.info("[明日方舟公告] 推送完毕")
