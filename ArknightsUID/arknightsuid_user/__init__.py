from typing import List

from gsuid_core.bot import Bot
from gsuid_core.models import Event
from gsuid_core.sv import SV

from ..utils.ark_prefix import PREFIX
from ..utils.database.models import ArknightsBind
from ..utils.message import send_diff_msg
from .deal_skd_cred import deal_skd_cred

# from .draw_user_card import get_user_card

sv_user_config = SV("ark用户管理", pm=2)
sv_user_add = SV("ark用户添加")
sv_user_info = SV("ark用户信息")
ark_skd_cred_add = SV("森空岛cred绑定")
# sv_user_help = SV('ark绑定帮助')


# @sv_user_info.on_fullmatch((f'{PREFIX}绑定信息'))
# async def send_bind_card(bot: Bot, ev: Event):
#     await bot.logger.info('ark开始执行[查询用户绑定状态]')
#     uid_list = await get_user_card(ev.bot_id, ev.user_id)
#     await bot.logger.info('ark[查询用户绑定状态]完成!等待图片发送中...')
#     await bot.send(uid_list)


@sv_user_info.on_command(
    (f"{PREFIX}绑定uid", f"{PREFIX}切换uid", f"{PREFIX}删除uid", f"{PREFIX}解绑uid")
)
async def send_link_uid_msg(bot: Bot, ev: Event):
    await bot.logger.info("开始执行[绑定/解绑用户信息]")
    qid = ev.user_id
    await bot.logger.info(f"[绑定/解绑]UserID: {qid}")

    ark_uid = ev.text.strip()
    if ark_uid and not ark_uid.isdigit():
        return await bot.send("你输入了错误的格式!")

    if "绑定" in ev.command:
        data = await ArknightsBind.insert_uid(qid, ev.bot_id, ark_uid, ev.group_id)
        return await send_diff_msg(
            bot,
            data,
            {
                0: f"绑定ARK_UID{ark_uid}成功!",
                -1: f"ARK_UID{ark_uid}的位数不正确!",
                -2: f"ARK_UID{ark_uid}已经绑定过了!",
                -3: "你输入了错误的格式!",
            },
        )
    elif "切换" in ev.command:
        data = await ArknightsBind.switch_uid_by_game(qid, ev.bot_id, ark_uid)
        if isinstance(data, List):
            return await bot.send(f"切换ARK_UID{ark_uid}成功!")
        else:
            return await bot.send(f"尚未绑定该ARK_UID{ark_uid}")
    else:
        data = await ArknightsBind.delete_uid(qid, ev.bot_id, ark_uid)
        return await send_diff_msg(
            bot,
            data,
            {
                0: f"删除ARK_UID{ark_uid}成功!",
                -1: f"该ARK_UID{ark_uid}不在已绑定列表中!",
            },
        )


@ark_skd_cred_add.on_prefix(("skd添加cred", "森空岛添加CRED"))
async def send_ark_skd_add_cred_msg(bot: Bot, ev: Event):
    im = await deal_skd_cred(ev.bot_id, ev.text, ev.user_id)
    await bot.send(im)
