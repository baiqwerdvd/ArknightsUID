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
    __version__ = '23-10-08-17-52-18-288259'

    maxFavor: int
    favorFrames: List[FavorDataFrames]
