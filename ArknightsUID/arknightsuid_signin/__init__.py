import asyncio
import random

from gsuid_core.aps import scheduler
from gsuid_core.bot import Bot
from gsuid_core.gss import gss
from gsuid_core.logger import logger
from gsuid_core.models import Event
from gsuid_core.sv import SV
from gsuid_core.utils.database.api import get_uid

from ..arknightsuid_config.ark_config import ArkConfig
from ..utils.ark_prefix import PREFIX
from ..utils.database.models import ArknightsBind
from .sign import daily_sign, sign_in

SIGN_TIME = ArkConfig.get_config("SignTime").data

sv_sign = SV("森空岛签到")
sv_sign_config = SV("森空岛管理", pm=2)


# 每日零点半执行森空岛签到
@scheduler.scheduled_job("cron", hour=SIGN_TIME[0], minute=SIGN_TIME[1])
async def ark_sign_at_night():
    if ArkConfig.get_config("SchedSignin").data:
        await send_daily_sign()


# 群聊内 签到 功能
@sv_sign.on_fullmatch(f"签到")
async def get_sign_func(bot: Bot, ev: Event):
    await bot.logger.info(f"[ARK签到]QQ号: {ev.user_id}")
    ark_uid = await get_uid(bot, ev, bind_model=ArknightsBind)
    if ark_uid is None:
        return "你还没有绑定UID噢,请使用[ark绑定uid123]完成绑定!"
    await bot.logger.info(f"[ARK签到]UID: {ark_uid}")
    await bot.send(await sign_in(ark_uid))
    return None


@sv_sign_config.on_fullmatch(f"全部重签")
async def recheck(bot: Bot, ev: Event):
    await bot.logger.info("开始执行[ARK全部重签]")
    await bot.send("已开始执行")
    await send_daily_sign()
    await bot.send("执行完成")


async def send_daily_sign():
    logger.info("开始执行[ARK每日全部签到]")
    # 执行签到 并获得推送消息
    result = await daily_sign()
    private_msg_list = result["private_msg_list"]
    group_msg_list = result["group_msg_list"]
    logger.info("[ARK每日全部签到]完成")

    # 执行私聊推送
    for qid in private_msg_list:
        try:
            for bot_id in gss.active_bot:
                for single in private_msg_list[qid]:
                    await gss.active_bot[bot_id].target_send(single["msg"], "direct", qid, single["bot_id"], "", "")
        except Exception as e:
            logger.warning(f"[ARK每日全部签到] QQ {qid} 私聊推送失败!错误信息:{e}")
        await asyncio.sleep(0.5)
    logger.info("[ARK每日全部签到]私聊推送完成")

    # 执行群聊推送
    for gid in group_msg_list:
        # 根据succee数判断是否为简洁推送
        if group_msg_list[gid]["success"] >= 0:
            report = (
                "以下为签到失败报告:{}".format(group_msg_list[gid]["push_message"])
                if group_msg_list[gid]["push_message"] != ""
                else ""
            )
            msg_title = "森空岛今日自动签到已完成!\n本群共签到成功{}人,共签到失败{}人。{}".format(
                group_msg_list[gid]["success"],
                group_msg_list[gid]["failed"],
                report,
            )
        else:
            msg_title = group_msg_list[gid]["push_message"]
        # 发送群消息
        try:
            for bot_id in gss.active_bot:
                await gss.active_bot[bot_id].target_send(
                    msg_title,
                    "group",
                    gid,
                    group_msg_list[gid]["bot_id"],
                    "",
                    "",
                )
        except Exception as e:
            logger.warning(f"[ARK每日全部签到]群 {gid} 推送失败!错误信息:{e}")
        await asyncio.sleep(0.5 + random.randint(1, 3))
    logger.info("[ARK每日全部签到]群聊推送完成")
