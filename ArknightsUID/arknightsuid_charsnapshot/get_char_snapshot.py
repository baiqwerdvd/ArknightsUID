from pathlib import Path
from typing import Dict

from gsuid_core.utils.image.convert import convert_img
from PIL import Image, ImageDraw

from ..arknightsuid_resource.constants import SKILL_TABLE
from ..utils.ark_api import ark_skd_api
from ..utils.fonts.source_han_sans import (
    sans_font_26,
    sans_font_28,
    sans_font_34,
)
from ..utils.models.skland.models import (
    PlayerCharInfo,
    PlayerEquipmentInfo,
    PlayerInfoChar,
)
from ..utils.resource.RESOURCE_PATH import (
    CHAR_COMMON_PATH,
    ELITE_HUB_PATH,
    POTENTIAL_HUB_PATH,
    PROFESSION_PATH,
    SKILL_ICONS_PATH,
    UI_CHAR_AVATAR_PATH,
    UI_EQUIP_TYPE_DIRECTION_HUB_PATH,
    UI_PLAYER_AVATAR_LIST_PATH,
)
from .const import char_sort_list

TEXT_PATH = Path(__file__).parent / "texture2D"

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


async def get_char_snapshot(uid: str, cur_page: int):
    data = await ark_skd_api.get_game_player_info(uid)
    if isinstance(data, int):
        return "查询失败, 请检查uid或者Cred是否正确"
    status = data.status
    chars = data.chars
    charInfoMap = data.charInfoMap
    equipmentInfoMap = data.equipmentInfoMap

    char_cnt = len(chars)

    six_star_chars = [char for char in chars if charInfoMap[char.charId].rarity == 5]
    outher_chars = [char for char in chars if charInfoMap[char.charId].rarity != 5]

    six_star_count = len(six_star_chars)

    # 6星角色按照list的顺序排序
    for char in chars:
        char_id = char.charId
        if charInfoMap[char_id].name not in char_sort_list:
            char_sort_list.append(charInfoMap[char_id].name)
    six_star_chars = sorted(
        six_star_chars,
        key=lambda x: char_sort_list.index(charInfoMap[x.charId].name),
    )

    # 5,4,3,2,1星角色按照 evolvePhase, level, specializeLevelCount, potentialRank, charId 排序
    for char in outher_chars:
        char.specializeLevelCount = 0
        if char.skills is None:
            continue
        for skill in char.skills:
            char.specializeLevelCount += skill.specializeLevel  # type: ignore
    outher_chars = sorted(
        outher_chars,
        key=lambda x: (
            x.evolvePhase,
            x.level,
            x.specializeLevelCount,
            x.potentialRank,
            x.charId,
        ),
        reverse=True,
    )

    total_char = six_star_chars + outher_chars

    if status.avatar is None:
        avatar_id = "avatar_activity_AW"
    else:
        avatar_id = status.avatar.id_
    try:
        try:
            avatar_img = Image.open(UI_PLAYER_AVATAR_LIST_PATH / f"{avatar_id}.png").resize(
                (235, 235)
            )
        except FileNotFoundError:
            avatar_img = Image.open(UI_CHAR_AVATAR_PATH / f"{avatar_id}.png").resize((235, 235))
    except FileNotFoundError:
        avatar_id_rep = avatar_id.replace("#", "_")
        if avatar_id_rep == "char_1013_chen2_1":
            avatar_id_rep = "char_1013_chen2"
        avatar_img = Image.open(UI_CHAR_AVATAR_PATH / f"{avatar_id_rep}.png").resize((235, 235))

    bg_img = Image.open(TEXT_PATH / "bg.jpg").convert("RGBA")
    avatar_fg = Image.open(TEXT_PATH / "avatar_fg.png")

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

    avail_page = (char_cnt + 16) // 17
    if cur_page > avail_page:
        cur_page = avail_page
    if cur_page < 1:
        cur_page = 1

    page_char = total_char[(cur_page - 1) * 17 : cur_page * 17]

    for i, char in enumerate(page_char):
        img = draw_char(char, charInfoMap, equipmentInfoMap)
        bg_img.paste(img, (0, 490 + 110 * i), mask=img)

    footer_img = Image.open(TEXT_PATH / "footer.png")
    bg_img.paste(footer_img, (0, 2365), mask=footer_img)
    res = await convert_img(bg_img)
    return res


def draw_char(
    test_char: PlayerInfoChar,
    charInfoMap: Dict[str, PlayerCharInfo],
    equipmentInfoMap: Dict[str, PlayerEquipmentInfo],
):
    avatar_bg = Image.open(TEXT_PATH / "avatar_bg.png").resize((118, 118))
    bar_img: Image.Image = Image.open(TEXT_PATH / "bar.png").convert("RGBA")

    charid = test_char.charId
    if charid == "char_1037_amiya3":
        charid = "char_1037_amiya3_2"
    ui_char_avatar = (
        Image.open(UI_CHAR_AVATAR_PATH / f"{charid}.png").resize((90, 90)).convert("RGBA")
    )
    bar_img.paste(avatar_bg, (24, 5), mask=avatar_bg)
    bar_img.paste(ui_char_avatar, (38, 21), mask=ui_char_avatar)

    potential_rank = test_char.potentialRank
    potential_img = Image.open(POTENTIAL_HUB_PATH / f"potential_{potential_rank}.png").resize(
        (45, 45)
    )
    bar_img.paste(potential_img, (135, 67), mask=potential_img)

    elite_level = test_char.evolvePhase
    elite_img = Image.open(ELITE_HUB_PATH / f"elite_{elite_level}_large.png")
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
    profession_img = Image.open(PROFESSION_PATH / f"icon_profession_{profession}_lighten.png")
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
            skill_img = Image.open(SKILL_ICONS_PATH / f"skill_icon_{skill_icon_id}.png")
            skill_img = skill_img.resize((70, 70))
            if test_char.defaultSkillId == skill_id:
                skill_img.paste(skill_selected, (38, -1), mask=skill_selected)
            skill_specialize_img = Image.open(
                CHAR_COMMON_PATH / f"evolve_small_icon_{skill_specialize_level}.png"
            )
            skill_img.paste(skill_specialize_img, (0, 0), mask=skill_specialize_img)
            skill_img = skill_img.resize((60, 60))
            bar_img.paste(skill_img, box=(355 + 70 * i, 37), mask=skill_img)

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
                UI_EQUIP_TYPE_DIRECTION_HUB_PATH / f"{equip_type_icon.lower()}.png"
            ).resize((92, 68))
            if test_char.defaultEquipId == equip_id.id_:
                bar_img.paste(equip_selected, (626 + 67 * i, 31), mask=equip_selected)
            bar_img.paste(equip_img, (616 + 68 * i, 32), mask=equip_img)

    return bar_img
