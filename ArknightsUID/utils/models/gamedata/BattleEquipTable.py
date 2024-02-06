from typing import Dict, List, Union

from ..common import BaseStruct


class CharacterDataUnlockCondition(BaseStruct):
    phase: int
    level: int


class Blackboard(BaseStruct):
    key: str
    value: Union[float, None] = None
    valueStr: Union[str, None] = None


class TalentData(BaseStruct):
    unlockCondition: CharacterDataUnlockCondition
    requiredPotentialRank: int
    prefabKey: Union[str, None]
    name: Union[str, None]
    description: Union[str, None]
    rangeId: Union[str, None]
    blackboard: List[Blackboard]


class EquipTalentData(TalentData):
    displayRangeId: bool
    upgradeDescription: str
    talentIndex: int
    tokenKey: Union[str, None] = None


class CharacterDataEquipTalentDataBundle(BaseStruct):
    candidates: Union[List[EquipTalentData], None]


class CharacterDataTraitData(BaseStruct):
    unlockCondition: CharacterDataUnlockCondition
    requiredPotentialRank: int
    blackboard: List[Blackboard]
    overrideDescripton: Union[str, None]
    prefabKey: Union[str, None]
    rangeId: Union[str, None]


class CharacterDataEquipTraitData(BaseStruct):
    additionalDescription: Union[str, None]
    unlockCondition: CharacterDataUnlockCondition
    requiredPotentialRank: int
    blackboard: List[Blackboard]
    overrideDescripton: Union[str, None]
    prefabKey: Union[str, None]
    rangeId: Union[str, None]


class CharacterDataEquipTraitDataBundle(BaseStruct):
    candidates: Union[List[CharacterDataEquipTraitData], None]


class BattleUniEquipData(BaseStruct):
    resKey: Union[str, None]
    target: str
    isToken: bool
    addOrOverrideTalentDataBundle: CharacterDataEquipTalentDataBundle
    overrideTraitDataBundle: CharacterDataEquipTraitDataBundle


class BattleEquipPerLevelPack(BaseStruct):
    equipLevel: int
    parts: List[BattleUniEquipData]
    attributeBlackboard: List[Blackboard]
    tokenAttributeBlackboard: Dict[str, List[Blackboard]]


class BattleEquipData(BaseStruct):
    phases: List[BattleEquipPerLevelPack]


class BattleEquipTable(BaseStruct):
    __version__ = '24-02-02-10-18-07-831ad8'

    equips: Dict[str, BattleEquipData]
