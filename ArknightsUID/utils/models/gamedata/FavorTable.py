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
    __version__ = "23-10-31-11-47-45-d410ff"

    maxFavor: int
    favorFrames: List[FavorDataFrames]
