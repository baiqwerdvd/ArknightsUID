from typing import Dict, List, Union

from msgspec import field

from ..common import BaseStruct


class StageDataConditionDesc(BaseStruct):
    stageId: str
    completeState: int


class StageDataDisplayRewards(BaseStruct):
    type_: str = field(name="type")
    id_: str = field(name="id")
    dropType: int


class StageDataDisplayDetailRewards(BaseStruct):
    occPercent: int
    type_: str = field(name="type")
    id_: str = field(name="id")
    dropType: int


class StageDataStageDropInfo(BaseStruct):
    firstPassRewards: None
    firstCompleteRewards: None
    passRewards: None
    completeRewards: None
    displayRewards: List[StageDataDisplayRewards]
    displayDetailRewards: List[StageDataDisplayDetailRewards]


class ExtraCondition(BaseStruct):
    index: int
    template: str
    unlockParam: List[str]


class ProgressInfo(BaseStruct):
    progressType: str
    descList: Union[Dict[str, str], None]


class ItemBundle(BaseStruct):
    id_: str = field(name="id")
    count: int
    type_: str = field(name="type")


class ExtraInfo(BaseStruct):
    stageId: str
    rewards: List[ItemBundle]
    progressInfo: ProgressInfo


class StageData(BaseStruct):
    stageType: str
    difficulty: str
    performanceStageFlag: str
    diffGroup: str
    unlockCondition: List[StageDataConditionDesc]
    stageId: str
    levelId: Union[str, None]
    zoneId: str
    code: str
    name: Union[str, None]
    description: Union[str, None]
    hardStagedId: Union[str, None]
    dangerLevel: Union[str, None]
    dangerPoint: Union[int, float]
    loadingPicId: str
    canPractice: bool
    canBattleReplay: bool
    apCost: int
    apFailReturn: int
    etItemId: Union[str, None]
    etCost: int
    etFailReturn: int
    etButtonStyle: Union[str, None]
    apProtectTimes: int
    diamondOnceDrop: int
    practiceTicketCost: int
    dailyStageDifficulty: int
    expGain: int
    goldGain: int
    loseExpGain: int
    loseGoldGain: int
    passFavor: int
    completeFavor: int
    slProgress: int
    displayMainItem: Union[str, None]
    hilightMark: bool
    bossMark: bool
    isPredefined: bool
    isHardPredefined: bool
    isSkillSelectablePredefined: bool
    isStoryOnly: bool
    appearanceStyle: int
    stageDropInfo: StageDataStageDropInfo
    startButtonOverrideId: Union[str, None]
    isStagePatch: bool
    mainStageId: Union[str, None]
    canContinuousBattle: Union[bool, None] = None
    canUseCharm: Union[bool, None] = None
    canUseTech: Union[bool, None] = None
    canUseTrapTool: Union[bool, None] = None
    canUseBattlePerformance: Union[bool, None] = None
    extraCondition: Union[List[ExtraCondition], None] = None
    extraInfo: Union[List[ExtraInfo], None] = None


class RuneStageGroupDataRuneStageInst(BaseStruct):
    stageId: str
    activePackedRuneIds: List[str]


class RuneStageGroupData(BaseStruct):
    groupId: str
    activeRuneStages: List[RuneStageGroupDataRuneStageInst]
    startTs: int
    endTs: int


class MapThemeData(BaseStruct):
    themeId: str
    unitColor: str
    buildableColor: Union[str, None]
    themeType: Union[str, None]
    trapTintColor: Union[str, None]


class TileAppendInfo(BaseStruct):
    tileKey: str
    name: str
    description: str
    isFunctional: bool


class WeeklyForceOpenTable(BaseStruct):
    id_: str = field(name="id")
    startTime: int
    endTime: int
    forceOpenList: List[str]


class TimelyDropTimeInfo(BaseStruct):
    startTs: int
    endTs: int
    stagePic: Union[str, None]
    dropPicId: Union[str, None]
    stageUnlock: str
    entranceDownPicId: Union[str, None]
    entranceUpPicId: Union[str, None]
    timelyGroupId: str
    weeklyPicId: Union[str, None]
    apSupplyOutOfDateDict: Dict[str, int]


class OverrideDropInfo(BaseStruct):
    itemId: str
    startTs: int
    endTs: int
    zoneRange: str
    times: int
    name: str
    egName: str
    desc1: str
    desc2: str
    desc3: str
    dropTag: str
    dropTypeDesc: str
    dropInfo: Dict[str, StageDataStageDropInfo]


class TimelyDropInfo(BaseStruct):
    dropInfo: Dict[str, StageDataStageDropInfo]


class StageValidInfo(BaseStruct):
    startTs: int
    endTs: int


class StageFogInfo(BaseStruct):
    lockId: str
    fogType: str
    stageId: str
    lockName: str
    lockDesc: str
    unlockItemId: str
    unlockItemType: str
    unlockItemNum: int
    preposedStageId: str
    preposedLockId: Union[str, None]


class StageStartCondRequireChar(BaseStruct):
    charId: str
    evolvePhase: int


class StageStartCond(BaseStruct):
    requireChars: List[StageStartCondRequireChar]
    excludeAssists: List[str]
    isNotPass: bool


class StageDiffGroupTable(BaseStruct):
    normalId: str
    toughId: Union[str, None]
    easyId: str


class StoryStageShowGroup(BaseStruct):
    displayRecordId: str
    stageId: str
    accordingStageId: Union[str, None]
    diffGroup: int


class SpecialBattleFinishStageData(BaseStruct):
    stageId: str
    skipAccomplishPerform: bool


class RecordRewardServerData(BaseStruct):
    stageId: str
    rewards: List[ItemBundle]


class ApProtectZoneInfoTimeRange(BaseStruct):
    startTs: int
    endTs: int


class ApProtectZoneInfo(BaseStruct):
    zoneId: str
    timeRanges: List[ApProtectZoneInfoTimeRange]


class StageTable(BaseStruct):
    __version__ = "24-02-02-10-18-07-831ad8"

    stages: Dict[str, StageData]
    runeStageGroups: Dict[str, RuneStageGroupData]
    mapThemes: Dict[str, MapThemeData]
    tileInfo: Dict[str, TileAppendInfo]
    forceOpenTable: Dict[str, WeeklyForceOpenTable]
    timelyStageDropInfo: Dict[str, TimelyDropTimeInfo]
    overrideDropInfo: Dict[str, OverrideDropInfo]
    timelyTable: Dict[str, TimelyDropInfo]
    stageValidInfo: Dict[str, StageValidInfo]
    stageFogInfo: Dict[str, StageFogInfo]
    stageStartConds: Dict[str, StageStartCond]
    diffGroupTable: Dict[str, StageDiffGroupTable]
    storyStageShowGroup: Dict[str, Dict[str, StoryStageShowGroup]]
    specialBattleFinishStageData: Dict[str, SpecialBattleFinishStageData]
    recordRewardData: Union[Dict[str, RecordRewardServerData], None]
    apProtectZoneInfo: Dict[str, ApProtectZoneInfo]
    actCustomStageDatas: Dict[str, Dict[str, str]]
    spNormalStageIdFor4StarList: List[str]
