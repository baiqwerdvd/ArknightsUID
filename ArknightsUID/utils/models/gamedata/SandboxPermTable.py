from typing import Dict, List, Union

from ..common import BaseStruct


class HomeEntryDisplayData(BaseStruct):
    displayId: str
    topicId: str
    startTs: int
    endTs: int


class SandboxPermBasicData(BaseStruct):
    topicId: str
    topicTemplate: str
    topicName: str
    topicStartTime: int
    fullStoredTime: int
    sortId: int
    priceItemId: str
    templateShopId: str
    homeEntryDisplayData: List[HomeEntryDisplayData]
    webBusType: str
    medalGroupId: str


class SandboxV2NodeData(BaseStruct):
    minDistance: float


class UnityEngineVector2(BaseStruct):
    x: float
    y: float


class SandboxV2MapZoneData(BaseStruct):
    zoneId: str
    hasBorder: bool
    center: Union[UnityEngineVector2, None] = None
    vertices: Union[List[UnityEngineVector2], None] = None
    triangles: Union[List[List[int]], None] = None


class SandboxV2MapConfig(BaseStruct):
    isRift: bool
    isGuide: bool
    cameraBoundMin: UnityEngineVector2
    cameraBoundMax: UnityEngineVector2
    cameraMaxNormalizedZoom: float
    backgroundId: str


class SandboxV2MapData(BaseStruct):
    nodes: Dict[str, SandboxV2NodeData]
    zones: Dict[str, SandboxV2MapZoneData]
    mapConfig: SandboxV2MapConfig
    centerNodeId: str
    monthModeNodeId: Union[str, None]


class SandboxV2ItemTrapData(BaseStruct):
    itemId: str
    trapId: str
    trapPhase: int
    trapLevel: int
    skillIndex: int
    skillLevel: int
    buildingLevel: int
    updatedItemId: Union[str, None]
    minLevelItemId: str
    baseItemName: str
    itemType: str
    itemTag: str


class SandboxV2ItemTrapTagData(BaseStruct):
    tag: str
    tagName: str
    tagPic: str
    sortId: int


class SandboxV2BuildingItemData(BaseStruct):
    itemId: str
    itemRarity: int


class SandboxV2CraftItemData(BaseStruct):
    itemId: str
    type: int
    buildingUnlockDesc: str
    materialItems: Dict[str, int]
    upgradeItems: Union[Dict[str, int], None]
    withdrawRatio: int
    repairCost: int
    craftGroupId: str
    recipeLevel: int
    isHidden: Union[bool, None] = None


class SandboxV2LivestockData(BaseStruct):
    livestockItemId: str
    shinyLivestockItemId: str
    livestockEnemyId: str


class SandboxV2CraftGroupData(BaseStruct):
    items: List[str]


class SandboxV2AlchemyMaterialData(BaseStruct):
    itemId: str
    count: int


class SandboxV2AlchemyRecipeData(BaseStruct):
    recipeId: str
    materials: List[SandboxV2AlchemyMaterialData]
    itemId: str
    onceAlchemyRatio: int
    recipeLevel: int
    unlockDesc: str


class SandboxV2DrinkMatData(BaseStruct):
    id: str
    type: str
    count: int


class SandboxV2FoodMatData(BaseStruct):
    id: str
    type: str
    sortId: int
    attribute: Union[str, None] = None
    buffDesc: Union[str, None] = None


class SandboxV2FoodRecipeData(BaseStruct):
    foodId: str
    mats: List[str]


class SandboxV2FoodData(BaseStruct):
    id: str
    attributes: List[str]
    duration: int
    itemName: str
    itemUsage: str
    sortId: int
    enhancedUsage: Union[str, None] = None
    generalName: Union[str, None] = None
    enhancedName: Union[str, None] = None
    recipes: Union[List[SandboxV2FoodRecipeData], None] = None


class SandboxV2NodeTypeData(BaseStruct):
    nodeType: str
    name: str
    iconId: str


class SandboxV2NodeUpgradeData(BaseStruct):
    nodeUpgradeId: str
    name: str
    description: str
    upgradeDesc: str
    upgradeTips: str
    itemType: str
    itemTag: str
    itemCnt: int
    itemRarity: int


class SandboxV2WeatherData(BaseStruct):
    weatherId: str
    name: str
    weatherLevel: int
    weatherType: str
    weatherTypeName: str
    weatherIconId: str
    functionDesc: str
    description: str
    buffId: Union[str, None]


class SandboxV2StageData(BaseStruct):
    stageId: str
    levelId: str
    code: str
    name: str
    description: str
    actionCost: int
    actionCostEnemyRush: int


class SandboxV2ZoneData(BaseStruct):
    zoneId: str
    zoneName: str
    displayName: bool
    appellation: Union[str, None]


class SandboxV2NodeBuffData(BaseStruct):
    runeId: str
    name: str
    description: str
    extra: str
    iconId: str


class SandboxV2RewardItemConfigData(BaseStruct):
    rewardItem: str
    rewardType: str


class SandboxV2RewardData(BaseStruct):
    rewardList: List[SandboxV2RewardItemConfigData]


class SandboxV2RewardCommonConfig(BaseStruct):
    rewardItemId: str
    rewardItemType: str
    count: int


class SandboxV2RewardConfigGroupData(BaseStruct):
    stageMapPreviewRewardDict: Dict[str, SandboxV2RewardData]
    stageDetailPreviewRewardDict: Dict[str, SandboxV2RewardData]
    trapRewardDict: Dict[str, SandboxV2RewardCommonConfig]
    enemyRewardDict: Dict[str, SandboxV2RewardCommonConfig]
    unitPreviewRewardDict: Dict[str, SandboxV2RewardData]
    stageRewardDict: Dict[str, SandboxV2RewardData]
    rushPreviewRewardDict: Dict[str, SandboxV2RewardData]


class SandboxV2FloatIconData(BaseStruct):
    picId: str
    picName: Union[str, None]


class SandboxV2EnemyRushTypeData(BaseStruct):
    type: str
    description: str
    sortId: int


class SandboxV2BattleRushEnemyConfig(BaseStruct):
    enemyKey: str
    branchId: str
    count: int
    interval: float
    preDelay: float


class SandboxV2BattleRushEnemyGroupConfig(BaseStruct):
    enemyGroupKey: str
    enemy: List[SandboxV2BattleRushEnemyConfig]
    dynamicEnemy: List[str]


class RushEnemyDBRef(BaseStruct):
    id: str
    level: int


class SandboxV2BattleRushEnemyData(BaseStruct):
    rushEnemyGroupConfigs: Dict[str, List[SandboxV2BattleRushEnemyGroupConfig]]
    rushEnemyDbRef: List[RushEnemyDBRef]


class SandboxV2GameConst(BaseStruct):
    mainMapId: str
    baseTrapId: str
    portableTrapId: str
    doorTrapId: str
    mineTrapId: str
    neutralBossEnemyId: List[str]
    nestTrapId: str
    shopNpcName: str
    daysBetweenAssessment: int
    portableConstructUnlockLevel: int
    outpostConstructUnlockLevel: int
    maxEnemyCountSameTimeInRush: int
    maxSaveCnt: int
    firstSeasonDuration: int
    seasonTransitionLoop: List[str]
    seasonDurationLoop: List[int]
    firstSeasonStartAngle: float
    seasonTransitionAngleLoop: List[float]
    seasonAngle: float
    battleItemDesc: str
    foodDesc: str
    multipleSurvivalDayDesc: str
    multipleTips: str
    techProgressScore: int
    otherEnemyRushName: str
    surviveDayText: str
    survivePeriodText: str
    surviveScoreText: str
    actionPointScoreText: str
    nodeExploreDesc: str
    dungeonExploreDesc: str
    nodeCompleteDesc: str
    noRiftDungeonDesc: str
    baseRushedDesc: str
    riftBaseDesc: str
    riftBaseRushedDesc: str
    dungeonTriggeredGuideQuestList: List[str]


class ItemBundle(BaseStruct):
    id: str
    count: int
    type: str


class SandboxV2BasicConst(BaseStruct):
    staminaItemId: str
    goldItemId: str
    dimensioncoinItemId: str
    alwaysShowItemIdsConstruct: List[str]
    alwaysShowItemIds: List[str]
    bagBottomBarResType: List[str]
    failedCookFood: str
    maxFoodDuration: int
    drinkCostOnce: int
    drinkMakeLimit: int
    specialMatWater: str
    enhancedSubFoodmat: str
    enhancedDuration: int
    workbenchMakeLimit: int
    logisticsPosLimit: int
    logisticsUnlockLevel: int
    logisticsDrinkCost: int
    logisticsEvacuateTips: str
    logisticsEvacuateWarning: str
    baseRepairCost: int
    portRepairCost: int
    unitFenceLimit: int
    cageId: str
    fenceId: str
    monthlyRushEntryText1: Union[str, None]
    monthlyEntryUnlockText: str
    monthlyEntryRiftText: str
    monthlyRushIntro: str
    monthlyCoin: ItemBundle
    charRarityColorList: List[str]
    squadCharCapacity: int
    totalSquadCnt: int
    toolboxCapacity: int
    toolCntLimitInSquad: int
    miniSquadCharCapacity: int
    miniSquadDrinkCost: int
    normalSquadDrinkCost: int
    emptySquadDrinkCost: int
    achieveTypeAll: str
    constructModeBgmHome: str
    battleBgmCollect: str
    battleBgmHunt: str
    battleBgmEnemyRush: str
    battleBgmBossRush: str
    imgLoadingNormalName: str
    imgLoadingBaseName: str
    imgUnloadingBaseName: str


class SandboxV2RiftConst(BaseStruct):
    refreshRate: int
    randomDungeonId: str
    subTargetRewardId: str
    dungeonSeasonId: str
    fixedDungeonTypeName: str
    randomDungeonTypeName: str
    noTeamDescription: str
    noTeamName: str
    noTeamBackgroundId: str
    noTeamSmallIconId: str
    noTeamBigIconId: str
    messengerEnemyId: str
    riftRushEnemyGroupLimit: int
    riftRushSpawnCd: int


class SandboxV2DevelopmentConst(BaseStruct):
    techPointsTotal: int


class TipData(BaseStruct):
    tip: str
    weight: float
    category: str


class RuneDataSelector(BaseStruct):
    professionMask: int
    buildableMask: int
    charIdFilter: Union[List[str], None] = None
    enemyIdFilter: Union[List[str], None] = None
    enemyIdExcludeFilter: Union[List[str], None] = None
    enemyLevelTypeFilter: Union[List[str], None] = None
    skillIdFilter: Union[List[str], None] = None
    tileKeyFilter: Union[List[str], None] = None
    groupTagFilter: Union[List[str], None] = None
    filterTagFilter: Union[List[str], None] = None
    filterTagExcludeFilter: Union[List[str], None] = None
    subProfessionExcludeFilter: Union[List[str], None] = None
    mapTagFilter: Union[List[str], None] = None


class BlackboardDataPair(BaseStruct):
    key: str
    value: Union[float, None] = None
    valueStr: Union[str, None] = None


class RuneData(BaseStruct):
    key: str
    selector: RuneDataSelector
    blackboard: List[BlackboardDataPair]


class PackedRuneData(BaseStruct):
    id: str
    points: float
    mutexGroupKey: Union[str, None]
    description: str
    runes: List[RuneData]


class LegacyInLevelRuneData(BaseException):
    difficultyMask: int
    key: str
    professionMask: int
    buildableMask: int
    blackboard: List[BlackboardDataPair]


class SandboxV2QuestData(BaseStruct):
    questId: str
    questLine: str
    questTitle: Union[str, None]
    questDesc: Union[str, None]
    questTargetDesc: Union[str, None]
    isDisplay: bool
    questRouteType: str
    questLineType: str
    questRouteParam: Union[str, None]
    showProgressIndex: int


class SandboxV2NpcData(BaseStruct):
    npcId: str
    trapId: str
    npcType: str
    dialogIds: Dict[str, str]
    npcLocation: Union[List[int], None]
    npcOrientation: int
    picId: str
    picName: str
    showPic: bool
    reactSkillIndex: int


class SandboxV2DialogData(BaseStruct):
    dialogId: str
    avgId: str


class SandboxV2QuestLineData(BaseStruct):
    questLineId: str
    questLineTitle: str
    questLineType: str
    questLineBadgeType: int
    questLineDesc: str
    sortId: int


class SandboxV2GuideQuestData(BaseStruct):
    questId: str
    storyId: str
    triggerKey: str


class SandboxV2DevelopmentData(BaseStruct):
    techId: str
    techType: str
    positionX: int
    positionY: int
    frontNodeId: Union[str, None]
    nextNodeIds: Union[List[str], None]
    limitBaseLevel: int
    tokenCost: int
    techName: str
    techIconId: str
    nodeTitle: str
    rawDesc: str
    canBuffReserch: bool


class SandboxV2EventData(BaseStruct):
    eventId: str
    type: str
    iconId: str
    iconName: Union[str, None]
    enterSceneId: str


class SandboxV2EventSceneData(BaseStruct):
    eventSceneId: str
    title: str
    desc: str
    choiceIds: List[str]


class SandboxV2EventChoiceData(BaseStruct):
    choiceId: str
    type: str
    costAction: int
    title: str
    desc: str
    expeditionId: Union[str, None]


class SandboxV2ExpeditionData(BaseStruct):
    expeditionId: str
    desc: str
    effectDesc: str
    costAction: int
    costDrink: int
    charCnt: int
    profession: int
    professions: List[str]
    minEliteRank: int
    duration: int


class SandboxV2EventEffectData(BaseStruct):
    eventEffectId: str
    buffId: str
    duration: int
    desc: str


class SandboxV2ShopGoodData(BaseStruct):
    goodId: str
    itemId: str
    count: int
    coinType: str
    value: int


class SandboxV2ShopDialogData(BaseStruct):
    seasonDialogs: Dict[str, List[str]]
    afterBuyDialogs: List[str]
    shopEmptyDialogs: List[str]


class SandboxV2LogisticsData(BaseStruct):
    id: str
    desc: str
    noBuffDesc: str
    iconId: str
    profession: str
    sortId: int
    levelParams: List[str]


class SandboxV2LogisticsCharData(BaseStruct):
    levelUpperLimit: int
    charUpperLimit: int


class SandboxV2MonthRushData(BaseStruct):
    monthlyRushId: str
    startTime: int
    endTime: int
    isLast: bool
    sortId: int
    rushGroupKey: str
    monthlyRushName: str
    monthlyRushDes: str
    weatherId: str
    nodeId: str
    conditionGroup: str
    conditionDesc: str
    rewardItemList: List[ItemBundle]


class SandboxV2RiftParamData(BaseStruct):
    id: str
    desc: str
    iconId: str
    bkColor: str


class SandboxV2RiftSubTargetData(BaseStruct):
    id: str
    name: str
    desc: str


class SandboxV2RiftMainTargetData(BaseStruct):
    id: str
    title: str
    desc: str
    storyDesc: str
    targetDayCount: int
    targetType: str
    questIconId: Union[str, None]
    questIconName: Union[str, None]


class SandboxV2RiftGlobalEffectData(BaseStruct):
    id: str
    desc: str


class SandboxV2FixedRiftData(BaseStruct):
    riftId: str
    riftName: str
    rewardGroupId: str


class SandboxV2RiftTeamBuffData(BaseStruct):
    teamId: str
    teamName: str
    buffLevel: int
    buffDesc: str
    teamSmallIconId: str
    teamBigIconId: str
    teamDesc: str
    teamBgId: str


class SandboxV2RiftDifficultyData(BaseStruct):
    id: str
    desc: str
    difficultyLevel: int
    rewardGroupId: str


class SandboxV2ArchiveQuestAvgData(BaseStruct):
    avgId: str
    avgName: str


class SandboxV2ArchiveQuestCgData(BaseStruct):
    cgId: str
    cgTitle: str
    cgDesc: str
    cgPath: str


class SandboxV2ArchiveQuestZoneData(BaseStruct):
    zoneId: str
    zoneName: str
    zoneBgPicId: str
    zoneNameIdEn: str


class SandboxV2ArchiveQuestData(BaseStruct):
    id: str
    sortId: int
    questType: str
    name: str
    desc: str
    avgDataList: List[SandboxV2ArchiveQuestAvgData]
    cgDataList: List[SandboxV2ArchiveQuestCgData]
    npcPicIdList: List[str]
    zoneData: SandboxV2ArchiveQuestZoneData


class SandboxV2ArchiveAchievementData(BaseStruct):
    id: str
    achievementType: List[str]
    raritySortId: int
    sortId: int
    name: str
    desc: str


class SandboxV2ArchiveAchievementTypeData(BaseStruct):
    achievementType: str
    name: str
    sortId: int


class SandboxV2ArchiveQuestTypeData(BaseStruct):
    type: str
    name: str
    iconId: str


class SandboxV2ArchiveMusicUnlockData(BaseStruct):
    musicId: str
    unlockCondDesc: Union[str, None]


class SandboxV2BaseUpdateCondition(BaseStruct):
    desc: str
    limitCond: str
    param: List[str]


class SandboxV2BaseUpdateFunctionPreviewDetailData(BaseStruct):
    funcId: str
    unlockType: str
    typeTitle: str
    desc: str
    icon: str
    darkMode: bool
    sortId: int
    displayType: str


class SandboxV2BaseFunctionPreviewData(BaseStruct):
    previewId: str
    previewValue: int
    detailData: SandboxV2BaseUpdateFunctionPreviewDetailData


class SandboxV2BaseUpdateData(BaseStruct):
    baseLevelId: str
    baseLevel: int
    conditions: List[SandboxV2BaseUpdateCondition]
    items: Dict[str, int]
    previewDatas: List[SandboxV2BaseFunctionPreviewData]
    scoreFactor: str
    portableRepairCost: int
    entryCount: int
    repairCost: int


class SandboxV2DevelopmentLineSegmentData(BaseStruct):
    fromNodeId: str
    passingNodeIds: List[str]
    fromAxisPosX: int
    fromAxisPosY: int
    toAxisPosX: int
    toAxisPosY: int
    lineStyle: int
    unlockBasementLevel: int


class SandboxV2BuildingNodeScoreData(BaseStruct):
    nodeId: str
    sortId: int
    limitScore: int


class SandboxV2SeasonData(BaseStruct):
    seasonType: str
    name: str
    functionDesc: str
    description: str
    color: str


class SandboxV2ConfirmIconData(BaseStruct):
    iconType: str
    iconPicId: str


class SandboxV2TutorialRepoCharData(BaseStruct):
    instId: int
    charId: str
    evolvePhase: int
    level: int
    favorPoint: int
    potentialRank: int
    mainSkillLv: int
    specSkillList: List[int]


class SandboxV2TutorialBasicConst(BaseStruct):
    trainingQuestList: List[str]


class SandboxV2TutorialData(BaseStruct):
    charRepoData: Dict[str, SandboxV2TutorialRepoCharData]
    questData: Dict[str, SandboxV2QuestData]
    guideQuestData: Dict[str, SandboxV2GuideQuestData]
    questLineData: Dict[str, SandboxV2QuestLineData]
    basicConst: SandboxV2TutorialBasicConst


class SandboxV2Data(BaseStruct):
    mapData: Dict[str, SandboxV2MapData]
    itemTrapData: Dict[str, SandboxV2ItemTrapData]
    itemTrapTagData: Dict[str, SandboxV2ItemTrapTagData]
    buildingItemData: Dict[str, SandboxV2BuildingItemData]
    craftItemData: Dict[str, SandboxV2CraftItemData]
    livestockProduceData: Dict[str, SandboxV2LivestockData]
    craftGroupData: Dict[str, SandboxV2CraftGroupData]
    alchemyRecipeData: Dict[str, SandboxV2AlchemyRecipeData]
    drinkMatData: Dict[str, SandboxV2DrinkMatData]
    foodMatData: Dict[str, SandboxV2FoodMatData]
    foodData: Dict[str, SandboxV2FoodData]
    nodeTypeData: Dict[str, SandboxV2NodeTypeData]
    nodeUpgradeData: Dict[str, SandboxV2NodeUpgradeData]
    weatherData: Dict[str, SandboxV2WeatherData]
    stageData: Dict[str, SandboxV2StageData]
    zoneData: Dict[str, SandboxV2ZoneData]
    nodeBuffData: Dict[str, SandboxV2NodeBuffData]
    rewardConfigData: SandboxV2RewardConfigGroupData
    floatIconData: Dict[str, SandboxV2FloatIconData]
    enemyRushTypeData: Dict[str, SandboxV2EnemyRushTypeData]
    rushEnemyData: SandboxV2BattleRushEnemyData
    gameConst: SandboxV2GameConst
    basicConst: SandboxV2BasicConst
    riftConst: SandboxV2RiftConst
    developmentConst: SandboxV2DevelopmentConst
    battleLoadingTips: List[TipData]
    runeDatas: Dict[str, PackedRuneData]
    itemRuneList: Union[Dict[str, List[LegacyInLevelRuneData]], None]
    questData: Dict[str, SandboxV2QuestData]
    npcData: Dict[str, SandboxV2NpcData]
    dialogData: Dict[str, SandboxV2DialogData]
    questLineData: Dict[str, SandboxV2QuestLineData]
    questLineStoryData: Dict[str, str]
    guideQuestData: Dict[str, SandboxV2GuideQuestData]
    developmentData: Dict[str, SandboxV2DevelopmentData]
    eventData: Dict[str, SandboxV2EventData]
    eventSceneData: Dict[str, SandboxV2EventSceneData]
    eventChoiceData: Dict[str, SandboxV2EventChoiceData]
    expeditionData: Dict[str, SandboxV2ExpeditionData]
    eventEffectData: Dict[str, SandboxV2EventEffectData]
    shopGoodData: Dict[str, SandboxV2ShopGoodData]
    shopDialogData: SandboxV2ShopDialogData
    logisticsData: List[SandboxV2LogisticsData]
    logisticsCharMapping: Dict[str, Dict[str, List[SandboxV2LogisticsCharData]]]
    materialKeywordData: Dict[str, str]
    monthRushData: List[SandboxV2MonthRushData]
    riftTerrainParamData: Dict[str, SandboxV2RiftParamData]
    riftClimateParamData: Dict[str, SandboxV2RiftParamData]
    riftEnemyParamData: Dict[str, SandboxV2RiftParamData]
    riftSubTargetData: Dict[str, SandboxV2RiftSubTargetData]
    riftMainTargetData: Dict[str, SandboxV2RiftMainTargetData]
    riftGlobalEffectData: Dict[str, SandboxV2RiftGlobalEffectData]
    fixedRiftData: Dict[str, SandboxV2FixedRiftData]
    riftTeamBuffData: Dict[str, List[SandboxV2RiftTeamBuffData]]
    riftDifficultyData: Dict[str, SandboxV2RiftDifficultyData]
    riftRewardDisplayData: Dict[str, List[str]]
    enemyReplaceData: Dict[str, Dict[str, str]]
    archiveQuestData: Dict[str, SandboxV2ArchiveQuestData]
    achievementData: Dict[str, SandboxV2ArchiveAchievementData]
    achievementTypeData: Dict[str, SandboxV2ArchiveAchievementTypeData]
    archiveQuestTypeData: Dict[str, SandboxV2ArchiveQuestTypeData]
    archiveMusicUnlockData: Dict[str, SandboxV2ArchiveMusicUnlockData]
    baseUpdate: List[SandboxV2BaseUpdateData]
    developmentLineSegmentDatas: List[SandboxV2DevelopmentLineSegmentData]
    buildingNodeScoreData: Dict[str, SandboxV2BuildingNodeScoreData]
    seasonData: Dict[str, SandboxV2SeasonData]
    confirmIconData: List[SandboxV2ConfirmIconData]
    shopUpdateTimeData: List[int]
    tutorialData: SandboxV2TutorialData


class SandboxPermDetailData(BaseStruct):
    SANDBOX_V2: Dict[str, SandboxV2Data]


class SandboxPermItemData(BaseStruct):
    itemId: str
    itemType: str
    itemName: str
    itemUsage: str
    itemDesc: str
    itemRarity: int
    sortId: int
    obtainApproach: str


class SandboxPermTable(BaseStruct):
    __version__ = "24-02-02-10-18-07-831ad8"

    basicInfo: Dict[str, SandboxPermBasicData]
    detail: SandboxPermDetailData
    itemData: Dict[str, SandboxPermItemData]
