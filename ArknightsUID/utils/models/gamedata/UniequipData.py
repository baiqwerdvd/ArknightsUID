from pydantic import BaseModel, Field


class ItemBundle(BaseModel):
    id_: str = Field(alias='id')
    count: int
    type_: str = Field(alias='type')


class UnlockCondition(BaseModel):
    phase: int
    level: int


class TraitDescBundle(BaseModel):
    unlockCondition: UnlockCondition
    requiredPotentialRank: int
    overrideDescription: None
    additiveDescription: str


class UniEquipData(BaseModel):
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
    missionList: list[str]
    itemCost: list[ItemBundle] | None
    type_: str = Field(..., alias='type')
    traitDescBundle: list[TraitDescBundle]


class UniEquipMissionData(BaseModel):
    template: str | None
    desc: str | None
    paramList: list[str]
    uniEquipMissionId: str
    uniEquipMissionSort: int
    uniEquipId: str


class SubProfessionData(BaseModel):
    subProfessionId: str
    subProfessionName: str
    subProfessionCatagory: int


class UniequipData(BaseModel):
    __version__ = '23-07-27-18-50-06-aeb568'

    equipDict: dict[str, UniEquipData]
    missionList: dict[str, UniEquipMissionData]
    subProfDict: dict[str, SubProfessionData]
    charEquip: dict[str, list[str]]
