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
    __version__ = '23-12-02-09-28-50-918524'

    maxFavor: int
    favorFrames: List[FavorDataFrames]
