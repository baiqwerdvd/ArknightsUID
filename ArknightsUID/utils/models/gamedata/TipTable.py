from pydantic import BaseModel


class TipData(BaseModel):
    tip: str
    weight: float
    category: str


class WorldViewTip(BaseModel):
    title: str
    description: str
    backgroundPicId: str
    weight: float


class TipTable(BaseModel):
    __version__ = '23-07-27-18-50-06-aeb568'

    tips: list[TipData]
    worldViewTips: list[WorldViewTip]
