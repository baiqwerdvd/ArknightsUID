from typing import Dict

from gsuid_core.gss import gss
from gsuid_core.logger import logger

from ..arknightsuid_config.ark_config import ArkConfig
from ..utils.ark_api import ark_skd_api
from ..utils.database.models import ArknightsPush, ArknightsUser
from ..utils.models.skland.models import ArknightsPlayerInfoModel
from .utils import now_ap

MR_NOTICE = "\n可发送[arkmr]或者[ark每日]来查看更多信息!\n"

NOTICE = {
    "ap": f"你的理智快满啦!{MR_NOTICE}",
    "training": f"你的专精即将可收取!{MR_NOTICE}",
}


async def get_notice_list() -> Dict[str, Dict[str, Dict]]:
    msg_dict: Dict[str, Dict[str, Dict]] = {}
    for _bot_id in gss.active_bot:
        user_list = await ArknightsUser.get_all_push_user_list()
        for user in user_list:
            if user.uid is not None:
                raw_data = await ark_skd_api.get_game_player_info(user.uid)
                if isinstance(raw_data, int):
                    logger.error(f"[ark推送提醒]获取{user.uid}的数据失败!")
                    continue
                push_data = await ArknightsPush.select_push_data(user.uid)
                msg_dict = await all_check(
                    user.bot_id,
                    raw_data,
                    push_data.__dict__,
                    msg_dict,
                    user.user_id,
                    user.uid,
                )
    return msg_dict


async def all_check(
    bot_id: str,
    raw_data: ArknightsPlayerInfoModel,
    push_data: Dict,
    msg_dict: Dict[str, Dict[str, Dict]],
    user_id: str,
    uid: str,
) -> Dict[str, Dict[str, Dict]]:
    for mode in NOTICE.keys():
        # 检查条件
        if push_data[f"{mode}_is_push"] is True:
            if ArkConfig.get_config("CrazyNotice").data:
                if not await check(mode, raw_data, push_data[f"{mode}_value"]):
                    await ArknightsPush.update_push_data(
                        uid,
                        {f"{mode}_is_push": False},
                    )
                continue
        # 准备推送
        if await check(mode, raw_data, push_data[f"{mode}_value"]):
            if push_data[f"{mode}_push"] is False:
                pass
            # on 推送到私聊
            else:
                # 初始化
                if bot_id not in msg_dict:
                    msg_dict[bot_id] = {"direct": {}, "group": {}}

                if push_data[f"{mode}_push"] is True:
                    # 添加私聊信息
                    if user_id not in msg_dict[bot_id]["direct"]:
                        msg_dict[bot_id]["direct"][user_id] = NOTICE[mode]
                    else:
                        msg_dict[bot_id]["direct"][user_id] += NOTICE[mode]
                    await ArknightsPush.update_push_data(uid, {f"{mode}_is_push": True})
                # 群号推送到群聊
                else:
                    # 初始化
                    gid = push_data[f"{mode}_push"]
                    if gid not in msg_dict[bot_id]["group"]:
                        msg_dict[bot_id]["group"][gid] = {}

                    if user_id not in msg_dict[bot_id]["group"][gid]:
                        msg_dict[bot_id]["group"][gid][user_id] = NOTICE[mode]
                    else:
                        msg_dict[bot_id]["group"][gid][user_id] += NOTICE[mode]
                    await ArknightsPush.update_push_data(uid, {f"{mode}_is_push": True})
    return msg_dict


async def check(mode: str, data: ArknightsPlayerInfoModel, limit: int) -> bool:
    if mode == "ap":
        current_ap = now_ap(data.status.ap)
        if current_ap >= limit:
            return True
        elif current_ap >= data.status.ap.max:
            return True
        else:
            return False
    if mode == "training":
        if data.building.training:
            remain_secs = data.building.training.remainSecs
            if remain_secs <= limit * 60:
                return True
            else:
                return True
    return False
