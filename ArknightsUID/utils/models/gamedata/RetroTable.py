from typing import Dict, List, Union

from ..common import BaseStruct

from msgspec import field


class ItemBundle(BaseStruct):
    id_: str = field(name='id')
    count: int
    type_: str = field(name='type')


class StageDataDisplayRewards(BaseStruct):
    type_: str = field(name='type')
    id_: str = field(name='id')
    dropType: int


class Blackboard(BaseStruct):
    key: str
    value: Union[float, None] = None
    valueStr: Union[str, None] = None


class Act17sideDataChoiceNodeOptionData(BaseStruct):
    canRepeat: bool
    eventId: str
    des: str
    unlockDes: Union[str, None]


class StageDataDisplayDetailRewards(BaseStruct):
    occPercent: int
    type_: str = field(name='type')
    id_: str = field(name='id')
    dropType: int
    CannotGetPercent: Union[float, None] = None
    GetPercent: Union[float, None] = None


class StageDataConditionDesc(BaseStruct):
    stageId: str
    completeState: int


class Act17sideDataConstData(BaseStruct):
    techTreeUnlockEventId: str


class Act17sideDataZoneData(BaseStruct):
    zoneId: str
    unlockPlaceId: Union[str, None]
    unlockText: str


class Act17sideDataMainlineData(BaseStruct):
    mainlineId: str
    nodeId: Union[str, None]
    sortId: int
    missionSort: str
    zoneId: str
    mainlineDes: str
    focusNodeId: Union[str, None]


class Act17sideDataMainlineChapterData(BaseStruct):
    chapterId: str
    chapterDes: str
    chapterIcon: str
    unlockDes: str
    id_: str = field(name='id')


class RunesSelector(BaseStruct):
    professionMask: int
    buildableMask: int
    charIdFilter: Union[List[str], None]
    enemyIdFilter: Union[List[str], None]
    enemyIdExcludeFilter: Union[List[str], None]
    enemyLevelTypeFilter: Union[List[str], None]
    skillIdFilter: Union[List[str], None]
    tileKeyFilter: Union[List[str], None]
    groupTagFilter: Union[List[str], None]
    filterTagFilter: Union[List[str], None]
    filterTagExcludeFilter: Union[List[str], None]
    subProfessionExcludeFilter: Union[List[str], None]
    mapTagFilter: Union[List[str], None]


class TechTreeBranchRunes(BaseStruct):
    key: str
    selector: RunesSelector
    blackboard: List[Blackboard]


class BranchRuneData(BaseStruct):
    id_: str = field(name='id')
    points: float
    mutexGroupKey: None
    description: str
    runes: List[TechTreeBranchRunes]


class Act17sideDataTechTreeBranchData(BaseStruct):
    techTreeBranchId: str
    techTreeId: str
    techTreeBranchName: str
    techTreeBranchIcon: str
    techTreeBranchDesc: str
    runeData: BranchRuneData


class Act17sideDataTechTreeData(BaseStruct):
    techTreeId: str
    sortId: int
    techTreeName: str
    defaultBranchId: str
    lockDes: str


class Act17sideDataArchiveItemUnlockData(BaseStruct):
    itemId: str
    itemType: str
    unlockCondition: str
    nodeId: Union[str, None]
    stageParam: str
    chapterId: Union[str, None]


class Act17sideDataEventData(BaseStruct):
    eventId: str
    eventTitle: str
    eventDesList: List[str]
    eventPic: Union[str, None] = None
    eventSpecialPic: Union[str, None] = None


class Act17sideDataChoiceNodeData(BaseStruct):
    nodeId: str
    isDisposable: bool
    choiceName: str
    choiceDesList: List[str]
    cancelDes: str
    choiceNum: int
    optionList: List[Act17sideDataChoiceNodeOptionData]
    choicePic: Union[str, None] = None
    choiceSpecialPic: Union[str, None] = None


class Act17sideDataTechNodeData(BaseStruct):
    nodeId: str
    techTreeId: str
    techTreeName: str
    techPic: None
    techSpecialPic: str
    endEventId: str
    confirmDes: str
    techDesList: List[str]
    missionIdList: List[None]


class Act17sideDataEventNodeData(BaseStruct):
    nodeId: str
    eventId: str
    endEventId: str


class Act17sideDataTreasureNodeData(BaseStruct):
    nodeId: str
    treasureId: str
    treasureName: str
    treasurePic: Union[str, None]
    treasureSpecialPic: None
    endEventId: str
    confirmDes: str
    treasureDesList: List[str]
    missionIdList: List[str]
    rewardList: List[ItemBundle]
    treasureType: str


class Act17sideDataBattleNodeData(BaseStruct):
    nodeId: str
    stageId: str


class Act17sideDataStoryNodeData(BaseStruct):
    nodeId: str
    storyId: str
    storyKey: str
    storyName: str
    storyPic: Union[str, None]
    confirmDes: str
    storyDesList: List[str]


class Act17sideDataLandmarkNodeData(BaseStruct):
    nodeId: str
    landmarkId: str
    landmarkName: str
    landmarkPic: Union[str, None]
    landmarkSpecialPic: str
    landmarkDesList: List[str]


class Act17sideDataNodeInfoData(BaseStruct):
    nodeId: str
    nodeType: str
    sortId: int
    placeId: str
    isPointPlace: bool
    chapterId: str
    trackPointType: str


class Act17sideDataPlaceData(BaseStruct):
    placeId: str
    placeDesc: str
    lockEventId: Union[str, None]
    zoneId: str


class Act17sideData(BaseStruct):
    archiveItemUnlockDataMap: Dict[str, Act17sideDataArchiveItemUnlockData]
    battleNodeDataMap: Dict[str, Act17sideDataBattleNodeData]
    choiceNodeDataMap: Dict[str, Act17sideDataChoiceNodeData]
    constData: Act17sideDataConstData
    eventDataMap: Dict[str, Act17sideDataEventData]
    eventNodeDataMap: Dict[str, Act17sideDataEventNodeData]
    landmarkNodeDataMap: Dict[str, Act17sideDataLandmarkNodeData]
    mainlineChapterDataMap: Dict[str, Act17sideDataMainlineChapterData]
    mainlineDataMap: Dict[str, Act17sideDataMainlineData]
    nodeInfoDataMap: Dict[str, Act17sideDataNodeInfoData]
    placeDataMap: Dict[str, Act17sideDataPlaceData]
    storyNodeDataMap: Dict[str, Act17sideDataStoryNodeData]
    techNodeDataMap: Dict[str, Act17sideDataTechNodeData]
    techTreeBranchDataMap: Dict[str, Act17sideDataTechTreeBranchData]
    techTreeDataMap: Dict[str, Act17sideDataTechTreeData]
    treasureNodeDataMap: Dict[str, Act17sideDataTreasureNodeData]
    zoneDataList: List[Act17sideDataZoneData]


class RuneDataSelector(BaseStruct):
    buildableMask: int
    professionMask: int
    charIdFilter: Union[List[str], None]
    enemyIdFilter: Union[List[str], None]
    enemyIdExcludeFilter: Union[List[str], None]
    enemyLevelTypeFilter: Union[List[str], None]
    skillIdFilter: Union[List[str], None]
    tileKeyFilter: Union[List[str], None]
    groupTagFilter: Union[List[str], None]
    filterTagFilter: Union[List[str], None]
    filterTagExcludeFilter: Union[List[str], None]
    subProfessionExcludeFilter: Union[List[str], None]
    mapTagFilter: Union[List[str], None]


class RuneData(BaseStruct):
    blackboard: List[Blackboard]
    key: str
    selector: RuneDataSelector
    m_inited: Union[bool, None] = None


class RuneTablePackedRuneData(BaseStruct):
    description: str
    id_: str = field(name='id')
    points: float
    runes: List[RuneData]
    mutexGroupKey: Union[str, None] = None


class Act25SideDataBattlePerformanceData(BaseStruct):
    itemDesc: str
    itemId: str
    itemIcon: str
    itemName: str
    itemTechType: str
    runeData: RuneTablePackedRuneData
    sortId: int


class ActivityCustomDataAct25sideCustomData(BaseStruct):
    battlePerformanceData: Dict[str, Act25SideDataBattlePerformanceData]


class ActivityCustomDataAct20sideCustomData(BaseStruct):
    zoneAdditionDataMap: Dict[str, str]
    residentCartDatas: Dict[str, Dict[str, str]]


class Act21SideDataZoneAddtionData(BaseStruct):
    zoneId: str
    unlockText: str
    stageUnlockText: Union[str, None]
    entryId: str


class Act21SideDataConstData(BaseStruct):
    lineConnectZone: str


class ActivityCustomDataAct21sideCustomData(BaseStruct):
    zoneAdditionDataMap: Dict[str, Act21SideDataZoneAddtionData]
    constData: Act21SideDataConstData


class ActivityCustomData(BaseStruct):
    TYPE_ACT17SIDE: Dict[str, Act17sideData]
    TYPE_ACT25SIDE: Dict[str, ActivityCustomDataAct25sideCustomData]
    TYPE_ACT20SIDE: Dict[str, ActivityCustomDataAct20sideCustomData]
    TYPE_ACT21SIDE: Dict[str, ActivityCustomDataAct21sideCustomData]


class RetroTrailRuleData(BaseStruct):
    title: List[str]
    desc: List[str]


class WeightItemBundle(BaseStruct):
    count: int
    dropType: str
    id_: str = field(name='id')
    type_: str = field(name='type')
    weight: int


class StageDataStageDropInfo(BaseStruct):
    displayRewards: List[StageDataDisplayRewards]
    displayDetailRewards: List[StageDataDisplayDetailRewards]
    firstPassRewards: Union[List[ItemBundle], None] = None
    firstCompleteRewards: Union[List[ItemBundle], None] = None
    passRewards: Union[List[List[WeightItemBundle]], None] = None
    completeRewards: Union[List[List[WeightItemBundle]], None] = None


class StageData(BaseStruct, kw_only=False):
    stageType: str
    difficulty: str
    performanceStageFlag: str
    diffGroup: str
    unlockCondition: List[StageDataConditionDesc]
    stageId: str
    levelId: Union[str, None]
    zoneId: str
    code: str
    name: str
    description: str
    hardStagedId: Union[str, None]
    dangerLevel: Union[str, None]
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
    canUseTech: Union[bool, None] = None
    canUseCharm: Union[bool, None] = None
    canUseBattlePerformance: Union[bool, None] = None


class RetroTrailRewardItem(BaseStruct):
    trailRewardId: str
    starCount: int
    rewardItem: ItemBundle


class RetroTrailData(BaseStruct):
    retroId: str
    trailStartTime: int
    trailRewardList: List[RetroTrailRewardItem]
    stageList: List[str]
    relatedChar: str
    relatedFullPotentialItemId: None
    themeColor: str
    fullPotentialItemId: str


class RetroActData(BaseStruct):
    retroId: str
    type_: int = field(name='type')
    linkedActId: List[str]
    startTime: int
    trailStartTime: int
    index: int
    name: str
    detail: str
    haveTrail: bool
    customActId: Union[str, None]
    customActType: str


class StageValidInfo(BaseStruct):
    startTs: int
    endTs: int


class RetroStageOverrideInfo(BaseStruct):
    apCost: int
    apFailReturn: int
    completeFavor: int
    dropInfo: StageDataStageDropInfo
    expGain: int
    goldGain: int
    passFavor: int
    zoneId: str


class RetroTable(BaseStruct):
    __version__ = '24-02-02-10-18-07-831ad8'

    customData: ActivityCustomData
    initRetroCoin: int
    retroActList: Dict[str, RetroActData]
    retroCoinMax: int
    retroCoinPerWeek: int
    retroDetail: str
    retroPreShowTime: int
    retroTrailList: Dict[str, RetroTrailData]
    retroUnlockCost: int
    ruleData: RetroTrailRuleData
    stageList: Dict[str, StageData]
    stageValidInfo: Dict[str, StageValidInfo]
    zoneToRetro: Dict[str, str]
    stages: Union[Dict[str, RetroStageOverrideInfo], None] = None
