from typing import Dict, List

from msgspec import field

from ..common import BaseStruct


class ItemBundle(BaseStruct):
    id_: str = field(name="id")
    count: int
    type_: str = field(name="type")


class MonthlySignInData(BaseStruct):
    itemId: str
    itemType: str
    count: int


class MonthlySignInGroupData(BaseStruct):
    groupId: str
    title: str
    description: str
    signStartTime: int
    signEndTime: int
    items: List[MonthlySignInData]


class MonthlyDailyBonusGroup(BaseStruct):
    groupId: str
    startTime: int
    endTime: int
    items: List[ItemBundle]
    imgId: str
    backId: str


class CheckinTable(BaseStruct):
    __version__ = "24-02-02-10-18-07-831ad8"

    groups: Dict[str, MonthlySignInGroupData]
    monthlySubItem: Dict[str, List[MonthlyDailyBonusGroup]]
    currentMonthlySubId: str
