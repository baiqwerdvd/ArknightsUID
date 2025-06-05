import asyncio

from gsuid_core.aps import scheduler
from gsuid_core.bot import Bot
from gsuid_core.gss import gss
from gsuid_core.logger import logger
from gsuid_core.models import Event
from gsuid_core.segment import MessageSegment
from gsuid_core.sv import SV

from ..utils.ark_prefix import PREFIX
from .draw_ap_card import get_ap_img
from .notice import get_notice_list

sv_get_ap = SV("ark查询体力")
sv_get_ap_admin = SV("ark强制推送", pm=1)


@sv_get_ap_admin.on_fullmatch((f"强制推送体力提醒"))  # noqa: UP034
async def force_notice_job(bot: Bot, ev: Event):
    await bot.logger.info("开始执行[ark强制推送体力信息]")
    await ark_notice_job()


@scheduler.scheduled_job("cron", minute="*/30")
async def ark_notice_job():
    result = await get_notice_list()
    logger.info("[ark推送检查]完成!等待消息推送中...")
    logger.debug(result)

    # 执行私聊推送
    for bot_id in result:
        for BOT_ID in gss.active_bot:
            bot = gss.active_bot[BOT_ID]
            for user_id in result[bot_id]["direct"]:
                msg = result[bot_id]["direct"][user_id]
                await bot.target_send(msg, "direct", user_id, bot_id, "", "")
                await asyncio.sleep(0.5)
            logger.info("[ark推送检查] 私聊推送完成")
            for gid in result[bot_id]["group"]:
                msg_list = []
                for user_id in result[bot_id]["group"][gid]:
                    msg_list.append(MessageSegment.at(user_id))
                    msg = result[bot_id]["group"][gid][user_id]
                    msg_list.append(MessageSegment.text(msg))
                await bot.target_send(msg_list, "group", gid, bot_id, "", "")
                await asyncio.sleep(0.5)
            logger.info("[ark推送检查] 群聊推送完成")


@sv_get_ap.on_fullmatch(
    (
        f"每日",
        f"mr",
        f"实时便笺",
        f"便笺",
        f"便签",
    )
)
async def send_daily_info_pic(bot: Bot, ev: Event):
    await bot.logger.info("开始执行[ark每日信息]")
    user_id = ev.at if ev.at else ev.user_id
    await bot.logger.info(f"[ark每日信息]QQ号: {user_id}")

    im = await get_ap_img(bot.bot_id, user_id)
    await bot.send(im)
