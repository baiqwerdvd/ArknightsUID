import math
from datetime import datetime

from ..utils.models.skland.models import PlayerStatusAp


def seconds2hours_zhcn(seconds: int) -> str:
    m, s = divmod(int(seconds), 60)
    h, m = divmod(m, 60)
    return f"{h}小时{m}分钟"


def now_ap(ap: PlayerStatusAp) -> int:
    _ap = ap.current + math.floor((datetime.now().timestamp() - ap.lastApAddTime) / 360)
    return _ap if _ap <= ap.max else ap.max
