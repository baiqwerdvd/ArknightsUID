from enum import Enum
from typing import Dict

from ..common import BaseStruct

from msgspec import field


class ItemBundle(BaseStruct):
    id_: str = field(name="id")
    count: int
    type_: str = field(name="type")


class StringKeyFrames(BaseStruct):
    level: int
    data: str


class CrisisV2ConstData(BaseStruct):
    sysStartTime: int
    blackScoreThreshold: int
    redScoreThreshold: int
    detailBkgRedThreshold: int
    voiceGrade: int
    seasonButtonUnlockInfo: int
    shopCoinId: str
    hardBgmSwitchScore: int
    stageId: str
    hideTodoWhenStageFinish: bool


class appraiseType(Enum):
    RANK_D = "RANK_D"
    RANK_C = "RANK_C"
    RANK_B = "RANK_B"
    RANK_A = "RANK_A"
    RANK_S = "RANK_S"
    RANK_SS = "RANK_SS"
    RANK_SSS = "RANK_SSS"


class CrisisV2ScoreLevelToAppraiseData(BaseStruct):
    appraiseType: appraiseType


class CrisisV2Table(BaseStruct):
    __version__ = "24-02-02-10-18-07-831ad8"

    seasonInfoDataMap: Dict
    scoreLevelToAppraiseDataMap: Dict[str, CrisisV2ScoreLevelToAppraiseData]
    constData: CrisisV2ConstData
    battleCommentRuneData: Dict
