from gsuid_core.bot import Bot
from gsuid_core.models import Event
from gsuid_core.sv import SV

from ..utils.ark_prefix import PREFIX
from ..utils.database.models import ArknightsBind
from .get_char_snapshot import get_char_snapshot

sv_get_char_snapshot = SV("ark角色快照")


@sv_get_char_snapshot.on_command(f"角色快照")
async def send_char_snapshot(bot: Bot, ev: Event):
    user_id = ev.at if ev.at else ev.user_id
    uid = await ArknightsBind.get_uid_by_game(user_id, ev.bot_id)
    if uid is None:
        return "你还没有绑定UID噢,请使用[ark绑定uid123]完成绑定!"

    # 获取需要查询的页数
    cur_page = ev.text.strip()
    if cur_page.isdigit():
        cur_page = int(cur_page)
    else:
        cur_page = 1

    await bot.logger.info("开始执行[ark角色快照]")
    im = await get_char_snapshot(uid, cur_page)
    await bot.send(im)
