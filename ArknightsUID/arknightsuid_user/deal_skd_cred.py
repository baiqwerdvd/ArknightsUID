from ..utils.ark_api import ark_skd_api
from ..utils.database.models import ArknightsUser

ERROR_HINT = '添加失败，格式为:明日方舟UID - Cred\n \
            例如:1810461245 - VropL583Sb1hClS5buQ4nSASkDlL8tMT'


async def deal_skd_cred(bot_id: str, cred: str, user_id: str) -> str:
    if '-' not in cred:
        return ERROR_HINT
    _ck = cred.replace(' ', '').split('-')
    if len(_ck) != 2 or not _ck[0] or not _ck[0].isdigit() or not _ck[1]:
        return ERROR_HINT

    check_cred = await ark_skd_api.check_cred_valid(_ck[1])
    if isinstance(check_cred, bool):
        return 'Cred无效!'
    else:
        skd_uid = check_cred.user.id_
    uid, cred = _ck[0], _ck[1]
    await ArknightsUser.insert_data(user_id, bot_id,
                                    cred=cred, uid=uid, skd_uid=skd_uid)
    return '添加成功!'
