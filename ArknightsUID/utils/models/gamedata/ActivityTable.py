from pydantic import BaseModel, Field


class ActivityTableBasicData(BaseModel):
    id_: str = Field(alias='id')
    type_: str = Field(alias='type')
    displayType: str | None = None
    name: str
    startTime: int
    endTime: int
    rewardEndTime: int
    displayOnHome: bool
    hasStage: bool
    templateShopId: str | None
    medalGroupId: str | None
    ungroupedMedalIds: list[str] | None = None
    isReplicate: bool
    needFixedSync: bool


class ActivityTableHomeActivityConfig(BaseModel):
    actId: str
    isPopupAfterCheckin: bool
    showTopBarMenu: bool
    actTopBarColor: str | None
    actTopBarText: str | None


class MissionDisplayRewards(BaseModel):
    type_: str = Field(alias='type')
    id_: str = Field(alias='id')
    count: int


class MissionData(BaseModel):
    id_: str = Field(alias='id')
    sortId: int
    description: str
    type_: str = Field(alias='type')
    itemBgType: str
    preMissionIds: list[str] | None
    template: str
    templateType: str
    param: list[str]
    unlockCondition: str | None
    unlockParam: list[str] | None
    missionGroup: str
    toPage: str | None
    periodicalPoint: int
    rewards: list[MissionDisplayRewards] | None
    backImagePath: str | None
    foldId: str | None
    haveSubMissionToUnlock: bool


class MissionGroup(BaseModel):
    id_: str = Field(alias='id')
    title: str | None
    type_: str = Field(alias='type')
    preMissionGroup: str | None
    period: list[int] | None
    rewards: list[MissionDisplayRewards] | None
    missionIds: list[str]
    startTs: int
    endTs: int


class DefaultZoneData(BaseModel):
    zoneId: str
    zoneIndex: str
    zoneName: str
    zoneDesc: str
    itemDropList: list[str]


class ItemBundle(BaseModel):
    id_: str = Field(alias='id')
    count: int
    type_: str = Field(alias='type')


class DefaultShopData(BaseModel):
    goodId: str
    slotId: int
    price: int
    availCount: int
    overrideName: str
    item: ItemBundle


class DefaultFirstData(BaseModel):
    zoneList: list[DefaultZoneData]
    shopList: list[DefaultShopData] | None


class DefaultCheckInDataCheckInDailyInfo(BaseModel):
    itemList: list[ItemBundle]
    order: int
    color: int
    keyItem: int
    showItemOrder: int
    isDynItem: bool


class DefaultCheckInDataDynCheckInDailyInfo(BaseModel):
    questionDesc: str
    preOption: str
    optionList: list[str]
    showDay: int
    spOrderIconId: str
    spOrderDesc: str
    spOrderCompleteDesc: str


class DefaultCheckInDataOptionInfo(BaseModel):
    optionDesc: str | None
    showImageId1: str | None
    showImageId2: str | None
    optionCompleteDesc: str | None
    isStart: bool


class DefaultCheckInDataDynamicCheckInConsts(BaseModel):
    firstQuestionDesc: str
    firstQuestionTipsDesc: str
    expirationDesc: str
    firstQuestionConfirmDesc: str


class DefaultCheckInDataDynamicCheckInData(BaseModel):
    dynCheckInDict: dict[str, DefaultCheckInDataDynCheckInDailyInfo]
    dynOptionDict: dict[str, DefaultCheckInDataOptionInfo]
    dynItemDict: dict[str, list[ItemBundle]]
    constData: DefaultCheckInDataDynamicCheckInConsts
    initOption: str


class DefaultCheckInDataExtraCheckinDailyInfo(BaseModel):
    order: int
    blessing: str
    absolutData: int
    adTip: str
    relativeData: int
    itemList: list[ItemBundle]


class DefaultCheckInData(BaseModel):
    checkInList: dict[str, DefaultCheckInDataCheckInDailyInfo]
    apSupplyOutOfDateDict: dict[str, int]
    dynCheckInData: DefaultCheckInDataDynamicCheckInData | None = None
    extraCheckinList: list[DefaultCheckInDataExtraCheckinDailyInfo] | None


class AllPlayerCheckinDataDailyInfo(BaseModel):
    itemList: list[ItemBundle]
    order: int
    keyItem: bool
    showItemOrder: int


class AllPlayerCheckinDataPublicBehaviour(BaseModel):
    sortId: int
    allBehaviorId: str
    displayOrder: int
    allBehaviorDesc: str
    requiringValue: int
    requireRepeatCompletion: bool
    rewardReceivedDesc: str
    rewards: list[ItemBundle]


class AllPlayerCheckinDataPersonalBehaviour(BaseModel):
    sortId: int
    personalBehaviorId: str
    displayOrder: int
    requireRepeatCompletion: bool
    desc: str


class AllPlayerCheckinDataConstData(BaseModel):
    characterName: str
    skinName: str


class AllPlayerCheckinData(BaseModel):
    checkInList: dict[str, AllPlayerCheckinDataDailyInfo]
    apSupplyOutOfDateDict: dict[str, int]
    pubBhvs: dict[str, AllPlayerCheckinDataPublicBehaviour]
    personalBhvs: dict[str, AllPlayerCheckinDataPersonalBehaviour]
    constData: AllPlayerCheckinDataConstData


class VersusCheckInDataDailyInfo(BaseModel):
    rewardList: list[ItemBundle]
    order: int


class VersusCheckInDataVoteData(BaseModel):
    plSweetNum: int
    plSaltyNum: int
    plTaste: int


class VersusCheckInDataTasteInfoData(BaseModel):
    plTaste: int
    tasteType: str
    tasteText: str


class VersusCheckInDataTasteRewardData(BaseModel):
    tasteType: str
    rewardItem: ItemBundle


class VersusCheckInData(BaseModel):
    checkInDict: dict[str, VersusCheckInDataDailyInfo]
    voteTasteList: list[VersusCheckInDataVoteData]
    tasteInfoDict: dict[str, VersusCheckInDataTasteInfoData]
    tasteRewardDict: dict[str, VersusCheckInDataTasteRewardData]
    apSupplyOutOfDateDict: dict[str, int]
    versusTotalDays: int
    ruleText: str


class Act3D0DataCampBasicInfo(BaseModel):
    campId: str
    campName: str
    campDesc: str
    rewardDesc: str | None


class Act3D0DataLimitedPoolDetailInfoPoolItemInfo(BaseModel):
    goodId: str
    itemInfo: ItemBundle | None
    goodType: str
    perCount: int
    totalCount: int
    weight: int
    type_: str = Field(alias='type')
    orderId: int


class Act3D0DataLimitedPoolDetailInfo(BaseModel):
    poolId: str
    poolItemInfo: list[Act3D0DataLimitedPoolDetailInfoPoolItemInfo]


class Act3D0DataInfinitePoolDetailInfoPoolItemInfo(BaseModel):
    goodId: str
    itemInfo: ItemBundle
    goodType: str
    perCount: int
    weight: int
    type_: str = Field(alias='type')
    orderId: int


class Act3D0DataInfinitePoolDetailInfo(BaseModel):
    poolId: str
    poolItemInfo: list[Act3D0DataInfinitePoolDetailInfoPoolItemInfo]


class Act3D0DataInfinitePoolPercent(BaseModel):
    percentDict: dict[str, int]


class Act3D0DataCampItemMapInfo(BaseModel):
    goodId: str
    itemDict: dict[str, ItemBundle]


class Act3D0DataClueInfo(BaseModel):
    itemId: str
    campId: str
    orderId: int
    imageId: str


class Act3D0DataMileStoneInfo(BaseModel):
    mileStoneId: str
    orderId: int
    mileStoneType: int
    normalItem: ItemBundle | None
    specialItemDict: dict[str, ItemBundle]
    tokenNum: int


class Act3D0DataGachaBoxInfo(BaseModel):
    gachaBoxId: str
    boxType: str
    keyGoodId: str | None
    tokenId: ItemBundle
    tokenNumOnce: int
    unlockImg: str | None
    nextGachaBoxInfoId: str | None


class Act3D0DataCampInfo(BaseModel):
    campId: str
    campChineseName: str


class Act3D0DataZoneDescInfo(BaseModel):
    zoneId: str
    lockedText: str | None


class CommonFavorUpInfo(BaseModel):
    charId: str
    displayStartTime: int
    displayEndTime: int


class Act3D0Data(BaseModel):
    campBasicInfo: dict[str, Act3D0DataCampBasicInfo]
    limitedPoolList: dict[str, Act3D0DataLimitedPoolDetailInfo]
    infinitePoolList: dict[str, Act3D0DataInfinitePoolDetailInfo]
    infinitePercent: dict[str, Act3D0DataInfinitePoolPercent] | None
    campItemMapInfo: dict[str, Act3D0DataCampItemMapInfo]
    clueInfo: dict[str, Act3D0DataClueInfo]
    mileStoneInfo: list[Act3D0DataMileStoneInfo]
    mileStoneTokenId: str
    coinTokenId: str
    etTokenId: str
    gachaBoxInfo: list[Act3D0DataGachaBoxInfo]
    campInfo: dict[str, Act3D0DataCampInfo] | None
    zoneDesc: dict[str, Act3D0DataZoneDescInfo]
    favorUpList: dict[str, CommonFavorUpInfo] | None


class Act4D0DataMileStoneItemInfo(BaseModel):
    mileStoneId: str
    orderId: int
    tokenNum: int
    item: ItemBundle


class Act4D0DataMileStoneStoryInfo(BaseModel):
    mileStoneId: str
    orderId: int
    tokenNum: int
    storyKey: str
    desc: str


class Act4D0DataStoryInfo(BaseModel):
    storyKey: str
    storyId: str
    storySort: str
    storyName: str
    lockDesc: str
    storyDesc: str


class Act4D0DataStageJumpInfo(BaseModel):
    stageKey: str
    zoneId: str
    stageId: str
    unlockDesc: str
    lockDesc: str


class Act4D0Data(BaseModel):
    mileStoneItemList: list[Act4D0DataMileStoneItemInfo]
    mileStoneStoryList: list[Act4D0DataMileStoneStoryInfo]
    storyInfoList: list[Act4D0DataStoryInfo]
    stageInfo: list[Act4D0DataStageJumpInfo]
    tokenItem: ItemBundle
    charStoneId: str
    apSupplyOutOfDateDict: dict[str, int]
    extraDropZones: list[str]


class MileStoneInfo(BaseModel):
    mileStoneId: str
    orderId: int
    tokenNum: int
    mileStoneType: int
    normalItem: ItemBundle
    IsBonus: int


class Act5D0DataZoneDescInfo(BaseModel):
    zoneId: str
    lockedText: str | None


class Act5D0DataMissionExtraInfo(BaseModel):
    difficultLevel: int
    levelDesc: str
    sortId: int


class Act5D0Data(BaseModel):
    mileStoneInfo: list[MileStoneInfo]
    mileStoneTokenId: str
    zoneDesc: dict[str, Act5D0DataZoneDescInfo]
    missionExtraList: dict[str, Act5D0DataMissionExtraInfo]
    spReward: str


class Act5D1DataRuneStageData(BaseModel):
    stageId: str
    levelId: str
    code: str
    name: str
    loadingPicId: str
    description: str
    picId: str


class Act5D1DataRuneRecurrentStateData(BaseModel):
    runeReId: str
    stageId: str
    slotId: int
    startTime: int
    endTime: int
    runeList: list[str]
    isAvail: bool
    warningPoint: int


class Act5D1DataRuneUnlockData(BaseModel):
    runeId: str
    priceItem: ItemBundle
    runeName: str
    bgPic: str
    runeDesc: str
    sortId: int
    iconId: str


class Act5D1DataRuneReleaseData(BaseModel):
    runeId: str
    stageId: str
    releaseTime: int


class Act5D1DataShopGood(BaseModel):
    goodId: str
    slotId: int
    price: int
    availCount: int
    item: ItemBundle
    progressGoodId: str
    goodType: str


class Act5D1DataProgessGoodItem(BaseModel):
    order: int
    price: int
    displayName: str
    item: ItemBundle


class Act5D1DataShopData(BaseModel):
    shopGoods: dict[str, Act5D1DataShopGood]
    progressGoods: dict[str, list[Act5D1DataProgessGoodItem]]


class RuneDataSelector(BaseModel):
    professionMask: int | str
    buildableMask: int
    charIdFilter: list[str] | None
    enemyIdFilter: list[str] | None
    enemyIdExcludeFilter: list[str] | None
    skillIdFilter: list[str] | None
    tileKeyFilter: list[str] | None
    groupTagFilter: list[str] | None
    filterTagFilter: list[str] | None


class Blackboard(BaseModel):
    key: str
    value: float | None = None
    valueStr: str | None = None


class RuneData(BaseModel):
    key: str
    selector: RuneDataSelector
    blackboard: list[Blackboard]


class RuneTablePackedRuneData(BaseModel):
    id_: str = Field(alias='id')
    points: float
    mutexGroupKey: str | None
    description: str
    runes: list[RuneData]


class RuneTableRuneStageExtraData(BaseModel):
    stageId: str
    runes: list[RuneTablePackedRuneData]


class Act5D1Data(BaseModel):
    stageCommonData: list[Act5D1DataRuneStageData]
    runeStageData: list[Act5D1DataRuneRecurrentStateData]
    runeUnlockDict: dict[str, list[Act5D1DataRuneUnlockData]]
    runeReleaseData: list[Act5D1DataRuneReleaseData]
    missionData: list[MissionData]
    missionGroup: list[MissionGroup]
    useBenefitMissionDict: dict[str, bool]
    shopData: Act5D1DataShopData
    coinItemId: str
    ptItemId: str
    stageRune: list[RuneTableRuneStageExtraData]
    showRuneMissionList: list[str]


class ActivityCollectionDataCollectionInfo(BaseModel):
    id_: int = Field(alias='id')
    itemType: str
    itemId: str
    itemCnt: int
    pointId: str
    pointCnt: int
    isBonus: bool
    pngName: str | None
    pngSort: int
    isShow: bool
    showInList: bool
    showIconBG: bool


class ActivityCollectionData(BaseModel):
    collections: list[ActivityCollectionDataCollectionInfo]
    apSupplyOutOfDateDict: dict[str, int]


class Act9D0DataZoneDescInfo(BaseModel):
    zoneId: str
    unlockText: str
    displayStartTime: int


class Act9D0DataFavorUpInfo(BaseModel):
    charId: str
    displayStartTime: int
    displayEndTime: int


class Act9D0DataSubMissionInfo(BaseModel):
    missionId: str
    missionTitle: str
    sortId: int
    missionIndex: str


class Act9D0DataActivityNewsStyleInfo(BaseModel):
    typeId: str
    typeName: str
    typeLogo: str
    typeMainLogo: str


class Act9D0DataActivityNewsLine(BaseModel):
    lineType: int
    content: str


class Act9D0DataActivityNewsInfo(BaseModel):
    newsId: str
    newsSortId: int
    styleInfo: Act9D0DataActivityNewsStyleInfo
    preposedStage: str | None
    titlePic: str
    newsTitle: str
    newsInfShow: int
    newsFrom: str
    newsText: str
    newsParam1: int
    newsParam2: int
    newsParam3: float
    newsLines: list[Act9D0DataActivityNewsLine]


class Act9D0DataActivityNewsServerInfo(BaseModel):
    newsId: str
    preposedStage: str


class Act9D0Data(BaseModel):
    tokenItemId: str
    zoneDescList: dict[str, Act9D0DataZoneDescInfo]
    favorUpList: dict[str, Act9D0DataFavorUpInfo]
    subMissionInfo: dict[str, Act9D0DataSubMissionInfo] | None
    hasSubMission: bool
    apSupplyOutOfDateDict: dict[str, int]
    newsInfoList: dict[str, Act9D0DataActivityNewsInfo] | None
    newsServerInfoList: dict[str, Act9D0DataActivityNewsServerInfo] | None
    miscHub: dict[str, str]


class Act12SideDataConstData(BaseModel):
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


class Act12SideDataZoneAdditionData(BaseModel):
    zoneId: str
    unlockText: str
    zoneClass: str


class Act12SideDataMissionDescInfo(BaseModel):
    zoneClass: str
    specialMissionDesc: str
    needLock: bool
    unlockHint: str | None
    unlockStage: str | None


class Act12SideDataMileStoneInfo(BaseModel):
    mileStoneId: str
    orderId: int
    tokenNum: int
    item: ItemBundle
    isPrecious: bool
    mileStoneStage: int


class Act12SideDataPhotoInfo(BaseModel):
    picId: str
    picName: str
    mileStoneId: str
    picDesc: str
    jumpStageId: str | None


class Act12SideDataRecycleDialogData(BaseModel):
    dialogType: str
    dialog: str
    dialogExpress: str


class Act12SideData(BaseModel):
    constData: Act12SideDataConstData
    zoneAdditionDataList: list[Act12SideDataZoneAdditionData]
    missionDescList: dict[str, Act12SideDataMissionDescInfo]
    mileStoneInfoList: list[Act12SideDataMileStoneInfo]
    photoList: dict[str, Act12SideDataPhotoInfo]
    recycleDialogDict: dict[str, list[Act12SideDataRecycleDialogData]]


class Act13SideDataConstData(BaseModel):
    prestigeDescList: list[str]
    dailyRandomCount: list[list[int]] | None
    dailyWeightInitial: int
    dailyWeightComplete: int
    agendaRecover: int
    agendaMax: int
    agendaHint: int
    missionPoolMax: int
    missionBoardMax: int
    itemRandomList: list[ItemBundle]
    unlockPrestigeCond: str
    hotSpotShowFlag: int


class Act13SideDataPrestigeData(BaseModel):
    rank: str
    threshold: int
    reward: ItemBundle | None
    newsCount: int
    archiveCount: int
    avgCount: int


class Act13SideDataLongTermMissionGroupData(BaseModel):
    groupId: str
    groupName: str
    orgId: str
    missionList: list[str]


class Act13SideDataOrgSectionData(BaseModel):
    sectionName: str
    sortId: int
    groupData: Act13SideDataLongTermMissionGroupData


class Act13SideDataOrgData(BaseModel):
    orgId: str
    orgName: str
    orgEnName: str
    openTime: int
    principalIdList: list[str]
    prestigeList: list[Act13SideDataPrestigeData]
    agendaCount2PrestigeItemMap: dict[str, ItemBundle]
    orgSectionList: list[Act13SideDataOrgSectionData]
    prestigeItem: ItemBundle


class Act13SideDataPrincipalData(BaseModel):
    principalId: str
    principalName: str
    principalEnName: str
    avgCharId: str
    principalDescList: list[str]


class Act13SideDataLongTermMissionData(BaseModel):
    missionName: str
    groupId: str
    principalId: str
    finishedDesc: str
    sectionSortId: int
    haveStageBtn: bool
    jumpStageId: str | None


class Act13SideDataDailyMissionData(BaseModel):
    id_: str = Field(alias='id')
    sortId: int
    description: str
    missionName: str
    template: str
    templateType: str
    param: list[str]
    rewards: list[MissionDisplayRewards] | None
    orgPool: list[str] | None
    rewardPool: list[str] | None
    jumpStageId: str
    agendaCount: int


class Act13SideDataDailyMissionRewardGroupData(BaseModel):
    groupId: str
    rewards: list[ItemBundle]


class Act13SideDataArchiveItemUnlockData(BaseModel):
    itemId: str
    itemType: str
    unlockCondition: str
    param1: str | None
    param2: str | None


class ActivityTableActHiddenAreaPreposeStageData(BaseModel):
    stageId: str
    unlockRank: int


class ActivityTableActivityHiddenAreaData(BaseModel):
    name: str
    desc: str
    preposedStage: list[ActivityTableActHiddenAreaPreposeStageData]
    preposedTime: int


class Act13SideDataZoneAdditionData(BaseModel):
    unlockText: str
    zoneClass: str


class Act13SideData(BaseModel):
    constData: Act13SideDataConstData
    orgDataMap: dict[str, Act13SideDataOrgData]
    principalDataMap: dict[str, Act13SideDataPrincipalData]
    longTermMissionDataMap: dict[str, Act13SideDataLongTermMissionData]
    dailyMissionDataList: list[Act13SideDataDailyMissionData]
    dailyRewardGroupDataMap: dict[str, Act13SideDataDailyMissionRewardGroupData]
    archiveItemUnlockData: dict[str, Act13SideDataArchiveItemUnlockData]
    hiddenAreaData: dict[str, ActivityTableActivityHiddenAreaData]
    zoneAddtionDataMap: dict[str, Act13SideDataZoneAdditionData]


class Act17sideDataPlaceData(BaseModel):
    placeId: str
    placeDesc: str
    lockEventId: str | None
    zoneId: str
    visibleCondType: str | None = None
    visibleParams: list[str] | None = None


class Act17sideDataNodeInfoData(BaseModel):
    nodeId: str
    nodeType: str
    sortId: int
    placeId: str
    isPointPlace: bool
    chapterId: str
    trackPointType: str
    unlockCondType: str | None = None
    unlockParams: list[str] | None = None


class Act17sideDataLandmarkNodeData(BaseModel):
    nodeId: str
    landmarkId: str
    landmarkName: str
    landmarkPic: str | None
    landmarkSpecialPic: str
    landmarkDesList: list[str]


class Act17sideDataStoryNodeData(BaseModel):
    nodeId: str
    storyId: str
    storyKey: str
    storyName: str
    storyPic: str | None
    confirmDes: str
    storyDesList: list[str]


class Act17sideDataBattleNodeData(BaseModel):
    nodeId: str
    stageId: str


class Act17sideDataTreasureNodeData(BaseModel):
    nodeId: str
    treasureId: str
    treasureName: str
    treasurePic: str | None
    treasureSpecialPic: str | None
    endEventId: str
    confirmDes: str
    treasureDesList: list[str]
    missionIdList: list[str]
    rewardList: list[ItemBundle]
    treasureType: str


class Act17sideDataEventNodeData(BaseModel):
    nodeId: str
    eventId: str
    endEventId: str


class Act17sideDataTechNodeData(BaseModel):
    nodeId: str
    techTreeId: str
    techTreeName: str
    techPic: str | None
    techSpecialPic: str
    endEventId: str
    confirmDes: str
    techDesList: list[str]
    missionIdList: list[str]


class Act17sideDataChoiceNodeOptionData(BaseModel):
    canRepeat: bool
    eventId: str
    des: str
    unlockDes: str | None
    unlockCondType: str | None = None
    unlockParams: str | None = None


class Act17sideDataChoiceNodeData(BaseModel):
    nodeId: str
    choicePic: str | None
    isDisposable: bool
    choiceSpecialPic: str | None
    choiceName: str
    choiceDesList: list[str]
    cancelDes: str
    choiceNum: int
    optionList: list[Act17sideDataChoiceNodeOptionData]


class Act17sideDataEventData(BaseModel):
    eventId: str
    eventPic: str | None
    eventSpecialPic: str | None
    eventTitle: str
    eventDesList: list[str]


class Act17sideDataArchiveItemUnlockData(BaseModel):
    itemId: str
    itemType: str
    unlockCondition: str
    nodeId: str | None
    stageParam: str
    chapterId: str | None


class Act17sideDataTechTreeData(BaseModel):
    techTreeId: str
    sortId: int
    techTreeName: str
    defaultBranchId: str
    lockDes: str


class Act17sideDataTechTreeBranchData(BaseModel):
    techTreeBranchId: str
    techTreeId: str
    techTreeBranchName: str
    techTreeBranchIcon: str
    techTreeBranchDesc: str
    runeData: RuneTablePackedRuneData


class Act17sideDataMainlineChapterData(BaseModel):
    chapterId: str
    chapterDes: str
    chapterIcon: str
    unlockDes: str
    id_: str = Field(alias='id')


class Act17sideDataMainlineData(BaseModel):
    mainlineId: str
    nodeId: str | None
    sortId: int
    missionSort: str
    zoneId: str
    mainlineDes: str
    focusNodeId: str | None


class Act17sideDataZoneData(BaseModel):
    zoneId: str
    unlockPlaceId: str | None
    unlockText: str


class Act17sideDataConstData(BaseModel):
    techTreeUnlockEventId: str


class Act17sideData(BaseModel):
    placeDataMap: dict[str, Act17sideDataPlaceData]
    nodeInfoDataMap: dict[str, Act17sideDataNodeInfoData]
    landmarkNodeDataMap: dict[str, Act17sideDataLandmarkNodeData]
    storyNodeDataMap: dict[str, Act17sideDataStoryNodeData]
    battleNodeDataMap: dict[str, Act17sideDataBattleNodeData]
    treasureNodeDataMap: dict[str, Act17sideDataTreasureNodeData]
    eventNodeDataMap: dict[str, Act17sideDataEventNodeData]
    techNodeDataMap: dict[str, Act17sideDataTechNodeData]
    choiceNodeDataMap: dict[str, Act17sideDataChoiceNodeData]
    eventDataMap: dict[str, Act17sideDataEventData]
    archiveItemUnlockDataMap: dict[str, Act17sideDataArchiveItemUnlockData]
    techTreeDataMap: dict[str, Act17sideDataTechTreeData]
    techTreeBranchDataMap: dict[str, Act17sideDataTechTreeBranchData]
    mainlineChapterDataMap: dict[str, Act17sideDataMainlineChapterData]
    mainlineDataMap: dict[str, Act17sideDataMainlineData]
    zoneDataList: list[Act17sideDataZoneData]
    constData: Act17sideDataConstData


class Act20SideDataResidentCartData(BaseModel):
    residentPic: str


class Act20SideData(BaseModel):
    zoneAdditionDataMap: dict[str, str]
    residentCartDatas: dict[str, Act20SideDataResidentCartData]


class Act21SideDataZoneAddtionData(BaseModel):
    zoneId: str
    unlockText: str
    stageUnlockText: str | None
    entryId: str


class Act21SideDataConstData(BaseModel):
    lineConnectZone: str


class Act21SideData(BaseModel):
    zoneAdditionDataMap: dict[str, Act21SideDataZoneAddtionData]
    constData: Act21SideDataConstData


class ActivityLoginData(BaseModel):
    description: str
    itemList: list[ItemBundle]
    apSupplyOutOfDateDict: dict[str, int]


class ActivitySwitchCheckinConstData(BaseModel):
    activityTime: str
    activityRule: str


class ActivitySwitchCheckinData(BaseModel):
    constData: ActivitySwitchCheckinConstData
    rewards: dict[str, list[ItemBundle]]
    apSupplyOutOfDateDict: dict[str, int]
    rewardsTitle: dict[str, str]


class ActivityMiniStoryDataZoneDescInfo(BaseModel):
    zoneId: str
    unlockText: str


class ActivityMiniStoryDataFavorUpInfo(BaseModel):
    charId: str
    displayStartTime: int
    displayEndTime: int


class ActivityMiniStoryData(BaseModel):
    tokenItemId: str
    zoneDescList: dict[str, ActivityMiniStoryDataZoneDescInfo]
    favorUpList: dict[str, ActivityMiniStoryDataFavorUpInfo]
    extraDropZoneList: list[str]


class ActivityRoguelikeDataOuterBuffUnlockInfo(BaseModel):
    buffLevel: int
    name: str
    iconId: str
    description: str
    usage: str
    itemId: str
    itemType: str
    cost: int


class ActivityRoguelikeDataOuterBuffUnlockInfoData(BaseModel):
    buffId: str
    buffUnlockInfos: dict[str, ActivityRoguelikeDataOuterBuffUnlockInfo]


class ActivityRoguelikeDataMileStoneItemInfo(BaseModel):
    mileStoneId: str
    orderId: int
    tokenNum: int
    item: ItemBundle


class ActivityTableCustomUnlockCond(BaseModel):
    actId: str | None
    stageId: str


class ActivityRoguelikeData(BaseModel):
    outBuffInfos: dict[str, ActivityRoguelikeDataOuterBuffUnlockInfoData]
    apSupplyOutOfDateDict: dict[str, int]
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
    milestone: list[ActivityRoguelikeDataMileStoneItemInfo]
    unlockConds: list[ActivityTableCustomUnlockCond]


class ActivityMultiplayDataStageData(BaseModel):
    stageId: str
    levelId: str
    groupId: str
    difficulty: str
    loadingPicId: str
    dangerLevel: str
    unlockConds: list[str]


class ActivityMultiplayDataStageGroupData(BaseModel):
    groupId: str
    sortId: int
    code: str
    name: str
    description: str


class ActivityMultiplayDataMissionExtraData(BaseModel):
    missionId: str
    isHard: bool


class ActivityMultiplayDataRoomMessageData(BaseModel):
    sortId: int
    picId: str


class ActivityMultiplayDataConstData(BaseModel):
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


class ActivityMultiplayData(BaseModel):
    stages: dict[str, ActivityMultiplayDataStageData]
    stageGroups: dict[str, ActivityMultiplayDataStageGroupData]
    missionExtras: dict[str, ActivityMultiplayDataMissionExtraData]
    roomMessages: list[ActivityMultiplayDataRoomMessageData]
    constData: ActivityMultiplayDataConstData
    unlockConds: list[ActivityTableCustomUnlockCond]


class ActivityInterlockDataStageAdditionData(BaseModel):
    stageId: str
    stageType: str
    lockStageKey: str | None
    lockSortIndex: int


class ActivityInterlockDataTreasureMonsterData(BaseModel):
    lockStageKey: str
    enemyId: str
    enemyName: str
    enemyIcon: str
    enemyDescription: str


class SharedCharDataCharEquipInfo(BaseModel):
    hide: int
    locked: bool | int
    level: int


class SharedCharDataSharedCharSkillData(BaseModel):
    completeUpgradeTime: int | None = None
    unlock: bool | int | None = None
    skillId: str
    specializeLevel: int
    state: int | None = None


class SharedCharDataTmplData(BaseModel):
    skinId: str
    defaultSkillIndex: int
    skills: list[SharedCharDataSharedCharSkillData]
    currentEquip: str | None
    equip: dict[str, SharedCharDataSharedCharSkillData] | None = None


class SharedCharData(BaseModel):
    charId: str
    potentialRank: int
    skillIndex: int | None = None
    skinId: str | None = None
    skin: str | None = None
    skills: list[SharedCharDataSharedCharSkillData] | None = None
    currentEquip: str | None = Field(alias='currentEquip', default=None)
    equips: dict[str, SharedCharDataCharEquipInfo] | None = Field(alias='equip', default={})
    mainSkillLvl: int
    evolvePhase: int
    level: int
    favorPoint: int
    crisisRecord: dict[str, int] | None = None
    currentTmpl: str | None | None = None
    tmpl: dict[str, SharedCharDataTmplData] | None = None


class ActivityInterlockDataMileStoneItemInfo(BaseModel):
    mileStoneId: str
    orderId: int
    tokenNum: int
    item: ItemBundle


class ActivityInterlockDataFinalStageProgressData(BaseModel):
    stageId: str
    killCnt: int
    apCost: int
    favor: int
    exp: int
    gold: int


class ActivityInterlockData(BaseModel):
    stageAdditionInfoMap: dict[str, ActivityInterlockDataStageAdditionData]
    treasureMonsterMap: dict[str, ActivityInterlockDataTreasureMonsterData]
    specialAssistData: SharedCharData
    mileStoneItemList: list[ActivityInterlockDataMileStoneItemInfo]
    finalStageProgressMap: dict[str, list[ActivityInterlockDataFinalStageProgressData]]


class ActivityBossRushDataZoneAdditionData(BaseModel):
    unlockText: str
    displayStartTime: int


class ActivityBossRushDataBossRushStageGroupData(BaseModel):
    stageGroupId: str
    sortId: int
    stageGroupName: str
    stageIdMap: dict[str, str]
    waveBossInfo: list[list[str]]
    normalStageCount: int
    isHardStageGroup: bool
    unlockCondtion: str | None


class ActivityBossRushDataBossRushStageAdditionData(BaseModel):
    stageId: str
    stageType: str
    stageGroupId: str
    teamIdList: list[str]
    unlockText: str | None


class ActivityBossRushDataDisplayDetailRewards(BaseModel):
    occPercent: int
    dropCount: int
    type_: str = Field(alias='type')
    id_: str = Field(alias='id')
    dropType: int


class ActivityBossRushDataBossRushDropInfo(BaseModel):
    clearWaveCount: int
    displayDetailRewards: list[ActivityBossRushDataDisplayDetailRewards]
    firstPassRewards: list[ItemBundle]
    passRewards: list[ItemBundle]


class ActivityBossRushDataBossRushMissionAdditionData(BaseModel):
    missionId: str
    isRelicTask: bool


class ActivityBossRushDataBossRushTeamData(BaseModel):
    teamId: str
    teamName: str
    charIdList: list[str]
    teamBuffName: str | None
    teamBuffDes: str | None
    teamBuffId: str | None
    maxCharNum: int
    runeData: RuneTablePackedRuneData | None


class ActivityBossRushDataRelicData(BaseModel):
    relicId: str
    sortId: int
    name: str
    icon: str
    relicTaskId: str


class ActivityBossRushDataRelicLevelInfo(BaseModel):
    level: int
    effectDesc: str
    runeData: RuneTablePackedRuneData


class ActivityBossRushDataRelicLevelInfoData(BaseModel):
    relicId: str
    levelInfos: dict[str, ActivityBossRushDataRelicLevelInfo]


class ActivityBossRushDataBossRushMileStoneData(BaseModel):
    mileStoneId: str
    mileStoneLvl: int
    needPointCnt: int
    rewardItem: ItemBundle


class ActivityBossRushDataConstData(BaseModel):
    maxProvidedCharNum: int
    textMilestoneItemLevelDesc: str
    milestonePointId: str
    relicUpgradeItemId: str
    defaultRelictList: list[str]
    rewardSkinId: str


class ActivityBossRushData(BaseModel):
    zoneAdditionDataMap: dict[str, ActivityBossRushDataZoneAdditionData]
    stageGroupMap: dict[str, ActivityBossRushDataBossRushStageGroupData]
    stageAdditionDataMap: dict[str, ActivityBossRushDataBossRushStageAdditionData]
    stageDropDataMap: dict[str, dict[str, ActivityBossRushDataBossRushDropInfo]]
    missionAdditionDataMap: dict[str, ActivityBossRushDataBossRushMissionAdditionData]
    teamDataMap: dict[str, ActivityBossRushDataBossRushTeamData]
    relicList: list[ActivityBossRushDataRelicData]
    relicLevelInfoDataMap: dict[str, ActivityBossRushDataRelicLevelInfoData]
    mileStoneList: list[ActivityBossRushDataBossRushMileStoneData]
    bestWaveRuneList: list[RuneTablePackedRuneData]
    constData: ActivityBossRushDataConstData


class ActivityFloatParadeDataConstData(BaseModel):
    cityName: str
    lowStandard: float
    variationTitle: str
    ruleDesc: str


class ActivityFloatParadeDataDailyData(BaseModel):
    dayIndex: int
    dateName: str
    placeName: str
    placeEnName: str
    placePic: str
    eventGroupId: int
    extReward: ItemBundle | None


class ActivityFloatParadeDataRewardPool(BaseModel):
    grpId: int
    id_: int = Field(alias='id')
    type_: str = Field(alias='type')
    name: str
    desc: str | None
    reward: ItemBundle


class ActivityFloatParadeDataTactic(BaseModel):
    id_: int = Field(alias='id')
    name: str
    packName: str
    briefName: str
    rewardVar: dict[str, float]


class ActivityFloatParadeDataGroupData(BaseModel):
    groupId: int
    name: str
    startDay: int
    endDay: int
    extRewardDay: int
    extRewardCount: int


class ActivityFloatParadeData(BaseModel):
    constData: ActivityFloatParadeDataConstData
    dailyDataDic: list[ActivityFloatParadeDataDailyData]
    rewardPools: dict[str, dict[str, ActivityFloatParadeDataRewardPool]]
    tacticList: list[ActivityFloatParadeDataTactic]
    groupInfos: dict[str, ActivityFloatParadeDataGroupData]


class ActSandboxDataMilestoneData(BaseModel):
    milestoneId: str
    orderId: int
    tokenId: str
    tokenNum: int
    item: ItemBundle
    isPrecious: bool


class ActSandboxData(BaseModel):
    milestoneDataList: list[ActSandboxDataMilestoneData]
    milestoneTokenId: str


class ActivityMainlineBuffDataMissionGroupData(BaseModel):
    id_: str = Field(alias='id')
    bindBanner: str
    sortId: int
    zoneId: str
    missionIdList: list[str]


class ActivityMainlineBuffDataPeriodDataStepData(BaseModel):
    isBlock: bool
    favorUpDesc: str | None
    unlockDesc: str | None
    bindStageId: str | None
    blockDesc: str | None


class ActivityMainlineBuffDataPeriodData(BaseModel):
    id_: str = Field(alias='id')
    startTime: int
    endTime: int
    favorUpCharDesc: str
    favorUpImgName: str
    newChapterImgName: str
    newChapterZoneId: str | None
    stepDataList: list[ActivityMainlineBuffDataPeriodDataStepData]


class ActivityMainlineBuffDataConstData(BaseModel):
    favorUpStageRange: str


class ActivityMainlineBuffData(BaseModel):
    missionGroupList: dict[str, ActivityMainlineBuffDataMissionGroupData]
    periodDataList: list[ActivityMainlineBuffDataPeriodData]
    apSupplyOutOfDateDict: dict[str, int]
    constData: ActivityMainlineBuffDataConstData


class Act24SideDataToolData(BaseModel):
    toolId: str
    sortId: int
    toolName: str
    toolDesc: str
    toolIcon1: str
    toolIcon2: str
    toolUnlockDesc: str
    toolBuffId: str
    runeData: RuneTablePackedRuneData


class Act24SideDataMealData(BaseModel):
    mealId: str
    sortId: int
    mealName: str
    mealEffectDesc: str
    mealDesc: str
    mealIcon: str
    mealCost: int
    mealRewardAP: int
    mealRewardItemInfo: ItemBundle


class Act24SideDataMeldingItemData(BaseModel):
    meldingId: str
    sortId: int
    meldingPrice: int
    rarity: int


class Act24SideDataMeldingGachaBoxData(BaseModel):
    gachaBoxId: str
    gachaSortId: int
    gachaIcon: str
    gachaBoxName: str
    gachaCost: int
    gachaTimesLimit: int
    themeColor: str
    remainItemBgColor: str


class Act24SideDataMeldingGachaBoxGoodData(BaseModel):
    goodId: str
    gachaBoxId: str
    orderId: int
    itemId: str
    itemType: str
    displayType: str
    perCount: int
    totalCount: int
    gachaType: str


class Act24SideDataZoneAdditionData(BaseModel):
    zoneId: str
    zoneIcon: str
    unlockText: str
    displayTime: str


class QuestStageData(BaseModel):
    stageId: str
    stageRank: int
    sortId: int
    isUrgentStage: bool
    isDragonStage: bool


class Act24SideDataMissionExtraData(BaseModel):
    taskTypeName: str
    taskTypeIcon: str
    taskType: str
    taskTitle: str
    taskClient: str
    taskClientDesc: str


class WeightItemBundle(BaseModel):
    id_: str = Field(alias='id')
    type_: str = Field(alias='type')
    dropType: str
    count: int
    weight: int


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
    firstPassRewards: list[ItemBundle] | None
    firstCompleteRewards: list[ItemBundle] | None
    passRewards: list[list[WeightItemBundle]] | None
    completeRewards: list[list[WeightItemBundle]] | None
    displayRewards: list[StageDataDisplayRewards]
    displayDetailRewards: list[StageDataDisplayDetailRewards]


class Act24SideDataConstData(BaseModel):
    stageUnlockToolDesc: str
    mealLackMoney: str
    mealDayTimesLimit: int
    toolMaximum: int
    stageCanNotUseToTool: list[str]
    gachaExtraProb: float | int


class Act24SideData(BaseModel):
    toolDataList: dict[str, Act24SideDataToolData]
    mealDataList: dict[str, Act24SideDataMealData]
    meldingDict: dict[str, Act24SideDataMeldingItemData]
    meldingGachaBoxDataList: dict[str, Act24SideDataMeldingGachaBoxData]
    meldingGachaBoxGoodDataMap: dict[str, list[Act24SideDataMeldingGachaBoxGoodData]]
    mealWelcomeTxtDataMap: dict[str, str]
    zoneAdditionDataMap: dict[str, Act24SideDataZoneAdditionData]
    questStageList: list[QuestStageData]
    missionDataList: dict[str, Act24SideDataMissionExtraData]
    meldingDropDict: dict[str, StageDataStageDropInfo]
    stageMapPreviewDict: dict[str, list[str]]
    constData: Act24SideDataConstData


class Act25SideDataConstData(BaseModel):
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


class Act25SideDataZoneDescInfo(BaseModel):
    zoneId: str
    unlockText: str
    displayStartTime: int


class Act25SideDataArchiveItemData(BaseModel):
    itemId: str
    itemType: int
    itemUnlockType: int
    itemUnlockParam: str
    unlockDesc: str | None
    iconId: str | None
    itemName: str


class Act25SideDataArchiveMapInfoData(BaseModel):
    objectId: str
    type_: int = Field(alias='type')
    numberId: str
    areaId: str
    sortId: int
    position: int
    hasDot: bool


class Act25SideDataAreaInfoData(BaseModel):
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


class Act25SideDataAreaMissionData(BaseModel):
    id_: str = Field(alias='id')
    areaId: str
    preposedMissionId: str | None
    sortId: int
    isZone: bool
    stageId: str
    costCount: int
    transform: int
    progress: int
    progressPicId: str
    template: str | None
    templateType: int
    desc: str
    param: list[str] | None
    rewards: list[ItemBundle]
    archiveItems: list[str]


class Act25SideDataBattlePerformanceData(BaseModel):
    itemId: str
    sortId: int
    itemName: str
    itemIcon: str
    itemDesc: str
    itemTechType: str
    runeData: RuneTablePackedRuneData


class Act25SideDataKeyData(BaseModel):
    keyId: str
    keyName: str
    keyIcon: str
    toastText: str


class Act25SideDataFogUnlockData(BaseModel):
    lockId: str
    lockedCollectionIconId: str
    unlockedCollectionIconId: str


class Act25SideDataDailyFarmData(BaseModel):
    transform: int
    unitTime: int


class Act25SideData(BaseModel):
    tokenItemId: str
    constData: Act25SideDataConstData
    zoneDescList: dict[str, Act25SideDataZoneDescInfo]
    archiveItemData: dict[str, Act25SideDataArchiveItemData]
    arcMapInfoData: dict[str, Act25SideDataArchiveMapInfoData]
    areaInfoData: dict[str, Act25SideDataAreaInfoData]
    areaMissionData: dict[str, Act25SideDataAreaMissionData]
    battlePerformanceData: dict[str, Act25SideDataBattlePerformanceData]
    keyData: dict[str, Act25SideDataKeyData]
    fogUnlockData: dict[str, Act25SideDataFogUnlockData]
    farmList: list[Act25SideDataDailyFarmData]


class Act38D1DataAct38D1NodeData(BaseModel):
    slotId: str
    groupId: str | None
    isUpper: bool
    adjacentSlotList: list[str]


class Act38D1DataAct38D1RoadData(BaseModel):
    roadId: str
    startSlotId: str
    endSlotId: str


class Act38D1DataAct38D1RewardBoxData(BaseModel):
    rewardBoxId: str
    roadId: str


class Act38D1DataAct38D1ExclusionGroupData(BaseModel):
    groupId: str
    slotIdList: list[str]


class Act38D1DataAct38D1DimensionItemData(BaseModel):
    desc: str
    maxScore: int


class Act38D1DataAct38D1CommentData(BaseModel):
    id_: str = Field(alias='id')
    sortId: int
    desc: str


class Act38D1DataAct38D1StageDetailData(BaseModel):
    nodeDataMap: dict[str, Act38D1DataAct38D1NodeData]
    roadDataMap: dict[str, Act38D1DataAct38D1RoadData]
    rewardBoxDataMap: dict[str, Act38D1DataAct38D1RewardBoxData]
    exclusionGroupDataMap: dict[str, Act38D1DataAct38D1ExclusionGroupData]
    dimensionItemList: list[Act38D1DataAct38D1DimensionItemData]
    commentDataMap: dict[str, Act38D1DataAct38D1CommentData]


class Act38D1DataAct38D1ConstData(BaseModel):
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


class Act38D1Data(BaseModel):
    scoreLevelToAppraiseDataMap: dict[str, str]
    detailDataMap: dict[str, Act38D1DataAct38D1StageDetailData]
    constData: Act38D1DataAct38D1ConstData
    trackPointPeriodData: list[int]


class Act27SideDataAct27SideGoodData(BaseModel):
    id_: str = Field(alias='id')
    name: str
    typeDesc: str
    iconId: str
    launchIconId: str
    purchasePrice: list[int]
    sellingPriceList: list[int]
    sellShopList: list[str]
    isPermanent: bool


class Act27SideDataAct27SideMileStoneData(BaseModel):
    mileStoneId: str
    mileStoneLvl: int
    needPointCnt: int
    rewardItem: ItemBundle


class Act27SideDataAct27SideGoodLaunchData(BaseModel):
    groupId: str
    startTime: int
    stageId: str | None
    code: str | None
    drinkId: str
    foodId: str
    souvenirId: str


class Act27SideDataAct27SideShopData(BaseModel):
    shopId: str
    sortId: int
    name: str
    iconId: str


class Act27SideDataAct27SideInquireData(BaseModel):
    mileStonePt: int
    inquireCount: int


class Act27SideDataAct27SideDynEntrySwitchData(BaseModel):
    entryId: str
    startHour: int
    signalId: str


class Act27SideDataAct27sideZoneAdditionData(BaseModel):
    zoneId: str
    unlockText: str
    displayTime: str


class Act27SideDataAct27SideMileStoneFurniRewardData(BaseModel):
    furniId: str
    pointNum: int


class Act27SideDataAct27SideConstData(BaseModel):
    stageId: str
    stageCode: str
    purchasePriceName: list[str]
    furniRewardList: list[Act27SideDataAct27SideMileStoneFurniRewardData]
    prizeText: str
    playerShopId: str
    milestonePointName: str
    inquirePanelTitle: str
    inquirePanelDesc: str
    gain123: list[float]
    gain113: list[float]
    gain122: list[float]
    gain111: list[float]
    gain11None: list[float]
    gain12None: list[float]
    campaignEnemyCnt: int


class Act27SideData(BaseModel):
    goodDataMap: dict[str, Act27SideDataAct27SideGoodData]
    mileStoneList: list[Act27SideDataAct27SideMileStoneData]
    goodLaunchDataList: list[Act27SideDataAct27SideGoodLaunchData]
    shopDataMap: dict[str, Act27SideDataAct27SideShopData]
    inquireDataList: list[Act27SideDataAct27SideInquireData]
    dynEntrySwitchData: list[Act27SideDataAct27SideDynEntrySwitchData]
    zoneAdditionDataMap: dict[str, Act27SideDataAct27sideZoneAdditionData]
    constData: Act27SideDataAct27SideConstData


class ActivityTableActivityDetailTable(BaseModel):
    DEFAULT: dict[str, DefaultFirstData]
    CHECKIN_ONLY: dict[str, DefaultCheckInData]
    CHECKIN_ALL_PLAYER: dict[str, AllPlayerCheckinData]
    CHECKIN_VS: dict[str, VersusCheckInData]
    TYPE_ACT3D0: dict[str, Act3D0Data]
    TYPE_ACT4D0: dict[str, Act4D0Data]
    TYPE_ACT5D0: dict[str, Act5D0Data]
    TYPE_ACT5D1: dict[str, Act5D1Data]
    COLLECTION: dict[str, ActivityCollectionData]
    TYPE_ACT9D0: dict[str, Act9D0Data]
    TYPE_ACT12SIDE: dict[str, Act12SideData]
    TYPE_ACT13SIDE: dict[str, Act13SideData]
    TYPE_ACT17SIDE: dict[str, Act17sideData]
    TYPE_ACT20SIDE: dict[str, Act20SideData]
    TYPE_ACT21SIDE: dict[str, Act21SideData]
    LOGIN_ONLY: dict[str, ActivityLoginData]
    SWITCH_ONLY: dict[str, ActivitySwitchCheckinData]
    MINISTORY: dict[str, ActivityMiniStoryData]
    ROGUELIKE: dict[str, ActivityRoguelikeData]
    MULTIPLAY: dict[str, ActivityMultiplayData]
    INTERLOCK: dict[str, ActivityInterlockData]
    BOSS_RUSH: dict[str, ActivityBossRushData]
    FLOAT_PARADE: dict[str, ActivityFloatParadeData]
    SANDBOX: dict[str, ActSandboxData]
    MAIN_BUFF: dict[str, ActivityMainlineBuffData]
    TYPE_ACT24SIDE: dict[str, Act24SideData]
    TYPE_ACT25SIDE: dict[str, Act25SideData]
    TYPE_ACT38D1: dict[str, Act38D1Data]
    TYPE_ACT27SIDE: dict[str, Act27SideData]


class ActivityStageRewardData(BaseModel):
    stageRewardsDict: dict[str, list[StageDataDisplayDetailRewards]]


class ActivityThemeDataTimeNode(BaseModel):
    title: str
    ts: int


class ActivityThemeData(BaseModel):
    id_: str = Field(alias='id')
    type_: str = Field(alias='type')
    funcId: str
    endTs: int
    sortId: int
    itemId: str | None
    timeNodes: list[ActivityThemeDataTimeNode]
    startTs: int


class StageDataConditionDesc(BaseModel):
    stageId: str
    completeState: int


class AprilFoolStageData(BaseModel):
    stageId: str
    levelId: str
    code: str
    name: str
    appearanceStyle: int
    loadingPicId: str
    difficulty: str
    unlockCondition: list[StageDataConditionDesc]
    stageDropInfo: list[ItemBundle]


class AprilFoolScoreData(BaseModel):
    stageId: str
    sortId: int
    playerName: str
    playerScore: int


class AprilFoolConst(BaseModel):
    battleFinishLoseDes: str
    killEnemyDes: str
    killBossDes: str
    totalTime: str


class Act4funPerformGroupInfo(BaseModel):
    performGroupId: str
    performIds: list[str]


class Act4funPerformWordData(BaseModel):
    text: str
    picId: str
    backgroundId: str


class Act4funPerformInfo(BaseModel):
    performId: str
    performFinishedPicId: str | None
    fixedCmpGroup: str | None
    cmpGroups: list[str | None]
    words: list[Act4funPerformWordData]


class Act4funLiveMatEffectInfo(BaseModel):
    liveMatEffectId: str
    valueId: str
    performGroup: str


class Act4funLiveMatInfoData(BaseModel):
    liveMatId: str
    stageId: str
    name: str
    picId: str
    tagTxt: str
    emojiIcon: str
    selectedPerformId: str
    effectInfos: dict[str, Act4funLiveMatEffectInfo]


class Act4funSpLiveMatInfoData(BaseModel):
    spLiveMatId: str
    spLiveEveId: str
    stageId: str
    name: str
    picId: str
    tagTxt: str
    emojiIcon: str
    accordingPerformId: str | None
    selectedPerformId: str | None
    valueEffectId: str
    accordingSuperChatId: str | None


class Act4funValueEffectInfoData(BaseModel):
    valueEffectId: str
    effectParams: dict[str, int]


class Act4funLiveValueInfoData(BaseModel):
    liveValueId: str
    name: str
    stageId: str
    iconId: str
    highEndingId: str
    lowEndingId: str
    increaseToastTxt: str
    decreaseToastTxt: str


class Act4funSuperChatInfo(BaseModel):
    superChatId: str
    chatType: int
    userName: str
    iconId: str
    valueEffectId: str
    performId: str
    superChatTxt: str


class Act4funCmtInfo(BaseModel):
    iconId: str | None
    name: str | None
    cmtTxt: str


class Act4funCmtGroupInfo(BaseModel):
    cmtGroupId: str
    cmtList: list[Act4funCmtInfo]


class Act4funEndingInfo(BaseModel):
    endingId: str
    endingAvg: str
    endingDesc: str | None
    stageId: str | None
    isGoodEnding: bool


class Act4funTokenInfoData(BaseModel):
    tokenLevelId: str
    levelDesc: str | None
    skillDesc: str
    tokenLevelNum: int
    levelIconId: str


class Act4funMissionData(BaseModel):
    missionId: str
    sortId: int
    missionDes: str
    rewardIconIds: list[str]
    rewards: list[ItemBundle]


class Act4funConst(BaseModel):
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


class Act4funStageExtraData(BaseModel):
    description: str
    valueIconId: str | None


class Act4funData(BaseModel):
    performGroupInfoDict: dict[str, Act4funPerformGroupInfo]
    performInfoDict: dict[str, Act4funPerformInfo]
    normalMatDict: dict[str, Act4funLiveMatInfoData]
    spMatDict: dict[str, Act4funSpLiveMatInfoData]
    valueEffectInfoDict: dict[str, Act4funValueEffectInfoData]
    liveValueInfoDict: dict[str, Act4funLiveValueInfoData]
    superChatInfoDict: dict[str, Act4funSuperChatInfo]
    cmtGroupInfoDict: dict[str, Act4funCmtGroupInfo]
    cmtUsers: list[str]
    endingDict: dict[str, Act4funEndingInfo]
    tokenLevelInfos: dict[str, Act4funTokenInfoData]
    missionDatas: dict[str, Act4funMissionData]
    constant: Act4funConst
    stageExtraDatas: dict[str, Act4funStageExtraData]
    randomMsgText: list[str]
    randomUserIconId: list[str]


class AprilFoolTable(BaseModel):
    stages: dict[str, AprilFoolStageData]
    scoreDict: dict[str, list[AprilFoolScoreData]]
    constant: AprilFoolConst
    act4FunData: Act4funData


class CartComponents(BaseModel):
    compId: str
    sortId: int
    type: str
    posList: list[str]
    posIdDict: dict[str, list[str]]
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
    additiveColor: str | None


class CartDataCartConstData(BaseModel):
    carItemUnlockStageId: str
    carItemUnlockDesc: str
    spLevelUnlockItemCnt: int
    mileStoneBaseInterval: int
    spStageIds: list[str]
    carFrameDefaultColor: str


class CartData(BaseModel):
    carDict: dict[str, CartComponents]
    runeDataDict: dict[str, RuneTablePackedRuneData]
    cartStages: list[str]
    constData: CartDataCartConstData


class SiracusaDataAreaData(BaseModel):
    areaId: str
    areaName: str
    areaSubName: str
    unlockType: str
    unlockStage: str | None
    areaIconId: str
    pointList: list[str]


class SiracusaDataPointData(BaseModel):
    pointId: str
    areaId: str
    pointName: str
    pointDesc: str
    pointIconId: str
    pointItaName: str


class SiracusaDataCharCardData(BaseModel):
    charCardId: str
    sortIndex: int
    avgChar: str
    avgCharOffsetY: float | int
    charCardName: str
    charCardItaName: str
    charCardTitle: str
    charCardDesc: str
    fullCompleteDes: str
    gainDesc: str
    themeColor: str
    taskRingList: list[str]
    operaItemId: str
    gainParamList: list[str] | None


class SiracusaDataTaskRingData(BaseModel):
    taskRingId: str
    sortIndex: int
    charCardId: str
    logicType: str
    ringText: str
    item: ItemBundle
    isPrecious: bool
    taskIdList: list[str]


class SiracusaDataTaskBasicInfoData(BaseModel):
    taskId: str
    taskRingId: str
    sortIndex: int
    placeId: str
    npcId: str | None
    taskType: str


class SiracusaDataBattleTaskData(BaseModel):
    taskId: str
    stageId: str
    battleTaskDesc: str


class SiracusaDataAVGTaskData(BaseModel):
    taskId: str
    taskAvg: str


class SiracusaDataItemInfoData(BaseModel):
    itemId: str
    itemName: str
    itemItalyName: str
    itemDesc: str
    itemIcon: str


class SiracusaDataItemCardInfoData(BaseModel):
    cardId: str
    cardName: str
    cardDesc: str
    optionScript: str


class SiracusaDataNavigationInfoData(BaseModel):
    entryId: str
    navigationType: str
    entryIcon: str
    entryName: str | None
    entrySubName: str | None


class SiracusaDataOptionInfoData(BaseModel):
    optionId: str
    optionDesc: str
    optionScript: str
    optionGoToScript: str | None
    isLeaveOption: bool
    needCommentLike: bool
    requireCardId: str | None


class SiracusaDataStagePointInfoData(BaseModel):
    stageId: str
    pointId: str
    sortId: int
    isTaskStage: bool


class SiracusaDataStoryBriefInfoData(BaseModel):
    storyId: str
    stageId: str
    storyInfo: str


class SiracusaDataOperaInfoData(BaseModel):
    operaId: str
    sortId: int
    operaName: str
    operaSubName: str
    operaScore: float
    unlockTime: int


class SiracusaDataOperaCommentInfoData(BaseModel):
    commentId: str
    referenceOperaId: str
    columnIndex: int
    columnSortId: int
    commentTitle: str
    score: float
    commentContent: str
    commentCharId: str


class SiracusaDataConstData(BaseModel):
    operaDailyNum: int
    operaAllUnlockTime: int
    defaultFocusArea: str


class SiracusaData(BaseModel):
    areaDataMap: dict[str, SiracusaDataAreaData]
    pointDataMap: dict[str, SiracusaDataPointData]
    charCardMap: dict[str, SiracusaDataCharCardData]
    taskRingMap: dict[str, SiracusaDataTaskRingData]
    taskInfoMap: dict[str, SiracusaDataTaskBasicInfoData]
    battleTaskMap: dict[str, SiracusaDataBattleTaskData]
    avgTaskMap: dict[str, SiracusaDataAVGTaskData]
    itemInfoMap: dict[str, SiracusaDataItemInfoData]
    itemCardInfoMap: dict[str, SiracusaDataItemCardInfoData]
    navigationInfoMap: dict[str, SiracusaDataNavigationInfoData]
    optionInfoMap: dict[str, SiracusaDataOptionInfoData]
    stagePointList: list[SiracusaDataStagePointInfoData]
    storyBriefInfoDataMap: dict[str, SiracusaDataStoryBriefInfoData]
    operaInfoMap: dict[str, SiracusaDataOperaInfoData]
    operaCommentInfoMap: dict[str, SiracusaDataOperaCommentInfoData]
    constData: SiracusaDataConstData


class KVSwitchInfo(BaseModel):
    isDefault: bool
    displayTime: int
    zoneId: str | None


class ActivityKVSwitchData(BaseModel):
    kvSwitchInfo: dict[str, KVSwitchInfo]


class DynEntrySwitchInfo(BaseModel):
    entryId: str
    sortId: int
    stageId: str | None


class ActivityDynEntrySwitchData(BaseModel):
    entrySwitchInfo: dict[str, DynEntrySwitchInfo]


class ActivityTableActivityHiddenStageUnlockConditionData(BaseModel):
    unlockStageId: str
    unlockTemplate: str
    unlockParams: list[str] | None
    missionStageId: str
    unlockedName: str
    lockedName: str
    lockCode: str
    unlockedDes: str
    templateDesc: str
    desc: str
    riddle: str


class ActivityTableActivityHiddenStageData(BaseModel):
    stageId: str
    encodedName: str
    showStageId: str
    rewardDiamond: bool
    missions: list[ActivityTableActivityHiddenStageUnlockConditionData]


class ActivityTable(BaseModel):
    __version__ = '23-07-27-18-50-06-aeb568'

    basicInfo: dict[str, ActivityTableBasicData]
    homeActConfig: dict[str, ActivityTableHomeActivityConfig]
    zoneToActivity: dict[str, str]
    missionData: list[MissionData]
    missionGroup: list[MissionGroup]
    replicateMissions: dict[str, str] | None
    activity: ActivityTableActivityDetailTable
    activityItems: dict[str, list[str]]
    syncPoints: dict[str, list[int]]
    dynActs: dict[str, dict[str, str | int | list[str | int] | dict[str, int] | ItemBundle]]
    stageRewardsData: dict[str, ActivityStageRewardData]
    actThemes: list[ActivityThemeData]
    actFunData: AprilFoolTable
    carData: CartData
    siracusaData: SiracusaData
    kvSwitchData: dict[str, ActivityKVSwitchData]
    dynEntrySwitchData: dict[str, ActivityDynEntrySwitchData]
    hiddenStageData: list[ActivityTableActivityHiddenStageData]
    stringRes: dict[str, dict[str, str]]

    class Config:
        extra = 'allow'
