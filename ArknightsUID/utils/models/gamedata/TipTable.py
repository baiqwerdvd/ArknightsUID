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
    __version__ = '24-02-02-10-18-07-831ad8'

    tips: List[TipData]
    worldViewTips: List[WorldViewTip]
