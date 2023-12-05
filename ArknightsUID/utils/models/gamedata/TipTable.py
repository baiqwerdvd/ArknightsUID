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
    __version__ = '23-12-02-09-28-50-918524'

    tips: List[TipData]
    worldViewTips: List[WorldViewTip]
