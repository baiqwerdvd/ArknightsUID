from gsuid_core.bot import Bot
from gsuid_core.logger import logger
from gsuid_core.models import Event
from gsuid_core.sv import SV

from ..utils.ark_prefix import PREFIX
from .get_help import get_core_help

sv_sr_help = SV('ark帮助')


@sv_sr_help.on_fullmatch((f'{PREFIX}帮助'))  # noqa: UP034
async def send_help_img(bot: Bot, ev: Event):
    logger.info('开始执行[ark帮助]')
    im = await get_core_help()
    await bot.send(im)
