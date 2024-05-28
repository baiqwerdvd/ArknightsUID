import sys
from tkinter import CHAR

from gsuid_core.data_store import get_res_path

MAIN_PATH = get_res_path() / "ArknightsUID"
sys.path.append(str(MAIN_PATH))

CU_BG_PATH = MAIN_PATH / "bg"
CONFIG_PATH = MAIN_PATH / "config.json"
PLAYER_PATH = MAIN_PATH / "players"
RESOURCE_PATH = MAIN_PATH / "resource"


GAMEDATA_PATH = RESOURCE_PATH / "gamedata"

CHAR_AVATAR_PATH = RESOURCE_PATH / "char_avatar"
CHARARTS_PATH = RESOURCE_PATH / "chararts"
MEDAL_DIY_FRAME_BKG_PATH = RESOURCE_PATH / "medal_diy_frame_bkg"
MEDAL_ICONS_PATH = RESOURCE_PATH / "medal_icons"
PLAYER_AVATAR_LIST = RESOURCE_PATH / "player_avatar_list"
SKILL_ICONS_PATH = RESOURCE_PATH / "skill_icons"
SKINPACK_PATH = RESOURCE_PATH / "skinpack"
SUB_PROFESSION_ICON_PATH = RESOURCE_PATH / "sub_profession_icon"
TEAM_ICON_PATH = RESOURCE_PATH / "team_icon"
UI_CHAR_AVATAR_PATH = RESOURCE_PATH / "ui_char_avatar"
UI_PLAYER_AVATAR_LIST_PATH = RESOURCE_PATH / "ui_player_avatar_list_h2"
UI_EQUIP_TYPE_DIRECTION_HUB_PATH = RESOURCE_PATH / "ui_equip_type_direction_hub_h2"
POTENTIAL_HUB_PATH = RESOURCE_PATH / "potential_hub"
ELITE_HUB_PATH = RESOURCE_PATH / "elite_hub"
PROFESSION_PATH = RESOURCE_PATH / "profession"
CHAR_COMMON_PATH = RESOURCE_PATH / "charcommon"
CHARPORTRAITS_PATH = RESOURCE_PATH / "charportraits"


def init_dir():
    for i in [
        MAIN_PATH,
        CU_BG_PATH,
        PLAYER_PATH,
        RESOURCE_PATH,
        GAMEDATA_PATH,
        SKINPACK_PATH,
        CHAR_AVATAR_PATH,
        CHARARTS_PATH,
        MEDAL_DIY_FRAME_BKG_PATH,
        MEDAL_ICONS_PATH,
        PLAYER_AVATAR_LIST,
        SKILL_ICONS_PATH,
        SKINPACK_PATH,
        SUB_PROFESSION_ICON_PATH,
        TEAM_ICON_PATH,
        UI_CHAR_AVATAR_PATH,
        UI_PLAYER_AVATAR_LIST_PATH,
        UI_EQUIP_TYPE_DIRECTION_HUB_PATH,
        POTENTIAL_HUB_PATH,
        ELITE_HUB_PATH,
        PROFESSION_PATH,
        CHAR_COMMON_PATH,
        CHARPORTRAITS_PATH,
    ]:
        i.mkdir(parents=True, exist_ok=True)


init_dir()
