from pathlib import Path

import aiofiles
from gsuid_core.help.draw_plugin_help import get_help
from gsuid_core.help.model import PluginHelp
from msgspec import json as msgjson
from PIL import Image

from ..utils.fonts.source_han_sans import source_han_sans_cn_origin
from ..version import Arknights_Client_version

TEXT_PATH = Path(__file__).parent / 'texture2d'
HELP_DATA = Path(__file__).parent / 'Help.json'


async def get_help_data() -> dict[str, PluginHelp] | None:
    if HELP_DATA.exists():
        async with aiofiles.open(HELP_DATA, 'rb') as file:
            return msgjson.decode(
                await file.read(), type=dict[str, PluginHelp],
            )


async def get_core_help() -> bytes | str:
    help_data = await get_help_data()
    if help_data is None:
        return '暂未找到帮助数据...'

    img = await get_help(
        'ArknightsUID',
        f'版本号:{Arknights_Client_version}',
        help_data,
        Image.open(TEXT_PATH / 'bg.jpg'),
        Image.open(TEXT_PATH / 'icon.png'),
        Image.open(TEXT_PATH / 'badge.png'),
        Image.open(TEXT_PATH / 'banner.png'),
        Image.open(TEXT_PATH / 'button.png'),
        source_han_sans_cn_origin,
    )
    return img
