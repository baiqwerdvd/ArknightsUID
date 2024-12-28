import asyncio
from datetime import datetime, timedelta
from pathlib import Path

from gsuid_core.logger import logger
from gsuid_core.utils.image.convert import convert_img
from PIL import Image, ImageDraw

from ..arknightsuid_resource.constants import CHARACTER_TABLE
from ..utils.ark_api import ark_skd_api
from ..utils.database.models import ArknightsBind
from ..utils.fonts.source_han_sans import (
    sans_font_18,
    sans_font_26,
    sans_font_34,
)
from .utils import now_ap, seconds2hours_zhcn

TEXT_PATH = Path(__file__).parent / "texture2D"

white_bg = Image.open(TEXT_PATH / "white_bg.png")
up_bar = Image.open(TEXT_PATH / "up_bar.png")
brain_pic = Image.open(TEXT_PATH / "brain.png")
warn_pic = Image.open(TEXT_PATH / "warn.png")
mask_pic = Image.open(TEXT_PATH / "mask.png").convert("RGBA")
logo_white = Image.open(TEXT_PATH / "logo_white.png")

blue_bar_bg1 = Image.open(TEXT_PATH / "blue_bar_bg1.png")
grey_bar_bg1 = Image.open(TEXT_PATH / "grey_bar_bg1.png")

based_w = 850
based_h = 1750

first_color = (29, 29, 29)
white_color = (255, 255, 255)
red_color = (235, 61, 75)


async def get_ap_img(bot_id: str, user_id: str):
    try:
        uid_list = await ArknightsBind.get_uid_list_by_game(user_id, bot_id)
        logger.info(f"[每日信息]UID: {uid_list}")
        # 进行校验UID是否绑定CK
        useable_uid_list = []
        if uid_list is None:
            return "请先绑定一个可用CRED & UID再来查询哦~"
        for uid in uid_list:
            # status = await ark_skd_api.check_cred_valid(uid=uid)
            # if status is not bool:
            # skd_uid = await ArknightsUser.get_user_attr_by_uid(
            #     uid=uid,
            #     attr="skd_uid",
            # )
            useable_uid_list.append(uid)
        logger.info(f"[每日信息]可用UID: {useable_uid_list}")
        if len(useable_uid_list) == 0:
            return "请先绑定一个可用CRED & UID再来查询哦~"
        # 开始绘图任务
        task = []
        img = Image.new(
            "RGBA",
            (based_w * len(useable_uid_list), based_h),
            (0, 0, 0, 0),
        )
        for uid_index, uid in enumerate(useable_uid_list):
            task.append(_draw_all_ap_img(img, uid, uid_index))
        await asyncio.gather(*task)
        res = await convert_img(img)
        logger.info("[查询每日信息]绘图已完成,等待发送!")
    except TypeError:
        logger.exception("[查询每日信息]绘图失败!")
        res = "你绑定过的UID中可能存在过期CRED~请重新绑定一下噢~"

    return res


async def _draw_all_ap_img(img: Image.Image, uid: str, index: int):
    ap_img = await draw_ap_img(uid)
    img.paste(ap_img, (850 * index, 0), ap_img)


def get_error(img: Image.Image, uid: str, daily_data: int):
    img_draw = ImageDraw.Draw(img)
    img.paste(warn_pic, (0, 0), warn_pic)
    # 写UID
    img_draw.text(
        (350, 680),
        f"UID{uid}",
        font=sans_font_26,
        fill=first_color,
        anchor="mm",
    )
    img_draw.text(
        (350, 650),
        f"错误码 {daily_data}",
        font=sans_font_26,
        fill=red_color,
        anchor="mm",
    )
    return img


async def draw_ap_img(uid: str) -> Image.Image:
    # char
    char_pic = (
        Image.open(TEXT_PATH / "char_1028_texas2_1b.png").resize((1700, 1700)).convert("RGBA")
    )

    tmp_img = Image.new("RGBA", (based_w, based_h))
    tmp_img.paste(char_pic, (-250, 50), char_pic)
    tmp_img2 = Image.new("RGBA", (based_w, based_h))
    tmp_img2.paste(tmp_img, (0, 0), mask_pic)

    img = Image.alpha_composite(white_bg, tmp_img2)

    # 获取数据
    player_info = await ark_skd_api.get_game_player_info(uid)
    if isinstance(player_info, int):
        return get_error(img, uid, player_info)

    # nickname
    nickname = player_info.status.name
    up_bar_img = up_bar.copy()
    up_bar_draw = ImageDraw.Draw(up_bar_img)
    up_bar_draw.text(
        (40, 130),
        f"Dr.{nickname}",
        font=sans_font_34,
        fill=white_color,
        anchor="lm",
    )
    img.paste(up_bar_img, (0, 0), up_bar_img)

    # ap
    current_ap = now_ap(player_info.status.ap)
    max_ap = player_info.status.ap.max
    brain_pic_img = brain_pic.copy()
    brain_pic_draw = ImageDraw.Draw(brain_pic_img)
    brain_pic_draw.text(
        (135, 255),
        f"{current_ap}/{max_ap}",
        font=sans_font_34,
        fill=white_color,
        anchor="lm",
    )
    img.paste(brain_pic_img, (50, 500), brain_pic_img)

    # logo
    logo_white_img = logo_white.copy().resize((400, 225), Image.LANCZOS)
    img.paste(logo_white_img, (400, 590), logo_white_img)

    # 详细信息

    # recruit check
    recruit = player_info.recruit
    recruit_task = [recruit[i].state for i in range(len(recruit))]
    recruit_task_finish_count = recruit_task.count(2)
    finishTs = -1

    if recruit_task_finish_count == 0:
        blue_bar_bg1_img = blue_bar_bg1.copy()
    else:
        blue_bar_bg1_img = grey_bar_bg1.copy()

    for i in range(len(recruit)):
        if finishTs < recruit[i].finishTs:
            finishTs = recruit[i].finishTs
    if finishTs != -1:
        # 获取当前时间与 finishTs 的时间差, 转换为几小时几分钟
        now = datetime.now()
        finishTs = datetime.fromtimestamp(finishTs)
        delta = finishTs - now
        delta_hour = delta.seconds // 3600
        delta_minute = (delta.seconds - delta_hour * 3600) // 60
    else:
        delta_hour = 0
        delta_minute = 0
    blue_bar_bg1_draw = ImageDraw.Draw(blue_bar_bg1_img)
    blue_bar_bg1_draw.text(
        (170, 60),
        "公开招募",
        font=sans_font_34,
        fill=first_color,
        anchor="lm",
    )

    if recruit_task_finish_count == len(recruit):
        blue_bar_bg1_draw.text(
            (540, 70),
            "招募已全部完成",
            font=sans_font_18,
            fill=first_color,
            anchor="rm",
        )
    else:
        blue_bar_bg1_draw.text(
            (540, 70),
            f"{delta_hour}小时{delta_minute}分钟后全部完成",
            font=sans_font_18,
            fill=first_color,
            anchor="rm",
        )

    blue_bar_bg1_draw.text(
        xy=(777, 58),
        text=f"{len(recruit) - recruit_task_finish_count}/{len(recruit)}",
        font=sans_font_34,
        fill=white_color,
        anchor="rm",
    )

    img.paste(blue_bar_bg1_img, (-20, 800), blue_bar_bg1_img)

    # recruit refresh check
    if player_info.building.hire:
        if player_info.building.hire.refreshCount == 0:
            grey_bar_bg1_img = grey_bar_bg1.copy()
            grey_bar_bg1_draw = ImageDraw.Draw(grey_bar_bg1_img)
            complete_work_time = player_info.building.hire.completeWorkTime
            # 获取当前时间与 completeWorkTime 的时间差, 转换为几小时几分钟
            now = datetime.now()
            complete_work_time = datetime.fromtimestamp(complete_work_time)
            delta = complete_work_time - now
            delta_hour = delta.seconds // 3600
            delta_minute = (delta.seconds - delta_hour * 3600) // 60
            grey_bar_bg1_draw.text(
                (170, 60),
                "公开刷新",
                font=sans_font_34,
                fill=first_color,
                anchor="lm",
            )
            grey_bar_bg1_draw.text(
                (540, 70),
                f"{delta_hour}小时{delta_minute}分钟后获取刷新次数",
                font=sans_font_18,
                fill=first_color,
                anchor="rm",
            )
            grey_bar_bg1_draw.text(
                xy=(777, 58),
                text="联络中",
                font=sans_font_34,
                fill=white_color,
                anchor="rm",
            )
            img.paste(grey_bar_bg1_img, (-20, 910), grey_bar_bg1_img)
        else:
            blue_bar_bg1_img = blue_bar_bg1.copy()
            blue_bar_bg1_draw = ImageDraw.Draw(blue_bar_bg1_img)
            blue_bar_bg1_draw.text(
                (170, 60),
                "公开招募刷新",
                font=sans_font_34,
                fill=first_color,
                anchor="lm",
            )
            blue_bar_bg1_draw.text(
                (540, 70),
                "可进行公开招募刷新",
                font=sans_font_18,
                fill=first_color,
                anchor="rm",
            )
            blue_bar_bg1_draw.text(
                xy=(777, 58),
                text="可刷新",
                font=sans_font_34,
                fill=white_color,
                anchor="rm",
            )
            img.paste(blue_bar_bg1_img, (-20, 910), blue_bar_bg1_img)
    else:
        grey_bar_bg1_img = grey_bar_bg1.copy()
        grey_bar_bg1_draw = ImageDraw.Draw(grey_bar_bg1_img)
        grey_bar_bg1_draw.text(
            (170, 60),
            "暂无数据",
            font=sans_font_34,
            fill=first_color,
            anchor="lm",
        )
        img.paste(grey_bar_bg1_img, (-20, 910), grey_bar_bg1_img)

    # training char check
    if player_info.building.training and player_info.building.training.trainee:
        training_char = player_info.building.training.trainee.charId
        remain_secs = player_info.building.training.remainSecs
        remain_time = 0
        if remain_secs != -1:
            # 将remainSecs(剩余秒数) , 转换为几小时几分钟
            remain_time = seconds2hours_zhcn(remain_secs)

        char_cn_name = CHARACTER_TABLE[training_char].name
        blue_bar_bg1_img = blue_bar_bg1.copy()
        blue_bar_bg1_draw = ImageDraw.Draw(blue_bar_bg1_img)
        blue_bar_bg1_draw.text(
            (170, 60),
            "训练室",
            font=sans_font_34,
            fill=first_color,
            anchor="lm",
        )
        blue_bar_bg1_draw.text(
            (540, 70),
            f"{remain_time}后完成专精" if remain_secs != -1 else "设备空闲中",
            font=sans_font_18,
            fill=first_color,
            anchor="rm",
        )
        blue_bar_bg1_draw.text(
            xy=(777, 58),
            text=f"{char_cn_name}",
            font=sans_font_34,
            fill=white_color,
            anchor="rm",
        )
        img.paste(blue_bar_bg1_img, (-20, 1020), blue_bar_bg1_img)
    else:
        grey_bar_bg1_img = grey_bar_bg1.copy()
        grey_bar_bg1_draw = ImageDraw.Draw(grey_bar_bg1_img)
        grey_bar_bg1_draw.text(
            (170, 60),
            "训练室",
            font=sans_font_34,
            fill=first_color,
            anchor="lm",
        )
        grey_bar_bg1_draw.text(
            (540, 70),
            "设备空闲中",
            font=sans_font_18,
            fill=first_color,
            anchor="rm",
        )
        grey_bar_bg1_draw.text(
            xy=(777, 58),
            text="无干员",
            font=sans_font_34,
            fill=white_color,
            anchor="rm",
        )
        img.paste(grey_bar_bg1_img, (-20, 1020), grey_bar_bg1_img)

    # campaign reward check
    campaign_reward = player_info.campaign.reward
    if campaign_reward.current == campaign_reward.total:
        blue_bar_bg1_img = blue_bar_bg1.copy()
    else:
        blue_bar_bg1_img = grey_bar_bg1.copy()
    blue_bar_bg1_draw = ImageDraw.Draw(blue_bar_bg1_img)
    blue_bar_bg1_draw.text(
        (170, 60),
        "每周报酬合成玉",
        font=sans_font_34,
        fill=first_color,
        anchor="lm",
    )

    # 获取当前时间与下一周周一早上4点的时间差, 转换为几天几小时
    now = datetime.now()
    next_monday = now + timedelta(days=-now.weekday(), weeks=1)
    next_monday = next_monday.replace(hour=4, minute=0, second=0, microsecond=0)
    delta = next_monday - now
    delta_day = delta.days
    delta_hour = delta.seconds // 3600
    blue_bar_bg1_draw.text(
        (540, 70),
        f"{delta_day}天{delta_hour}小时后刷新",
        font=sans_font_18,
        fill=first_color,
        anchor="rm",
    )

    blue_bar_bg1_draw.text(
        xy=(777, 58),
        text=f"{campaign_reward.current}/{campaign_reward.total}",
        font=sans_font_34,
        fill=white_color,
        anchor="rm",
    )
    img.paste(blue_bar_bg1_img, (-20, 1130), blue_bar_bg1_img)

    # routine daily check
    routine_daily = player_info.routine.daily
    # 获取当前时间与下一天早上4点的时间差, 转换为几小时几分钟
    now = datetime.now()
    next_day = now + timedelta(days=1)
    next_day = next_day.replace(hour=4, minute=0, second=0, microsecond=0)
    delta = next_day - now
    delta_hour = delta.seconds // 3600
    delta_minute = (delta.seconds - delta_hour * 3600) // 60
    if routine_daily.total == routine_daily.current:
        blue_bar_bg1_img = blue_bar_bg1.copy()
    else:
        blue_bar_bg1_img = grey_bar_bg1.copy()
    blue_bar_bg1_draw = ImageDraw.Draw(blue_bar_bg1_img)
    blue_bar_bg1_draw.text(
        (170, 60),
        "每日任务",
        font=sans_font_34,
        fill=first_color,
        anchor="lm",
    )
    blue_bar_bg1_draw.text(
        (540, 70),
        f"{delta_hour}小时{delta_minute}分钟后刷新",
        font=sans_font_18,
        fill=first_color,
        anchor="rm",
    )
    blue_bar_bg1_draw.text(
        xy=(777, 58),
        text=f"{routine_daily.current}/{routine_daily.total}",
        font=sans_font_34,
        fill=white_color,
        anchor="rm",
    )
    img.paste(blue_bar_bg1_img, (-20, 1240), blue_bar_bg1_img)

    # routine weekly check
    routine_weekly = player_info.routine.weekly
    # 获取当前时间与下一周周一早上4点的时间差, 转换为几天几小时
    now = datetime.now()
    next_monday = now + timedelta(days=-now.weekday(), weeks=1)
    next_monday = next_monday.replace(hour=4, minute=0, second=0, microsecond=0)
    delta = next_monday - now
    delta_day = delta.days
    delta_hour = delta.seconds // 3600
    if routine_weekly.total == routine_weekly.current:
        blue_bar_bg1_img = blue_bar_bg1.copy()
    else:
        blue_bar_bg1_img = grey_bar_bg1.copy()
    blue_bar_bg1_draw = ImageDraw.Draw(blue_bar_bg1_img)
    blue_bar_bg1_draw.text(
        (170, 60),
        "每周任务",
        font=sans_font_34,
        fill=first_color,
        anchor="lm",
    )
    blue_bar_bg1_draw.text(
        (540, 70),
        f"{delta_day}天{delta_hour}小时后刷新",
        font=sans_font_18,
        fill=first_color,
        anchor="rm",
    )
    blue_bar_bg1_draw.text(
        xy=(777, 58),
        text=f"{routine_weekly.current}/{routine_weekly.total}",
        font=sans_font_34,
        fill=white_color,
        anchor="rm",
    )
    img.paste(blue_bar_bg1_img, (-20, 1350), blue_bar_bg1_img)

    # tower reward check
    tower_reward = player_info.tower.reward
    higher_item = tower_reward.higherItem
    term_ts = tower_reward.termTs
    # 获取当前时间与 termTs 的时间差, 转换为几天几小时
    now = datetime.now()
    term_ts = datetime.fromtimestamp(term_ts)
    delta = term_ts - now
    delta_day = delta.days
    delta_hour = delta.seconds // 3600
    if higher_item.current == higher_item.total:
        blue_bar_bg1_img = blue_bar_bg1.copy()
    else:
        blue_bar_bg1_img = grey_bar_bg1.copy()
    blue_bar_bg1_draw = ImageDraw.Draw(blue_bar_bg1_img)
    blue_bar_bg1_draw.text(
        (170, 60),
        "数据增补仪",
        font=sans_font_34,
        fill=first_color,
        anchor="lm",
    )
    blue_bar_bg1_draw.text(
        (540, 70),
        f"{delta_day}天{delta_hour}小时后刷新",
        font=sans_font_18,
        fill=first_color,
        anchor="rm",
    )
    blue_bar_bg1_draw.text(
        xy=(777, 58),
        text=f"{higher_item.current}/{higher_item.total}",
        font=sans_font_34,
        fill=white_color,
        anchor="rm",
    )
    img.paste(blue_bar_bg1_img, (-20, 1460), blue_bar_bg1_img)

    lower_item = tower_reward.lowerItem
    if lower_item.current == lower_item.total:
        blue_bar_bg1_img = blue_bar_bg1.copy()
    else:
        blue_bar_bg1_img = grey_bar_bg1.copy()
    blue_bar_bg1_draw = ImageDraw.Draw(blue_bar_bg1_img)
    blue_bar_bg1_draw.text(
        (170, 60),
        "数据增补条",
        font=sans_font_34,
        fill=first_color,
        anchor="lm",
    )
    blue_bar_bg1_draw.text(
        (540, 70),
        f"{delta_day}天{delta_hour}小时后刷新",
        font=sans_font_18,
        fill=first_color,
        anchor="rm",
    )
    blue_bar_bg1_draw.text(
        xy=(777, 58),
        text=f"{lower_item.current}/{lower_item.total}",
        font=sans_font_34,
        fill=white_color,
        anchor="rm",
    )
    img.paste(blue_bar_bg1_img, (-20, 1570), blue_bar_bg1_img)

    img_draw = ImageDraw.Draw(img)
    img_draw.text(
        (425, 1710),
        "Powerd By ArknightsUID | GsCore",
        font=sans_font_26,
        fill=first_color,
        anchor="mm",
    )

    return img
