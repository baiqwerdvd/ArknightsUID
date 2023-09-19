import re
from ..utils.ark_api import ark_skd_api
from ..utils.database.models import ArknightsBind, ArknightsUser

ERROR_HINT = '添加失败, 格式为: skd添加cred Cred 例如: skd添加cred VropL583Sb1hClS5buQ4nSASkDlL8tMT'
UID_HINT = '添加失败, 请先绑定明日方舟UID'


async def deal_skd_cred(bot_id: str, cred: str, user_id: str) -> str:
    uid_list = await ArknightsBind.get_uid_list_by_game(user_id, bot_id)
    if uid_list is None:
        return UID_HINT
    
    match = re.search(r'\S+', cred)
    if not match:
        return 'Cred无效!'

    # refresh token
    token = await ark_skd_api.refresh_token(match.group())
    print(token)

    check_cred = await ark_skd_api.check_cred_valid(cred=match.group(), token=token)

    if isinstance(check_cred, bool):
        return 'Cred无效!'
    else:
        skd_uid = check_cred.user.id_
        uid = check_cred.gameStatus.uid
    if uid not in uid_list:
        return '请先绑定该 Cred 对应的 uid'

    # 检查是否已经绑定过 Cred, 如果有的话就 update
    skd_data = await ArknightsUser.select_data_by_uid(uid)
    if not skd_data:
        await ArknightsUser.insert_data(user_id, bot_id,
                                        cred=match.group(), uid=uid, skd_uid=skd_uid, token=token)
    else:
        await ArknightsUser.update_data(user_id, bot_id,
                                        cred=match.group(), uid=uid, skd_uid=skd_uid, token=token)
    return '添加成功!'
