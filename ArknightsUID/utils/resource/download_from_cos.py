from gsuid_core.utils.download_resource.download_core import download_all_file

from .RESOURCE_PATH import (
    CHAR_AVATAR_PATH,
    CHARARTS_PATH,
    GAMEDATA_PATH,
    MEDAL_DIY_FRAME_BKG_PATH,
    MEDAL_ICONS_PATH,
    PLAYER_AVATAR_LIST,
    SKILL_ICONS_PATH,
    SKINPACK_PATH,
    SUB_PROFESSION_ICON_PATH,
    TEAM_ICON_PATH,
)


async def download_all_file_from_cos():
    await download_all_file(
        'ArknightsUID',
        {
            'resource/gamedata': GAMEDATA_PATH,
            'resource/char_avatar': CHAR_AVATAR_PATH,
            'resource/chararts': CHARARTS_PATH,
            'resource/medal_diy_frame_bkg': MEDAL_DIY_FRAME_BKG_PATH,
            'resource/medal_icons': MEDAL_ICONS_PATH,
            'resource/player_avatar_list': PLAYER_AVATAR_LIST,
            'resource/skill_icons': SKILL_ICONS_PATH,
            'resource/skinpack': SKINPACK_PATH,
            'resource/sub_profession_icon': SUB_PROFESSION_ICON_PATH,
            'resource/team_icon': TEAM_ICON_PATH,
        },
    )
