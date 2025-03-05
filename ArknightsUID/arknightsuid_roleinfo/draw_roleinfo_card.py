from pathlib import Path

from gsuid_core.data_store import get_res_path
from gsuid_core.utils.error_reply import get_error
from gsuid_core.utils.image.convert import convert_img
from msgspec import json as msgjson
from PIL import Image, ImageDraw

from ..utils.ark_api import ark_skd_api
from ..utils.fonts.source_han_serif import sans_font_28
from ..utils.resource.RESOURCE_PATH import SKINPACK_PATH

TEXT_PATH = Path(__file__).parent / "texture2D"
bg_img = Image.open(TEXT_PATH / "bg.png")
base_info_img = Image.open(TEXT_PATH / "base_info.png")


async def get_role_img(uid: str):
    player_info = await ark_skd_api.get_game_player_info(uid)
    if isinstance(player_info, int):
        return get_error(player_info)

    player_save_path = get_res_path(["ArknightsUID", "players"])

    with Path.open(player_save_path / f"{player_info.status.uid}.json", "wb") as file:
        file.write(msgjson.format(msgjson.encode(player_info), indent=4))

    # 放 background
    char_info = bg_img.copy()

    # 放干员主立绘
    secretary = player_info.status.secretary
    # secretary_charId = secretary.charId
    secretary_skinId = secretary.skinId.replace("@", "_")

    secretary_char_img = Image.open(SKINPACK_PATH / f"{secretary_skinId}b.png").resize((768, 768)).convert("RGBA")
    char_info.paste(secretary_char_img, (0, -20), secretary_char_img)

    # 放基础信息
    base_info = base_info_img.copy()
    base_info_draw = ImageDraw.Draw(base_info)
    base_info_draw.text(
        (400, 163),
        player_info.status.name,
        (255, 255, 255),
        sans_font_28,
        "lm",
    )

    # 放入职信息

    base_info.resize((475, 400)).convert("RGBA")
    char_info.paste(base_info, (200, 0), base_info)

    char_info.show()

    res = await convert_img(char_info)
    return res
