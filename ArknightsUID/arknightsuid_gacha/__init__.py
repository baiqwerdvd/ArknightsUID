from gsuid_core.bot import Bot
from gsuid_core.models import Event
from gsuid_core.sv import SV

from ..utils.ark_prefix import PREFIX
from ..utils.database.models import ArknightsBind
from .gacha import gacha

sv_ark_gacha = SV("ark十连")


@sv_ark_gacha.on_fullmatch(f"{PREFIX}十连")
async def send_gacha_info(bot: Bot, ev: Event):
    return "WIP"
    user_id = ev.at if ev.at else ev.user_id
    uid = await ArknightsBind.get_uid_by_game(user_id, ev.bot_id)
    if uid is None:
        return "你还没有绑定UID噢,请使用[ark绑定uid123]完成绑定!"

    await bot.logger.info("开始执行[ark角色快照]")
    im = await gacha(uid)
    await bot.send(im)
