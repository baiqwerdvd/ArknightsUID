from pydantic import BaseModel, Field


class SandboxMapConstTable(BaseModel):
    directionNames: list[str]
    homeNodeStageId: str
    homeRushStageCode: str
    homeRushStageName: str
    homeRushDesc: str
    crazyRevengeRushGroup: str
    homeBuildModeBGM: str


class SandboxBaseConstTable(BaseModel):
    cookRegularCostItemId: str
    cookRegularCostItemIdCnt: int
    squadTabNameList: list[str]
    charRarityColorList: list[str]
    sumFoodLimitedCount: int
    sumBuildingLimitedCount: int
    sumTacticalLimitedCount: int
    sumFoodMatLimitedCount: int
    sumBuildingMatLimitedCount: int
    sumStaminaPotLimitedCount: int
    sumGoldLimitedCount: int
    itemLimitedCount: int
    blackBoxSlotCnt: int
    scoutNodeUpgradeId: str
    battleNodeUpgradeId: str
    staminaPotCostOnce: int
    staminaPotItemId: str
    staminapotRedMinCnt: int
    staminapotYellowMinCnt: int
    staminapotGreenMinCnt: int
    staminapotMaxPercentCnt: int
    staminaPotActionPoint: int
    goldItemId: str
    toolboxSlotCapacity: int
    toolboxSlotCnt: int
    teamPopulationLimit: int
    researchInformationDesc: str
    settleFailDesc: str
    settleAbortDesc: str
    settleSucDesc: str


class TipData(BaseModel):
    tip: str
    weight: int | float
    category: str


class SandboxFoodProduceData(BaseModel):
    itemId: str
    mainMaterialItems: list[str]
    buffId: str
    unlockDesc: str


class SandboxFoodmatBuffData(BaseModel):
    itemId: str
    buffId: str | None
    buffDesc: str | None
    matType: str
    sortId: int


class SandboxFoodStaminaData(BaseModel):
    itemId: str
    potCnt: int
    foodStaminaCnt: int


class SandboxBuildProduceData(BaseModel):
    itemProduceId: str
    itemId: str
    itemTypeText: str
    materialItems: dict[str, int]


class SandboxBuildGoldRatioData(BaseModel):
    itemId: str
    ratio: int
    effectDesc: str


class SandboxBuildingItemData(BaseModel):
    itemId: str
    itemSubType: str
    itemRarity: int


class SandboxBuildProduceUnlockData(BaseModel):
    itemId: str
    buildingEffectDesc: str
    buildingItemDesc: str
    buildingUnlockDesc: str


class SandboxCraftItemData(BaseModel):
    itemId: str
    sortId: int
    getFrom: str
    npcId: str | None
    notObtainedDesc: str
    itemType: str


class SandboxItemTrapData(BaseModel):
    itemId: str
    trapId: str
    trapPhase: int
    trapLevel: int
    skillIndex: int
    skillLevel: int


class SandboxDevelopmentData(BaseModel):
    buffId: str
    positionX: int
    positionY: int
    frontNodeId: str | None
    nextNodeIds: list[str] | None
    buffLimitedId: str
    tokenCost: int
    canBuffResearch: bool
    buffResearchDesc: str | None
    buffName: str
    buffIconId: str
    nodeTitle: str
    buffEffectDesc: str


class SandboxDevelopmentLimitData(BaseModel):
    buffLimitedId: str
    positionX: int
    buffCostLimitedCount: int


class SandboxItemToastData(BaseModel):
    itemType: str
    toastDesc: str
    color: str


class SandboxDevelopmentLineSegmentData(BaseModel):
    fromNodeId: str
    passingNodeIds: list[str]
    fromAxisPosX: int
    fromAxisPosY: int
    toAxisPosX: int
    toAxisPosY: int


class SandboxRewardItemConfigData(BaseModel):
    rewardItem: str
    rewardType: str


class SandboxRewardData(BaseModel):
    rewardList: list[SandboxRewardItemConfigData]


class SandboxRewardCommonConfig(BaseModel):
    dropType: int | None = None
    rewardItemId: str
    rewardItemType: str
    count: int


class SandboxTrapRewardConfigData(SandboxRewardCommonConfig):
    dropType: int


class SandboxRewardConfigGroupData(BaseModel):
    stagePreviewRewardDict: dict[str, SandboxRewardData]
    stageDefaultPreviewRewardDict: dict[str, SandboxRewardData]
    rushPreviewRewardDict: dict[str, SandboxRewardData]
    stageRewardDict: dict[str, SandboxRewardData]
    rushRewardDict: dict[str, SandboxRewardData]
    trapRewardDict: dict[str, SandboxRewardCommonConfig]
    enemyRewardDict: dict[str, SandboxRewardCommonConfig]
    keyWordData: dict[str, str]


class SandboxStaminaData(BaseModel):
    levelUpperLimit: int
    staminaUpperLimit: int


class SandboxNodeTypeData(BaseModel):
    nodeType: str
    name: str
    subName: str
    iconId: str


class SandboxNodeUpgradeData(BaseModel):
    nodeUpdradeId: str
    name: str
    description: str
    upgradeDesc: str
    itemType: str
    itemSubType: str
    itemCnt: int
    itemRarity: int


class SandboxWeatherData(BaseModel):
    weatherId: str
    weatherType: str
    weatherLevel: int
    name: str
    description: str
    weatherTypeName: str
    weatherTypeIconId: str
    functionDesc: str
    buffId: str


class SandboxStageData(BaseModel):
    stageId: str
    levelId: str
    code: str
    name: str
    loadingPicId: str
    description: str
    actionCost: int
    powerCost: int


class SandboxEventData(BaseModel):
    eventSceneId: str
    hasThumbtack: bool


class SandboxEventSceneData(BaseModel):
    choiceSceneId: str
    type_: str = Field(alias='type')
    title: str
    description: str
    choices: list[str]


class SandboxEventChoiceData(BaseModel):
    choiceId: str
    type_: str = Field(alias='type')
    costAction: int
    finishScene: bool
    title: str
    description: str


class SandboxEventTypeData(BaseModel):
    eventType: str
    iconId: str


class SandboxMissionData(BaseModel):
    missionId: str
    desc: str
    effectDesc: str | None
    costAction: int
    charCnt: int
    professionIds: list[str]
    profession: int
    costStamina: int


class SandboxUnitData(BaseModel):
    id_: str = Field(alias='id')
    name: str


class SandboxDailyDescTemplateData(BaseModel):
    type_: str = Field(alias='type')
    templateDesc: list[str]


class RushEnemyConfig(BaseModel):
    enemyKey: str
    branchId: str
    count: int
    interval: int | float


class RushEnemyGroupConfig(BaseModel):
    enemyGroupKey: str
    weight: int
    enemy: list[RushEnemyConfig]
    dynamicEnemy: list[str]


class RushEnemyGroupRushEnemyDBRef(BaseModel):
    id_: str = Field(alias='id')
    level: int


class RushEnemyGroup(BaseModel):
    rushEnemyGroupConfigs: dict[str, list[RushEnemyGroupConfig]]
    rushEnemyDbRef: list[RushEnemyGroupRushEnemyDBRef]


class RuneDataSelector(BaseModel):
    professionMask: int
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
    value: int | float | None = None
    valueStr: str | None = None


class RuneData(BaseModel):
    key: str
    selector: RuneDataSelector
    blackboard: list[Blackboard]


class RuneTablePackedRuneData(BaseModel):
    id_: str = Field(alias='id')
    points: int | float
    mutexGroupKey: str | None
    description: str
    runes: list[RuneData]


class LegacyInLevelRuneData(BaseModel):
    difficultyMask: int
    key: str
    professionMask: int
    buildableMask: int
    blackboard: list[Blackboard]


class SandboxActTable(BaseModel):
    mapConstTable: SandboxMapConstTable
    baseConstTable: SandboxBaseConstTable
    battleLoadingTips: list[TipData]
    foodProduceDatas: dict[str, SandboxFoodProduceData]
    foodmatDatas: dict[str, SandboxFoodmatBuffData]
    foodmatBuffDatas: dict[str, SandboxFoodmatBuffData]
    foodStaminaDatas: dict[str, SandboxFoodStaminaData]
    buildProduceDatas: dict[str, SandboxBuildProduceData]
    buildGoldRatioDatas: list[SandboxBuildGoldRatioData]
    buildingItemDatas: dict[str, SandboxBuildingItemData]
    buildProduceUnlockDatas: dict[str, SandboxBuildProduceUnlockData]
    craftItemDatas: dict[str, SandboxCraftItemData]
    itemTrapDatas: dict[str, SandboxItemTrapData]
    trapDeployLimitDatas: dict[str, int]
    developmentDatas: dict[str, SandboxDevelopmentData]
    developmentLimitDatas: dict[str, SandboxDevelopmentLimitData]
    itemToastDatas: dict[str, SandboxItemToastData]
    developmentLineSegmentDatas: list[SandboxDevelopmentLineSegmentData]
    rewardConfigDatas: SandboxRewardConfigGroupData
    charStaminaMapping: dict[str, dict[str, list[SandboxStaminaData]]]
    nodeTypeDatas: dict[str, SandboxNodeTypeData]
    nodeUpgradeDatas: dict[str, SandboxNodeUpgradeData]
    weatherDatas: dict[str, SandboxWeatherData]
    stageDatas: dict[str, SandboxStageData]
    eventDatas: dict[str, SandboxEventData]
    eventSceneDatas: dict[str, SandboxEventSceneData]
    eventChoiceDatas: dict[str, SandboxEventChoiceData]
    eventTypeDatas: dict[str, SandboxEventTypeData]
    missionDatas: dict[str, SandboxMissionData]
    unitData: dict[str, SandboxUnitData]
    dailyDescTemplateDatas: dict[str, SandboxDailyDescTemplateData]
    rushAvgDict: dict[str, str]
    rushEnemyGroup: RushEnemyGroup
    runeDatas: dict[str, RuneTablePackedRuneData]
    itemRuneList: dict[str, list[LegacyInLevelRuneData]]


class SandboxItemData(BaseModel):
    itemId: str
    itemType: str
    itemName: str
    itemUsage: str
    itemDesc: str
    itemRarity: int
    sortId: int
    recommendTypeList: list[str] | None
    recommendPriority: int
    obtainApproach: str


class SandboxTable(BaseModel):
    __version__ = '23-07-27-18-50-06-aeb568'

    sandboxActTables: dict[str, SandboxActTable]
    itemDatas: dict[str, SandboxItemData]
