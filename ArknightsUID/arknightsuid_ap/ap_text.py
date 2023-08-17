# import math
# from datetime import datetime

# from gsuid_core.data_store import get_res_path
# from gsuid_core.logger import logger
# from gsuid_core.utils.error_reply import get_error
# from msgspec import json as msgjson

# # from ..arknightsuid_resource.constants import Excel
# from ..utils.ark_api import ark_skd_api
# from ..utils.models.skland.models import PlayerStatusAp

# daily_im = """*数据刷新可能存在一定延迟，请以当前游戏实际数据为准
# ==============
# 理智：{}/{}
# 公开招募：{}/{}
# 公招刷新：{}
# 训练室：{}
# 每周报酬合成玉：{}/{}
# 每日任务：{}/{}
# 每周任务：{}/{}
# 数据增补仪：{}/{}
# 数据增补条：{}/{}
# =============="""


# def seconds2hours(seconds: int) -> str:
#     m, s = divmod(int(seconds), 60)
#     h, m = divmod(m, 60)
#     return '%02d:%02d:%02d' % (h, m, s)

# def now_ap(ap: PlayerStatusAp) -> int:
#     _ap =  ap.current + math.floor((datetime.now().timestamp() - ap.lastApAddTime) / 360)
#     return _ap if _ap <= ap.max else ap.max


# async def get_ap_text(uid: str) -> str:
#     try:
#         player_info = await ark_skd_api.get_game_player_info(uid)
#         if isinstance(player_info, int):
#             return get_error(player_info)

#         player_save_path = get_res_path(['ArknightsUID', 'players'])

#         with open(player_save_path / f'{player_info.status.uid}.json', 'wb') as file:
#             file.write(msgjson.format(msgjson.encode(player_info), indent=4))

#         ap = player_info.status.ap
#         current_ap = now_ap(ap)
#         max_ap = ap.max
#         rec_time = ''
#         if current_ap < max_ap:
#             ap_recover_time = seconds2hours(
#                 ap.completeRecoveryTime
#             )
#             next_ap_rec_time = seconds2hours(
#                 8 * 60
#                 - (
#                     (max_ap - current_ap)
#                     * 8
#                     * 60
#                     - int(ap.completeRecoveryTime)
#                 )
#             )
#             rec_time = f' ({next_ap_rec_time}/{ap_recover_time})'

#         accepted_epedition_num = dailydata['accepted_epedition_num']
#         total_expedition_num = dailydata['total_expedition_num']
#         finished_expedition_num = 0
#         expedition_info: list[str] = []
#         for expedition in dailydata['expeditions']:
#             expedition_name = expedition['name']

#             if expedition['status'] == 'Finished':
#                 expedition_info.append(f'{expedition_name} 探索完成')
#                 finished_expedition_num += 1
#             else:
#                 remaining_time: str = seconds2hours(
#                     expedition['remaining_time']
#                 )
#                 expedition_info.append(
#                     f'{expedition_name} 剩余时间{remaining_time}'
#                 )

#         expedition_data = '\n'.join(expedition_info)
#         print(expedition_data)
#         send_mes = daily_im.format(
#             current_ap,
#             max_ap,
#             rec_time,
#             accepted_epedition_num,
#             finished_expedition_num,
#             total_expedition_num,
#             expedition_data,
#         )
#         return send_mes
#     except TypeError:
#         logger.exception('[查询当前状态]查询失败!')
#         return '你绑定过的UID中可能存在过期CK~请重新绑定一下噢~'