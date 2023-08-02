from pydantic import BaseModel, Field


class RuneDataSelector(BaseModel):
    professionMask: int
    buildableMask: int
    charIdFilter: list[str] | None
    enemyIdFilter: list[str] | None
    skillIdFilter: list[str] | None
    tileKeyFilter: list[str] | None


class Blackboard(BaseModel):
    key: str
    value: float | None = None
    valueStr: str | None = None


class RuneData(BaseModel):
    key: str
    selector: RuneDataSelector
    blackboard: list[Blackboard]


class PackedRuneData(BaseModel):
    id_: str = Field(alias='id')
    points: float
    mutexGroupKey: str | None
    description: str
    runes: list[RuneData]


class TechBuffTable(BaseModel):
    __version__ = '23-07-27-18-50-06-aeb568'

    runes: list[PackedRuneData]
