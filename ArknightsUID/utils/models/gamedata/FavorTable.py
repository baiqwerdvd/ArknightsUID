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
    __version__ = "24-02-02-10-18-07-831ad8"

    maxFavor: int
    favorFrames: List[FavorDataFrames]
