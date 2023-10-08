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
    __version__ = '23-09-29-15-41-03-569cae'

    tips: List[TipData]
    worldViewTips: List[WorldViewTip]
