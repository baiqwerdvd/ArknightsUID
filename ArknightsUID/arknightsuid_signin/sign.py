import asyncio
import random
from copy import deepcopy
from datetime import datetime
from typing import List

from gsuid_core.gss import gss
from gsuid_core.logger import logger

from ..arknightsuid_config.ark_config import arkconfig
from ..utils.ark_api import ark_skd_api
from ..utils.database.models import ArknightsUser

private_msg_list = {}
group_msg_list = {}
already = 0


# 签到函数
async def sign_in(ark_uid: str) -> str:
    logger.info(f'[ARK签到] {ark_uid} 开始执行签到')
    # 获得签到信息
    sign_info = await ark_skd_api.get_sign_info(ark_uid)
    # 初步校验数据
    if isinstance(sign_info, int):
        logger.warning(f'[ARK签到] {ark_uid} 出错, 请检查森空岛Cred是否过期!')
        return '签到失败...请检查森空岛Cred是否过期!'
    # 检测是否已签到
    for calendar in sign_info.calendar:
        if calendar.available:
            break
    else:
        logger.info(f'[ARK签到] {ark_uid} 该用户今日已签到,跳过...')
        global already  # noqa: PLW0603
        already += 1
        # 获取今天和月初的日期,计算漏签次数
        day_of_month = datetime.now().day
        special_count = 0
        count = 0
        for calendar in sign_info.calendar:
            special_count += 1 if calendar.type_ == 'first' else 0
            done = calendar.done
            if done is True:
                count += 1
        sign_missed = day_of_month - count + special_count
        return f'今日已签到!本月漏签次数:{sign_missed}'

    # 进行一次签到
    sign_data = await ark_skd_api.skd_sign(uid=ark_uid)
    # 检测数据
    if isinstance(sign_data, int):
        logger.warning(f'[ARK签到] {ark_uid} 出错, 请检查森空岛Cred是否过期!')
        return 'ark签到失败...请检查森空岛Cred是否过期!'
    # 获取签到奖励物品,拿旧的总签到天数 + 1 为新的签到天数,再 -1 即为今日奖励物品的下标
    getitem = sign_data.awards
    get_im = ''
    for award in getitem:
        get_im = f'本次ark签到获得{award.resource.name}x{award.count}'
    # 签到后计算漏签次数
    new_sign_info = await ark_skd_api.get_sign_info(ark_uid)
    # 校验数据
    if isinstance(new_sign_info, int):
        logger.warning(f'[ARK签到] {ark_uid} 出错, 请检查森空岛Cred是否过期!')
        return '签到失败...请检查森空岛Cred是否过期!'
    # 获取今天和月初的日期,计算漏签次数
    day_of_month = datetime.now().day
    special_count = 0
    count = 0
    for calendar in new_sign_info.calendar:
        special_count += 1 if calendar.type_ == 'first' else 0
        done = calendar.done
        if done is True:
            count += 1
    sign_missed = day_of_month - count + special_count
    im = f'ark签到成功!\n{get_im}\n本月漏签次数:{sign_missed}'
    logger.info(f'[ARK签到] {ark_uid} 签到完成, 结果: ark签到成功, 漏签次数: {sign_missed}')
    return im


async def single_daily_sign(bot_id: str, ark_uid: str, gid: str, qid: str):
    im = await sign_in(ark_uid)
    if gid == 'on':
        if qid not in private_msg_list:
            private_msg_list[qid] = []
        private_msg_list[qid].append({'bot_id': bot_id, 'uid': ark_uid, 'msg': im})
    else:
        # 向群消息推送列表添加这个群
        if gid not in group_msg_list:
            group_msg_list[gid] = {
                'bot_id': bot_id,
                'success': 0,
                'failed': 0,
                'push_message': '',
            }
        # 检查是否开启简洁签到
        if arkconfig.get_config('SignReportSimple').data:
            # 如果失败, 则添加到推送列表
            if im.startswith(('ark签到失败', '网络有点忙', 'OK', 'ok')):
                message = f'[CQ:at,qq={qid}] {im}'
                group_msg_list[gid]['failed'] += 1
                group_msg_list[gid]['push_message'] += '\n' + message
            else:
                group_msg_list[gid]['success'] += 1
        # 没有开启简洁签到, 则每条消息都要携带@信息
        else:
            # 不用MessageSegment.at(row[2]),因为不方便移植
            message = f'[CQ:at,qq={qid}] {im}'
            group_msg_list[gid]['push_message'] += '\n' + message
            group_msg_list[gid]['success'] -= 1


async def daily_sign():
    global already  # noqa: PLW0603
    tasks = []
    for _ in gss.active_bot:
        user_list: List[ArknightsUser] = await ArknightsUser.get_all_user()
        logger.info(f'[ARK签到] 共有{len(user_list)}个用户需要签到')
        logger.info(f'[ARK签到] {user_list}')
        for user in user_list:
            if user.sign_switch != 'off' and user.uid is not None:
                tasks.append(
                    single_daily_sign(
                        user.bot_id,
                        user.uid,
                        user.sign_switch,
                        user.user_id,
                    )
                )
            if len(tasks) >= 1:
                await asyncio.gather(*tasks)
                if already >= 1:
                    delay = 1
                else:
                    delay = 50 + random.randint(3, 45)
                logger.info(f'[ARK签到] 已签到{len(tasks)}个用户, 等待{delay}秒进行下一次签到')
                tasks.clear()
                already = 0
                await asyncio.sleep(delay)
    await asyncio.gather(*tasks)
    tasks.clear()
    result = {
        'private_msg_list': deepcopy(private_msg_list),
        'group_msg_list': deepcopy(group_msg_list),
    }
    private_msg_list.clear()
    group_msg_list.clear()
    logger.info(result)
    return result
