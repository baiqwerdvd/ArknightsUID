# from gsuid_core.bot import Bot
# from gsuid_core.logger import logger
# from gsuid_core.models import Event
# from gsuid_core.sv import SV

# from .get_help import get_core_help

# sv_ark_help = SV("ark帮助")


# @sv_ark_help.on_fullmatch(("帮助"))  # noqa: UP034
# async def send_help_img(bot: Bot, ev: Event):
#     logger.info("开始执行[ark帮助]")
#     im = await get_core_help()
#     await bot.send(im)

from gsuid_core.bot import Bot
from gsuid_core.help.utils import register_help
from gsuid_core.logger import logger
from gsuid_core.models import Event
from gsuid_core.sv import SV
from PIL import Image

from .get_help import ICON, get_help

sv_ark_help = SV("ark帮助")


@sv_ark_help.on_fullmatch("帮助")
async def send_help_img(bot: Bot, ev: Event):
    logger.info("开始执行[ark帮助]")
    im = await get_help()
    await bot.send(im)


register_help("ArknightsUID", "ark帮助", Image.open(ICON))
