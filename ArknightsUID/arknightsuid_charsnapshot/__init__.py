from gsuid_core.bot import Bot
from gsuid_core.models import Event
from gsuid_core.sv import SV
from gsuid_core.utils.database.api import get_uid

from ..utils.ark_prefix import PREFIX
from ..utils.database.models import ArknightsBind
from .get_char_snapshot import get_char_snapshot

sv_get_char_snapshot = SV("ark角色快照")


@sv_get_char_snapshot.on_fullmatch(f"{PREFIX}角色快照")
async def send_char_snapshot(bot: Bot, ev: Event):
    uid = await get_uid(bot, ev, bind_model=ArknightsBind)
    if uid is None:
        return "你还没有绑定UID噢,请使用[ark绑定uid123]完成绑定!"

    await bot.logger.info("开始执行[ark角色快照]")
    await get_char_snapshot(uid)
