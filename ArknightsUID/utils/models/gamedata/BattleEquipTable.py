from pydantic import BaseModel


class CharacterDataUnlockCondition(BaseModel):
    phase: int
    level: int


class Blackboard(BaseModel):
    key: str
    value: float | None = None
    valueStr: str | None = None


class TalentData(BaseModel):
    unlockCondition: CharacterDataUnlockCondition
    requiredPotentialRank: int
    prefabKey: str | None
    name: str | None
    description: str | None
    rangeId: str | None
    blackboard: list[Blackboard]


class EquipTalentData(TalentData):
    displayRangeId: bool
    upgradeDescription: str
    talentIndex: int


class CharacterDataEquipTalentDataBundle(BaseModel):
    candidates: list[EquipTalentData] | None


class CharacterDataTraitData(BaseModel):
    unlockCondition: CharacterDataUnlockCondition
    requiredPotentialRank: int
    blackboard: list[Blackboard]
    overrideDescripton: str | None
    prefabKey: str | None
    rangeId: str | None


class CharacterDataEquipTraitData(BaseModel):
    additionalDescription: str | None


class CharacterDataEquipTraitDataBundle(BaseModel):
    candidates: list[CharacterDataEquipTraitData] | None


class BattleUniEquipData(BaseModel):
    resKey: str | None
    target: str
    isToken: bool
    addOrOverrideTalentDataBundle: CharacterDataEquipTalentDataBundle
    overrideTraitDataBundle: CharacterDataEquipTraitDataBundle


class BattleEquipPerLevelPack(BaseModel):
    equipLevel: int
    parts: list[BattleUniEquipData]
    attributeBlackboard: list[Blackboard]
    tokenAttributeBlackboard: dict[str, list[Blackboard]]


class BattleEquipData(BaseModel):
    phases: list[BattleEquipPerLevelPack]


class BattleEquipTable(BaseModel):
    __version__ = '23-07-27-18-50-06-aeb568'

    equips: dict[str, BattleEquipData]

    class Config:
        extra = 'allow'

    def __init__(self, data: dict) -> None:
        super().__init__(equips=data)
