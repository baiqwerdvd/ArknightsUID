UID_HINT = '添加失败, 请先绑定明日方舟UID'

def get_error(retcode: int | str) -> str:
    if retcode == 10000:
        return '请求异常, 请检查具体实现代码...'
    if retcode == 10001:
        return '请勿重复签到！'
    if retcode == 10003:
        return '请勿修改设备时间'
    return f'API报错, 错误码为{retcode}!'