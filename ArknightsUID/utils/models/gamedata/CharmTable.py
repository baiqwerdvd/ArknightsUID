from pydantic import BaseModel, Field


class RuneDataSelector(BaseModel):
    professionMask: int | str
    buildableMask: int
    charIdFilter: list[str] | None
    enemyIdFilter: list[str] | None
    enemyIdExcludeFilter: list[str] | None
    skillIdFilter: list[str] | None
    tileKeyFilter: list[str] | None
    groupTagFilter: list[str] | None
    filterTagFilter: list[str] | None


class Blackboard(BaseModel):
    key: str
    value: float | None = None
    valueStr: str | None = None


class RuneData(BaseModel):
    key: str
    selector: RuneDataSelector
    blackboard: list[Blackboard]


class RuneTablePackedRuneData(BaseModel):
    id_: str = Field(alias='id')
    points: float
    mutexGroupKey: str | None
    description: str
    runes: list[RuneData]


class CharmItemData(BaseModel):
    id_: str = Field(alias='id')
    sort: int
    name: str
    icon: str
    itemUsage: str
    itemDesc: str
    itemObtainApproach: str
    rarity: int
    desc: str
    price: int
    specialObtainApproach: str | None
    charmType: str
    obtainInRandom: bool
    dropStages: list[str]
    runeData: RuneTablePackedRuneData
    charmEffect: str


class CharmTable(BaseModel):
    __version__ = '23-07-27-18-50-06-aeb568'

    class Config:
        extra = 'allow'

    charmList: list[CharmItemData]
