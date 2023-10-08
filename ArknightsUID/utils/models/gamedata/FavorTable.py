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
    __version__ = '23-09-29-15-41-03-569cae'

    maxFavor: int
    favorFrames: List[FavorDataFrames]
