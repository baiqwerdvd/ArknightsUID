from typing import Dict, List

from ..common import BaseStruct

from msgspec import field


class ItemBundle(BaseStruct):
    id_: str = field(name='id')
    count: int
    type_: str = field(name='type')


class SpCharMissionData(BaseStruct):
    charId: str
    missionId: str
    sortId: int
    condType: str
    param: List[str]
    rewards: List[ItemBundle]


class CharMetaTable(BaseStruct):
    __version__ = '23-10-31-11-47-45-d410ff'

    spCharGroups: Dict[str, List[str]]
    spCharMissions: Dict[str, Dict[str, SpCharMissionData]]
    spCharVoucherSkinTime: Dict[str, int]
