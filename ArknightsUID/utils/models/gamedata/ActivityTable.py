from enum import Enum
from typing import Any, Dict, List, Union

from msgspec import field

from ..common import BaseStruct


class ActivityTableBasicData(BaseStruct):
    id_: str = field(name="id")
    type_: str = field(name="type")
    name: str
    startTime: int
    endTime: int
    rewardEndTime: int
    displayOnHome: bool
    hasStage: bool
    templateShopId: Union[str, None]
    medalGroupId: Union[str, None]
    isReplicate: bool
    needFixedSync: bool
    displayType: Union[str, None] = None
    ungroupedMedalIds: Union[List[str], None] = None


class ActivityTableHomeActivityConfig(BaseStruct):
    actId: str
    isPopupAfterCheckin: bool
    showTopBarMenu: bool
    actTopBarColor: Union[str, None]
    actTopBarText: Union[str, None]


class MissionDisplayRewards(BaseStruct):
    type_: str = field(name="type")
    id_: str = field(name="id")
    count: int


class MissionData(BaseStruct):
    id_: str = field(name="id")
    sortId: int
    description: str
    type_: str = field(name="type")
    itemBgType: str
    preMissionIds: Union[List[str], None]
    template: str
    templateType: str
    param: List[str]
    unlockCondition: Union[str, None]
    unlockParam: Union[List[str], None]
    missionGroup: str
    toPage: Union[str, None]
    periodicalPoint: int
    rewards: Union[List[MissionDisplayRewards], None]
    backImagePath: Union[str, None]
    foldId: Union[str, None]
    haveSubMissionToUnlock: bool


class MissionGroup(BaseStruct):
    id_: str = field(name="id")
    title: Union[str, None]
    type_: str = field(name="type")
    preMissionGroup: Union[str, None]
    period: Union[List[int], None]
    rewards: Union[List[MissionDisplayRewards], None]
    missionIds: List[str]
    startTs: int
    endTs: int


class DefaultZoneData(BaseStruct):
    zoneId: str
    zoneIndex: str
    zoneName: str
    zoneDesc: str
    itemDropList: List[str]


class ItemBundle(BaseStruct):
    id_: str = field(name="id")
    count: int
    type_: str = field(name="type")


class DefaultShopData(BaseStruct):
    goodId: str
    slotId: int
    price: int
    availCount: int
    overrideName: str
    item: ItemBundle


class DefaultFirstData(BaseStruct):
    zoneList: List[DefaultZoneData]
    shopList: Union[List[DefaultShopData], None]


class DefaultCheckInDataCheckInDailyInfo(BaseStruct):
    itemList: List[ItemBundle]
    order: int
    color: int
    keyItem: int
    showItemOrder: int
    isDynItem: bool


class DefaultCheckInDataDynCheckInDailyInfo(BaseStruct):
    questionDesc: str
    preOption: str
    optionList: List[str]
    showDay: int
    spOrderIconId: str
    spOrderDesc: str
    spOrderCompleteDesc: str


class DefaultCheckInDataOptionInfo(BaseStruct):
    optionDesc: Union[str, None]
    showImageId1: Union[str, None]
    showImageId2: Union[str, None]
    optionCompleteDesc: Union[str, None]
    isStart: bool


class DefaultCheckInDataDynamicCheckInConsts(BaseStruct):
    firstQuestionDesc: str
    firstQuestionTipsDesc: str
    expirationDesc: str
    firstQuestionConfirmDesc: str


class DefaultCheckInDataDynamicCheckInData(BaseStruct):
    dynCheckInDict: Dict[str, DefaultCheckInDataDynCheckInDailyInfo]
    dynOptionDict: Dict[str, DefaultCheckInDataOptionInfo]
    dynItemDict: Dict[str, List[ItemBundle]]
    constData: DefaultCheckInDataDynamicCheckInConsts
    initOption: str


class DefaultCheckInDataExtraCheckinDailyInfo(BaseStruct):
    order: int
    blessing: str
    absolutData: int
    adTip: str
    relativeData: int
    itemList: List[ItemBundle]


class DefaultCheckInData(BaseStruct):
    checkInList: Dict[str, DefaultCheckInDataCheckInDailyInfo]
    apSupplyOutOfDateDict: Dict[str, int]
    extraCheckinList: Union[
        List[DefaultCheckInDataExtraCheckinDailyInfo],
        None,
    ]
    dynCheckInData: Union[DefaultCheckInDataDynamicCheckInData, None] = None


class AllPlayerCheckinDataDailyInfo(BaseStruct):
    itemList: List[ItemBundle]
    order: int
    keyItem: bool
    showItemOrder: int


class AllPlayerCheckinDataPublicBehaviour(BaseStruct):
    sortId: int
    allBehaviorId: str
    displayOrder: int
    allBehaviorDesc: str
    requiringValue: int
    requireRepeatCompletion: bool
    rewardReceivedDesc: str
    rewards: List[ItemBundle]


class AllPlayerCheckinDataPersonalBehaviour(BaseStruct):
    sortId: int
    personalBehaviorId: str
    displayOrder: int
    requireRepeatCompletion: bool
    desc: str


class AllPlayerCheckinDataConstData(BaseStruct):
    characterName: str
    skinName: str


class AllPlayerCheckinData(BaseStruct):
    checkInList: Dict[str, AllPlayerCheckinDataDailyInfo]
    apSupplyOutOfDateDict: Dict[str, int]
    pubBhvs: Dict[str, AllPlayerCheckinDataPublicBehaviour]
    personalBhvs: Dict[str, AllPlayerCheckinDataPersonalBehaviour]
    constData: AllPlayerCheckinDataConstData


class VersusCheckInDataDailyInfo(BaseStruct):
    rewardList: List[ItemBundle]
    order: int


class VersusCheckInDataVoteData(BaseStruct):
    plSweetNum: int
    plSaltyNum: int
    plTaste: int


class VersusCheckInDataTasteInfoData(BaseStruct):
    plTaste: int
    tasteType: str
    tasteText: str


class VersusCheckInDataTasteRewardData(BaseStruct):
    tasteType: str
    rewardItem: ItemBundle


class VersusCheckInData(BaseStruct):
    checkInDict: Dict[str, VersusCheckInDataDailyInfo]
    voteTasteList: List[VersusCheckInDataVoteData]
    tasteInfoDict: Dict[str, VersusCheckInDataTasteInfoData]
    tasteRewardDict: Dict[str, VersusCheckInDataTasteRewardData]
    apSupplyOutOfDateDict: Dict[str, int]
    versusTotalDays: int
    ruleText: str


class Act3D0DataCampBasicInfo(BaseStruct):
    campId: str
    campName: str
    campDesc: str
    rewardDesc: Union[str, None]


class Act3D0DataLimitedPoolDetailInfoPoolItemInfo(BaseStruct):
    goodId: str
    itemInfo: Union[ItemBundle, None]
    goodType: str
    perCount: int
    totalCount: int
    weight: int
    type_: str = field(name="type")
    orderId: int


class Act3D0DataLimitedPoolDetailInfo(BaseStruct):
    poolId: str
    poolItemInfo: List[Act3D0DataLimitedPoolDetailInfoPoolItemInfo]


class Act3D0DataInfinitePoolDetailInfoPoolItemInfo(BaseStruct):
    goodId: str
    itemInfo: ItemBundle
    goodType: str
    perCount: int
    weight: int
    type_: str = field(name="type")
    orderId: int


class Act3D0DataInfinitePoolDetailInfo(BaseStruct):
    poolId: str
    poolItemInfo: List[Act3D0DataInfinitePoolDetailInfoPoolItemInfo]


class Act3D0DataInfinitePoolPercent(BaseStruct):
    percentDict: Dict[str, int]


class Act3D0DataCampItemMapInfo(BaseStruct):
    goodId: str
    itemDict: Dict[str, ItemBundle]


class Act3D0DataClueInfo(BaseStruct):
    itemId: str
    campId: str
    orderId: int
    imageId: str


class Act3D0DataMileStoneInfo(BaseStruct):
    mileStoneId: str
    orderId: int
    mileStoneType: int
    normalItem: Union[ItemBundle, None]
    specialItemDict: Dict[str, ItemBundle]
    tokenNum: int


class Act3D0DataGachaBoxInfo(BaseStruct):
    gachaBoxId: str
    boxType: str
    keyGoodId: Union[str, None]
    tokenId: ItemBundle
    tokenNumOnce: int
    unlockImg: Union[str, None]
    nextGachaBoxInfoId: Union[str, None]


class Act3D0DataCampInfo(BaseStruct):
    campId: str
    campChineseName: str


class Act3D0DataZoneDescInfo(BaseStruct):
    zoneId: str
    lockedText: Union[str, None]


class CommonFavorUpInfo(BaseStruct):
    charId: str
    displayStartTime: int
    displayEndTime: int


class Act3D0Data(BaseStruct):
    campBasicInfo: Dict[str, Act3D0DataCampBasicInfo]
    limitedPoolList: Dict[str, Act3D0DataLimitedPoolDetailInfo]
    infinitePoolList: Dict[str, Act3D0DataInfinitePoolDetailInfo]
    infinitePercent: Union[Dict[str, Act3D0DataInfinitePoolPercent], None]
    campItemMapInfo: Dict[str, Act3D0DataCampItemMapInfo]
    clueInfo: Dict[str, Act3D0DataClueInfo]
    mileStoneInfo: List[Act3D0DataMileStoneInfo]
    mileStoneTokenId: str
    coinTokenId: str
    etTokenId: str
    gachaBoxInfo: List[Act3D0DataGachaBoxInfo]
    campInfo: Union[Dict[str, Act3D0DataCampInfo], None]
    zoneDesc: Dict[str, Act3D0DataZoneDescInfo]
    favorUpList: Union[Dict[str, CommonFavorUpInfo], None]


class Act4D0DataMileStoneItemInfo(BaseStruct):
    mileStoneId: str
    orderId: int
    tokenNum: int
    item: ItemBundle


class Act4D0DataMileStoneStoryInfo(BaseStruct):
    mileStoneId: str
    orderId: int
    tokenNum: int
    storyKey: str
    desc: str


class Act4D0DataStoryInfo(BaseStruct):
    storyKey: str
    storyId: str
    storySort: str
    storyName: str
    lockDesc: str
    storyDesc: str


class Act4D0DataStageJumpInfo(BaseStruct):
    stageKey: str
    zoneId: str
    stageId: str
    unlockDesc: str
    lockDesc: str


class Act4D0Data(BaseStruct):
    mileStoneItemList: List[Act4D0DataMileStoneItemInfo]
    mileStoneStoryList: List[Act4D0DataMileStoneStoryInfo]
    storyInfoList: List[Act4D0DataStoryInfo]
    stageInfo: List[Act4D0DataStageJumpInfo]
    tokenItem: ItemBundle
    charStoneId: str
    apSupplyOutOfDateDict: Dict[str, int]
    extraDropZones: List[str]


class MileStoneInfo(BaseStruct):
    mileStoneId: str
    orderId: int
    tokenNum: int
    mileStoneType: int
    normalItem: ItemBundle
    IsBonus: int


class Act5D0DataZoneDescInfo(BaseStruct):
    zoneId: str
    lockedText: Union[str, None]


class Act5D0DataMissionExtraInfo(BaseStruct):
    difficultLevel: int
    levelDesc: str
    sortId: int


class Act5D0Data(BaseStruct):
    mileStoneInfo: List[MileStoneInfo]
    mileStoneTokenId: str
    zoneDesc: Dict[str, Act5D0DataZoneDescInfo]
    missionExtraList: Dict[str, Act5D0DataMissionExtraInfo]
    spReward: str


class Act5D1DataRuneStageData(BaseStruct):
    stageId: str
    levelId: str
    code: str
    name: str
    loadingPicId: str
    description: str
    picId: str


class Act5D1DataRuneRecurrentStateData(BaseStruct):
    runeReId: str
    stageId: str
    slotId: int
    startTime: int
    endTime: int
    runeList: List[str]
    isAvail: bool
    warningPoint: int


class Act5D1DataRuneUnlockData(BaseStruct):
    runeId: str
    priceItem: ItemBundle
    runeName: str
    bgPic: str
    runeDesc: str
    sortId: int
    iconId: str


class Act5D1DataRuneReleaseData(BaseStruct):
    runeId: str
    stageId: str
    releaseTime: int


class Act5D1DataShopGood(BaseStruct):
    goodId: str
    slotId: int
    price: int
    availCount: int
    item: ItemBundle
    progressGoodId: str
    goodType: str


class Act5D1DataProgessGoodItem(BaseStruct):
    order: int
    price: int
    displayName: str
    item: ItemBundle


class Act5D1DataShopData(BaseStruct):
    shopGoods: Dict[str, Act5D1DataShopGood]
    progressGoods: Dict[str, List[Act5D1DataProgessGoodItem]]


class RuneDataSelector(BaseStruct):
    professionMask: Union[int, str]
    buildableMask: int
    charIdFilter: Union[List[str], None]
    enemyIdFilter: Union[List[str], None]
    enemyLevelTypeFilter: Union[List[str], None]
    enemyIdExcludeFilter: Union[List[str], None]
    skillIdFilter: Union[List[str], None]
    tileKeyFilter: Union[List[str], None]
    groupTagFilter: Union[List[str], None]
    filterTagFilter: Union[List[str], None]
    filterTagExcludeFilter: Union[List[str], None]
    subProfessionExcludeFilter: Union[List[str], None]
    mapTagFilter: Union[List[str], None]


class Blackboard(BaseStruct):
    key: str
    value: Union[float, None] = None
    valueStr: Union[str, None] = None


class RuneData(BaseStruct):
    key: str
    selector: RuneDataSelector
    blackboard: List[Blackboard]


class RuneTablePackedRuneData(BaseStruct):
    id_: str = field(name="id")
    points: float
    mutexGroupKey: Union[str, None]
    description: Union[str, None]
    runes: List[RuneData]


class RuneTableRuneStageExtraData(BaseStruct):
    stageId: str
    runes: List[RuneTablePackedRuneData]


class Act5D1Data(BaseStruct):
    stageCommonData: List[Act5D1DataRuneStageData]
    runeStageData: List[Act5D1DataRuneRecurrentStateData]
    runeUnlockDict: Dict[str, List[Act5D1DataRuneUnlockData]]
    runeReleaseData: List[Act5D1DataRuneReleaseData]
    missionData: List[MissionData]
    missionGroup: List[MissionGroup]
    useBenefitMissionDict: Dict[str, bool]
    shopData: Act5D1DataShopData
    coinItemId: str
    ptItemId: str
    stageRune: List[RuneTableRuneStageExtraData]
    showRuneMissionList: List[str]


class ActivityCollectionDataCollectionInfo(BaseStruct):
    id_: int = field(name="id")
    itemType: str
    itemId: str
    itemCnt: int
    pointId: str
    pointCnt: int
    isBonus: bool
    pngName: Union[str, None]
    pngSort: int
    isShow: bool
    showInList: bool
    showIconBG: bool


class ActivityCollectionData(BaseStruct):
    collections: List[ActivityCollectionDataCollectionInfo]
    apSupplyOutOfDateDict: Dict[str, int]


class Act9D0DataZoneDescInfo(BaseStruct):
    zoneId: str
    unlockText: str
    displayStartTime: int


class Act9D0DataFavorUpInfo(BaseStruct):
    charId: str
    displayStartTime: int
    displayEndTime: int


class Act9D0DataSubMissionInfo(BaseStruct):
    missionId: str
    missionTitle: str
    sortId: int
    missionIndex: str


class Act9D0DataActivityNewsStyleInfo(BaseStruct):
    typeId: str
    typeName: str
    typeLogo: str
    typeMainLogo: str


class Act9D0DataActivityNewsLine(BaseStruct):
    lineType: int
    content: str


class Act9D0DataActivityNewsInfo(BaseStruct):
    newsId: str
    newsSortId: int
    styleInfo: Act9D0DataActivityNewsStyleInfo
    preposedStage: Union[str, None]
    titlePic: str
    newsTitle: str
    newsInfShow: int
    newsFrom: str
    newsText: str
    newsParam1: int
    newsParam2: int
    newsParam3: float
    newsLines: List[Act9D0DataActivityNewsLine]


class Act9D0DataActivityNewsServerInfo(BaseStruct):
    newsId: str
    preposedStage: str


class Act9D0Data(BaseStruct):
    tokenItemId: str
    zoneDescList: Dict[str, Act9D0DataZoneDescInfo]
    favorUpList: Dict[str, Act9D0DataFavorUpInfo]
    subMissionInfo: Union[Dict[str, Act9D0DataSubMissionInfo], None]
    hasSubMission: bool
    apSupplyOutOfDateDict: Dict[str, int]
    newsInfoList: Union[Dict[str, Act9D0DataActivityNewsInfo], None]
    newsServerInfoList: Union[
        Dict[str, Act9D0DataActivityNewsServerInfo],
        None,
    ]
    miscHub: Dict[str, str]


class Act12SideDataConstData(BaseStruct):
    recycleRewardThreshold: int
    charmRepoUnlockStageId: str
    recycleLowThreshold: int
    recycleMediumThreshold: int
    recycleHighThreshold: int
    autoGetCharmId: str
    fogStageId: str
    fogUnlockStageId: str
    fogUnlockTs: int
    fogUnlockDesc: str


class Act12SideDataZoneAdditionData(BaseStruct):
    zoneId: str
    unlockText: str
    zoneClass: str


class Act12SideDataMissionDescInfo(BaseStruct):
    zoneClass: str
    specialMissionDesc: str
    needLock: bool
    unlockHint: Union[str, None]
    unlockStage: Union[str, None]


class Act12SideDataMileStoneInfo(BaseStruct):
    mileStoneId: str
    orderId: int
    tokenNum: int
    item: ItemBundle
    isPrecious: bool
    mileStoneStage: int


class Act12SideDataPhotoInfo(BaseStruct):
    picId: str
    picName: str
    mileStoneId: str
    picDesc: str
    jumpStageId: Union[str, None]


class Act12SideDataRecycleDialogData(BaseStruct):
    dialogType: str
    dialog: str
    dialogExpress: str


class Act12SideData(BaseStruct):
    constData: Act12SideDataConstData
    zoneAdditionDataList: List[Act12SideDataZoneAdditionData]
    missionDescList: Dict[str, Act12SideDataMissionDescInfo]
    mileStoneInfoList: List[Act12SideDataMileStoneInfo]
    photoList: Dict[str, Act12SideDataPhotoInfo]
    recycleDialogDict: Dict[str, List[Act12SideDataRecycleDialogData]]


class Act13SideDataConstData(BaseStruct):
    prestigeDescList: List[str]
    dailyRandomCount: Union[List[List[int]], None]
    dailyWeightInitial: int
    dailyWeightComplete: int
    agendaRecover: int
    agendaMax: int
    agendaHint: int
    missionPoolMax: int
    missionBoardMax: int
    itemRandomList: List[ItemBundle]
    unlockPrestigeCond: str
    hotSpotShowFlag: int


class Act13SideDataPrestigeData(BaseStruct):
    rank: str
    threshold: int
    reward: Union[ItemBundle, None]
    newsCount: int
    archiveCount: int
    avgCount: int


class Act13SideDataLongTermMissionGroupData(BaseStruct):
    groupId: str
    groupName: str
    orgId: str
    missionList: List[str]


class Act13SideDataOrgSectionData(BaseStruct):
    sectionName: str
    sortId: int
    groupData: Act13SideDataLongTermMissionGroupData


class Act13SideDataOrgData(BaseStruct):
    orgId: str
    orgName: str
    orgEnName: str
    openTime: int
    principalIdList: List[str]
    prestigeList: List[Act13SideDataPrestigeData]
    agendaCount2PrestigeItemMap: Dict[str, ItemBundle]
    orgSectionList: List[Act13SideDataOrgSectionData]
    prestigeItem: ItemBundle


class Act13SideDataPrincipalData(BaseStruct):
    principalId: str
    principalName: str
    principalEnName: str
    avgCharId: str
    principalDescList: List[str]


class Act13SideDataLongTermMissionData(BaseStruct):
    missionName: str
    groupId: str
    principalId: str
    finishedDesc: str
    sectionSortId: int
    haveStageBtn: bool
    jumpStageId: Union[str, None]


class Act13SideDataDailyMissionData(BaseStruct):
    id_: str = field(name="id")
    sortId: int
    description: str
    missionName: str
    template: str
    templateType: str
    param: List[str]
    rewards: Union[List[MissionDisplayRewards], None]
    orgPool: Union[List[str], None]
    rewardPool: Union[List[str], None]
    jumpStageId: str
    agendaCount: int


class Act13SideDataDailyMissionRewardGroupData(BaseStruct):
    groupId: str
    rewards: List[ItemBundle]


class Act13SideDataArchiveItemUnlockData(BaseStruct):
    itemId: str
    itemType: str
    unlockCondition: str
    param1: Union[str, None]
    param2: Union[str, None]


class ActivityTableActHiddenAreaPreposeStageData(BaseStruct):
    stageId: str
    unlockRank: int


class ActivityTableActivityHiddenAreaData(BaseStruct):
    name: str
    desc: str
    preposedStage: List[ActivityTableActHiddenAreaPreposeStageData]
    preposedTime: int


class Act13SideDataZoneAdditionData(BaseStruct):
    unlockText: str
    zoneClass: str


class Act13SideData(BaseStruct):
    constData: Act13SideDataConstData
    orgDataMap: Dict[str, Act13SideDataOrgData]
    principalDataMap: Dict[str, Act13SideDataPrincipalData]
    longTermMissionDataMap: Dict[str, Act13SideDataLongTermMissionData]
    dailyMissionDataList: List[Act13SideDataDailyMissionData]
    dailyRewardGroupDataMap: Dict[
        str,
        Act13SideDataDailyMissionRewardGroupData,
    ]
    archiveItemUnlockData: Dict[str, Act13SideDataArchiveItemUnlockData]
    hiddenAreaData: Dict[str, ActivityTableActivityHiddenAreaData]
    zoneAddtionDataMap: Dict[str, Act13SideDataZoneAdditionData]


class Act17sideDataPlaceData(BaseStruct):
    placeId: str
    placeDesc: str
    lockEventId: Union[str, None]
    zoneId: str
    visibleCondType: Union[str, None] = None
    visibleParams: Union[List[str], None] = None


class Act17sideDataNodeInfoData(BaseStruct):
    nodeId: str
    nodeType: str
    sortId: int
    placeId: str
    isPointPlace: bool
    chapterId: str
    trackPointType: str
    unlockCondType: Union[str, None] = None
    unlockParams: Union[List[str], None] = None


class Act17sideDataLandmarkNodeData(BaseStruct):
    nodeId: str
    landmarkId: str
    landmarkName: str
    landmarkPic: Union[str, None]
    landmarkSpecialPic: str
    landmarkDesList: List[str]


class Act17sideDataStoryNodeData(BaseStruct):
    nodeId: str
    storyId: str
    storyKey: str
    storyName: str
    storyPic: Union[str, None]
    confirmDes: str
    storyDesList: List[str]


class Act17sideDataBattleNodeData(BaseStruct):
    nodeId: str
    stageId: str


class Act17sideDataTreasureNodeData(BaseStruct):
    nodeId: str
    treasureId: str
    treasureName: str
    treasurePic: Union[str, None]
    treasureSpecialPic: Union[str, None]
    endEventId: str
    confirmDes: str
    treasureDesList: List[str]
    missionIdList: List[str]
    rewardList: List[ItemBundle]
    treasureType: str


class Act17sideDataEventNodeData(BaseStruct):
    nodeId: str
    eventId: str
    endEventId: str


class Act17sideDataTechNodeData(BaseStruct):
    nodeId: str
    techTreeId: str
    techTreeName: str
    techPic: Union[str, None]
    techSpecialPic: str
    endEventId: str
    confirmDes: str
    techDesList: List[str]
    missionIdList: List[str]


class Act17sideDataChoiceNodeOptionData(BaseStruct):
    canRepeat: bool
    eventId: str
    des: str
    unlockDes: Union[str, None]
    unlockCondType: Union[str, None] = None
    unlockParams: Union[str, None] = None


class Act17sideDataChoiceNodeData(BaseStruct):
    nodeId: str
    choicePic: Union[str, None]
    isDisposable: bool
    choiceSpecialPic: Union[str, None]
    choiceName: str
    choiceDesList: List[str]
    cancelDes: str
    choiceNum: int
    optionList: List[Act17sideDataChoiceNodeOptionData]


class Act17sideDataEventData(BaseStruct):
    eventId: str
    eventPic: Union[str, None]
    eventSpecialPic: Union[str, None]
    eventTitle: str
    eventDesList: List[str]


class Act17sideDataArchiveItemUnlockData(BaseStruct):
    itemId: str
    itemType: str
    unlockCondition: str
    nodeId: Union[str, None]
    stageParam: str
    chapterId: Union[str, None]


class Act17sideDataTechTreeData(BaseStruct):
    techTreeId: str
    sortId: int
    techTreeName: str
    defaultBranchId: str
    lockDes: str


class Act17sideDataTechTreeBranchData(BaseStruct):
    techTreeBranchId: str
    techTreeId: str
    techTreeBranchName: str
    techTreeBranchIcon: str
    techTreeBranchDesc: str
    runeData: RuneTablePackedRuneData


class Act17sideDataMainlineChapterData(BaseStruct):
    chapterId: str
    chapterDes: str
    chapterIcon: str
    unlockDes: str
    id_: str = field(name="id")


class Act17sideDataMainlineData(BaseStruct):
    mainlineId: str
    nodeId: Union[str, None]
    sortId: int
    missionSort: str
    zoneId: str
    mainlineDes: str
    focusNodeId: Union[str, None]


class Act17sideDataZoneData(BaseStruct):
    zoneId: str
    unlockPlaceId: Union[str, None]
    unlockText: str


class Act17sideDataConstData(BaseStruct):
    techTreeUnlockEventId: str


class Act17sideData(BaseStruct):
    placeDataMap: Dict[str, Act17sideDataPlaceData]
    nodeInfoDataMap: Dict[str, Act17sideDataNodeInfoData]
    landmarkNodeDataMap: Dict[str, Act17sideDataLandmarkNodeData]
    storyNodeDataMap: Dict[str, Act17sideDataStoryNodeData]
    battleNodeDataMap: Dict[str, Act17sideDataBattleNodeData]
    treasureNodeDataMap: Dict[str, Act17sideDataTreasureNodeData]
    eventNodeDataMap: Dict[str, Act17sideDataEventNodeData]
    techNodeDataMap: Dict[str, Act17sideDataTechNodeData]
    choiceNodeDataMap: Dict[str, Act17sideDataChoiceNodeData]
    eventDataMap: Dict[str, Act17sideDataEventData]
    archiveItemUnlockDataMap: Dict[str, Act17sideDataArchiveItemUnlockData]
    techTreeDataMap: Dict[str, Act17sideDataTechTreeData]
    techTreeBranchDataMap: Dict[str, Act17sideDataTechTreeBranchData]
    mainlineChapterDataMap: Dict[str, Act17sideDataMainlineChapterData]
    mainlineDataMap: Dict[str, Act17sideDataMainlineData]
    zoneDataList: List[Act17sideDataZoneData]
    constData: Act17sideDataConstData


class Act20SideDataResidentCartData(BaseStruct):
    residentPic: str


class Act20SideData(BaseStruct):
    zoneAdditionDataMap: Dict[str, str]
    residentCartDatas: Dict[str, Act20SideDataResidentCartData]


class Act21SideDataZoneAddtionData(BaseStruct):
    zoneId: str
    unlockText: str
    stageUnlockText: Union[str, None]
    entryId: str


class Act21SideDataConstData(BaseStruct):
    lineConnectZone: str


class Act21SideData(BaseStruct):
    zoneAdditionDataMap: Dict[str, Act21SideDataZoneAddtionData]
    constData: Act21SideDataConstData


class ActivityLoginData(BaseStruct):
    description: str
    itemList: List[ItemBundle]
    apSupplyOutOfDateDict: Dict[str, int]


class ActivitySwitchCheckinConstData(BaseStruct):
    activityTime: str
    activityRule: str


class ActivitySwitchCheckinData(BaseStruct):
    constData: ActivitySwitchCheckinConstData
    rewards: Dict[str, List[ItemBundle]]
    apSupplyOutOfDateDict: Dict[str, int]
    rewardsTitle: Dict[str, str]


class ActivityMiniStoryDataZoneDescInfo(BaseStruct):
    zoneId: str
    unlockText: str


class ActivityMiniStoryDataFavorUpInfo(BaseStruct):
    charId: str
    displayStartTime: int
    displayEndTime: int


class ActivityMiniStoryData(BaseStruct):
    tokenItemId: str
    zoneDescList: Dict[str, ActivityMiniStoryDataZoneDescInfo]
    favorUpList: Dict[str, ActivityMiniStoryDataFavorUpInfo]
    extraDropZoneList: List[str]


class ActivityRoguelikeDataOuterBuffUnlockInfo(BaseStruct):
    buffLevel: int
    name: str
    iconId: str
    description: str
    usage: str
    itemId: str
    itemType: str
    cost: int


class ActivityRoguelikeDataOuterBuffUnlockInfoData(BaseStruct):
    buffId: str
    buffUnlockInfos: Dict[str, ActivityRoguelikeDataOuterBuffUnlockInfo]


class ActivityRoguelikeDataMileStoneItemInfo(BaseStruct):
    mileStoneId: str
    orderId: int
    tokenNum: int
    item: ItemBundle


class ActivityTableCustomUnlockCond(BaseStruct):
    actId: Union[str, None]
    stageId: str


class ActivityRoguelikeData(BaseStruct):
    outBuffInfos: Dict[str, ActivityRoguelikeDataOuterBuffUnlockInfoData]
    apSupplyOutOfDateDict: Dict[str, int]
    outerBuffToken: str
    shopToken: str
    relicUnlockTime: int
    milestoneTokenRatio: float
    outerBuffTokenRatio: float
    relicTokenRatio: float
    relicOuterBuffTokenRatio: float
    reOpenCoolDown: int
    tokenItem: ItemBundle
    charStoneId: str
    milestone: List[ActivityRoguelikeDataMileStoneItemInfo]
    unlockConds: List[ActivityTableCustomUnlockCond]


class ActivityMultiplayDataStageData(BaseStruct):
    stageId: str
    levelId: str
    groupId: str
    difficulty: str
    loadingPicId: str
    dangerLevel: str
    unlockConds: List[str]


class ActivityMultiplayDataStageGroupData(BaseStruct):
    groupId: str
    sortId: int
    code: str
    name: str
    description: str


class ActivityMultiplayDataMissionExtraData(BaseStruct):
    missionId: str
    isHard: bool


class ActivityMultiplayDataRoomMessageData(BaseStruct):
    sortId: int
    picId: str


class ActivityMultiplayDataConstData(BaseStruct):
    linkActId: str
    maxRetryTimeInTeamRoom: int
    maxRetryTimeInMatchRoom: int
    maxRetryTimeInBattle: int
    maxOperatorDelay: float
    maxPlaySpeed: float
    delayTimeNeedTip: float
    blockTimeNeedTip: float
    hideTeamNameFlag: bool
    settleRetryTime: float


class ActivityMultiplayData(BaseStruct):
    stages: Dict[str, ActivityMultiplayDataStageData]
    stageGroups: Dict[str, ActivityMultiplayDataStageGroupData]
    missionExtras: Dict[str, ActivityMultiplayDataMissionExtraData]
    roomMessages: List[ActivityMultiplayDataRoomMessageData]
    constData: ActivityMultiplayDataConstData
    unlockConds: List[ActivityTableCustomUnlockCond]


class ActivityInterlockDataStageAdditionData(BaseStruct):
    stageId: str
    stageType: str
    lockStageKey: Union[str, None]
    lockSortIndex: int


class ActivityInterlockDataTreasureMonsterData(BaseStruct):
    lockStageKey: str
    enemyId: str
    enemyName: str
    enemyIcon: str
    enemyDescription: str


class SharedCharDataCharEquipInfo(BaseStruct):
    hide: int
    locked: Union[bool, int]
    level: int


class SharedCharDataSharedCharSkillData(BaseStruct):
    skillId: str
    specializeLevel: int
    completeUpgradeTime: Union[int, None] = None
    unlock: Union[bool, Union[int, None]] = None
    state: Union[int, None] = None


class SharedCharDataTmplData(BaseStruct):
    skinId: str
    defaultSkillIndex: int
    skills: List[SharedCharDataSharedCharSkillData]
    currentEquip: Union[str, None]
    equip: Union[Dict[str, SharedCharDataSharedCharSkillData], None] = None


class SharedCharData(BaseStruct):
    charId: str
    potentialRank: int
    mainSkillLvl: int
    evolvePhase: int
    level: int
    favorPoint: int
    currentEquip: Union[str, None] = field(name="currentEquip", default=None)
    equips: Union[Dict[str, SharedCharDataCharEquipInfo], None] = field(
        name="equip",
        default={},
    )
    skillIndex: Union[int, None] = None
    skinId: Union[str, None] = None
    skin: Union[str, None] = None
    skills: Union[List[SharedCharDataSharedCharSkillData], None] = None
    crisisRecord: Union[Dict[str, int], None] = None
    crisisV2Record: Union[Dict[str, int], None] = None
    currentTmpl: Union[str, None] = None
    tmpl: Union[Dict[str, SharedCharDataTmplData], None] = None


class ActivityInterlockDataMileStoneItemInfo(BaseStruct):
    mileStoneId: str
    orderId: int
    tokenNum: int
    item: ItemBundle


class ActivityInterlockDataFinalStageProgressData(BaseStruct):
    stageId: str
    killCnt: int
    apCost: int
    favor: int
    exp: int
    gold: int


class ActivityInterlockData(BaseStruct):
    stageAdditionInfoMap: Dict[str, ActivityInterlockDataStageAdditionData]
    treasureMonsterMap: Dict[str, ActivityInterlockDataTreasureMonsterData]
    specialAssistData: SharedCharData
    mileStoneItemList: List[ActivityInterlockDataMileStoneItemInfo]
    finalStageProgressMap: Dict[
        str,
        List[ActivityInterlockDataFinalStageProgressData],
    ]


class ActivityBossRushDataZoneAdditionData(BaseStruct):
    unlockText: str
    displayStartTime: int


class ActivityBossRushDataBossRushStageGroupData(BaseStruct):
    stageGroupId: str
    sortId: int
    stageGroupName: str
    stageIdMap: Dict[str, str]
    waveBossInfo: List[List[str]]
    normalStageCount: int
    isHardStageGroup: bool
    unlockCondtion: Union[str, None]


class ActivityBossRushDataBossRushStageAdditionData(BaseStruct):
    stageId: str
    stageType: str
    stageGroupId: str
    teamIdList: List[str]
    unlockText: Union[str, None]


class ActivityBossRushDataDisplayDetailRewards(BaseStruct):
    occPercent: int
    dropCount: int
    type_: str = field(name="type")
    id_: str = field(name="id")
    dropType: int


class ActivityBossRushDataBossRushDropInfo(BaseStruct):
    clearWaveCount: int
    displayDetailRewards: List[ActivityBossRushDataDisplayDetailRewards]
    firstPassRewards: List[ItemBundle]
    passRewards: List[ItemBundle]


class ActivityBossRushDataBossRushMissionAdditionData(BaseStruct):
    missionId: str
    isRelicTask: bool


class ActivityBossRushDataBossRushTeamData(BaseStruct):
    teamId: str
    teamName: str
    charIdList: List[str]
    teamBuffName: Union[str, None]
    teamBuffDes: Union[str, None]
    teamBuffId: Union[str, None]
    maxCharNum: int
    runeData: Union[RuneTablePackedRuneData, None]


class ActivityBossRushDataRelicData(BaseStruct):
    relicId: str
    sortId: int
    name: str
    icon: str
    relicTaskId: str


class ActivityBossRushDataRelicLevelInfo(BaseStruct):
    level: int
    effectDesc: str
    runeData: RuneTablePackedRuneData
    needItemCount: int


class ActivityBossRushDataRelicLevelInfoData(BaseStruct):
    relicId: str
    levelInfos: Dict[str, ActivityBossRushDataRelicLevelInfo]


class ActivityBossRushDataBossRushMileStoneData(BaseStruct):
    mileStoneId: str
    mileStoneLvl: int
    needPointCnt: int
    rewardItem: ItemBundle


class ActivityBossRushDataConstData(BaseStruct):
    maxProvidedCharNum: int
    textMilestoneItemLevelDesc: str
    milestonePointId: str
    relicUpgradeItemId: str
    defaultRelictList: List[str]
    rewardSkinId: str


class ActivityBossRushData(BaseStruct):
    zoneAdditionDataMap: Dict[str, ActivityBossRushDataZoneAdditionData]
    stageGroupMap: Dict[str, ActivityBossRushDataBossRushStageGroupData]
    stageAdditionDataMap: Dict[
        str,
        ActivityBossRushDataBossRushStageAdditionData,
    ]
    stageDropDataMap: Dict[
        str,
        Dict[str, ActivityBossRushDataBossRushDropInfo],
    ]
    missionAdditionDataMap: Dict[
        str,
        ActivityBossRushDataBossRushMissionAdditionData,
    ]
    teamDataMap: Dict[str, ActivityBossRushDataBossRushTeamData]
    relicList: List[ActivityBossRushDataRelicData]
    relicLevelInfoDataMap: Dict[str, ActivityBossRushDataRelicLevelInfoData]
    mileStoneList: List[ActivityBossRushDataBossRushMileStoneData]
    bestWaveRuneList: List[RuneTablePackedRuneData]
    constData: ActivityBossRushDataConstData


class ActivityFloatParadeDataConstData(BaseStruct):
    cityName: str
    cityNamePic: str
    lowStandard: float
    variationTitle: str
    ruleDesc: str


class ActivityFloatParadeDataDailyData(BaseStruct):
    dayIndex: int
    dateName: str
    placeName: str
    placeEnName: str
    placePic: str
    eventGroupId: str
    extReward: Union[ItemBundle, None]


class ActivityFloatParadeDataRewardPool(BaseStruct):
    grpId: str
    id_: str = field(name="id")
    type_: str = field(name="type")
    name: str
    desc: Union[str, None]
    reward: ItemBundle


class ActivityFloatParadeDataTactic(BaseStruct):
    id_: int = field(name="id")
    name: str
    packName: str
    briefName: str
    rewardVar: Dict[str, float]


class ActivityFloatParadeDataGroupData(BaseStruct):
    groupId: str
    name: str
    startDay: int
    endDay: int
    extRewardDay: int
    extRewardCount: int


class ActivityFloatParadeData(BaseStruct):
    constData: ActivityFloatParadeDataConstData
    dailyDataDic: List[ActivityFloatParadeDataDailyData]
    rewardPools: Dict[str, Dict[str, ActivityFloatParadeDataRewardPool]]
    tacticList: List[ActivityFloatParadeDataTactic]
    groupInfos: Dict[str, ActivityFloatParadeDataGroupData]


class ActSandboxDataMilestoneData(BaseStruct):
    milestoneId: str
    orderId: int
    tokenId: str
    tokenNum: int
    item: ItemBundle
    isPrecious: bool


class ActSandboxData(BaseStruct):
    milestoneDataList: List[ActSandboxDataMilestoneData]
    milestoneTokenId: str


class ActivityMainlineBuffDataMissionGroupData(BaseStruct):
    id_: str = field(name="id")
    bindBanner: str
    sortId: int
    zoneId: str
    missionIdList: List[str]


class ActivityMainlineBuffDataPeriodDataStepData(BaseStruct):
    isBlock: bool
    favorUpDesc: Union[str, None]
    unlockDesc: Union[str, None]
    bindStageId: Union[str, None]
    blockDesc: Union[str, None]


class ActivityMainlineBuffDataPeriodData(BaseStruct):
    id_: str = field(name="id")
    startTime: int
    endTime: int
    favorUpCharDesc: str
    favorUpImgName: str
    newChapterImgName: str
    newChapterZoneId: Union[str, None]
    stepDataList: List[ActivityMainlineBuffDataPeriodDataStepData]


class ActivityMainlineBuffDataConstData(BaseStruct):
    favorUpStageRange: str


class ActivityMainlineBuffData(BaseStruct):
    missionGroupList: Dict[str, ActivityMainlineBuffDataMissionGroupData]
    periodDataList: List[ActivityMainlineBuffDataPeriodData]
    apSupplyOutOfDateDict: Dict[str, int]
    constData: ActivityMainlineBuffDataConstData


class Act24SideDataToolData(BaseStruct):
    toolId: str
    sortId: int
    toolName: str
    toolDesc: str
    toolIcon1: str
    toolIcon2: str
    toolUnlockDesc: str
    toolBuffId: str
    runeData: RuneTablePackedRuneData


class Act24SideDataMealData(BaseStruct):
    mealId: str
    sortId: int
    mealName: str
    mealEffectDesc: str
    mealDesc: str
    mealIcon: str
    mealCost: int
    mealRewardAP: int
    mealRewardItemInfo: ItemBundle


class Act24SideDataMeldingItemData(BaseStruct):
    meldingId: str
    sortId: int
    meldingPrice: int
    rarity: int


class Act24SideDataMeldingGachaBoxData(BaseStruct):
    gachaBoxId: str
    gachaSortId: int
    gachaIcon: str
    gachaBoxName: str
    gachaCost: int
    gachaTimesLimit: int
    themeColor: str
    remainItemBgColor: str


class Act24SideDataMeldingGachaBoxGoodData(BaseStruct):
    goodId: str
    gachaBoxId: str
    orderId: int
    itemId: str
    itemType: str
    displayType: str
    perCount: int
    totalCount: int
    gachaType: str


class Act24SideDataZoneAdditionData(BaseStruct):
    zoneId: str
    zoneIcon: str
    unlockText: str
    displayTime: str


class QuestStageData(BaseStruct):
    stageId: str
    stageRank: int
    sortId: int
    isUrgentStage: bool
    isDragonStage: bool


class Act24SideDataMissionExtraData(BaseStruct):
    taskTypeName: str
    taskTypeIcon: str
    taskType: str
    taskTitle: str
    taskClient: str
    taskClientDesc: str


class WeightItemBundle(BaseStruct):
    id_: str = field(name="id")
    type_: str = field(name="type")
    dropType: str
    count: int
    weight: int


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
    firstPassRewards: Union[List[ItemBundle], None]
    firstCompleteRewards: Union[List[ItemBundle], None]
    passRewards: Union[List[List[WeightItemBundle]], None]
    completeRewards: Union[List[List[WeightItemBundle]], None]
    displayRewards: List[StageDataDisplayRewards]
    displayDetailRewards: List[StageDataDisplayDetailRewards]


class Act24SideDataConstData(BaseStruct):
    stageUnlockToolDesc: str
    mealLackMoney: str
    mealDayTimesLimit: int
    toolMaximum: int
    stageCanNotUseToTool: List[str]
    gachaExtraProb: Union[float, int]


class Act24SideData(BaseStruct):
    toolDataList: Dict[str, Act24SideDataToolData]
    mealDataList: Dict[str, Act24SideDataMealData]
    meldingDict: Dict[str, Act24SideDataMeldingItemData]
    meldingGachaBoxDataList: Dict[str, Act24SideDataMeldingGachaBoxData]
    meldingGachaBoxGoodDataMap: Dict[
        str,
        List[Act24SideDataMeldingGachaBoxGoodData],
    ]
    mealWelcomeTxtDataMap: Dict[str, str]
    zoneAdditionDataMap: Dict[str, Act24SideDataZoneAdditionData]
    questStageList: List[QuestStageData]
    missionDataList: Dict[str, Act24SideDataMissionExtraData]
    meldingDropDict: Dict[str, StageDataStageDropInfo]
    stageMapPreviewDict: Dict[str, List[str]]
    constData: Act24SideDataConstData


class Act25SideDataConstData(BaseStruct):
    getDailyCount: int
    costName: str
    costDesc: str
    costLimit: int
    rewardLimit: int
    researchUnlockText: str
    harvestReward: ItemBundle
    costCount: int
    costCountLimit: int
    basicProgress: int
    harvestDesc: str


class Act25SideDataZoneDescInfo(BaseStruct):
    zoneId: str
    unlockText: str
    displayStartTime: int


class Act25SideDataArchiveItemData(BaseStruct):
    itemId: str
    itemType: int
    itemUnlockType: int
    itemUnlockParam: str
    unlockDesc: Union[str, None]
    iconId: Union[str, None]
    itemName: str


class Act25SideDataArchiveMapInfoData(BaseStruct):
    objectId: str
    type_: int = field(name="type")
    numberId: str
    areaId: str
    sortId: int
    position: int
    hasDot: bool


class Act25SideDataAreaInfoData(BaseStruct):
    areaId: str
    sortId: int
    areaIcon: str
    areaName: str
    unlockText: str
    preposedStage: str
    areaInitialDesc: str
    areaEndingDesc: str
    areaEndingAud: str
    reward: ItemBundle
    finalId: str


class Act25SideDataAreaMissionData(BaseStruct):
    id_: str = field(name="id")
    areaId: str
    preposedMissionId: Union[str, None]
    sortId: int
    isZone: bool
    stageId: str
    costCount: int
    transform: int
    progress: int
    progressPicId: str
    template: Union[str, None]
    templateType: int
    desc: str
    param: Union[List[str], None]
    rewards: List[ItemBundle]
    archiveItems: List[str]


class Act25SideDataBattlePerformanceData(BaseStruct):
    itemId: str
    sortId: int
    itemName: str
    itemIcon: str
    itemDesc: str
    itemTechType: str
    runeData: RuneTablePackedRuneData


class Act25SideDataKeyData(BaseStruct):
    keyId: str
    keyName: str
    keyIcon: str
    toastText: str


class Act25SideDataFogUnlockData(BaseStruct):
    lockId: str
    lockedCollectionIconId: str
    unlockedCollectionIconId: str


class Act25SideDataDailyFarmData(BaseStruct):
    transform: int
    unitTime: int


class Act25SideData(BaseStruct):
    tokenItemId: str
    constData: Act25SideDataConstData
    zoneDescList: Dict[str, Act25SideDataZoneDescInfo]
    archiveItemData: Dict[str, Act25SideDataArchiveItemData]
    arcMapInfoData: Dict[str, Act25SideDataArchiveMapInfoData]
    areaInfoData: Dict[str, Act25SideDataAreaInfoData]
    areaMissionData: Dict[str, Act25SideDataAreaMissionData]
    battlePerformanceData: Dict[str, Act25SideDataBattlePerformanceData]
    keyData: Dict[str, Act25SideDataKeyData]
    fogUnlockData: Dict[str, Act25SideDataFogUnlockData]
    farmList: List[Act25SideDataDailyFarmData]


class Act38D1DataAct38D1NodeData(BaseStruct):
    slotId: str
    groupId: Union[str, None]
    isUpper: bool
    adjacentSlotList: List[str]


class Act38D1DataAct38D1RoadData(BaseStruct):
    roadId: str
    startSlotId: str
    endSlotId: str


class Act38D1DataAct38D1RewardBoxData(BaseStruct):
    rewardBoxId: str
    roadId: str


class Act38D1DataAct38D1ExclusionGroupData(BaseStruct):
    groupId: str
    slotIdList: List[str]


class Act38D1DataAct38D1DimensionItemData(BaseStruct):
    desc: str
    maxScore: int


class Act38D1DataAct38D1CommentData(BaseStruct):
    id_: str = field(name="id")
    sortId: int
    desc: str


class Act38D1DataAct38D1StageDetailData(BaseStruct):
    nodeDataMap: Dict[str, Act38D1DataAct38D1NodeData]
    roadDataMap: Dict[str, Act38D1DataAct38D1RoadData]
    rewardBoxDataMap: Dict[str, Act38D1DataAct38D1RewardBoxData]
    exclusionGroupDataMap: Dict[str, Act38D1DataAct38D1ExclusionGroupData]
    dimensionItemList: List[Act38D1DataAct38D1DimensionItemData]
    commentDataMap: Dict[str, Act38D1DataAct38D1CommentData]


class Act38D1DataAct38D1ConstData(BaseStruct):
    redScoreThreshold: int
    detailBkgRedThreshold: int
    voiceGrade: int
    stageInfoTitle: str
    missionListReceiveRewardText: str
    missionListChangeMapText: str
    missionListCompleteTagText: str
    mapStartBattleText: str
    mapJumpDailyMapText: str
    mapRewardReceivedText: str


class Act38D1Data(BaseStruct):
    scoreLevelToAppraiseDataMap: Dict[str, str]
    detailDataMap: Dict[str, Act38D1DataAct38D1StageDetailData]
    constData: Act38D1DataAct38D1ConstData
    trackPointPeriodData: List[int]


class Act27SideDataAct27SideGoodData(BaseStruct):
    id_: str = field(name="id")
    name: str
    typeDesc: str
    iconId: str
    launchIconId: str
    purchasePrice: List[int]
    sellingPriceList: List[int]
    sellShopList: List[str]
    isPermanent: bool


class Act27SideDataAct27SideMileStoneData(BaseStruct):
    mileStoneId: str
    mileStoneLvl: int
    needPointCnt: int
    rewardItem: ItemBundle


class Act27SideDataAct27SideGoodLaunchData(BaseStruct):
    groupId: str
    startTime: int
    stageId: Union[str, None]
    code: Union[str, None]
    drinkId: str
    foodId: str
    souvenirId: str


class Act27SideDataAct27SideShopData(BaseStruct):
    shopId: str
    sortId: int
    name: str
    iconId: str


class Act27SideDataAct27SideInquireData(BaseStruct):
    mileStonePt: int
    inquireCount: int


class Act27SideDataAct27SideDynEntrySwitchData(BaseStruct):
    entryId: str
    startHour: int
    signalId: str


class Act27SideDataAct27sideZoneAdditionData(BaseStruct):
    zoneId: str
    unlockText: str
    displayTime: str


class Act27SideDataAct27SideMileStoneFurniRewardData(BaseStruct):
    furniId: str
    pointNum: int


class Act27SideDataAct27SideConstData(BaseStruct):
    stageId: str
    stageCode: str
    purchasePriceName: List[str]
    furniRewardList: List[Act27SideDataAct27SideMileStoneFurniRewardData]
    prizeText: str
    playerShopId: str
    milestonePointName: str
    inquirePanelTitle: str
    inquirePanelDesc: str
    gain123: List[float]
    gain113: List[float]
    gain122: List[float]
    gain111: List[float]
    gain11None: List[float]
    gain12None: List[float]
    campaignEnemyCnt: int


class Act27SideData(BaseStruct):
    goodDataMap: Dict[str, Act27SideDataAct27SideGoodData]
    mileStoneList: List[Act27SideDataAct27SideMileStoneData]
    goodLaunchDataList: List[Act27SideDataAct27SideGoodLaunchData]
    shopDataMap: Dict[str, Act27SideDataAct27SideShopData]
    inquireDataList: List[Act27SideDataAct27SideInquireData]
    dynEntrySwitchData: List[Act27SideDataAct27SideDynEntrySwitchData]
    zoneAdditionDataMap: Dict[str, Act27SideDataAct27sideZoneAdditionData]
    constData: Act27SideDataAct27SideConstData


class Act42D0DataAreaInfoData(BaseStruct):
    areaId: str
    sortId: int
    areaCode: str
    areaName: str
    difficulty: str
    areaDesc: str
    costLimit: int
    bossIcon: str
    bossId: Union[str, None]
    nextAreaStage: Union[str, None]


class Act42D0DataStageInfoData(BaseStruct):
    stageId: str
    areaId: str
    stageCode: str
    sortId: int
    stageDesc: List[str]
    levelId: str
    code: str
    name: str
    loadingPicId: str


class Act42D0DataEffectGroupInfoData(BaseStruct):
    effectGroupId: str
    sortId: int
    effectGroupName: str


class Act42D0DataEffectInfoRuneData(BaseStruct):
    id_: str = field(name="id")
    points: int
    mutexGroupKey: Union[str, None]
    description: str
    runes: List[RuneData]


class Act42D0DataEffectInfoData(BaseStruct):
    effectId: str
    effectGroupId: str
    row: int
    col: int
    effectName: str
    effectIcon: str
    cost: int
    effectDesc: str
    unlockTime: int
    runeData: Act42D0DataEffectInfoRuneData


class ChallengeMissionData(BaseStruct):
    missionId: str
    sortId: int
    stageId: str
    missionDesc: str
    milestoneCount: int


class Act42D0DataChallengeInfoData(BaseStruct):
    stageId: str
    stageDesc: str
    startTs: int
    endTs: int
    levelId: str
    code: str
    name: str
    loadingPicId: str
    challengeMissionData: List[ChallengeMissionData]


class StageRatingInfoMilestoneData(BaseStruct):
    ratingLevel: int
    costUpLimit: int
    achivement: str
    icon: str
    milestoneCount: int


class Act42D0DataStageRatingInfo(BaseStruct):
    stageId: str
    areaId: str
    milestoneData: List[StageRatingInfoMilestoneData]


class Act42D0DataMilestoneData(BaseStruct):
    milestoneId: str
    orderId: int
    tokenNum: int
    item: ItemBundle


class Act42D0DataConstData(BaseStruct):
    milestoneId: str
    strifeName: str
    strifeDesc: str
    unlockDesc: str
    rewardDesc: str
    traumaDesc: str
    milestoneAreaName: str
    traumaName: str


class Act42D0Data(BaseStruct):
    areaInfoData: Dict[str, Act42D0DataAreaInfoData]
    stageInfoData: Dict[str, Act42D0DataStageInfoData]
    effectGroupInfoData: Dict[str, Act42D0DataEffectGroupInfoData]
    effectInfoData: Dict[str, Act42D0DataEffectInfoData]
    challengeInfoData: Dict[str, Act42D0DataChallengeInfoData]
    stageRatingInfoData: Dict[str, Act42D0DataStageRatingInfo]
    milestoneData: List[Act42D0DataMilestoneData]
    constData: Act42D0DataConstData
    trackPointPeriodData: List[int]


class Act29SideFragData(BaseStruct):
    fragId: str
    sortId: int
    fragName: str
    fragIcon: str
    fragStoreIcon: str


class Act29SideOrcheType(Enum):
    ORCHE_1 = "ORCHE_1"
    ORCHE_2 = "ORCHE_2"
    ORCHE_3 = "ORCHE_3"
    ENUM = "ENUM"


class Act29SideOrcheData(BaseStruct):
    id_: str = field(name="id")
    name: str
    desc: str
    icon: str
    sortId: int
    orcheType: Act29SideOrcheType


class Act29SideProductType(Enum):
    PRODUCT_TYPE_1 = "PRODUCT_TYPE_1"
    PRODUCT_TYPE_2 = "PRODUCT_TYPE_2"
    PRODUCT_TYPE_3 = "PRODUCT_TYPE_3"
    PRODUCT_TYPE_4 = "PRODUCT_TYPE_4"
    PRODUCT_TYPE_5 = "PRODUCT_TYPE_5"
    ENUM = "ENUM"


class Act29SideProductGroupData(BaseStruct):
    groupId: str
    groupName: str
    groupIcon: str
    groupDesc: str
    defaultBgmSignal: str
    productList: List[str]
    groupEngName: str
    groupSmallName: str
    groupTypeIcon: str
    groupStoreIconId: str
    groupTypeBasePic: str
    groupTypeEyeIcon: str
    groupSortId: int
    formList: List[str]
    sheetId: str
    sheetNum: int
    sheetRotateSpd: float
    productType: Act29SideProductType
    productDescColor: str
    playTintColor: str
    confirmTintColor: str
    confirmDescColor: str
    bagThemeColor: str


class Act29SideProductData(BaseStruct):
    id_: str = field(name="id")
    orcheId: Union[str, None]
    groupId: str
    formId: Union[str, None]
    musicId: str


class Act29SideFormData(BaseStruct):
    formId: str
    fragIdList: List[str]
    formDesc: str
    productIdDict: Dict[str, str]
    withoutOrcheProductId: str
    groupId: str
    formSortId: int


class Act29SideInvestResultData(BaseStruct):
    resultId: str
    resultTitle: str
    resultDesc1: str
    resultDesc2: str


class Act29SideInvestType(Enum):
    MAJOR = "MAJOR"
    RARE = "RARE"
    NORMAL = "NORMAL"


class Act29SideInvestData(BaseStruct):
    investId: str
    investType: Act29SideInvestType
    investNpcName: str
    storyId: str
    investNpcPic: str
    investNpcAvatarPic: str
    majorNpcPic: Union[str, None]
    majorNpcBlackPic: Union[str, None]
    reward: Union[ItemBundle, None]
    investSucResultId: Union[str, None]
    investFailResultId: str
    investRareResultId: Union[str, None]


class Act29SideConstData(BaseStruct):
    majorInvestUnlockItemName: str
    wrongTipsTriggerTime: int
    majorInvestCompleteImgId: str
    majorInvestUnknownAvatarId: str
    majorInvestDetailDesc1: str
    majorInvestDetailDesc2: str
    majorInvestDetailDesc3: str
    majorInvestDetailDesc4: str
    hiddenInvestImgId: str
    hiddenInvestHeadImgId: str
    hiddenInvestNpcName: str
    unlockLevelId: str
    investResultHint: str
    investUnlockText: str
    noOrcheDesc: str


class Act29SideZoneAdditionData(BaseStruct):
    zoneId: str
    unlockText: str


class Act29SideMusicData(BaseStruct):
    groupId: str
    orcheId: Union[str, None]
    musicId: str


class Act29SideData(BaseStruct):
    fragDataMap: Dict[str, Act29SideFragData]
    orcheDataMap: Dict[str, Act29SideOrcheData]
    productGroupDataMap: Dict[str, Act29SideProductGroupData]
    productDataMap: Dict[str, Act29SideProductData]
    formDataMap: Dict[str, Act29SideFormData]
    investResultDataMap: Dict[str, Act29SideInvestResultData]
    investDataMap: Dict[str, Act29SideInvestData]
    majorInvestIdList: List[str]
    rareInvestIdList: List[str]
    constData: Act29SideConstData
    zoneAdditionDataMap: Dict[str, Act29SideZoneAdditionData]
    musicDataMap: List[Act29SideMusicData]


class ActivityTableActivityDetailTable(BaseStruct):
    DEFAULT: Dict[str, DefaultFirstData]
    CHECKIN_ONLY: Dict[str, DefaultCheckInData]
    CHECKIN_ALL_PLAYER: Dict[str, AllPlayerCheckinData]
    CHECKIN_VS: Dict[str, VersusCheckInData]
    TYPE_ACT3D0: Dict[str, Act3D0Data]
    TYPE_ACT4D0: Dict[str, Act4D0Data]
    TYPE_ACT5D0: Dict[str, Act5D0Data]
    TYPE_ACT5D1: Dict[str, Act5D1Data]
    COLLECTION: Dict[str, ActivityCollectionData]
    TYPE_ACT9D0: Dict[str, Act9D0Data]
    TYPE_ACT12SIDE: Dict[str, Act12SideData]
    TYPE_ACT13SIDE: Dict[str, Act13SideData]
    TYPE_ACT17SIDE: Dict[str, Act17sideData]
    TYPE_ACT20SIDE: Dict[str, Act20SideData]
    TYPE_ACT21SIDE: Dict[str, Act21SideData]
    TYPE_ACT29SIDE: Dict[str, Act29SideData]
    LOGIN_ONLY: Dict[str, ActivityLoginData]
    SWITCH_ONLY: Dict[str, ActivitySwitchCheckinData]
    MINISTORY: Dict[str, ActivityMiniStoryData]
    ROGUELIKE: Dict[str, ActivityRoguelikeData]
    MULTIPLAY: Dict[str, ActivityMultiplayData]
    INTERLOCK: Dict[str, ActivityInterlockData]
    BOSS_RUSH: Dict[str, ActivityBossRushData]
    FLOAT_PARADE: Dict[str, ActivityFloatParadeData]
    MAIN_BUFF: Dict[str, ActivityMainlineBuffData]
    TYPE_ACT24SIDE: Dict[str, Act24SideData]
    TYPE_ACT25SIDE: Dict[str, Act25SideData]
    TYPE_ACT27SIDE: Dict[str, Act27SideData]
    TYPE_ACT42D0: Dict[str, Act42D0Data]
    SANDBOX: Union[Dict[str, ActSandboxData], None] = None  # Remove in 2.2.01
    TYPE_ACT38D1: Union[Dict[str, Act38D1Data], None] = None  # Remove in 2.1.21


class ActivityStageRewardData(BaseStruct):
    stageRewardsDict: Dict[str, List[StageDataDisplayDetailRewards]]


class ActivityThemeDataTimeNode(BaseStruct):
    title: str
    ts: int


class ActivityThemeData(BaseStruct):
    id_: str = field(name="id")
    type_: str = field(name="type")
    funcId: str
    endTs: int
    sortId: int
    itemId: Union[str, None]
    timeNodes: List[ActivityThemeDataTimeNode]
    startTs: int


class StageDataConditionDesc(BaseStruct):
    stageId: str
    completeState: int


class AprilFoolStageData(BaseStruct):
    stageId: str
    levelId: str
    code: str
    name: str
    appearanceStyle: int
    loadingPicId: str
    difficulty: str
    unlockCondition: List[StageDataConditionDesc]
    stageDropInfo: List[ItemBundle]


class AprilFoolScoreData(BaseStruct):
    stageId: str
    sortId: int
    playerName: str
    playerScore: int


class AprilFoolConst(BaseStruct):
    battleFinishLoseDes: str
    killEnemyDes: str
    killBossDes: str
    totalTime: str


class Act4funPerformGroupInfo(BaseStruct):
    performGroupId: str
    performIds: List[str]


class Act4funPerformWordData(BaseStruct):
    text: str
    picId: str
    backgroundId: str


class Act4funPerformInfo(BaseStruct):
    performId: str
    performFinishedPicId: Union[str, None]
    fixedCmpGroup: Union[str, None]
    cmpGroups: List[Union[str, None]]
    words: List[Act4funPerformWordData]


class Act4funLiveMatEffectInfo(BaseStruct):
    liveMatEffectId: str
    valueId: str
    performGroup: str


class Act4funLiveMatInfoData(BaseStruct):
    liveMatId: str
    stageId: str
    name: str
    picId: str
    tagTxt: str
    emojiIcon: str
    selectedPerformId: str
    effectInfos: Dict[str, Act4funLiveMatEffectInfo]


class Act4funSpLiveMatInfoData(BaseStruct):
    spLiveMatId: str
    spLiveEveId: str
    stageId: str
    name: str
    picId: str
    tagTxt: str
    emojiIcon: str
    accordingPerformId: Union[str, None]
    selectedPerformId: Union[str, None]
    valueEffectId: str
    accordingSuperChatId: Union[str, None]


class Act4funValueEffectInfoData(BaseStruct):
    valueEffectId: str
    effectParams: Dict[str, int]


class Act4funLiveValueInfoData(BaseStruct):
    liveValueId: str
    name: str
    stageId: str
    iconId: str
    highEndingId: str
    lowEndingId: str
    increaseToastTxt: str
    decreaseToastTxt: str


class Act4funSuperChatInfo(BaseStruct):
    superChatId: str
    chatType: int
    userName: str
    iconId: str
    valueEffectId: str
    performId: str
    superChatTxt: str


class Act4funCmtInfo(BaseStruct):
    iconId: Union[str, None]
    name: Union[str, None]
    cmtTxt: str


class Act4funCmtGroupInfo(BaseStruct):
    cmtGroupId: str
    cmtList: List[Act4funCmtInfo]


class Act4funEndingInfo(BaseStruct):
    endingId: str
    endingAvg: str
    endingDesc: Union[str, None]
    stageId: Union[str, None]
    isGoodEnding: bool


class Act4funTokenInfoData(BaseStruct):
    tokenLevelId: str
    levelDesc: Union[str, None]
    skillDesc: str
    tokenLevelNum: int
    levelIconId: str


class Act4funMissionData(BaseStruct):
    missionId: str
    sortId: str
    missionDes: str
    rewardIconIds: List[str]
    rewards: List[ItemBundle]


class Act4funConst(BaseStruct):
    liveMatAmtLowerLimit: int
    liveTurnUpperLimit: int
    superChatCountDownNum: int
    badEndingPerformEffectTitle: str
    performEffectTitle: str
    defaultPerformPicId: str
    defaultTxtBackground: str
    openingPerformGroup: str
    forgetPerformGroup: str
    runPerformGroup: str
    liveMatDefaultUserIcon: str
    liveMatAttributeIcon: str
    liveMatAttribIconDiffNum: int
    liveValueAbsLimit: int
    cmtAppearTimeLowerLimit: float
    cmtAppearTimeUpperLimit: float
    subtitleIntervalTime: float
    mainPageEventDes: str
    spStageEndingTip: str
    noLiveEndingTip: str
    notEnoughEndingTip: str
    enoughEndingTip: str
    mainPagePersonal: str
    mainPageJobDes: str
    endingPageConfirmTxt: str
    runConfirmTxt: str
    mainPageDiamondMissionId: str
    reconnectConfirmTxt: str
    studyStageId: str
    goodEndingToastTxt: str
    tokenLevelUpToastTxt: str
    studyStageToastTxt: str
    matNotEnoughToastTxt: str
    formalLevelUnlockToastTxt: str


class Act4funStageExtraData(BaseStruct):
    description: str
    valueIconId: Union[str, None]


class Act4funData(BaseStruct):
    performGroupInfoDict: Dict[str, Act4funPerformGroupInfo]
    performInfoDict: Dict[str, Act4funPerformInfo]
    normalMatDict: Dict[str, Act4funLiveMatInfoData]
    spMatDict: Dict[str, Act4funSpLiveMatInfoData]
    valueEffectInfoDict: Dict[str, Act4funValueEffectInfoData]
    liveValueInfoDict: Dict[str, Act4funLiveValueInfoData]
    superChatInfoDict: Dict[str, Act4funSuperChatInfo]
    cmtGroupInfoDict: Dict[str, Act4funCmtGroupInfo]
    cmtUsers: List[str]
    endingDict: Dict[str, Act4funEndingInfo]
    tokenLevelInfos: Dict[str, Act4funTokenInfoData]
    missionDatas: Dict[str, Act4funMissionData]
    constant: Act4funConst
    stageExtraDatas: Dict[str, Act4funStageExtraData]
    randomMsgText: List[str]
    randomUserIconId: List[str]


class AprilFoolTable(BaseStruct):
    stages: Dict[str, AprilFoolStageData]
    scoreDict: Dict[str, List[AprilFoolScoreData]]
    constant: AprilFoolConst
    act4FunData: Act4funData


class CartComponents(BaseStruct):
    compId: str
    sortId: int
    type_: str = field(name="type")
    posList: List[str]
    posIdDict: Dict[str, List[str]]
    name: str
    icon: str
    showScores: int
    itemUsage: str
    itemDesc: str
    itemObtain: str
    rarity: int
    detailDesc: str
    price: int
    specialObtain: str
    obtainInRandom: bool
    additiveColor: Union[str, None]


class CartDataCartConstData(BaseStruct):
    carItemUnlockStageId: str
    carItemUnlockDesc: str
    spLevelUnlockItemCnt: int
    mileStoneBaseInterval: int
    spStageIds: List[str]
    carFrameDefaultColor: str


class CartData(BaseStruct):
    carDict: Dict[str, CartComponents]
    runeDataDict: Dict[str, RuneTablePackedRuneData]
    cartStages: List[str]
    constData: CartDataCartConstData


class SiracusaDataAreaData(BaseStruct):
    areaId: str
    areaName: str
    areaSubName: str
    unlockType: str
    unlockStage: Union[str, None]
    areaIconId: str
    pointList: List[str]


class SiracusaDataPointData(BaseStruct):
    pointId: str
    areaId: str
    pointName: str
    pointDesc: str
    pointIconId: str
    pointItaName: str


class SiracusaDataCharCardData(BaseStruct):
    charCardId: str
    sortIndex: int
    avgChar: str
    avgCharOffsetY: Union[float, int]
    charCardName: str
    charCardItaName: str
    charCardTitle: str
    charCardDesc: str
    fullCompleteDes: str
    gainDesc: str
    themeColor: str
    taskRingList: List[str]
    operaItemId: str
    gainParamList: Union[List[str], None]


class SiracusaDataTaskRingData(BaseStruct):
    taskRingId: str
    sortIndex: int
    charCardId: str
    logicType: str
    ringText: str
    item: ItemBundle
    isPrecious: bool
    taskIdList: List[str]


class SiracusaDataTaskBasicInfoData(BaseStruct):
    taskId: str
    taskRingId: str
    sortIndex: int
    placeId: str
    npcId: Union[str, None]
    taskType: str


class SiracusaDataBattleTaskData(BaseStruct):
    taskId: str
    stageId: str
    battleTaskDesc: str


class SiracusaDataAVGTaskData(BaseStruct):
    taskId: str
    taskAvg: str


class SiracusaDataItemInfoData(BaseStruct):
    itemId: str
    itemName: str
    itemItalyName: str
    itemDesc: str
    itemIcon: str


class SiracusaDataItemCardInfoData(BaseStruct):
    cardId: str
    cardName: str
    cardDesc: str
    optionScript: str


class SiracusaDataNavigationInfoData(BaseStruct):
    entryId: str
    navigationType: str
    entryIcon: str
    entryName: Union[str, None]
    entrySubName: Union[str, None]


class SiracusaDataOptionInfoData(BaseStruct):
    optionId: str
    optionDesc: str
    optionScript: str
    optionGoToScript: Union[str, None]
    isLeaveOption: bool
    needCommentLike: bool
    requireCardId: Union[str, None]


class SiracusaDataStagePointInfoData(BaseStruct):
    stageId: str
    pointId: str
    sortId: int
    isTaskStage: bool


class SiracusaDataStoryBriefInfoData(BaseStruct):
    storyId: str
    stageId: str
    storyInfo: str


class SiracusaDataOperaInfoData(BaseStruct):
    operaId: str
    sortId: int
    operaName: str
    operaSubName: str
    operaScore: str
    unlockTime: int


class SiracusaDataOperaCommentInfoData(BaseStruct):
    commentId: str
    referenceOperaId: str
    columnIndex: int
    columnSortId: int
    commentTitle: str
    score: str
    commentContent: str
    commentCharId: str


class SiracusaDataConstData(BaseStruct):
    operaDailyNum: int
    operaAllUnlockTime: int
    defaultFocusArea: str


class SiracusaData(BaseStruct):
    areaDataMap: Dict[str, SiracusaDataAreaData]
    pointDataMap: Dict[str, SiracusaDataPointData]
    charCardMap: Dict[str, SiracusaDataCharCardData]
    taskRingMap: Dict[str, SiracusaDataTaskRingData]
    taskInfoMap: Dict[str, SiracusaDataTaskBasicInfoData]
    battleTaskMap: Dict[str, SiracusaDataBattleTaskData]
    avgTaskMap: Dict[str, SiracusaDataAVGTaskData]
    itemInfoMap: Dict[str, SiracusaDataItemInfoData]
    itemCardInfoMap: Dict[str, SiracusaDataItemCardInfoData]
    navigationInfoMap: Dict[str, SiracusaDataNavigationInfoData]
    optionInfoMap: Dict[str, SiracusaDataOptionInfoData]
    stagePointList: List[SiracusaDataStagePointInfoData]
    storyBriefInfoDataMap: Dict[str, SiracusaDataStoryBriefInfoData]
    operaInfoMap: Dict[str, SiracusaDataOperaInfoData]
    operaCommentInfoMap: Dict[str, SiracusaDataOperaCommentInfoData]
    constData: SiracusaDataConstData


class KVSwitchInfo(BaseStruct):
    isDefault: bool
    displayTime: int
    zoneId: Union[str, None]


class ActivityKVSwitchData(BaseStruct):
    kvSwitchInfo: Dict[str, KVSwitchInfo]


class DynEntrySwitchInfo(BaseStruct):
    entryId: str
    sortId: int
    stageId: Union[str, None]


class ActivityDynEntrySwitchData(BaseStruct):
    entrySwitchInfo: Dict[str, DynEntrySwitchInfo]


class ActivityTableActivityHiddenStageUnlockConditionData(BaseStruct):
    unlockStageId: str
    unlockTemplate: str
    unlockParams: Union[List[str], None]
    missionStageId: str
    unlockedName: str
    lockedName: str
    lockCode: str
    unlockedDes: str
    templateDesc: str
    desc: str
    riddle: str


class ActivityTableActivityHiddenStageData(BaseStruct):
    stageId: str
    encodedName: str
    showStageId: str
    rewardDiamond: bool
    missions: List[ActivityTableActivityHiddenStageUnlockConditionData]


class ActivityTableExtraData(BaseStruct):
    periodId: str
    startTs: int
    endTs: int


class ActivityTable(BaseStruct):
    __version__ = "24-02-02-10-18-07-831ad8"

    basicInfo: Dict[str, ActivityTableBasicData]
    homeActConfig: Dict[str, ActivityTableHomeActivityConfig]
    zoneToActivity: Dict[str, str]
    missionData: List[MissionData]
    missionGroup: List[MissionGroup]
    replicateMissions: Union[Dict[str, str], None]
    activity: ActivityTableActivityDetailTable
    extraData: Dict[str, Dict[str, Dict[str, List[ActivityTableExtraData]]]]
    activityItems: Dict[str, List[str]]
    syncPoints: Dict[str, List[int]]
    dynActs: Any
    stageRewardsData: Dict[str, ActivityStageRewardData]
    actThemes: List[ActivityThemeData]
    actFunData: AprilFoolTable
    carData: CartData
    siracusaData: SiracusaData
    kvSwitchData: Dict[str, ActivityKVSwitchData]
    dynEntrySwitchData: Dict[str, ActivityDynEntrySwitchData]
    hiddenStageData: List[ActivityTableActivityHiddenStageData]
    stringRes: Dict[str, Dict[str, str]]
