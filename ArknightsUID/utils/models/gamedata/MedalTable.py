from typing import Dict, List, Union

from ..common import BaseStruct

from msgspec import field


class MedalExpireTime(BaseStruct):
    start: int
    end: int
    type_: str = field(name='type')


class ItemBundle(BaseStruct):
    id_: str = field(name='id')
    count: int
    type_: str = field(name='type')


class MedalGroupData(BaseStruct):
    groupId: str
    groupName: str
    groupDesc: str
    medalId: List[str]
    sortId: int
    groupBackColor: str
    groupGetTime: int
    sharedExpireTimes: Union[List[MedalExpireTime], None]


class MedalRewardGroupData(BaseStruct):
    groupId: str
    slotId: int
    itemList: List[ItemBundle]


class MedalTypeData(BaseStruct):
    medalGroupId: str
    sortId: int
    medalName: str
    groupData: List[MedalGroupData]


class MedalPerData(BaseStruct):
    medalId: Union[str, None]
    medalName: Union[str, None]
    medalType: Union[str, None]
    slotId: Union[int, None]
    preMedalIdList: Union[List[str], None]
    rarity: int
    template: Union[str, None]
    unlockParam: List[str]
    getMethod: Union[str, None]
    description: Union[str, None]
    advancedMedal: Union[str, None]
    originMedal: Union[str, None]
    displayTime: int
    expireTimes: List[MedalExpireTime]
    medalRewardGroup: List[MedalRewardGroupData]
    isHidden: Union[bool, None] = None


class MedalTable(BaseStruct):
    __version__ = '24-02-02-10-18-07-831ad8'

    medalList: List[MedalPerData]
    medalTypeData: Dict[str, MedalTypeData]
