from typing import List
from ..common import BaseStruct


class FavorData(BaseStruct):
    favorPoint: int
    percent: int
    battlePhase: int


class FavorDataFrames(BaseStruct):
    level: int
    data: FavorData


class FavorTable(BaseStruct):
    __version__ = '23-07-27-18-50-06-aeb568'

    maxFavor: int
    favorFrames: List[FavorDataFrames]
