from typing import Dict, List, Union

from ..common import BaseStruct

from msgspec import field


class ItemBundle(BaseStruct):
    id_: str = field(name='id')
    count: int
    type_: str = field(name='type')


class SpData(BaseStruct):
    spType: int
    levelUpCost: Union[List[ItemBundle], None]
    maxChargeTime: int
    spCost: int
    initSp: int
    increment: Union[int, float]


class Blackboard(BaseStruct):
    key: str
    value: Union[Union[int, float], None] = None
    valueStr: Union[str, None] = None


class SkillDataBundleLevelData(BaseStruct):
    name: str
    rangeId: Union[str, None]
    description: Union[str, None]
    skillType: int
    durationType: int
    spData: SpData
    prefabId: Union[str, None]
    duration: Union[int, float]
    blackboard: List[Blackboard]


class SkillDataBundle(BaseStruct):
    skillId: str
    iconId: Union[str, None]
    hidden: bool
    levels: List[SkillDataBundleLevelData]


class SkillTable(BaseStruct):
    __version__ = '24-02-02-10-18-07-831ad8'

    skills: Dict[str, SkillDataBundle]
