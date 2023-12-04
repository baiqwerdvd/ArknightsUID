import re

from gsuid_core.bot import Bot
from gsuid_core.models import Event
from gsuid_core.plugins.ArknightsUID.ArknightsUID.arknightsuid_wiki.draw_wiki_img import (
    get_equip_info,
    get_wiki_info,
)
from gsuid_core.sv import SV
from gsuid_core.utils.image.convert import convert_img
from gsuid_core.utils.image.image_tools import draw_center_text_by_line
from PIL import Image, ImageDraw

from ..arknightsuid_resource.constants import Excel
from ..utils.fonts.source_han_sans import sans_font_20

sv_sr_wiki = SV('arkWIKI')


async def text2pic(text: str, max_size: int = 800, font_size: int = 20):
    if text.endswith('\n'):
        text = text[:-1]

    img = Image.new(
        'RGB', (max_size, len(text) * font_size // 5), (228, 222, 210)
    )
    img_draw = ImageDraw.ImageDraw(img)
    y = draw_center_text_by_line(
        img_draw, (25, 0), text, sans_font_20, 'black', 750, True
    )
    img = img.crop((0, 0, 800, int(y + 30)))
    return await convert_img(img)


@sv_sr_wiki.on_prefix('ark角色图鉴')
async def send_role_wiki_pic(bot: Bot, ev: Event):
    char_name = ' '.join(re.findall('[\u4e00-\u9fa5]+', ev.text))

    CHARACTER_TABLE = Excel.CHARATER_TABLE

    char_id = None
    for char_id_, char_info in CHARACTER_TABLE.chars.items():
        if char_info.name == char_name:
            char_id = char_id_
            break
    if not char_id:
        await bot.send('未找到该干员')
        return
    await bot.logger.info(f'开始获取{char_name}图鉴')
    img = await get_wiki_info(char_id=char_id)
    await bot.send(await text2pic(img))

@sv_sr_wiki.on_prefix('ark模组图鉴')
async def send_equip_wiki_pic(bot: Bot, ev: Event):
    char_name = ' '.join(re.findall('[\u4e00-\u9fa5]+', ev.text))

    CHARACTER_TABLE = Excel.CHARATER_TABLE

    char_id = None
    for char_id_, char_info in CHARACTER_TABLE.chars.items():
        if char_info.name == char_name:
            char_id = char_id_
            break
    if not char_id:
        await bot.send('未找到该干员')
        return
    await bot.logger.info(f'开始获取{char_name}图鉴')
    img = await get_equip_info(char_id=char_id)
    await bot.send(await text2pic(img))
