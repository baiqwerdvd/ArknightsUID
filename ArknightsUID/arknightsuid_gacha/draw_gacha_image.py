from pathlib import Path
from typing import List, Tuple

from PIL import Image

from ..utils.resource.RESOURCE_PATH import CHARPORTRAITS_PATH

IMG_DIR = Path(__file__).parent / "texture2D"

GACHA_BG = Image.open(IMG_DIR / "bg.png")
print(GACHA_BG.size)
back_four = Image.open(IMG_DIR / "back_four.png").convert("RGBA").resize((115, 350))
print(back_four.size)
# (140 388)


async def draw_gacha_image(char_get: List[Tuple[str, int]]):
    if len(char_get) != 10:
        return
    img = GACHA_BG.copy().resize((1170, 580))
    print(img.size)
    for i, char in enumerate(char_get):
        char_name, star = char
        char_img = Image.open(CHARPORTRAITS_PATH / f"{char_name}_1.png").convert("RGBA")

        radio = 480 / img.size[1]

        width = int(char_img.size[0] * radio)
        height = int(char_img.size[1] * radio)

        step = int((width - 97) / 2)
        print(step)
        crop = (step - 2, 0, width - step - 1, height)
        print(width, height)

        char_img = char_img.resize((width, height))
        char_img = char_img.crop(crop)
        print(char_img.size)
        img.paste(back_four, box=(83 + 99 * i, 100), mask=back_four)
        img.paste(char_img, box=(90 + 99 * i, 135), mask=char_img)
        print(char_name, star)
        # img.show()
        # break
    img.show()


import asyncio

test: List[Tuple[str, int]] = [
    ("char_328_cammou", 4),
    ("char_473_mberry", 4),
    ("char_103_angel", 5),
    ("char_124_kroos", 2),
    ("char_130_doberm", 3),
    ("char_473_mberry", 4),
    ("char_103_angel", 5),
    ("char_124_kroos", 2),
    ("char_103_angel", 5),
    ("char_124_kroos", 2),
]

asyncio.run(draw_gacha_image(test))
