import sys

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
    ]:
        i.mkdir(parents=True, exist_ok=True)


init_dir()
