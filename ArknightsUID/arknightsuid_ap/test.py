from pathlib import Path

from PIL import Image

path = Path(__file__).parent / 'texture2D'

char = Image.open(path / 'char_1028_texas2_1b.png')
mask = Image.open(path / 'mask.png')
img = Image.new('RGB',(850,1750))
temp_img = Image.new('RGB',(850,1750))
temp_img.paste(char, (-500,0), char )
img.paste(temp_img, (0,0), mask)
img.show()
