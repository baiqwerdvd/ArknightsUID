from typing import Dict, List, Union

from ..common import BaseStruct

from msgspec import field


class CharacterDataUnlockCondition(BaseStruct):
    phase: int
    level: int


class Blackboard(BaseStruct):
    key: str
    value: Union[float, None] = None
    valueStr: Union[str, None] = None


class CharacterDataTraitData(BaseStruct):
    unlockCondition: CharacterDataUnlockCondition
    requiredPotentialRank: int
    blackboard: List[Blackboard]
    overrideDescripton: Union[str, None]
    prefabKey: Union[str, None]
    rangeId: Union[str, None]


class CharacterDataTraitDataBundle(BaseStruct):
    candidates: List[CharacterDataTraitData]


class AttributesData(BaseStruct):
    maxHp: int
    atk: int
    def_: int = field(name='def')
    magicResistance: float
    cost: int
    blockCnt: int
    moveSpeed: float
    attackSpeed: float
    baseAttackTime: float
    respawnTime: int
    hpRecoveryPerSec: float
    spRecoveryPerSec: float
    maxDeployCount: int
    maxDeckStackCnt: int
    tauntLevel: int
    massLevel: int
    baseForceLevel: int
    stunImmune: bool
    silenceImmune: bool
    sleepImmune: bool
    frozenImmune: bool
    levitateImmune: bool
    disarmedCombatImmune: bool


class CharacterDataAttributesKeyFrame(BaseStruct):
    level: int
    data: AttributesData


class ItemBundle(BaseStruct):
    id_: str = field(name='id')
    count: int
    type_: str = field(name='type')


class CharacterDataPhaseData(BaseStruct):
    characterPrefabKey: str
    rangeId: Union[str, None]
    maxLevel: int
    attributesKeyFrames: List[CharacterDataAttributesKeyFrame]
    evolveCost: Union[List[ItemBundle], None]


class CharacterDataMainSkillSpecializeLevelData(BaseStruct):
    unlockCond: CharacterDataUnlockCondition
    lvlUpTime: int
    levelUpCost: Union[List[ItemBundle], None]


class CharacterDataMainSkill(BaseStruct):
    skillId: Union[str, None]
    overridePrefabKey: Union[str, None]
    overrideTokenKey: Union[str, None]
    levelUpCostCond: List[CharacterDataMainSkillSpecializeLevelData]
    unlockCond: CharacterDataUnlockCondition


class TalentData(BaseStruct):
    unlockCondition: CharacterDataUnlockCondition
    requiredPotentialRank: int
    prefabKey: str
    name: Union[str, None]
    description: Union[str, None]
    rangeId: Union[str, None]
    blackboard: List[Blackboard]


class CharacterDataTalentDataBundle(BaseStruct):
    candidates: Union[List[TalentData], None]


class AttributeModifierDataAttributeModifier(BaseStruct):
    attributeType: int
    formulaItem: int
    value: float
    loadFromBlackboard: bool
    fetchBaseValueFromSourceEntity: bool


class AttributeModifierData(BaseStruct):
    abnormalFlags: Union[List[str], None]
    abnormalImmunes: Union[List[str], None]
    abnormalAntis: Union[List[str], None]
    abnormalCombos: Union[List[str], None]
    abnormalComboImmunes: Union[List[str], None]
    attributeModifiers: List[AttributeModifierDataAttributeModifier]


class ExternalBuff(BaseStruct):
    attributes: AttributeModifierData


class CharacterDataPotentialRank(BaseStruct):
    type_: int = field(name='type')
    description: str
    buff: Union[ExternalBuff, None]
    equivalentCost: Union[ItemBundle, None]


class CharacterDataSkillLevelCost(BaseStruct):
    unlockCond: CharacterDataUnlockCondition
    lvlUpCost: Union[List[ItemBundle], None]


class TokenCharacterData(BaseStruct):
    name: str
    description: Union[str, None]
    canUseGeneralPotentialItem: bool
    canUseActivityPotentialItem: bool
    potentialItemId: Union[str, None]
    activityPotentialItemId: Union[str, None]
    nationId: Union[str, None]
    groupId: Union[str, None]
    teamId: Union[str, None]
    displayNumber: Union[str, None]
    appellation: str
    position: str
    tagList: Union[List[str], None]
    itemUsage: Union[str, None]
    itemDesc: Union[str, None]
    itemObtainApproach: Union[str, None]
    isNotObtainable: bool
    isSpChar: bool
    maxPotentialLevel: int
    rarity: int
    profession: str
    subProfessionId: str
    trait: Union[CharacterDataTraitDataBundle, None]
    phases: List[CharacterDataPhaseData]
    skills: Union[List[CharacterDataMainSkill], None]
    talents: Union[List[CharacterDataTalentDataBundle], None]
    potentialRanks: Union[List[CharacterDataPotentialRank], None]
    favorKeyFrames: Union[List[CharacterDataAttributesKeyFrame], None]
    allSkillLvlup: Union[List[CharacterDataSkillLevelCost], None]
    minPowerId: str
    maxPowerId: str
    tokenKey: Union[str, None] = None


class TokenTable(BaseStruct):
    __version__ = '23-12-02-09-28-50-918524'

    tokens: Dict[str, TokenCharacterData]
