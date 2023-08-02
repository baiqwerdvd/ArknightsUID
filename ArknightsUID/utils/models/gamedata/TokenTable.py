from pydantic import BaseModel, Field

# 部分数据似乎不是float类型,等之后问问dice吧awa


class CharacterDataUnlockCondition(BaseModel):
    phase: int
    level: int


class Blackboard(BaseModel):
    key: str
    value: float | None = None
    valueStr: str | None = None


class CharacterDataTraitData(BaseModel):
    unlockCondition: CharacterDataUnlockCondition
    requiredPotentialRank: int
    blackboard: list[Blackboard]
    overrideDescripton: str | None
    prefabKey: str | None
    rangeId: str | None


class CharacterDataTraitDataBundle(BaseModel):
    candidates: list[CharacterDataTraitData]


class AttributesData(BaseModel):
    maxHp: int
    atk: int
    def_: int = Field(..., alias='def')
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


class CharacterDataAttributesKeyFrame(BaseModel):
    level: int
    data: AttributesData


class ItemBundle(BaseModel):
    id_: str = Field(..., alias='id')
    count: int
    type_: str = Field(..., alias='type')


class CharacterDataPhaseData(BaseModel):
    characterPrefabKey: str
    rangeId: str | None
    maxLevel: int
    attributesKeyFrames: list[CharacterDataAttributesKeyFrame]
    evolveCost: list[ItemBundle] | None


class CharacterDataMainSkillSpecializeLevelData(BaseModel):
    unlockCond: CharacterDataUnlockCondition
    lvlUpTime: int
    levelUpCost: list[ItemBundle] | None


class CharacterDataMainSkill(BaseModel):
    skillId: str | None
    overridePrefabKey: str | None
    overrideTokenKey: str | None
    levelUpCostCond: list[CharacterDataMainSkillSpecializeLevelData]
    unlockCond: CharacterDataUnlockCondition


class TalentData(BaseModel):
    unlockCondition: CharacterDataUnlockCondition
    requiredPotentialRank: int
    prefabKey: str
    name: str | None
    description: str | None
    rangeId: str | None
    blackboard: list[Blackboard]


class CharacterDataTalentDataBundle(BaseModel):
    candidates: list[TalentData] | None


class AttributeModifierDataAttributeModifier(BaseModel):
    attributeType: int
    formulaItem: int
    value: float
    loadFromBlackboard: bool
    fetchBaseValueFromSourceEntity: bool


class AttributeModifierData(BaseModel):
    abnormalFlags: list[str] | None
    abnormalImmunes: list[str] | None
    abnormalAntis: list[str] | None
    abnormalCombos: list[str] | None
    abnormalComboImmunes: list[str] | None
    attributeModifiers: list[AttributeModifierDataAttributeModifier]


class ExternalBuff(BaseModel):
    attributes: AttributeModifierData


class CharacterDataPotentialRank(BaseModel):
    type_: int = Field(..., alias='type')
    description: str
    buff: ExternalBuff | None
    equivalentCost: ItemBundle | None


class CharacterDataSkillLevelCost(BaseModel):
    unlockCond: CharacterDataUnlockCondition
    lvlUpCost: list[ItemBundle] | None


class CharacterData(BaseModel):
    name: str
    description: str | None
    canUseGeneralPotentialItem: bool
    canUseActivityPotentialItem: bool
    potentialItemId: str | None
    activityPotentialItemId: str | None
    nationId: str | None
    groupId: str | None
    teamId: str | None
    displayNumber: str | None
    tokenKey: str | None = None
    appellation: str
    position: str
    tagList: list[str] | None
    itemUsage: str | None
    itemDesc: str | None
    itemObtainApproach: str | None
    isNotObtainable: bool
    isSpChar: bool
    maxPotentialLevel: int
    rarity: int
    profession: str
    subProfessionId: str
    trait: CharacterDataTraitDataBundle | None
    phases: list[CharacterDataPhaseData]
    skills: list[CharacterDataMainSkill] | None
    talents: list[CharacterDataTalentDataBundle] | None
    potentialRanks: list[CharacterDataPotentialRank] | None
    favorKeyFrames: list[CharacterDataAttributesKeyFrame] | None
    allSkillLvlup: list[CharacterDataSkillLevelCost] | None
    minPowerId: str
    maxPowerId: str


class TokenTable(BaseModel):
    __version__ = '23-07-27-18-50-06-aeb568'

    tokens: dict[str, CharacterData]

    def __init__(self, data: dict) -> None:
        super().__init__(tokens=data)
