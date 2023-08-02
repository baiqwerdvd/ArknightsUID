from pydantic import BaseModel, Field


class StageDataConditionDesc(BaseModel):
    stageId: str
    completeState: int


class StageDataDisplayRewards(BaseModel):
    type_: str = Field(alias='type')
    id_: str = Field(alias='id')
    dropType: int


class StageDataDisplayDetailRewards(BaseModel):
    occPercent: int
    type_: str = Field(alias='type')
    id_: str = Field(alias='id')
    dropType: int


class StageDataStageDropInfo(BaseModel):
    firstPassRewards: None
    firstCompleteRewards: None
    passRewards: None
    completeRewards: None
    displayRewards: list[StageDataDisplayRewards]
    displayDetailRewards: list[StageDataDisplayDetailRewards]


class ExtraCondition(BaseModel):
    index: int
    template: str
    unlockParam: list[str]


class ProgressInfo(BaseModel):
    progressType: str
    descList: dict[str, str] | None


class ItemBundle(BaseModel):
    id_: str = Field(alias='id')
    count: int
    type_: str = Field(alias='type')


class ExtraInfo(BaseModel):
    stageId: str
    rewards: list[ItemBundle]
    progressInfo: ProgressInfo


class StageData(BaseModel):
    stageType: str
    difficulty: str
    performanceStageFlag: str
    diffGroup: str
    unlockCondition: list[StageDataConditionDesc]
    stageId: str
    levelId: str | None
    zoneId: str
    code: str
    name: str | None
    description: str | None
    hardStagedId: str | None
    dangerLevel: str | None
    dangerPoint: int | float
    loadingPicId: str
    canPractice: bool
    canBattleReplay: bool
    apCost: int
    apFailReturn: int
    etItemId: str | None
    etCost: int
    etFailReturn: int
    etButtonStyle: str | None
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
    displayMainItem: str | None
    hilightMark: bool
    bossMark: bool
    isPredefined: bool
    isHardPredefined: bool
    isSkillSelectablePredefined: bool
    isStoryOnly: bool
    appearanceStyle: int
    stageDropInfo: StageDataStageDropInfo
    canUseCharm: bool | None = None
    canUseTech: bool | None = None
    canUseTrapTool: bool | None = None
    canUseBattlePerformance: bool | None = None
    startButtonOverrideId: str | None
    isStagePatch: bool
    mainStageId: str | None
    extraCondition: list[ExtraCondition] | None = None
    extraInfo: list[ExtraInfo] | None = None


class RuneStageGroupDataRuneStageInst(BaseModel):
    stageId: str
    activePackedRuneIds: list[str]


class RuneStageGroupData(BaseModel):
    groupId: str
    activeRuneStages: list[RuneStageGroupDataRuneStageInst]
    startTs: int
    endTs: int


class MapThemeData(BaseModel):
    themeId: str
    unitColor: str
    buildableColor: str | None
    themeType: str | None
    trapTintColor: str | None


class TileAppendInfo(BaseModel):
    tileKey: str
    name: str
    description: str
    isFunctional: bool


class WeeklyForceOpenTable(BaseModel):
    id_: str = Field(alias='id')
    startTime: int
    endTime: int
    forceOpenList: list[str]


class TimelyDropTimeInfo(BaseModel):
    startTs: int
    endTs: int
    stagePic: str | None
    dropPicId: str | None
    stageUnlock: str
    entranceDownPicId: str | None
    entranceUpPicId: str | None
    timelyGroupId: str
    weeklyPicId: str | None
    apSupplyOutOfDateDict: dict[str, int]


class OverrideDropInfo(BaseModel):
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
    dropInfo: dict[str, StageDataStageDropInfo]


class TimelyDropInfo(BaseModel):
    dropInfo: dict[str, StageDataStageDropInfo]


class StageValidInfo(BaseModel):
    startTs: int
    endTs: int


class StageFogInfo(BaseModel):
    lockId: str
    fogType: str
    stageId: str
    lockName: str
    lockDesc: str
    unlockItemId: str
    unlockItemType: str
    unlockItemNum: int
    preposedStageId: str
    preposedLockId: str | None


class StageStartCondRequireChar(BaseModel):
    charId: str
    evolvePhase: int


class StageStartCond(BaseModel):
    requireChars: list[StageStartCondRequireChar]
    excludeAssists: list[str]
    isNotPass: bool


class StageDiffGroupTable(BaseModel):
    normalId: str
    toughId: str | None
    easyId: str


class StoryStageShowGroup(BaseModel):
    displayRecordId: str
    stageId: str
    accordingStageId: str | None
    diffGroup: int


class SpecialBattleFinishStageData(BaseModel):
    stageId: str
    skipAccomplishPerform: bool


class RecordRewardServerData(BaseModel):
    stageId: str
    rewards: list[ItemBundle]


class ApProtectZoneInfoTimeRange(BaseModel):
    startTs: int
    endTs: int


class ApProtectZoneInfo(BaseModel):
    zoneId: str
    timeRanges: list[ApProtectZoneInfoTimeRange]


class StageTable(BaseModel):
    __version__ = '23-07-27-18-50-06-aeb568'

    stages: dict[str, StageData]
    runeStageGroups: dict[str, RuneStageGroupData]
    mapThemes: dict[str, MapThemeData]
    tileInfo: dict[str, TileAppendInfo]
    forceOpenTable: dict[str, WeeklyForceOpenTable]
    timelyStageDropInfo: dict[str, TimelyDropTimeInfo]
    overrideDropInfo: dict[str, OverrideDropInfo]
    timelyTable: dict[str, TimelyDropInfo]
    stageValidInfo: dict[str, StageValidInfo]
    stageFogInfo: dict[str, StageFogInfo]
    stageStartConds: dict[str, StageStartCond]
    diffGroupTable: dict[str, StageDiffGroupTable]
    storyStageShowGroup: dict[str, dict[str, StoryStageShowGroup]]
    specialBattleFinishStageData: dict[str, SpecialBattleFinishStageData]
    recordRewardData: dict[str, RecordRewardServerData] | None
    apProtectZoneInfo: dict[str, ApProtectZoneInfo]
    spNormalStageIdFor4StarList: list[str]
