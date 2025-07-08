import json
from pathlib import Path

import aiofiles
from gsuid_core.help.draw_new_plugin_help import get_new_help
from gsuid_core.help.model import PluginHelp
from gsuid_core.sv import get_plugin_available_prefix
from PIL import Image

from ..version import (
    Arknights_Client_version,
    Arknights_Res_version,
    ArknightsUID_version,
)

ICON = Path(__file__).parent.parent.parent / "ICON.png"
TEXT_PATH = Path(__file__).parent / "texture2d"
HELP_DATA = Path(__file__).parent / "Help.json"

PREFIX = get_plugin_available_prefix("ArknightsUID")


async def get_help_data() -> dict[str, PluginHelp]:
    async with aiofiles.open(HELP_DATA, "rb") as file:
        return json.loads(await file.read())


# async def get_core_help() -> bytes | str:
#     help_data = await get_help_data()
#     if help_data is None:
#         return "暂未找到帮助数据..."

#     img = await get_help(
#         "ArknightsUID",
#         f"版本号:{ArknightsUID_version}",
#         help_data,
#         Image.open(TEXT_PATH / "bg.jpg"),
#         Image.open(TEXT_PATH / "icon.png"),
#         Image.open(TEXT_PATH / "badge.png"),
#         Image.open(TEXT_PATH / "banner.png"),
#         Image.open(TEXT_PATH / "button.png"),
#         source_han_sans_cn_origin,
#         extra_message=[f"Client Version:{Arknights_Client_version}  Res version: {Arknights_Res_version}"],
#     )
#     return img


async def get_help():
    return await get_new_help(
        plugin_name="ArknightsUID",
        plugin_info={f"v{ArknightsUID_version}": ""},
        plugin_icon=Image.open(TEXT_PATH / "icon.png"),
        plugin_help=await get_help_data(),
        plugin_prefix=PREFIX,
        help_mode="dark",
        banner_sub_text=f"Client Version:{Arknights_Client_version}  Res version: {Arknights_Res_version}",
        help_bg=Image.open(TEXT_PATH / "bg.jpg"),
        enable_cache=True,
    )
