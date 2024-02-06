from typing import Dict, List, Union

from ..common import BaseStruct

from msgspec import field


class SandboxMapConstTable(BaseStruct):
    directionNames: List[str]
    homeNodeStageId: str
    homeRushStageCode: str
    homeRushStageName: str
    homeRushDesc: str
    crazyRevengeRushGroup: str
    homeBuildModeBGM: str


class SandboxBaseConstTable(BaseStruct):
    cookRegularCostItemId: str
    cookRegularCostItemIdCnt: int
    squadTabNameList: List[str]
    charRarityColorList: List[str]
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


class TipData(BaseStruct):
    tip: str
    weight: Union[int, float]
    category: str


class SandboxFoodProduceData(BaseStruct):
    itemId: str
    mainMaterialItems: List[str]
    buffId: str
    unlockDesc: str


class SandboxFoodmatBuffData(BaseStruct):
    itemId: str
    buffId: Union[str, None]
    buffDesc: Union[str, None]
    matType: str
    sortId: int


class SandboxFoodStaminaData(BaseStruct):
    itemId: str
    potCnt: int
    foodStaminaCnt: int


class SandboxBuildProduceData(BaseStruct):
    itemProduceId: str
    itemId: str
    itemTypeText: str
    materialItems: Dict[str, int]


class SandboxBuildGoldRatioData(BaseStruct):
    itemId: str
    ratio: int
    effectDesc: str


class SandboxBuildingItemData(BaseStruct):
    itemId: str
    itemSubType: str
    itemRarity: int


class SandboxBuildProduceUnlockData(BaseStruct):
    itemId: str
    buildingEffectDesc: str
    buildingItemDesc: str
    buildingUnlockDesc: str


class SandboxCraftItemData(BaseStruct):
    itemId: str
    sortId: int
    getFrom: str
    npcId: Union[str, None]
    notObtainedDesc: str
    itemType: str


class SandboxItemTrapData(BaseStruct):
    itemId: str
    trapId: str
    trapPhase: int
    trapLevel: int
    skillIndex: int
    skillLevel: int


class SandboxDevelopmentData(BaseStruct):
    buffId: str
    positionX: int
    positionY: int
    frontNodeId: Union[str, None]
    nextNodeIds: Union[List[str], None]
    buffLimitedId: str
    tokenCost: int
    canBuffResearch: bool
    buffResearchDesc: Union[str, None]
    buffName: str
    buffIconId: str
    nodeTitle: str
    buffEffectDesc: str


class SandboxDevelopmentLimitData(BaseStruct):
    buffLimitedId: str
    positionX: int
    buffCostLimitedCount: int


class SandboxItemToastData(BaseStruct):
    itemType: str
    toastDesc: str
    color: str


class SandboxDevelopmentLineSegmentData(BaseStruct):
    fromNodeId: str
    passingNodeIds: List[str]
    fromAxisPosX: int
    fromAxisPosY: int
    toAxisPosX: int
    toAxisPosY: int


class SandboxRewardItemConfigData(BaseStruct):
    rewardItem: str
    rewardType: str


class SandboxRewardData(BaseStruct):
    rewardList: List[SandboxRewardItemConfigData]


class SandboxRewardCommonConfig(BaseStruct):
    rewardItemId: str
    rewardItemType: str
    count: int
    dropType: Union[int, None] = None


class SandboxTrapRewardConfigData(SandboxRewardCommonConfig):
    dropType: int


class SandboxRewardConfigGroupData(BaseStruct):
    stagePreviewRewardDict: Dict[str, SandboxRewardData]
    stageDefaultPreviewRewardDict: Dict[str, SandboxRewardData]
    rushPreviewRewardDict: Dict[str, SandboxRewardData]
    stageRewardDict: Dict[str, SandboxRewardData]
    rushRewardDict: Dict[str, SandboxRewardData]
    trapRewardDict: Dict[str, SandboxRewardCommonConfig]
    enemyRewardDict: Dict[str, SandboxRewardCommonConfig]
    keyWordData: Dict[str, str]


class SandboxStaminaData(BaseStruct):
    levelUpperLimit: int
    staminaUpperLimit: int


class SandboxNodeTypeData(BaseStruct):
    nodeType: str
    name: str
    subName: str
    iconId: str


class SandboxNodeUpgradeData(BaseStruct):
    nodeUpdradeId: str
    name: str
    description: str
    upgradeDesc: str
    itemType: str
    itemSubType: str
    itemCnt: int
    itemRarity: int


class SandboxWeatherData(BaseStruct):
    weatherId: str
    weatherType: str
    weatherLevel: int
    name: str
    description: str
    weatherTypeName: str
    weatherTypeIconId: str
    functionDesc: str
    buffId: str


class SandboxStageData(BaseStruct):
    stageId: str
    levelId: str
    code: str
    name: str
    loadingPicId: str
    description: str
    actionCost: int
    powerCost: int


class SandboxEventData(BaseStruct):
    eventSceneId: str
    hasThumbtack: bool


class SandboxEventSceneData(BaseStruct):
    choiceSceneId: str
    type_: str = field(name='type')
    title: str
    description: str
    choices: List[str]


class SandboxEventChoiceData(BaseStruct):
    choiceId: str
    type_: str = field(name='type')
    costAction: int
    finishScene: bool
    title: str
    description: str


class SandboxEventTypeData(BaseStruct):
    eventType: str
    iconId: str


class SandboxMissionData(BaseStruct):
    missionId: str
    desc: str
    effectDesc: Union[str, None]
    costAction: int
    charCnt: int
    professionIds: List[str]
    profession: int
    costStamina: int


class SandboxUnitData(BaseStruct):
    id_: str = field(name='id')
    name: str


class SandboxDailyDescTemplateData(BaseStruct):
    type_: str = field(name='type')
    templateDesc: List[str]


class RushEnemyConfig(BaseStruct):
    enemyKey: str
    branchId: str
    count: int
    interval: Union[int, float]


class RushEnemyGroupConfig(BaseStruct):
    enemyGroupKey: str
    weight: int
    enemy: List[RushEnemyConfig]
    dynamicEnemy: List[str]


class RushEnemyGroupRushEnemyDBRef(BaseStruct):
    id_: str = field(name='id')
    level: int


class RushEnemyGroup(BaseStruct):
    rushEnemyGroupConfigs: Dict[str, List[RushEnemyGroupConfig]]
    rushEnemyDbRef: List[RushEnemyGroupRushEnemyDBRef]


class RuneDataSelector(BaseStruct):
    professionMask: int
    buildableMask: int
    charIdFilter: Union[List[str], None]
    enemyIdFilter: Union[List[str], None]
    enemyIdExcludeFilter: Union[List[str], None]
    skillIdFilter: Union[List[str], None]
    tileKeyFilter: Union[List[str], None]
    groupTagFilter: Union[List[str], None]
    filterTagFilter: Union[List[str], None]
    subProfessionExcludeFilter: Union[List[str], None]


class Blackboard(BaseStruct):
    key: str
    value: Union[Union[int, float], None] = None
    valueStr: Union[str, None] = None


class RuneData(BaseStruct):
    key: str
    selector: RuneDataSelector
    blackboard: List[Blackboard]


class RuneTablePackedRuneData(BaseStruct):
    id_: str = field(name='id')
    points: Union[int, float]
    mutexGroupKey: Union[str, None]
    description: str
    runes: List[RuneData]


class LegacyInLevelRuneData(BaseStruct):
    difficultyMask: int
    key: str
    professionMask: int
    buildableMask: int
    blackboard: List[Blackboard]


class SandboxActTable(BaseStruct):
    mapConstTable: SandboxMapConstTable
    baseConstTable: SandboxBaseConstTable
    battleLoadingTips: List[TipData]
    foodProduceDatas: Dict[str, SandboxFoodProduceData]
    foodmatDatas: Dict[str, SandboxFoodmatBuffData]
    foodmatBuffDatas: Dict[str, SandboxFoodmatBuffData]
    foodStaminaDatas: Dict[str, SandboxFoodStaminaData]
    buildProduceDatas: Dict[str, SandboxBuildProduceData]
    buildGoldRatioDatas: List[SandboxBuildGoldRatioData]
    buildingItemDatas: Dict[str, SandboxBuildingItemData]
    buildProduceUnlockDatas: Dict[str, SandboxBuildProduceUnlockData]
    craftItemDatas: Dict[str, SandboxCraftItemData]
    itemTrapDatas: Dict[str, SandboxItemTrapData]
    trapDeployLimitDatas: Dict[str, int]
    developmentDatas: Dict[str, SandboxDevelopmentData]
    developmentLimitDatas: Dict[str, SandboxDevelopmentLimitData]
    itemToastDatas: Dict[str, SandboxItemToastData]
    developmentLineSegmentDatas: List[SandboxDevelopmentLineSegmentData]
    rewardConfigDatas: SandboxRewardConfigGroupData
    charStaminaMapping: Dict[str, Dict[str, List[SandboxStaminaData]]]
    nodeTypeDatas: Dict[str, SandboxNodeTypeData]
    nodeUpgradeDatas: Dict[str, SandboxNodeUpgradeData]
    weatherDatas: Dict[str, SandboxWeatherData]
    stageDatas: Dict[str, SandboxStageData]
    eventDatas: Dict[str, SandboxEventData]
    eventSceneDatas: Dict[str, SandboxEventSceneData]
    eventChoiceDatas: Dict[str, SandboxEventChoiceData]
    eventTypeDatas: Dict[str, SandboxEventTypeData]
    missionDatas: Dict[str, SandboxMissionData]
    unitData: Dict[str, SandboxUnitData]
    dailyDescTemplateDatas: Dict[str, SandboxDailyDescTemplateData]
    rushAvgDict: Dict[str, str]
    rushEnemyGroup: RushEnemyGroup
    runeDatas: Dict[str, RuneTablePackedRuneData]
    itemRuneList: Dict[str, List[LegacyInLevelRuneData]]


class SandboxItemData(BaseStruct):
    itemId: str
    itemType: str
    itemName: str
    itemUsage: str
    itemDesc: str
    itemRarity: int
    sortId: int
    recommendTypeList: Union[List[str], None]
    recommendPriority: int
    obtainApproach: str


class SandboxTable(BaseStruct):
    __version__ = '24-02-02-10-18-07-831ad8'

    sandboxActTables: Dict[str, SandboxActTable]
    itemDatas: Dict[str, SandboxItemData]
