from pydantic import BaseModel


class FavorData(BaseModel):
    favorPoint: int
    percent: int
    battlePhase: int


class FavorDataFrames(BaseModel):
    level: int
    data: FavorData


class FavorTable(BaseModel):
    __version__ = '23-07-27-18-50-06-aeb568'

    maxFavor: int
    favorFrames: list[FavorDataFrames]
