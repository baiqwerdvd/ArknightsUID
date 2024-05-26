from typing import Dict
from PIL import Image, ImageDraw
from pathlib import Path
from ..utils.models.skland.models import (
    PlayerCharInfo,
    PlayerEquipmentInfo,
    PlayerInfoChar,
)

from ..arknightsuid_resource.constants import SKILL_TABLE
from ..utils.fonts.source_han_sans import (
    sans_font_26,
    sans_font_28,
    sans_font_34,
)
from ..utils.ark_api import ark_skd_api


char_sort_list = [
    "伊内丝",
    "维什戴尔",
    "逻各斯",
    "刻俄柏",
    "琴柳",
    "风笛",
    "史尔特尔",
    "黍",
    "锏",
    "焰影苇草",
    "缄默德克萨斯",
    "艾拉",
    "麒麟R夜刀",
    "铃兰",
    "玛恩纳",
    "温蒂",
    "莱伊",
    "假日威龙陈",
    "耀骑士临光",
    "夜莺",
    "塞雷娅",
    "归溟幽灵鲨",
    "歌蕾蒂娅",
    "灵知",
    "阿尔图罗",
    "艾雅法拉",
    "林",
    "莫斯提马",
    "瑕光",
    " 伊芙利特",
    "阿",
    "令",
    "涤火杰西卡",
    "年",
    "麦哲伦",
    "浊心斯卡蒂",
    "纯烬艾雅法拉",
    "白铁",
    "左乐",
    "仇白",
    "百炼嘉维尔",
    "银灰",
    "傀影",
    "号角",
    "泥岩",
    "凯尔希",
    "星熊",
    "斥罪",
    "山",
    "黑键",
    "多萝西",
    "缪尔赛思",
    "赫德雷",
    "圣约送葬人",
    "重岳",
    "煌",
    "提丰",
    "鸿雪",
    "澄闪",
    "黑",
    "闪灵",
    "霍尔海雅",
    "灰烬",
    "薇薇安娜",
    "早露",
    "安洁莉娜",
    "淬羽赫默",
    "森蚺",
    "嵯峨",
    "斯卡蒂",
    "陈",
    "艾丽妮",
    "卡涅利安",
    "琳琅诗怀雅",
    "老鲤",
    "能天使",
    "迷迭香",
    "空弦",
    "夕",
    "菲亚梅塔",
    "水月",
    "流明",
    "异客",
    "棘刺",
    "止颂",
    "赫拉格",
    "帕拉斯",
    "焰尾",
    "推进之王",
    "远牙",
    "W",
    "伺夜",
]

TEXT_PATH = Path(__file__).parent / "texture2D"

bg_img = Image.open(TEXT_PATH / "bg.jpg").convert("RGBA")
avatar_bg = Image.open(TEXT_PATH / "avatar_bg.png").resize((118, 118))
avatar_fg = Image.open(TEXT_PATH / "avatar_fg.png")

skill_selected = Image.open(TEXT_PATH / "skill_selected.png")
skill_selected = skill_selected.resize((40, 40))
data = skill_selected.getdata()
new_data = []
for item in data:
    if item[0] < 100 and item[1] < 100 and item[2] < 100:
        new_data.append((0, 0, 0, 0))
    else:
        new_data.append(item)
skill_selected.putdata(new_data)

equip_selected = Image.open(TEXT_PATH / "equip_selected.png")


async def get_char_snapshot(uid: str):
    data = await ark_skd_api.get_game_player_info(uid)
    if isinstance(data, int):
        return "查询失败, 请检查uid或者Cred是否正确"
    status = data.status
    chars = data.chars
    charInfoMap = data.charInfoMap
    equipmentInfoMap = data.equipmentInfoMap

    char_cnt = len(chars)

    six_star_count = 0
    for char in chars:
        char_id = char.charId
        char_rarity = charInfoMap[char_id].rarity
        if char_rarity == 5:
            six_star_count += 1

    if status.avatar is None:
        avatar_id = "avatar_activity_AW"
    else:
        avatar_id = status.avatar.id_
    avatar_img = Image.open(TEXT_PATH / "ui_player_avatar_list_h2" / f"{avatar_id}.png").resize(
        (235, 235)
    )

    avatar_fg_draw = ImageDraw.Draw(avatar_fg)
    avatar_fg_draw.text(
        (50, 39),
        str(status.level),
        font=sans_font_34,
        fill=(255, 255, 255),
        anchor="mm",
    )

    title_img = Image.open(TEXT_PATH / "title.png")
    title_img.paste(avatar_img, (360, 85), mask=avatar_img)
    title_img.paste(avatar_fg, (328, 50), mask=avatar_fg)
    title_img_draw = ImageDraw.Draw(title_img)
    title_img_draw.text(
        (480, 345),
        status.name,
        font=sans_font_28,
        fill=(255, 255, 255),
        anchor="mm",
    )
    title_img_draw.text(
        (610, 415),
        str(six_star_count),
        font=sans_font_26,
        fill=(255, 255, 255),
        anchor="mm",
    )
    title_img_draw.text(
        (405, 415),
        str(char_cnt),
        font=sans_font_26,
        fill=(255, 255, 255),
        anchor="mm",
    )
    bg_img.paste(title_img, (0, 0), mask=title_img)

    info_img = Image.open(TEXT_PATH / "info.png")
    bg_img.paste(info_img, (0, 440), mask=info_img)

    if six_star_count > 20:
        chars = [char for char in chars if charInfoMap[char.charId].rarity == 5]
        # 按照list的顺序排序, 特殊处理不在list中的角色
        for char in chars:
            char_id = char.charId
            if charInfoMap[char_id].name not in char_sort_list:
                char_sort_list.append(charInfoMap[char_id].name)

        chars = sorted(
            chars,
            key=lambda x: char_sort_list.index(charInfoMap[x.charId].name),
        )
    else:
        for char in chars:
            char.specializeLevelCount = 0
            if char.skills is None:
                continue
            for skill in char.skills:
                char.specializeLevelCount += skill.specializeLevel  # type: ignore
        chars = sorted(
            chars,
            key=lambda x: (
                x.evolvePhase,
                x.level,
                x.specializeLevelCount,
                x.potentialRank,
                x.charId,
            ),
            reverse=True,
        )

    for i in range(17):
        img = draw_char(chars[i], charInfoMap, equipmentInfoMap)
        bg_img.paste(img, (0, 490 + 110 * i), mask=img)

    footer_img = Image.open(TEXT_PATH / "footer.png")
    bg_img.paste(footer_img, (0, 2365), mask=footer_img)


def draw_char(
    test_char: PlayerInfoChar,
    charInfoMap: Dict[str, PlayerCharInfo],
    equipmentInfoMap: Dict[str, PlayerEquipmentInfo],
):
    bar_img: Image.Image = Image.open(TEXT_PATH / "bar.png").convert("RGBA")

    ui_char_avatar = (
        Image.open(TEXT_PATH / "ui_char_avatar" / f"{test_char.charId}.png")
        .resize((90, 90))
        .convert("RGBA")
    )
    bar_img.paste(avatar_bg, (24, 5), mask=avatar_bg)
    bar_img.paste(ui_char_avatar, (38, 21), mask=ui_char_avatar)

    potential_rank = test_char.potentialRank
    potential_img = Image.open(
        TEXT_PATH / f"potential_hub/potential_{potential_rank}.png"
    ).resize((45, 45))
    bar_img.paste(potential_img, (135, 67), mask=potential_img)

    elite_level = test_char.evolvePhase
    elite_img = Image.open(TEXT_PATH / "elite_hub" / f"elite_{elite_level}_large.png")
    elite_img = elite_img.resize((44, 37))
    bar_img.paste(elite_img, (186, 71), mask=elite_img)

    white_color = (255, 255, 255)

    char_level = test_char.level
    bar_img_draw = ImageDraw.Draw(bar_img)
    bar_img_draw.text(
        (298, 92),
        f"Lv{char_level}",
        font=sans_font_26,
        fill=white_color,
        anchor="rm",
    )

    profession = charInfoMap[test_char.charId].profession.lower()
    profession_img = Image.open(
        TEXT_PATH / "profession" / f"icon_profession_{profession}_lighten.png"
    )
    profession_img = profession_img.resize((35, 35))
    bar_img.paste(profession_img, (139, 26), mask=profession_img)

    char_name = charInfoMap[test_char.charId].name
    bar_img_draw.text(
        (180, 42),
        char_name,
        font=sans_font_26,
        fill=white_color,
        anchor="lm",
    )

    char_skills = test_char.skills
    if char_skills is not None:
        for i, skill in enumerate(char_skills):
            skill_id = skill.id_
            skill_icon_id = SKILL_TABLE.skills[skill_id].iconId
            skill_specialize_level = skill.specializeLevel
            if skill_icon_id is None:
                skill_icon_id = skill_id
            skill_img = Image.open(TEXT_PATH / "skill_icons" / f"skill_icon_{skill_icon_id}.png")
            skill_img = skill_img.resize((70, 70))
            if test_char.defaultSkillId == skill_id:
                skill_img.paste(skill_selected, (38, -1), mask=skill_selected)
            skill_specialize_img = Image.open(
                TEXT_PATH / "charcommon" / f"evolve_small_icon_{skill_specialize_level}.png"
            )
            skill_img.paste(skill_specialize_img, (0, 0), mask=skill_specialize_img)
            bar_img.paste(skill_img, (345 + 78 * i, 30), mask=skill_img)

    favor_percent = test_char.favorPercent
    bar_img_draw.text(
        (600, 62),
        f"{favor_percent}",
        font=sans_font_34,
        fill=white_color,
        anchor="lm",
    )

    char_equips = test_char.equip
    if char_equips is not None:
        for i, equip_id in enumerate(char_equips):
            equip_type_icon = equipmentInfoMap[equip_id.id_].typeIcon
            if equip_type_icon == "original":
                continue
            equip_img = Image.open(
                TEXT_PATH / "ui_equip_type_direction_hub_h2" / f"{equip_type_icon}.png"
            ).resize((92, 68))
            if test_char.defaultEquipId == equip_id.id_:
                bar_img.paste(equip_selected, (626 + 67 * i, 31), mask=equip_selected)
            bar_img.paste(equip_img, (616 + 68 * i, 32), mask=equip_img)

    return bar_img
