UID_HINT = '添加失败, 请先绑定明日方舟UID'

def get_error(retcode: int | str) -> str:
    if retcode == 10001:
        return '请求体出错, 请检查具体实现代码...'
    if retcode == -10001:
        return '请求体出错, 请检查具体实现代码...'
    if retcode == -201:
        return '你的账号可能已被封禁, 请联系米游社客服...'
    if retcode == -501101:
        return '当前角色冒险等阶未达到10级, 暂时无法参加此活动...'
    if retcode == 400:
        return '[MINIGG]暂未找到此内容...'
    if retcode == -400:
        return '请输入更详细的名称...'
    return f'API报错, 错误码为{retcode}!'