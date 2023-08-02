from pydantic import BaseModel, Field


class ItemBundle(BaseModel):
    id_: str = Field(alias='id')
    count: int
    type_: str = Field(alias='type')


class StageDataDisplayRewards(BaseModel):
    type_: str = Field(alias='type')
    id_: str = Field(alias='id')
    dropType: int


class BlackboardStr(BaseModel):
    key: str
    valueStr: str


class BlackboardInt(BaseModel):
    key: str
    value: float


class Act17sideDataChoiceNodeOptionData(BaseModel):
    canRepeat: bool
    eventId: str
    des: str
    unlockDes: str | None


class StageDataDisplayDetailRewards(BaseModel):
    occPercent: int
    type_: str = Field(alias='type')
    id_: str = Field(alias='id')
    dropType: int
    CannotGetPercent: float | None = None
    GetPercent: float | None = None


class StageDataConditionDesc(BaseModel):
    stageId: str
    completeState: int


class Act17sideDataConstData(BaseModel):
    techTreeUnlockEventId: str


class Act17sideDataZoneData(BaseModel):
    zoneId: str
    unlockPlaceId: str | None
    unlockText: str


class Act17sideDataMainlineData(BaseModel):
    mainlineId: str
    nodeId: str | None
    sortId: int
    missionSort: str
    zoneId: str
    mainlineDes: str
    focusNodeId: str | None


class Act17sideDataMainlineChapterData(BaseModel):
    chapterId: str
    chapterDes: str
    chapterIcon: str
    unlockDes: str
    id_: str = Field(alias='id')


class RunesSelector(BaseModel):
    professionMask: int
    buildableMask: int
    charIdFilter: None
    enemyIdFilter: None
    enemyIdExcludeFilter: None
    skillIdFilter: None
    tileKeyFilter: None
    groupTagFilter: None
    filterTagFilter: None


class TechTreeBranchRunes(BaseModel):
    key: str
    selector: RunesSelector
    blackboard: list[BlackboardInt | BlackboardStr]


class BranchRuneData(BaseModel):
    id_: str = Field(alias='id')
    points: float
    mutexGroupKey: None
    description: str
    runes: list[TechTreeBranchRunes]


class Act17sideDataTechTreeBranchData(BaseModel):
    techTreeBranchId: str
    techTreeId: str
    techTreeBranchName: str
    techTreeBranchIcon: str
    techTreeBranchDesc: str
    runeData: BranchRuneData


class Act17sideDataTechTreeData(BaseModel):
    techTreeId: str
    sortId: int
    techTreeName: str
    defaultBranchId: str
    lockDes: str


class Act17sideDataArchiveItemUnlockData(BaseModel):
    itemId: str
    itemType: str
    unlockCondition: str
    nodeId: str | None
    stageParam: str
    chapterId: str | None


class Act17sideDataEventData(BaseModel):
    eventId: str
    eventPic: str | None = None
    eventSpecialPic: str | None = None
    eventTitle: str
    eventDesList: list[str]


class Act17sideDataChoiceNodeData(BaseModel):
    nodeId: str
    choicePic: str | None = None
    isDisposable: bool
    choiceSpecialPic: str | None = None
    choiceName: str
    choiceDesList: list[str]
    cancelDes: str
    choiceNum: int
    optionList: list[Act17sideDataChoiceNodeOptionData]


class Act17sideDataTechNodeData(BaseModel):
    nodeId: str
    techTreeId: str
    techTreeName: str
    techPic: None
    techSpecialPic: str
    endEventId: str
    confirmDes: str
    techDesList: list[str]
    missionIdList: list[None]


class Act17sideDataEventNodeData(BaseModel):
    nodeId: str
    eventId: str
    endEventId: str


class Act17sideDataTreasureNodeData(BaseModel):
    nodeId: str
    treasureId: str
    treasureName: str
    treasurePic: str | None
    treasureSpecialPic: None
    endEventId: str
    confirmDes: str
    treasureDesList: list[str]
    missionIdList: list[str]
    rewardList: list[ItemBundle]


class Act17sideDataBattleNodeData(BaseModel):
    nodeId: str
    stageId: str


class Act17sideDataStoryNodeData(BaseModel):
    nodeId: str
    storyId: str
    storyKey: str
    storyName: str
    storyPic: str | None
    confirmDes: str
    storyDesList: list[str]


class Act17sideDataLandmarkNodeData(BaseModel):
    nodeId: str
    landmarkId: str
    landmarkName: str
    landmarkPic: str | None
    landmarkSpecialPic: str
    landmarkDesList: list[str]


class Act17sideDataNodeInfoData(BaseModel):
    nodeId: str
    nodeType: str
    sortId: int
    placeId: str
    isPointPlace: bool
    chapterId: str
    trackPointType: str


class Act17sideDataPlaceData(BaseModel):
    placeId: str
    placeDesc: str
    lockEventId: str | None
    zoneId: str


class Act17sideData(BaseModel):
    archiveItemUnlockDataMap: dict[str, Act17sideDataArchiveItemUnlockData]
    battleNodeDataMap: dict[str, Act17sideDataBattleNodeData]
    choiceNodeDataMap: dict[str, Act17sideDataChoiceNodeData]
    constData: Act17sideDataConstData
    eventDataMap: dict[str, Act17sideDataEventData]
    eventNodeDataMap: dict[str, Act17sideDataEventNodeData]
    landmarkNodeDataMap: dict[str, Act17sideDataLandmarkNodeData]
    mainlineChapterDataMap: dict[str, Act17sideDataMainlineChapterData]
    mainlineDataMap: dict[str, Act17sideDataMainlineData]
    nodeInfoDataMap: dict[str, Act17sideDataNodeInfoData]
    placeDataMap: dict[str, Act17sideDataPlaceData]
    storyNodeDataMap: dict[str, Act17sideDataStoryNodeData]
    techNodeDataMap: dict[str, Act17sideDataTechNodeData]
    techTreeBranchDataMap: dict[str, Act17sideDataTechTreeBranchData]
    techTreeDataMap: dict[str, Act17sideDataTechTreeData]
    treasureNodeDataMap: dict[str, Act17sideDataTreasureNodeData]
    zoneDataList: list[Act17sideDataZoneData]


class Blackboard(BaseModel):
    key: str
    value: float | None = None
    valueStr: str | None = None


class RuneDataSelector(BaseModel):
    buildableMask: int
    charIdFilter: list[str] | None
    enemyIdExcludeFilter: list[str] | None
    enemyIdFilter: list[str] | None
    filterTagFilter: list[str] | None
    groupTagFilter: list[str] | None
    professionMask: int
    skillIdFilter: list[str] | None
    tileKeyFilter: list[str] | None


class RuneData(BaseModel):
    blackboard: list[Blackboard]
    key: str
    m_inited: bool | None = None
    selector: RuneDataSelector


class RuneTablePackedRuneData(BaseModel):
    description: str
    id_: str = Field(alias='id')
    mutexGroupKey: str | None = None
    points: float
    runes: list[RuneData]


class Act25SideDataBattlePerformanceData(BaseModel):
    itemDesc: str
    itemId: str
    itemIcon: str
    ItemName: str | None = None
    itemTechType: str
    runeData: RuneTablePackedRuneData
    sortId: int


class ActivityCustomDataAct25sideCustomData(BaseModel):
    battlePerformanceData: dict[str, Act25SideDataBattlePerformanceData]


class ActivityCustomData(BaseModel):
    TYPE_ACT17SIDE: dict[str, Act17sideData]
    TYPE_ACT25SIDE: dict[str, ActivityCustomDataAct25sideCustomData]


class RetroTrailRuleData(BaseModel):
    title: list[str]
    desc: list[str]


class WeightItemBundle(BaseModel):
    count: int
    dropType: str
    id_: str = Field(alias='id')
    type_: str = Field(alias='type')
    weight: int


class StageDataStageDropInfo(BaseModel):
    firstPassRewards: list[ItemBundle] | None = None
    firstCompleteRewards: list[ItemBundle] | None = None
    passRewards: list[list[WeightItemBundle]] | None = None
    completeRewards: list[list[WeightItemBundle]] | None = None
    displayRewards: list[StageDataDisplayRewards]
    displayDetailRewards: list[StageDataDisplayDetailRewards]


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
    name: str
    description: str
    hardStagedId: str | None
    dangerLevel: str | None
    dangerPoint: float
    loadingPicId: str
    canPractice: bool
    canBattleReplay: bool
    apCost: int
    apFailReturn: int
    etItemId: str
    etCost: int
    etFailReturn: int
    etButtonStyle: None
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
    displayMainItem: None
    hilightMark: bool
    bossMark: bool
    isPredefined: bool
    isHardPredefined: bool
    isSkillSelectablePredefined: bool
    isStoryOnly: bool
    appearanceStyle: int
    stageDropInfo: StageDataStageDropInfo
    startButtonOverrideId: None
    isStagePatch: bool
    mainStageId: str


class RetroTrailRewardItem(BaseModel):
    trailRewardId: str
    starCount: int
    rewardItem: ItemBundle


class RetroTrailData(BaseModel):
    retroId: str
    trailStartTime: int
    trailRewardList: list[RetroTrailRewardItem]
    stageList: list[str]
    relatedChar: str
    relatedFullPotentialItemId: None
    themeColor: str
    fullPotentialItemId: str


class RetroActData(BaseModel):
    retroId: str
    type_: int = Field(alias='type')
    linkedActId: list[str]
    startTime: int
    trailStartTime: int
    index: int
    name: str
    detail: str
    haveTrail: bool
    customActId: str | None
    customActType: str


class StageValidInfo(BaseModel):
    startTs: int
    endTs: int


class RetroStageOverrideInfo(BaseModel):
    apCost: int
    apFailReturn: int
    completeFavor: int
    dropInfo: StageDataStageDropInfo
    expGain: int
    goldGain: int
    passFavor: int
    zoneId: str


class RetroTable(BaseModel):
    __version__ = '23-07-27-18-50-06-aeb568'

    customData: ActivityCustomData
    initRetroCoin: int
    retroActList: dict[str, RetroActData]
    retroCoinMax: int
    retroCoinPerWeek: int
    retroDetail: str
    retroPreShowTime: int
    retroTrailList: dict[str, RetroTrailData]
    retroUnlockCost: int
    ruleData: RetroTrailRuleData
    stageList: dict[str, StageData]
    stages: dict[str, RetroStageOverrideInfo] | None = None
    stageValidInfo: dict[str, StageValidInfo]
    zoneToRetro: dict[str, str]

    class Config:
        extra = 'allow'
