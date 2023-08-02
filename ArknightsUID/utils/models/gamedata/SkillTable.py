
from pydantic import BaseModel, Field


class ItemBundle(BaseModel):
    id_: str = Field(alias='id')
    count: int
    type_: str = Field(alias='type')


class SpData(BaseModel):
    spType: int
    levelUpCost: list[ItemBundle] | None
    maxChargeTime: int
    spCost: int
    initSp: int
    increment: int | float


class Blackboard(BaseModel):
    key: str
    value: int | float | None = None
    valueStr: str | None = None


class SkillDataBundleLevelData(BaseModel):
    name: str
    rangeId: str | None
    description: str | None
    skillType: int
    durationType: int
    spData: SpData
    prefabId: str | None
    duration: int | float
    blackboard: list[Blackboard]


class SkillDataBundle(BaseModel):
    skillId: str
    iconId: str | None
    hidden: bool
    levels: list[SkillDataBundleLevelData]


class SkillTable(BaseModel):
    __version__ = '23-07-27-18-50-06-aeb568'

    skills: dict[str, SkillDataBundle]

    def __init__(self, data: dict) -> None:
        super().__init__(skills=data)
