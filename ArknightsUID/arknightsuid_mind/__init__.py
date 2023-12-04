# import asyncio
# import json
# from typing import Dict

# import aiohttp
# from gsuid_core.aps import scheduler
# from gsuid_core.bot import Bot
# from gsuid_core.gss import gss
# from gsuid_core.logger import logger
# from gsuid_core.models import Event
# from gsuid_core.segment import MessageSegment
# from gsuid_core.sv import SV
# from msgspec import Struct, convert

# from ..utils.ark_prefix import PREFIX
# from ..utils.database.models import (
#     ArknightsPush,
#     ArknightsUser,
# )
# from ..version import Arknights_Client_version, Arknights_Res_version

# sv_get_version = SV('ark查询版本')
# sv_get_version_admin = SV('ark推送版本更新', pm=1)


# @sv_get_version_admin.on_fullmatch((f'{PREFIX}开启推送版本更新'))  # noqa: UP034
# async def force_version_job(bot: Bot, ev: Event):
#     await bot.logger.info('开始执行[ark推送版本更新]')
#     await ark_version_job()


# class ArkVersion(Struct):
#     clientVersion: str
#     resVersion: str


# async def get_notice_list(im: list[str]) -> Dict[str, Dict[str, Dict]]:
#     msg_dict: Dict[str, Dict[str, Dict]] = {}
#     for _bot_id in gss.active_bot:
#         user_list = await ArknightsUser.get_all_push_user_list()
#         print(user_list)
#         for user in user_list:
#             if user.uid is not None:
#                 push_data = await ArknightsPush.select_push_data(user.uid)
#                 print(push_data)
#                 if push_data is None:
#                     continue

#                 if push_data.version_push is False:
#                     pass
#                 else:
#                     if user.bot_id not in msg_dict:
#                         msg_dict[user.bot_id] = {'direct': {}, 'group': {}}
#                     if push_data.version_push:
#                         # 添加私聊信息
#                         if user.user_id not in msg_dict[user.bot_id]['direct']:
#                             msg_dict[user.bot_id]['direct'][user.user_id] = im
#                         else:
#                             msg_dict[user.bot_id]['direct'][user.user_id] += im
#                         await ArknightsPush.update_push_data(
#                             user.uid, {'version_is_push': True}
#                         )
#                     # 群号推送到群聊
#                     else:
#                         # 初始化
#                         gid = push_data.version_push
#                         if gid not in msg_dict[user.bot_id]['group']:
#                             msg_dict[user.bot_id]['group'][gid] = {}

#                         if (
#                             user.user_id
#                             not in msg_dict[user.bot_id]['group'][gid]
#                         ):
#                             msg_dict[user.bot_id]['group'][gid][
#                                 user.user_id
#                             ] = im
#                         else:
#                             msg_dict[user.bot_id]['group'][gid][
#                                 user.user_id
#                             ] += im
#                         await ArknightsPush.update_push_data(
#                             user.uid, {'version_is_push': True}
#                         )
#     return msg_dict


# async def get_resVersion():
#     async with aiohttp.ClientSession() as session:
#         async with session.get(
#             "https://ak-conf.hypergryph.com/config/prod/official/Android/version"
#         ) as response:
#             version = convert(json.loads(await response.text()), ArkVersion)
#             if (
#                 version.clientVersion != Arknights_Client_version
#                 and version.resVersion != Arknights_Res_version
#             ):
#                 im = []
#                 im.append(MessageSegment.text("检测到明日方舟版本更新！"))
#                 im.append(
#                     MessageSegment.text(f"客户端版本号：{version.clientVersion}")
#                 )
#                 im.append(MessageSegment.text(f"资源版本号：{version.resVersion}"))
#                 return im
#             logger.info("Version no update")


# @scheduler.scheduled_job('interval', seconds=3)
# async def ark_version_job():
#     im = await get_resVersion()
#     im = ['test']
#     if im is not None:
#         result = await get_notice_list(im)
#         logger.info('[ark更新检查]完成!等待消息推送中...')
#         logger.debug(result)

#         # 执行私聊推送
#         for bot_id in result:
#             for BOT_ID in gss.active_bot:
#                 bot = gss.active_bot[BOT_ID]
#                 for user_id in result[bot_id]['direct']:
#                     msg = result[bot_id]['direct'][user_id]
#                     await bot.target_send(
#                         msg, 'direct', user_id, bot_id, '', ''
#                     )
#                     await asyncio.sleep(0.5)
#                 logger.info('[ark更新检查] 私聊推送完成')
#                 for gid in result[bot_id]['group']:
#                     msg_list = []
#                     for user_id in result[bot_id]['group'][gid]:
#                         msg_list.append(MessageSegment.at(user_id))
#                         msg = result[bot_id]['group'][gid][user_id]
#                         msg_list.append(MessageSegment.text(msg))
#                     await bot.target_send(
#                         msg_list, 'group', gid, bot_id, '', ''
#                     )
#                     await asyncio.sleep(0.5)
#                 logger.info('[ark更新检查] 群聊推送完成')
