from typing import Dict, List, Union

from ..common import BaseStruct

from msgspec import field


class RoguelikeTopicBasicDataHomeEntryDisplayData(BaseStruct):
    topicId: str
    displayId: str
    startTs: int
    endTs: int


class RoguelikeTopicConfig(BaseStruct):
    webBusType: str
    monthChatTrigType: int
    loadRewardHpDecoPlugin: bool
    loadRewardExtraInfoPlugin: bool
    loadCharCardPlugin: Union[bool, None] = None


class RoguelikeTopicBasicData(BaseStruct):
    id_: str = field(name='id')
    name: str
    startTime: int
    disappearTimeOnMainScreen: int
    sort: int
    showMedalId: str
    medalGroupId: str
    fullStoredTime: int
    lineText: str
    homeEntryDisplayData: List[RoguelikeTopicBasicDataHomeEntryDisplayData]
    moduleTypes: List[str]
    config: RoguelikeTopicConfig


class RoguelikeTopicConstPredefinedChar(BaseStruct):
    charId: str
    canBeFree: bool
    uniEquipId: Union[str, None]
    recruitType: str


class RoguelikeTopicConst(BaseStruct):
    milestoneTokenRatio: int
    outerBuffTokenRatio: Union[int, float]
    relicTokenRatio: int
    rogueSystemUnlockStage: str
    ordiModeReOpenCoolDown: int
    monthModeReOpenCoolDown: int
    monthlyTaskUncompletedTime: int
    monthlyTaskManualRefreshLimit: int
    monthlyTeamUncompletedTime: int
    bpPurchaseSystemUnlockTime: int
    predefinedChars: Dict[str, RoguelikeTopicConstPredefinedChar]


class RoguelikeTopicUpdate(BaseStruct):
    updateId: str
    topicUpdateTime: int
    topicEndTime: int


class RoguelikeTopicEnroll(BaseStruct):
    enrollId: str
    enrollTime: int


class RoguelikeTopicBP(BaseStruct):
    id_: str = field(name='id')
    level: int
    tokenNum: int
    nextTokenNum: int
    itemID: str
    itemType: str
    itemCount: int
    isGoodPrize: bool
    isGrandPrize: bool


class RoguelikeTopicMilestoneUpdateData(BaseStruct):
    updateTime: int
    endTime: int
    maxBpLevel: int
    maxBpCount: int
    maxDisplayBpCount: int


class ItemBundle(BaseStruct):
    id_: str = field(name='id')
    count: int
    type_: str = field(name='type')


class RoguelikeTopicBPGrandPrize(BaseStruct):
    grandPrizeDisplayId: str
    sortId: int
    displayUnlockYear: int
    displayUnlockMonth: int
    acquireTitle: str
    purchaseTitle: str
    displayName: str
    displayDiscription: str
    bpLevelId: str
    itemBundle: Union[ItemBundle, None] = None
    accordingCharId: Union[str, None] = None
    accordingSkinId: Union[str, None] = None
    detailAnnounceTime: Union[str, None] = None
    picIdAftrerUnlock: Union[str, None] = None


class RoguelikeTopicMonthMission(BaseStruct):
    id_: str = field(name='id')
    taskName: str
    taskClass: str
    innerClassWeight: int
    template: str
    paramList: List[str]
    desc: str
    tokenRewardNum: int


class RoguelikeTopicMonthSquad(BaseStruct):
    id_: str = field(name='id')
    teamName: str
    teamSubName: Union[str, None]
    teamFlavorDesc: Union[str, None]
    teamDes: str
    teamColor: str
    teamMonth: str
    teamYear: str
    teamIndex: Union[str, None]
    teamChars: List[str]
    zoneId: Union[str, None]
    chatId: str
    tokenRewardNum: int
    items: List[ItemBundle]
    startTime: int
    endTime: int
    taskDes: Union[str, None]


class RoguelikeTopicChallengeTask(BaseStruct):
    taskId: str
    taskDes: str
    completionClass: str
    completionParams: List[str]


class RoguelikeTopicChallenge(BaseStruct):
    challengeId: str
    sortId: int
    challengeName: str
    challengeGroup: int
    challengeGroupSortId: int
    challengeGroupName: Union[str, None]
    challengeUnlockDesc: Union[str, None]
    challengeUnlockToastDesc: Union[str, None]
    challengeDes: str
    challengeConditionDes: List[str]
    challengeTasks: Dict[str, RoguelikeTopicChallengeTask]
    defaultTaskId: str
    rewards: List[ItemBundle]


class RoguelikeTopicDifficulty(BaseStruct):
    modeDifficulty: str
    grade: int
    name: str
    subName: Union[str, None]
    enrollId: Union[str, None]
    haveInitialRelicIcon: bool
    scoreFactor: Union[int, float]
    canUnlockItem: bool
    doMonthTask: bool
    ruleDesc: str
    failTitle: str
    failImageId: str
    failForceDesc: str
    sortId: int
    equivalentGrade: int
    color: Union[str, None]
    bpValue: int
    bossValue: int
    addDesc: Union[str, None]
    isHard: bool
    unlockText: Union[str, None]
    displayIconId: Union[str, None]
    hideEndingStory: bool


class RoguelikeTopicBankReward(BaseStruct):
    rewardId: str
    unlockGoldCnt: int
    rewardType: str
    desc: str


class ActArchiveRelicItemData(BaseStruct):
    relicId: str
    relicSortId: int
    relicGroupId: int
    orderId: str
    isSpRelic: bool
    enrollId: Union[str, None]


class ActArchiveRelicData(BaseStruct):
    relic: Dict[str, ActArchiveRelicItemData]


class ActArchiveCapsuleItemData(BaseStruct):
    capsuleId: str
    capsuleSortId: int
    englishName: str
    enrollId: Union[str, None]


class ActArchiveCapsuleData(BaseStruct):
    capsule: Dict[str, ActArchiveCapsuleItemData]


class ActArchiveTrapItemData(BaseStruct):
    trapId: str
    trapSortId: int
    orderId: str
    enrollId: Union[str, None]


class ActArchiveTrapData(BaseStruct):
    trap: Dict[str, ActArchiveTrapItemData]


class ActArchiveChatItemData(BaseStruct):
    chatFloor: int
    chatDesc: Union[str, None]
    chatStoryId: str


class ActArchiveChatGroupData(BaseStruct):
    sortId: int
    numChat: int
    clientChatItemData: List[ActArchiveChatItemData]


class ActArchiveChatData(BaseStruct):
    chat: Dict[str, ActArchiveChatGroupData]


class ActArchiveEndbookItemData(BaseStruct):
    endBookId: str
    sortId: int
    endbookName: str
    unlockDesc: str
    textId: str
    enrollId: Union[str, None] = None
    isLast: Union[bool, None] = None


class ActArchiveEndbookGroupData(BaseStruct):
    endId: str
    endingId: str
    sortId: int
    title: str
    cgId: str
    backBlurId: str
    cardId: str
    hasAvg: bool
    avgId: str
    clientEndbookItemDatas: List[ActArchiveEndbookItemData]


class ActArchiveEndbookData(BaseStruct):
    endbook: Dict[str, ActArchiveEndbookGroupData]


class ActArchiveBuffItemData(BaseStruct):
    buffId: str
    buffGroupIndex: int
    innerSortId: int
    name: str
    iconId: str
    usage: str
    desc: str
    color: str


class ActArchiveBuffData(BaseStruct):
    buff: Dict[str, ActArchiveBuffItemData]


class ActArchiveTotemItemData(BaseStruct):
    id_: str = field(name='id')
    type_: int = field(name='type')
    enrollConditionId: Union[str, None]
    sortId: int


class ActArchiveTotemData(BaseStruct):
    totem: Dict[str, ActArchiveTotemItemData]


class ActArchiveChaosItemData(BaseStruct):
    id_: str = field(name='id')
    isHidden: bool
    enrollId: Union[str, None]
    sortId: int


class ActArchiveChaosData(BaseStruct):
    chaos: Dict[str, ActArchiveChaosItemData]


class RoguelikeArchiveComponentData(BaseStruct):
    relic: ActArchiveRelicData
    capsule: Union[ActArchiveCapsuleData, None]
    trap: ActArchiveTrapData
    chat: ActArchiveChatData
    endbook: ActArchiveEndbookData
    buff: ActArchiveBuffData
    totem: Union[ActArchiveTotemData, None]
    chaos: Union[ActArchiveChaosData, None]
    challengeBook: Dict[str, Dict[str, None]]


class RoguelikeArchiveUnlockCondDesc(BaseStruct):
    archiveType: str
    description: str


class RoguelikeArchiveEnroll(BaseStruct):
    archiveType: str
    enrollId: Union[str, None]


class RoguelikeArchiveUnlockCondData(BaseStruct):
    unlockCondDesc: Dict[str, RoguelikeArchiveUnlockCondDesc]
    enroll: Dict[str, RoguelikeArchiveEnroll]


class RoguelikeTopicDetailConstPlayerLevelData(BaseStruct):
    exp: int
    populationUp: int
    squadCapacityUp: int
    battleCharLimitUp: int
    maxHpUp: int


class RoguelikeTopicDetailConstCharUpgradeData(BaseStruct):
    evolvePhase: int
    skillLevel: int
    skillSpecializeLevel: int


class RoguelikeTopicDetailConst(BaseStruct):
    playerLevelTable: Dict[str, RoguelikeTopicDetailConstPlayerLevelData]
    charUpgradeTable: Dict[str, RoguelikeTopicDetailConstCharUpgradeData]
    difficultyUpgradeRelicDescTable: Dict[str, str]
    tokenBpId: str
    tokenOuterBuffId: str
    previewedRewardsAccordingUpdateId: str
    tipButtonName: str
    collectButtonName: str
    bpSystemName: str
    autoSetKV: str
    bpPurchaseActiveEnroll: str
    defaultSacrificeDesc: Union[str, None]
    defaultExpeditionSelectDesc: Union[str, None]
    gotCharBuffToast: Union[str, None]
    gotSquadBuffToast: Union[str, None]
    loseCharBuffToast: Union[str, None]
    monthTeamSystemName: str
    battlePassUpdateName: str
    monthCharCardTagName: str
    monthTeamDescTagName: str
    outerBuffCompleteText: str
    outerProgressTextColor: str
    challengeTaskTargetName: str
    challengeTaskConditionName: str
    challengeTaskRewardName: str
    challengeTaskModeName: str
    challengeTaskName: str
    outerBuffTokenSum: int
    needAllFrontNode: bool
    showBlurBack: bool


class RoguelikeGameInitData(BaseStruct):
    modeId: str
    modeGrade: int
    predefinedId: Union[str, None]
    predefinedStyle: Union[str, None]
    initialBandRelic: List[str]
    initialRecruitGroup: Union[List[str], None]
    initialHp: int
    initialPopulation: int
    initialGold: int
    initialSquadCapacity: int
    initialShield: int
    initialMaxHp: int
    initialKey: int


class RoguelikeGameStageData(BaseStruct):
    id_: str = field(name='id')
    linkedStageId: str
    levelId: str
    code: str
    name: str
    loadingPicId: str
    description: str
    eliteDesc: Union[str, None]
    isBoss: int
    isElite: int
    difficulty: str
    capsulePool: Union[str, None]
    capsuleProb: Union[int, float]
    vutresProb: List[float]
    boxProb: List[float]
    specialNodeId: Union[str, None] = None


class RoguelikeGameZoneData(BaseStruct):
    id_: str = field(name='id')
    name: str
    clockPerformance: Union[str, None]
    displayTime: Union[str, None]
    description: str
    endingDescription: str
    backgroundId: str
    zoneIconId: str
    isHiddenZone: bool


class RoguelikeZoneVariationData(BaseStruct):
    pass


class RoguelikeGameTrapData(BaseStruct):
    itemId: str
    trapId: str
    trapDesc: str


class RoguelikeGameRecruitTicketData(BaseStruct):
    id_: str = field(name='id')
    profession: int
    rarity: int
    professionList: List[str]
    rarityList: List[int]
    extraEliteNum: int
    extraFreeRarity: List[int]
    extraCharIds: List[str]


class RoguelikeGameUpgradeTicketData(BaseStruct):
    id_: str = field(name='id')
    profession: int
    rarity: int
    professionList: List[str]
    rarityList: List[int]


class RoguelikeGameCustomTicketData(BaseStruct):
    id_: str = field(name='id')
    subType: str
    discardText: str


class Blackboard(BaseStruct):
    key: str
    value: Union[Union[int, float], None] = None
    valueStr: Union[str, None] = None


class RoguelikeBuff(BaseStruct):
    key: str
    blackboard: List[Blackboard]


class RoguelikeGameRelicData(BaseStruct):
    id_: str = field(name='id')
    buffs: List[RoguelikeBuff]


class RoguelikeGameRelicCheckParam(BaseStruct):
    valueProfessionMask: int
    valueStrs: Union[List[str], None]
    valueInt: int


class RoguelikeGameRelicParamData(BaseStruct):
    id_: str = field(name='id')
    checkCharBoxTypes: List[str]
    checkCharBoxParams: List[RoguelikeGameRelicCheckParam]


class RoguelikeGameRecruitGrpData(BaseStruct):
    id_: str = field(name='id')
    iconId: str
    name: str
    desc: str
    unlockDesc: Union[str, None]


class RoguelikeChoiceDisplayData(BaseStruct):
    type_: str = field(name='type')
    funcIconId: Union[str, None]
    itemId: Union[str, None]
    taskId: Union[str, None]
    costHintType: Union[int, None] = None
    effectHintType: Union[int, None] = None
    difficultyUpgradeRelicGroupId: Union[str, None] = None


class RoguelikeGameChoiceData(BaseStruct):
    id_: str = field(name='id')
    title: str
    description: Union[str, None]
    lockedCoverDesc: Union[str, None]
    type_: str = field(name='type')
    leftDecoType: str
    nextSceneId: Union[str, None]
    icon: Union[str, None]
    displayData: RoguelikeChoiceDisplayData
    forceShowWhenOnlyLeave: bool


class RoguelikeGameChoiceSceneData(BaseStruct):
    id_: str = field(name='id')
    title: str
    description: str
    background: Union[str, None]
    titleIcon: Union[str, None]
    subTypeId: int
    useHiddenMusic: bool


class RoguelikeGameNodeTypeData(BaseStruct):
    name: str
    description: str


class RoguelikeGameNodeSubTypeData(BaseStruct):
    eventType: str
    subTypeId: int
    iconId: str
    name: Union[str, None]
    description: str


class RoguelikeGameVariationData(BaseStruct):
    id_: str = field(name='id')
    type_: str = field(name='type')
    outerName: str
    innerName: str
    functionDesc: str
    desc: str
    iconId: Union[str, None]
    sound: Union[str, None]


class RoguelikeGameCharBuffData(BaseStruct):
    id_: str = field(name='id')
    iconId: str
    outerName: str
    innerName: str
    functionDesc: str
    desc: str
    buffs: List[RoguelikeBuff]


class RoguelikeGameSquadBuffData(BaseStruct):
    id_: str = field(name='id')
    iconId: str
    outerName: str
    innerName: str
    functionDesc: str
    desc: str
    buffs: List[RoguelikeBuff]


class RoguelikeTaskData(BaseStruct):
    taskId: str
    taskName: str
    taskDesc: str
    rewardSceneId: str
    taskRarity: str


class RoguelikeGameConst(BaseStruct):
    initSceneName: str
    failSceneName: str
    hpItemId: str
    goldItemId: str
    populationItemId: str
    squadCapacityItemId: str
    expItemId: str
    initialBandShowGradeFlag: bool
    bankMaxGold: int
    bankCostId: Union[str, None]
    bankDrawCount: int
    bankDrawLimit: int
    mimicEnemyIds: List[str]
    bossIds: List[str]
    goldChestTrapId: str
    normBoxTrapId: Union[str, None]
    rareBoxTrapId: Union[str, None]
    badBoxTrapId: Union[str, None]
    maxHpItemId: Union[str, None]
    shieldItemId: Union[str, None]
    keyItemId: Union[str, None]
    chestKeyCnt: int
    chestKeyItemId: Union[str, None]
    keyColorId: Union[str, None]
    onceNodeTypeList: List[str]
    gpScoreRatio: int
    overflowUsageSquadBuff: Union[str, None]
    specialTrapId: Union[str, None]
    trapRewardRelicId: Union[str, None]
    unlockRouteItemId: Union[str, None]
    hideBattleNodeName: Union[str, None]
    hideBattleNodeDescription: Union[str, None]
    hideNonBattleNodeName: Union[str, None]
    hideNonBattleNodeDescription: Union[str, None]
    charSelectExpeditionConflictToast: Union[str, None]
    itemDropTagDict: Dict[str, str]
    expeditionReturnDescCureUpgrade: Union[str, None]
    expeditionReturnDescUpgrade: Union[str, None]
    expeditionReturnDescCure: Union[str, None]
    expeditionReturnDesc: Union[str, None]
    expeditionReturnDescItem: Union[str, None]
    expeditionReturnRewardBlackList: List[str]
    gainBuffDiffGrade: int
    dsPredictTips: Union[str, None]
    dsBuffActiveTips: Union[str, None]
    totemDesc: Union[str, None]
    relicDesc: Union[str, None]
    buffDesc: Union[str, None]
    portalZones: List[str]
    exploreExpOnKill: Union[str, None]


class RoguelikeTopicCapsule(BaseStruct):
    itemId: str
    maskType: str
    innerColor: str


class RoguelikeGameEndingDataLevelIcon(BaseStruct):
    level: int
    iconId: str


class RoguelikeGameEndingData(BaseStruct):
    id_: str = field(name='id')
    familyId: int
    name: str
    desc: str
    bgId: str
    icons: List[RoguelikeGameEndingDataLevelIcon]
    priority: int
    changeEndingDesc: Union[str, None]
    bossIconId: Union[str, None]


class RoguelikeBattleSummeryDescriptionData(BaseStruct):
    randomDescriptionList: List[str]


class TipData(BaseStruct):
    tip: str
    weight: Union[int, float]
    category: str


class RoguelikeGameItemData(BaseStruct):
    id_: str = field(name='id')
    name: str
    description: Union[str, None]
    usage: str
    obtainApproach: str
    iconId: str
    type_: str = field(name='type')
    subType: str
    rarity: str
    value: int
    sortId: int
    canSacrifice: bool
    unlockCondDesc: Union[str, None]


class RoguelikeBandRefData(BaseStruct):
    itemId: str
    iconId: str
    description: str
    bandLevel: int
    normalBandId: str


class RoguelikeEndingDetailText(BaseStruct):
    textId: str
    text: str
    eventType: str
    showType: int
    choiceSceneId: Union[str, None]
    paramList: List[str]
    otherPara1: Union[str, None]


class RoguelikeGameTreasureData(BaseStruct):
    treasureId: str
    groupId: str
    subIndex: int
    name: str
    usage: str


class RoguelikeDifficultyUpgradeRelicData(BaseStruct):
    relicId: str
    equivalentGrade: int


class RoguelikeDifficultyUpgradeRelicGroupData(BaseStruct):
    relicData: List[RoguelikeDifficultyUpgradeRelicData]


class RoguelikePredefinedStyleData(BaseStruct):
    styleId: str
    styleConfig: int


class RoguelikeTopicDetail(BaseStruct):
    updates: List[RoguelikeTopicUpdate]
    enrolls: Dict[str, RoguelikeTopicEnroll]
    milestones: List[RoguelikeTopicBP]
    milestoneUpdates: List[RoguelikeTopicMilestoneUpdateData]
    grandPrizes: List[RoguelikeTopicBPGrandPrize]
    monthMission: List[RoguelikeTopicMonthMission]
    monthSquad: Dict[str, RoguelikeTopicMonthSquad]
    challenges: Dict[str, RoguelikeTopicChallenge]
    difficulties: List[RoguelikeTopicDifficulty]
    bankRewards: List[RoguelikeTopicBankReward]
    archiveComp: RoguelikeArchiveComponentData
    archiveUnlockCond: RoguelikeArchiveUnlockCondData
    detailConst: RoguelikeTopicDetailConst
    init: List[RoguelikeGameInitData]
    stages: Dict[str, RoguelikeGameStageData]
    zones: Dict[str, RoguelikeGameZoneData]
    variation: Dict[str, RoguelikeZoneVariationData]
    traps: Dict[str, RoguelikeGameTrapData]
    recruitTickets: Dict[str, RoguelikeGameRecruitTicketData]
    upgradeTickets: Dict[str, RoguelikeGameUpgradeTicketData]
    customTickets: Dict[str, RoguelikeGameCustomTicketData]
    relics: Dict[str, RoguelikeGameRelicData]
    relicParams: Dict[str, RoguelikeGameRelicParamData]
    recruitGrps: Dict[str, RoguelikeGameRecruitGrpData]
    choices: Dict[str, RoguelikeGameChoiceData]
    choiceScenes: Dict[str, RoguelikeGameChoiceSceneData]
    nodeTypeData: Dict[str, RoguelikeGameNodeTypeData]
    subTypeData: List[RoguelikeGameNodeSubTypeData]
    variationData: Dict[str, RoguelikeGameVariationData]
    charBuffData: Dict[str, RoguelikeGameCharBuffData]
    squadBuffData: Dict[str, RoguelikeGameSquadBuffData]
    taskData: Dict[str, RoguelikeTaskData]
    gameConst: RoguelikeGameConst
    shopDialogs: Dict[str, List[str]]
    capsuleDict: Union[Dict[str, RoguelikeTopicCapsule], None]
    endings: Dict[str, RoguelikeGameEndingData]
    battleSummeryDescriptions: Dict[str, RoguelikeBattleSummeryDescriptionData]
    battleLoadingTips: List[TipData]
    items: Dict[str, RoguelikeGameItemData]
    bandRef: Dict[str, RoguelikeBandRefData]
    endingDetailList: List[RoguelikeEndingDetailText]
    treasures: Dict[str, List[RoguelikeGameTreasureData]]
    difficultyUpgradeRelicGroups: Dict[
        str,
        RoguelikeDifficultyUpgradeRelicGroupData,
    ]
    styleConfig: Dict[str, RoguelikePredefinedStyleData]
    styles: Union[Dict[str, RoguelikePredefinedStyleData], None] = {}


class RoguelikeModuleBaseData(BaseStruct):
    moduleType: str


class RoguelikeSanRangeData(BaseStruct):
    sanMax: int
    diceGroupId: str
    description: str
    sanDungeonEffect: str
    sanEffectRank: str
    sanEndingDesc: Union[str, None]


class RoguelikeSanCheckConsts(BaseStruct):
    sanDecreaseToast: str


class RoguelikeSanCheckModuleData(RoguelikeModuleBaseData):
    sanRanges: List[RoguelikeSanRangeData]
    moduleConsts: RoguelikeSanCheckConsts


class RoguelikeDiceData(BaseStruct):
    diceId: str
    description: str
    isUpgradeDice: int
    upgradeDiceId: Union[str, None]
    diceFaceCount: int
    battleDiceId: str


class RoguelikeDiceRuleData(BaseStruct):
    dicePointMax: int
    diceResultClass: str
    diceGroupId: str
    diceEventId: str
    resultDesc: str
    showType: str
    canReroll: bool
    diceEndingScene: str
    diceEndingDesc: str
    sound: str


class RoguelikeDiceRuleGroupData(BaseStruct):
    ruleGroupId: str
    minGoodNum: int


class RoguelikeDicePredefineData(BaseStruct):
    modeId: str
    modeGrade: int
    predefinedId: Union[str, None]
    initialDiceCount: int


class RoguelikeDiceModuleData(RoguelikeModuleBaseData):
    dice: Dict[str, RoguelikeDiceData]
    diceEvents: Dict[str, RoguelikeDiceRuleData]
    diceChoices: Dict[str, str]
    diceRuleGroups: Dict[str, RoguelikeDiceRuleGroupData]
    dicePredefines: List[RoguelikeDicePredefineData]


class RoguelikeChaosData(BaseStruct):
    chaosId: str
    level: int
    nextChaosId: Union[str, None]
    prevChaosId: Union[str, None]
    iconId: str
    name: str
    functionDesc: str
    desc: str
    sound: str
    sortId: int


class RoguelikeChaosRangeData(BaseStruct):
    chaosMax: int
    chaosDungeonEffect: str


class RoguelikeChaosPredefineLevelInfo(BaseStruct):
    chaosLevelBeginNum: int
    chaosLevelEndNum: int


class RoguelikeChaosModuleConsts(BaseStruct):
    maxChaosLevel: int
    maxChaosSlot: int
    chaosNotMaxDescription: str
    chaosMaxDescription: str
    chaosPredictDescription: str


class RoguelikeChaosModuleData(RoguelikeModuleBaseData):
    chaosDatas: Dict[str, RoguelikeChaosData]
    chaosRanges: List[RoguelikeChaosRangeData]
    levelInfoDict: Dict[str, Dict[str, RoguelikeChaosPredefineLevelInfo]]
    moduleConsts: RoguelikeChaosModuleConsts


class RoguelikeTotemLinkedNodeTypeData(BaseStruct):
    effectiveNodeTypes: List[str]
    blurNodeTypes: List[str]


class RoguelikeTotemBuffData(BaseStruct):
    totemId: str
    color: str
    pos: str
    rhythm: str
    normalDesc: str
    synergyDesc: str
    archiveDesc: str
    combineGroupName: str
    bgIconId: str
    isManual: bool
    linkedNodeTypeData: RoguelikeTotemLinkedNodeTypeData
    distanceMin: int
    distanceMax: int
    vertPassable: bool
    expandLength: int
    onlyForVert: bool
    portalLinkedNodeTypeData: RoguelikeTotemLinkedNodeTypeData


class RoguelikeTotemSubBuffData(BaseStruct):
    subBuffId: str
    name: str
    desc: str
    combinedDesc: str
    info: str


class RoguelikeTotemModuleConsts(BaseStruct):
    totemPredictDescription: str
    colorCombineDesc: Dict[str, str]
    bossCombineDesc: str
    battleNoPredictDescription: str
    shopNoGoodsDescription: str


class RoguelikeTotemBuffModuleData(RoguelikeModuleBaseData):
    totemBuffDatas: Dict[str, RoguelikeTotemBuffData]
    subBuffs: Dict[str, RoguelikeTotemSubBuffData]
    moduleConsts: RoguelikeTotemModuleConsts


class RoguelikeVisionData(BaseStruct):
    sightNum: int
    level: int
    canForesee: bool
    dividedDis: int
    status: str
    clr: str
    desc1: str
    desc2: str
    icon: str


class RoguelikeVisionModuleDataVisionChoiceConfig(BaseStruct):
    value: int
    type_: int = field(name='type')


class RoguelikeVisionModuleConsts(BaseStruct):
    maxVision: int
    totemBottomDescription: str
    chestBottomDescription: str
    goodsBottomDescription: str


class RoguelikeVisionModuleData(RoguelikeModuleBaseData):
    visionDatas: Dict[str, RoguelikeVisionData]
    visionChoices: Dict[str, RoguelikeVisionModuleDataVisionChoiceConfig]
    moduleConsts: RoguelikeVisionModuleConsts


class RoguelikeModule(BaseStruct):
    moduleTypes: List[str]
    sanCheck: Union[RoguelikeSanCheckModuleData, None]
    dice: Union[RoguelikeDiceModuleData, None]
    chaos: Union[RoguelikeChaosModuleData, None]
    totemBuff: Union[RoguelikeTotemBuffModuleData, None]
    vision: Union[RoguelikeVisionModuleData, None]


class RoguelikeTopicDisplayItem(BaseStruct):
    displayType: str
    displayNum: int
    displayForm: str
    tokenDesc: str
    sortId: int


class RoguelikeTopicDev(BaseStruct):
    buffId: str
    sortId: int
    nodeType: str
    nextNodeId: List[str]
    frontNodeId: List[str]
    tokenCost: int
    buffName: str
    buffIconId: str
    buffTypeName: str
    buffDisplayInfo: List[RoguelikeTopicDisplayItem]


class RoguelikeTopicDevToken(BaseStruct):
    sortId: int
    displayForm: str
    tokenDesc: str


class RL01EndingText(BaseStruct):
    summaryVariation: str
    summaryDefeatBoss: str
    summaryAccidentMeet: str
    summaryCapsule: str
    summaryActiveTool: str
    summaryActor: str
    summaryTop: str
    summaryZone: str
    summaryEnding: str
    summaryMode: str
    summaryGroup: str
    summarySupport: str
    summaryNormalRecruit: str
    summaryDirectRecruit: str
    summaryFriendRecruit: str
    summaryFreeRecruit: str
    summaryMonthRecruit: str
    summaryUpgrade: str
    summaryCompleteEnding: str
    summaryEachZone: str
    summaryPerfectBattle: str
    summaryMeetBattle: str
    summaryMeetEvent: str
    summaryMeetShop: str
    summaryMeetTreasure: str
    summaryBuy: str
    summaryInvest: str
    summaryGet: str
    summaryRelic: str
    summarySafeHouse: str
    summaryFailEnd: str


class RL01CustomizeData(BaseStruct):
    developments: Dict[str, RoguelikeTopicDev]
    developmentTokens: Dict[str, RoguelikeTopicDevToken]
    endingText: RL01EndingText


class RL02Development(BaseStruct):
    buffId: str
    nodeType: str
    frontNodeId: List[str]
    nextNodeId: List[str]
    positionP: int
    positionR: int
    tokenCost: int
    buffName: str
    buffIconId: str
    effectType: str
    rawDesc: str
    buffDisplayInfo: List[RoguelikeTopicDisplayItem]
    enrollId: Union[str, None]


class RL02DevRawTextBuffGroup(BaseStruct):
    nodeIdList: List[str]
    useLevelMark: bool
    groupIconId: str
    useUpBreak: bool
    sortId: int


class RL02DevelopmentLine(BaseStruct):
    fromNode: str
    toNode: str
    fromNodeP: int
    fromNodeR: int
    toNodeP: int
    toNodeR: int
    enrollId: Union[str, None]


class RL02EndingText(BaseStruct):
    summaryMutation: str
    summaryDice: str
    summaryDiceResultGood: str
    summaryDiceResultNormal: str
    summaryDiceResultBad: str
    summaryDiceResultDesc: str
    summaryCommuDesc: str
    summaryHiddenDesc: str
    summaryKnightDesc: str
    summaryGoldDesc: str
    summaryPracticeDesc: str
    summaryCommuEmptyDesc: str
    summaryCommuNotEmptyDesc: str
    summaryHiddenPassedDesc: str
    summaryHiddenNotPassedDesc: str
    summaryKnightPassedDesc: str
    summaryKnightNotPassedDesc: str
    summaryGoldThreshold: int
    summaryGoldHighDesc: str
    summaryGoldLowDesc: str
    summaryPracticeThreshold: int
    summaryPracticeHighDesc: str
    summaryPracticeLowDesc: str


class RL02CustomizeData(BaseStruct):
    developments: Dict[str, RL02Development]
    developmentTokens: Dict[str, RoguelikeTopicDevToken]
    developmentRawTextGroup: List[RL02DevRawTextBuffGroup]
    developmentLines: List[RL02DevelopmentLine]
    endingText: RL02EndingText


class RL03Development(BaseStruct):
    buffId: str
    nodeType: str
    frontNodeId: List[str]
    nextNodeId: List[str]
    positionRow: int
    positionOrder: int
    tokenCost: int
    buffName: str
    buffIconId: str
    effectType: str
    rawDesc: List[str]
    buffDisplayInfo: List[RoguelikeTopicDisplayItem]
    groupId: str
    enrollId: Union[str, None]


class RL03DevRawTextBuffGroup(BaseStruct):
    nodeIdList: List[str]
    useLevelMark: bool
    groupIconId: str
    sortId: int


class RL03DevDifficultyNodePairInfo(BaseStruct):
    frontNode: str
    nextNode: str


class RL03DevDifficultyNodeInfo(BaseStruct):
    buffId: str
    nodeMap: List[RL03DevDifficultyNodePairInfo]
    enableGrade: int


class RL03EndingText(BaseStruct):
    summaryGetTotem: str
    summaryDemoPointUp: str
    summaryDemoPointDown: str
    summaryDemoGradeUp: str
    summaryDemoGradeDown: str
    summaryVisionPointUp: str
    summaryVisionPointDown: str
    summaryVisionGradeUp: str
    summaryVisionGradeDown: str
    summaryMeetTrade: str
    summaryFightWin: str
    summaryFightFail: str
    summaryExchangeTotem: str
    summaryExchangeRelic: str
    summaryMeetSecretpath: str
    summaryUseTotem: str
    summaryVisionGrade: str
    summaryActor: str
    summaryTop: str
    summaryZone: str
    summaryEnding: str
    summaryMode: str
    summaryGroup: str
    summarySupport: str
    summaryNormalRecruit: str
    summaryDirectRecruit: str
    summaryFriendRecruit: str
    summaryFreeRecruit: str
    summaryMonthRecruit: str
    summaryUpgrade: str
    summaryCompleteEnding: str
    summaryEachZone: str
    summaryPerfectBattle: str
    summaryMeetBattle: str
    summaryMeetEvent: str
    summaryMeetShop: str
    summaryMeetTreasure: str
    summaryBuy: str
    summaryInvest: str
    summaryGet: str
    summaryRelic: str
    summarySafeHouse: str
    summaryFailEnd: str


class RL03DifficultyExt(BaseStruct):
    modeDifficulty: str
    grade: int
    totemProb: Union[int, float]
    relicDevLevel: str
    buffs: Union[List[str], None]
    buffDesc: List[str]


class RL03CustomizeData(BaseStruct):
    developments: Dict[str, RL03Development]
    developmentsTokens: Dict[str, RoguelikeTopicDevToken]
    developmentRawTextGroup: List[RL03DevRawTextBuffGroup]
    developmentsDifficultyNodeInfos: Dict[str, RL03DevDifficultyNodeInfo]
    endingText: RL03EndingText
    difficulties: List[RL03DifficultyExt]


class RoguelikeTopicCustomizeData(BaseStruct):
    rogue_1: RL01CustomizeData
    rogue_2: RL02CustomizeData
    rogue_3: RL03CustomizeData


class RoguelikeTopicTable(BaseStruct):
    __version__ = '23-04-23-15-07-53-24a81c'

    topics: Dict[str, RoguelikeTopicBasicData]
    constant: RoguelikeTopicConst
    details: Dict[str, RoguelikeTopicDetail]
    modules: Dict[str, RoguelikeModule]
    customizeData: RoguelikeTopicCustomizeData
