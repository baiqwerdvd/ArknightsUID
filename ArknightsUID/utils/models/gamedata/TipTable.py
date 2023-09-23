from typing import List
from ..common import BaseStruct


class TipData(BaseStruct):
    tip: str
    weight: float
    category: str


class WorldViewTip(BaseStruct):
    title: str
    description: str
    backgroundPicId: str
    weight: float


class TipTable(BaseStruct):
    __version__ = '23-07-27-18-50-06-aeb568'

    tips: List[TipData]
    worldViewTips: List[WorldViewTip]
