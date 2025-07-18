from gsuid_core.bot import Bot
from gsuid_core.logger import logger
from gsuid_core.models import Event
from gsuid_core.sv import SV

from ..utils.ark_api import ark_skd_api
from ..utils.database.models import (
    ArknightsBind,
    ArknightsPush,
    ArknightsUser,
)
from ..utils.error_reply import UID_HINT
from .login import SklandLogin

sv_skland_login = SV("ark森空岛登录")


@sv_skland_login.on_prefix("森空岛登录")
async def get_resp_msg(bot: Bot, ev: Event):
    uid_list = await ArknightsBind.get_uid_list_by_game(ev.user_id, ev.bot_id)
    if uid_list is None:
        return await bot.send(UID_HINT)
    phone_number = ev.text.strip()
    if phone_number[0] == " ":
        phone_number = phone_number[1:]
    if not phone_number.isdigit():
        return await bot.send("你输入了错误的格式!")
    resp = await bot.receive_resp(
        f"请确认你的手机号码: {phone_number}. 如果正确请回复'确认', 其他任何回复将取消本次操作."
    )
    if resp is not None and resp.text == "确认":
        login = SklandLogin(phone_number)
        _ = login.send_phone_code()
        code = await bot.receive_resp("请输入验证码:")
        if code is None or not code.text.isdigit():
            return await bot.send("你输入了错误的格式!")
        logger.info(code.text)
        login.token_by_phone_code(code.text)
        # login.post_account_info_hg()
        await login.user_oauth2_v2_grant()
        await login.generate_cred_by_code()
        uid = login.ark_uid
        skd_uid = login.skland_userId

        # check_cred = await ark_skd_api.check_cred_valid(
        #     cred=skland_cred,
        #     token=skland_token,
        # )

        # if isinstance(check_cred, bool):
        #     return await bot.send("Cred Check 不通过!")
        # else:
        #     skd_uid = check_cred.user.id_
        #     uid = check_cred.gameStatus.uid
        if uid not in uid_list:
            return await bot.send("请先绑定该 Cred 对应的 uid")

        skd_data = await ArknightsUser.select_data_by_uid(uid)
        push_data = await ArknightsPush.select_data_by_uid(uid)
        if not skd_data:
            _ = await ArknightsUser.insert_data(
                ev.user_id,
                ev.bot_id,
                cred=login.skland_cred,
                uid=uid,
                skd_uid=skd_uid,
                token=login.skland_token,
            )
        else:
            _ = await ArknightsUser.update_data(
                ev.user_id,
                ev.bot_id,
                cred=login.skland_cred,
                uid=uid,
                skd_uid=skd_uid,
                token=login.skland_token,
            )
        if not push_data:
            await ArknightsPush.insert_push_data(ev.bot_id, uid=uid, skd_uid=skd_uid)
        return await bot.send("登录成功!")
