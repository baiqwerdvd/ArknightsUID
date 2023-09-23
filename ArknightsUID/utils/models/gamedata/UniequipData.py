from typing import Dict, List, Union
from ..common import BaseStruct
from msgspec import field


class ItemBundle(BaseStruct):
    id_: str = field(name='id')
    count: int
    type_: str = field(name='type')


class UnlockCondition(BaseStruct):
    phase: int
    level: int


class TraitDescBundle(BaseStruct):
    unlockCondition: UnlockCondition
    requiredPotentialRank: int
    overrideDescription: None
    additiveDescription: str


class UniEquipData(BaseStruct):
    uniEquipId: str
    uniEquipName: str
    uniEquipIcon: str
    uniEquipDesc: str
    typeIcon: str
    typeName: str
    showEvolvePhase: int
    unlockEvolvePhase: int
    charId: str
    tmplId: None
    showLevel: int
    unlockLevel: int
    unlockFavorPercent: int
    missionList: List[str]
    itemCost: Union[List[ItemBundle], None]
    type_: str = field(name='type')
    traitDescBundle: List[TraitDescBundle]


class UniEquipMissionData(BaseStruct):
    template: Union[str, None]
    desc: Union[str, None]
    paramList: List[str]
    uniEquipMissionId: str
    uniEquipMissionSort: int
    uniEquipId: str


class SubProfessionData(BaseStruct):
    subProfessionId: str
    subProfessionName: str
    subProfessionCatagory: int


class UniequipData(BaseStruct):
    __version__ = '23-07-27-18-50-06-aeb568'

    equipDict: Dict[str, UniEquipData]
    missionList: Dict[str, UniEquipMissionData]
    subProfDict: Dict[str, SubProfessionData]
    charEquip: Dict[str, List[str]]
