from gsuid_core.utils.download_resource.download_core import download_all_file

from .RESOURCE_PATH import (
    CHAR_AVATAR_PATH,
    CHAR_COMMON_PATH,
    CHARARTS_PATH,
    CHARPORTRAITS_PATH,
    ELITE_HUB_PATH,
    GAMEDATA_PATH,
    MEDAL_DIY_FRAME_BKG_PATH,
    MEDAL_ICONS_PATH,
    PLAYER_AVATAR_LIST,
    POTENTIAL_HUB_PATH,
    PROFESSION_PATH,
    SKILL_ICONS_PATH,
    SKINPACK_PATH,
    SUB_PROFESSION_ICON_PATH,
    TEAM_ICON_PATH,
    UI_CHAR_AVATAR_PATH,
    UI_EQUIP_TYPE_DIRECTION_HUB_PATH,
    UI_PLAYER_AVATAR_LIST_PATH,
)


async def download_all_file_from_cos():
    await download_all_file(
        "ArknightsUID",
        {
            "resource/gamedata": GAMEDATA_PATH,
            "resource/char_avatar": CHAR_AVATAR_PATH,
            "resource/chararts": CHARARTS_PATH,
            "resource/medal_diy_frame_bkg": MEDAL_DIY_FRAME_BKG_PATH,
            "resource/medal_icons": MEDAL_ICONS_PATH,
            "resource/player_avatar_list": PLAYER_AVATAR_LIST,
            "resource/skill_icons": SKILL_ICONS_PATH,
            "resource/skinpack": SKINPACK_PATH,
            "resource/sub_profession_icon": SUB_PROFESSION_ICON_PATH,
            "resource/team_icon": TEAM_ICON_PATH,
            "resource/ui_char_avatar": UI_CHAR_AVATAR_PATH,
            "resource/ui_player_avatar_list_h2": UI_PLAYER_AVATAR_LIST_PATH,
            "resource/ui_equip_type_direction_hub_h2": UI_EQUIP_TYPE_DIRECTION_HUB_PATH,
            "resource/potential_hub": POTENTIAL_HUB_PATH,
            "resource/elite_hub": ELITE_HUB_PATH,
            "resource/profession": PROFESSION_PATH,
            "resource/charcommon": CHAR_COMMON_PATH,
            "resource/charportraits": CHARPORTRAITS_PATH,
        },
    )
