from typing import Any, Dict, Union

from gsuid_core.bot import Bot


async def send_diff_msg(bot: Bot, code: Any, data: Union[Dict, None] = None):
    if data is None:
        data = {
            0: '绑定UID成功!',
            -1: 'UID的位数不正确!',
            -2: 'UID已经绑定过了!',
            -3: '你输入了错误的格式!',
        }
    for retcode in data:
        if code == retcode:
            return await bot.send(data[retcode])
