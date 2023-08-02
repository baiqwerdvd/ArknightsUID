from pydantic import BaseModel, Field


class RoguelikeTopicBasicDataHomeEntryDisplayData(BaseModel):
    topicId: str
    displayId: str
    startTs: int
    endTs: int


class RoguelikeTopicConfig(BaseModel):
    loadCharCardPlugin: bool | None = None
    webBusType: str
    monthChatTrigType: int
    loadRewardHpDecoPlugin: bool
    loadRewardExtraInfoPlugin: bool


class RoguelikeTopicBasicData(BaseModel):
    id_: str = Field(alias='id')
    name: str
    startTime: int
    disappearTimeOnMainScreen: int
    sort: int
    showMedalId: str
    medalGroupId: str
    fullStoredTime: int
    lineText: str
    homeEntryDisplayData: list[RoguelikeTopicBasicDataHomeEntryDisplayData]
    moduleTypes: list[str]
    config: RoguelikeTopicConfig


class RoguelikeTopicConstPredefinedChar(BaseModel):
    charId: str
    canBeFree: bool
    uniEquipId: str | None
    recruitType: str


class RoguelikeTopicConst(BaseModel):
    milestoneTokenRatio: int
    outerBuffTokenRatio: int | float
    relicTokenRatio: int
    rogueSystemUnlockStage: str
    ordiModeReOpenCoolDown: int
    monthModeReOpenCoolDown: int
    monthlyTaskUncompletedTime: int
    monthlyTaskManualRefreshLimit: int
    monthlyTeamUncompletedTime: int
    bpPurchaseSystemUnlockTime: int
    predefinedChars: dict[str, RoguelikeTopicConstPredefinedChar]


class RoguelikeTopicUpdate(BaseModel):
    updateId: str
    topicUpdateTime: int
    topicEndTime: int


class RoguelikeTopicEnroll(BaseModel):
    enrollId: str
    enrollTime: int


class RoguelikeTopicBP(BaseModel):
    id_: str = Field(alias='id')
    level: int
    tokenNum: int
    nextTokenNum: int
    itemID: str
    itemType: str
    itemCount: int
    isGoodPrize: bool
    isGrandPrize: bool


class RoguelikeTopicMilestoneUpdateData(BaseModel):
    updateTime: int
    endTime: int
    maxBpLevel: int
    maxBpCount: int
    maxDisplayBpCount: int


class RoguelikeTopicBPGrandPrize(BaseModel):
    grandPrizeDisplayId: str
    sortId: int
    displayUnlockYear: int
    displayUnlockMonth: int
    acquireTitle: str
    purchaseTitle: str
    displayName: str
    displayDiscription: str
    bpLevelId: str
    accordingCharId: str | None = None
    accordingSkinId: str | None = None
    detailAnnounceTime: str | None = None
    picIdAftrerUnlock: str | None = None


class RoguelikeTopicMonthMission(BaseModel):
    id_: str = Field(alias='id')
    taskName: str
    taskClass: str
    innerClassWeight: int
    template: str
    paramList: list[str]
    desc: str
    tokenRewardNum: int


class ItemBundle(BaseModel):
    id_: str = Field(alias='id')
    count: int
    type_: str = Field(alias='type')


class RoguelikeTopicMonthSquad(BaseModel):
    id_: str = Field(alias='id')
    teamName: str
    teamSubName: str | None
    teamFlavorDesc: str | None
    teamDes: str
    teamColor: str
    teamMonth: str
    teamYear: str
    teamIndex: str | None
    teamChars: list[str]
    zoneId: str | None
    chatId: str
    tokenRewardNum: int
    items: list[ItemBundle]
    startTime: int
    endTime: int
    taskDes: str | None


class RoguelikeTopicChallenge(BaseModel):
    challengeId: str
    sortId: int
    challengeName: str
    challengeGroup: int
    challengeGroupSortId: int
    challengeGroupName: str | None
    challengeUnlockDesc: str | None
    challengeUnlockToastDesc: str | None
    challengeDes: str
    challengeConditionDes: list[str]
    taskDes: str
    completionClass: str
    completionParams: list[str]
    rewards: list[ItemBundle]


class RoguelikeTopicDifficulty(BaseModel):
    modeDifficulty: str
    grade: int
    name: str
    subName: str | None
    enrollId: str | None
    haveInitialRelicIcon: bool
    scoreFactor: int | float
    canUnlockItem: bool
    doMonthTask: bool
    ruleDesc: str
    failTitle: str
    failImageId: str
    failForceDesc: str
    sortId: int
    equivalentGrade: int
    color: str | None
    bpValue: int
    bossValue: int
    addDesc: str | None
    isHard: bool
    unlockText: str | None
    displayIconId: str | None


class RoguelikeTopicBankReward(BaseModel):
    rewardId: str
    unlockGoldCnt: int
    rewardType: str
    desc: str


class ActArchiveRelicItemData(BaseModel):
    relicId: str
    relicSortId: int
    relicGroupId: int
    orderId: str
    isSpRelic: bool
    enrollId: str | None


class ActArchiveRelicData(BaseModel):
    relic: dict[str, ActArchiveRelicItemData]


class ActArchiveCapsuleItemData(BaseModel):
    capsuleId: str
    capsuleSortId: int
    englishName: str
    enrollId: str | None


class ActArchiveCapsuleData(BaseModel):
    capsule: dict[str, ActArchiveCapsuleItemData]


class ActArchiveTrapItemData(BaseModel):
    trapId: str
    trapSortId: int
    orderId: str
    enrollId: str | None


class ActArchiveTrapData(BaseModel):
    trap: dict[str, ActArchiveTrapItemData]


class ActArchiveChatItemData(BaseModel):
    chatFloor: int
    chatDesc: str | None
    chatStoryId: str


class ActArchiveChatGroupData(BaseModel):
    sortId: int
    numChat: int
    clientChatItemData: list[ActArchiveChatItemData]


class ActArchiveChatData(BaseModel):
    chat: dict[str, ActArchiveChatGroupData]


class ActArchiveEndbookItemData(BaseModel):
    endBookId: str
    sortId: int
    enrollId: str | None = None
    isLast: bool | None = None
    endbookName: str
    unlockDesc: str
    textId: str


class ActArchiveEndbookGroupData(BaseModel):
    endId: str
    endingId: str
    sortId: int
    title: str
    cgId: str
    backBlurId: str
    cardId: str
    hasAvg: bool
    avgId: str
    clientEndbookItemDatas: list[ActArchiveEndbookItemData]


class ActArchiveEndbookData(BaseModel):
    endbook: dict[str, ActArchiveEndbookGroupData]


class ActArchiveBuffItemData(BaseModel):
    buffId: str
    buffGroupIndex: int
    innerSortId: int
    name: str
    iconId: str
    usage: str
    desc: str
    color: str


class ActArchiveBuffData(BaseModel):
    buff: dict[str, ActArchiveBuffItemData]


class ActArchiveTotemItemData(BaseModel):
    id_: str = Field(alias='id')
    type_: int = Field(alias='type')
    enrollConditionId: str | None
    sortId: int


class ActArchiveTotemData(BaseModel):
    totem: dict[str, ActArchiveTotemItemData]


class ActArchiveChaosItemData(BaseModel):
    id_: str = Field(alias='id')
    isHidden: bool
    enrollId: str | None
    sortId: int


class ActArchiveChaosData(BaseModel):
    chaos: dict[str, ActArchiveChaosItemData]


class RoguelikeArchiveComponentData(BaseModel):
    relic: ActArchiveRelicData
    capsule: ActArchiveCapsuleData | None
    trap: ActArchiveTrapData
    chat: ActArchiveChatData
    endbook: ActArchiveEndbookData
    buff: ActArchiveBuffData
    totem: ActArchiveTotemData | None
    chaos: ActArchiveChaosData | None


class RoguelikeArchiveUnlockCondDesc(BaseModel):
    archiveType: str
    description: str


class RoguelikeArchiveEnroll(BaseModel):
    archiveType: str
    enrollId: str | None


class RoguelikeArchiveUnlockCondData(BaseModel):
    unlockCondDesc: dict[str, RoguelikeArchiveUnlockCondDesc]
    enroll: dict[str, RoguelikeArchiveEnroll]


class RoguelikeTopicDetailConstPlayerLevelData(BaseModel):
    exp: int
    populationUp: int
    squadCapacityUp: int
    battleCharLimitUp: int
    maxHpUp: int


class RoguelikeTopicDetailConstCharUpgradeData(BaseModel):
    evolvePhase: int
    skillLevel: int
    skillSpecializeLevel: int


class RoguelikeTopicDetailConst(BaseModel):
    playerLevelTable: dict[str, RoguelikeTopicDetailConstPlayerLevelData]
    charUpgradeTable: dict[str, RoguelikeTopicDetailConstCharUpgradeData]
    difficultyUpgradeRelicDescTable: dict[str, str]
    tokenBpId: str
    tokenOuterBuffId: str
    previewedRewardsAccordingUpdateId: str
    tipButtonName: str
    collectButtonName: str
    bpSystemName: str
    autoSetKV: str
    bpPurchaseActiveEnroll: str
    defaultSacrificeDesc: str | None
    defaultExpeditionSelectDesc: str | None
    gotCharBuffToast: str | None
    gotSquadBuffToast: str | None
    loseCharBuffToast: str | None
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


class RoguelikeGameInitData(BaseModel):
    modeId: str
    modeGrade: int
    predefinedId: str | None
    initialBandRelic: list[str]
    initialRecruitGroup: list[str] | None
    initialHp: int
    initialPopulation: int
    initialGold: int
    initialSquadCapacity: int
    initialShield: int
    initialMaxHp: int
    initialKey: int


class RoguelikeGameStageData(BaseModel):
    id_: str = Field(alias='id')
    linkedStageId: str
    levelId: str
    code: str
    name: str
    loadingPicId: str
    description: str
    eliteDesc: str | None
    isBoss: int
    isElite: int
    difficulty: str
    capsulePool: str | None
    capsuleProb: int | float
    vutresProb: list[float]
    boxProb: list[float]
    specialNodeId: str | None = None


class RoguelikeGameZoneData(BaseModel):
    id_: str = Field(alias='id')
    name: str
    clockPerformance: str | None
    displayTime: str | None
    description: str
    endingDescription: str
    backgroundId: str
    zoneIconId: str
    isHiddenZone: bool


class RoguelikeZoneVariationData(BaseModel):
    pass


class RoguelikeGameTrapData(BaseModel):
    itemId: str
    trapId: str
    trapDesc: str


class RoguelikeGameRecruitTicketData(BaseModel):
    id_: str = Field(alias='id')
    profession: int
    rarity: int
    professionList: list[str]
    rarityList: list[int]
    extraEliteNum: int
    extraFreeRarity: list[int]
    extraCharIds: list[str]


class RoguelikeGameUpgradeTicketData(BaseModel):
    id_: str = Field(alias='id')
    profession: int
    rarity: int
    professionList: list[str]
    rarityList: list[int]


class RoguelikeGameCustomTicketData(BaseModel):
    id_: str = Field(alias='id')
    subType: str
    discardText: str


class Blackboard(BaseModel):
    key: str
    value: int | float | None = None
    valueStr: str | None = None


class RoguelikeBuff(BaseModel):
    key: str
    blackboard: list[Blackboard]


class RoguelikeGameRelicData(BaseModel):
    id_: str = Field(alias='id')
    buffs: list[RoguelikeBuff]


class RoguelikeGameRelicCheckParam(BaseModel):
    valueProfessionMask: int
    valueStrs: list[str] | None
    valueInt: int


class RoguelikeGameRelicParamData(BaseModel):
    id_: str = Field(alias='id')
    checkCharBoxTypes: list[str]
    checkCharBoxParams: list[RoguelikeGameRelicCheckParam]


class RoguelikeGameRecruitGrpData(BaseModel):
    id_: str = Field(alias='id')
    iconId: str
    name: str
    desc: str
    unlockDesc: str | None


class RoguelikeChoiceDisplayData(BaseModel):
    type_: str = Field(alias='type')
    costHintType: int | None = None
    effectHintType: int | None = None
    funcIconId: str | None
    itemId: str | None
    difficultyUpgradeRelicGroupId: str | None = None
    taskId: str | None


class RoguelikeGameChoiceData(BaseModel):
    id_: str = Field(alias='id')
    title: str
    description: str | None
    lockedCoverDesc: str | None
    type_: str = Field(alias='type')
    leftDecoType: str
    nextSceneId: str | None
    icon: str | None
    displayData: RoguelikeChoiceDisplayData
    forceShowWhenOnlyLeave: bool


class RoguelikeGameChoiceSceneData(BaseModel):
    id_: str = Field(alias='id')
    title: str
    description: str
    background: str | None
    titleIcon: str | None
    subTypeId: int
    useHiddenMusic: bool


class RoguelikeGameNodeTypeData(BaseModel):
    name: str
    description: str


class RoguelikeGameNodeSubTypeData(BaseModel):
    eventType: str
    subTypeId: int
    iconId: str
    name: str | None
    description: str


class RoguelikeGameVariationData(BaseModel):
    id_: str = Field(alias='id')
    type_: str = Field(alias='type')
    outerName: str
    innerName: str
    functionDesc: str
    desc: str
    iconId: str | None
    sound: str | None


class RoguelikeGameCharBuffData(BaseModel):
    id_: str = Field(alias='id')
    iconId: str
    outerName: str
    innerName: str
    functionDesc: str
    desc: str
    buffs: list[RoguelikeBuff]


class RoguelikeGameSquadBuffData(BaseModel):
    id_: str = Field(alias='id')
    iconId: str
    outerName: str
    innerName: str
    functionDesc: str
    desc: str
    buffs: list[RoguelikeBuff]


class RoguelikeTaskData(BaseModel):
    taskId: str
    taskName: str
    taskDesc: str
    rewardSceneId: str
    taskRarity: str


class RoguelikeGameConst(BaseModel):
    initSceneName: str
    failSceneName: str
    hpItemId: str
    goldItemId: str
    populationItemId: str
    squadCapacityItemId: str
    expItemId: str
    bankMaxGold: int
    bankCostId: str | None
    bankDrawCount: int
    bankDrawLimit: int
    mimicEnemyIds: list[str]
    bossIds: list[str]
    goldChestTrapId: str
    normBoxTrapId: str | None
    rareBoxTrapId: str | None
    badBoxTrapId: str | None
    maxHpItemId: str | None
    shieldItemId: str | None
    keyItemId: str | None
    chestKeyCnt: int
    chestKeyItemId: str | None
    keyColorId: str | None
    onceNodeTypeList: list[str]
    gpScoreRatio: int
    overflowUsageSquadBuff: str | None
    specialTrapId: str | None
    trapRewardRelicId: str | None
    unlockRouteItemId: str | None
    hideBattleNodeName: str | None
    hideBattleNodeDescription: str | None
    hideNonBattleNodeName: str | None
    hideNonBattleNodeDescription: str | None
    charSelectExpeditionConflictToast: str | None
    itemDropTagDict: dict[str, str]
    expeditionReturnDescCureUpgrade: str | None
    expeditionReturnDescUpgrade: str | None
    expeditionReturnDescCure: str | None
    expeditionReturnDesc: str | None
    expeditionReturnDescItem: str | None
    expeditionReturnRewardBlackList: list[str]
    gainBuffDiffGrade: int
    dsPredictTips: str | None
    dsBuffActiveTips: str | None
    totemDesc: str | None
    relicDesc: str | None
    buffDesc: str | None
    portalZones: list[str]


class RoguelikeTopicCapsule(BaseModel):
    itemId: str
    maskType: str
    innerColor: str


class RoguelikeGameEndingDataLevelIcon(BaseModel):
    level: int
    iconId: str


class RoguelikeGameEndingData(BaseModel):
    id_: str = Field(alias='id')
    familyId: int
    name: str
    desc: str
    bgId: str
    icons: list[RoguelikeGameEndingDataLevelIcon]
    priority: int
    changeEndingDesc: str | None
    bossIconId: str | None


class RoguelikeBattleSummeryDescriptionData(BaseModel):
    randomDescriptionList: list[str]


class TipData(BaseModel):
    tip: str
    weight: int | float
    category: str


class RoguelikeGameItemData(BaseModel):
    id_: str = Field(alias='id')
    name: str
    description: str | None
    usage: str
    obtainApproach: str
    iconId: str
    type_: str = Field(alias='type')
    subType: str
    rarity: str
    value: int
    sortId: int
    canSacrifice: bool
    unlockCondDesc: str | None


class RoguelikeBandRefData(BaseModel):
    itemId: str
    iconId: str
    description: str
    bandLevel: int
    normalBandId: str


class RoguelikeEndingDetailText(BaseModel):
    textId: str
    text: str
    eventType: str
    showType: int
    choiceSceneId: str | None
    paramList: list[str]
    otherPara1: str | None


class RoguelikeGameTreasureData(BaseModel):
    treasureId: str
    groupId: str
    subIndex: int
    name: str
    usage: str


class RoguelikeDifficultyUpgradeRelicData(BaseModel):
    relicId: str
    equivalentGrade: int


class RoguelikeDifficultyUpgradeRelicGroupData(BaseModel):
    relicData: list[RoguelikeDifficultyUpgradeRelicData]


class RoguelikeTopicDetail(BaseModel):
    updates: list[RoguelikeTopicUpdate]
    enrolls: dict[str, RoguelikeTopicEnroll]
    milestones: list[RoguelikeTopicBP]
    milestoneUpdates: list[RoguelikeTopicMilestoneUpdateData]
    grandPrizes: list[RoguelikeTopicBPGrandPrize]
    monthMission: list[RoguelikeTopicMonthMission]
    monthSquad: dict[str, RoguelikeTopicMonthSquad]
    challenges: dict[str, RoguelikeTopicChallenge]
    difficulties: list[RoguelikeTopicDifficulty]
    bankRewards: list[RoguelikeTopicBankReward]
    archiveComp: RoguelikeArchiveComponentData
    archiveUnlockCond: RoguelikeArchiveUnlockCondData
    detailConst: RoguelikeTopicDetailConst
    init: list[RoguelikeGameInitData]
    stages: dict[str, RoguelikeGameStageData]
    zones: dict[str, RoguelikeGameZoneData]
    variation: dict[str, RoguelikeZoneVariationData]
    traps: dict[str, RoguelikeGameTrapData]
    recruitTickets: dict[str, RoguelikeGameRecruitTicketData]
    upgradeTickets: dict[str, RoguelikeGameUpgradeTicketData]
    customTickets: dict[str, RoguelikeGameCustomTicketData]
    relics: dict[str, RoguelikeGameRelicData]
    relicParams: dict[str, RoguelikeGameRelicParamData]
    recruitGrps: dict[str, RoguelikeGameRecruitGrpData]
    choices: dict[str, RoguelikeGameChoiceData]
    choiceScenes: dict[str, RoguelikeGameChoiceSceneData]
    nodeTypeData: dict[str, RoguelikeGameNodeTypeData]
    subTypeData: list[RoguelikeGameNodeSubTypeData]
    variationData: dict[str, RoguelikeGameVariationData]
    charBuffData: dict[str, RoguelikeGameCharBuffData]
    squadBuffData: dict[str, RoguelikeGameSquadBuffData]
    taskData: dict[str, RoguelikeTaskData]
    gameConst: RoguelikeGameConst
    shopDialogs: dict[str, list[str]]
    capsuleDict: dict[str, RoguelikeTopicCapsule] | None
    endings: dict[str, RoguelikeGameEndingData]
    battleSummeryDescriptions: dict[str, RoguelikeBattleSummeryDescriptionData]
    battleLoadingTips: list[TipData]
    items: dict[str, RoguelikeGameItemData]
    bandRef: dict[str, RoguelikeBandRefData]
    endingDetailList: list[RoguelikeEndingDetailText]
    treasures: dict[str, list[RoguelikeGameTreasureData]]
    difficultyUpgradeRelicGroups: dict[str, RoguelikeDifficultyUpgradeRelicGroupData]


class RoguelikeModuleBaseData(BaseModel):
    moduleType: str


class RoguelikeSanRangeData(BaseModel):
    sanMax: int
    diceGroupId: str
    description: str
    sanDungeonEffect: str
    sanEffectRank: str
    sanEndingDesc: str | None


class RoguelikeSanCheckConsts(BaseModel):
    sanDecreaseToast: str


class RoguelikeSanCheckModuleData(RoguelikeModuleBaseData):
    sanRanges: list[RoguelikeSanRangeData]
    moduleConsts: RoguelikeSanCheckConsts


class RoguelikeDiceData(BaseModel):
    diceId: str
    description: str
    isUpgradeDice: int
    upgradeDiceId: str | None
    diceFaceCount: int
    battleDiceId: str


class RoguelikeDiceRuleData(BaseModel):
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


class RoguelikeDiceRuleGroupData(BaseModel):
    ruleGroupId: str
    minGoodNum: int


class RoguelikeDicePredefineData(BaseModel):
    modeId: str
    modeGrade: int
    predefinedId: str | None
    initialDiceCount: int


class RoguelikeDiceModuleData(RoguelikeModuleBaseData):
    dice: dict[str, RoguelikeDiceData]
    diceEvents: dict[str, RoguelikeDiceRuleData]
    diceChoices: dict[str, str]
    diceRuleGroups: dict[str, RoguelikeDiceRuleGroupData]
    dicePredefines: list[RoguelikeDicePredefineData]


class RoguelikeChaosData(BaseModel):
    chaosId: str
    level: int
    nextChaosId: str | None
    prevChaosId: str | None
    iconId: str
    name: str
    functionDesc: str
    desc: str
    sound: str
    sortId: int


class RoguelikeChaosRangeData(BaseModel):
    chaosMax: int
    chaosDungeonEffect: str


class RoguelikeChaosPredefineLevelInfo(BaseModel):
    chaosLevelBeginNum: int
    chaosLevelEndNum: int


class RoguelikeChaosModuleConsts(BaseModel):
    maxChaosLevel: int
    maxChaosSlot: int
    chaosNotMaxDescription: str
    chaosMaxDescription: str
    chaosPredictDescription: str


class RoguelikeChaosModuleData(RoguelikeModuleBaseData):
    chaosDatas: dict[str, RoguelikeChaosData]
    chaosRanges: list[RoguelikeChaosRangeData]
    levelInfoDict: dict[str, dict[str, RoguelikeChaosPredefineLevelInfo]]
    moduleConsts: RoguelikeChaosModuleConsts


class RoguelikeTotemLinkedNodeTypeData(BaseModel):
    effectiveNodeTypes: list[str]
    blurNodeTypes: list[str]


class RoguelikeTotemBuffData(BaseModel):
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


class RoguelikeTotemSubBuffData(BaseModel):
    subBuffId: str
    name: str
    desc: str
    combinedDesc: str
    info: str


class RoguelikeTotemModuleConsts(BaseModel):
    totemPredictDescription: str
    colorCombineDesc: dict[str, str]
    bossCombineDesc: str
    battleNoPredictDescription: str
    shopNoGoodsDescription: str


class RoguelikeTotemBuffModuleData(RoguelikeModuleBaseData):
    totemBuffDatas: dict[str, RoguelikeTotemBuffData]
    subBuffs: dict[str, RoguelikeTotemSubBuffData]
    moduleConsts: RoguelikeTotemModuleConsts


class RoguelikeVisionData(BaseModel):
    sightNum: int
    level: int
    canForesee: bool
    dividedDis: int
    status: str
    clr: str
    desc1: str
    desc2: str
    icon: str


class RoguelikeVisionModuleDataVisionChoiceConfig(BaseModel):
    value: int
    type_: int = Field(alias='type')


class RoguelikeVisionModuleConsts(BaseModel):
    maxVision: int
    totemBottomDescription: str
    chestBottomDescription: str
    goodsBottomDescription: str


class RoguelikeVisionModuleData(RoguelikeModuleBaseData):
    visionDatas: dict[str, RoguelikeVisionData]
    visionChoices: dict[str, RoguelikeVisionModuleDataVisionChoiceConfig]
    moduleConsts: RoguelikeVisionModuleConsts


class RoguelikeModule(BaseModel):
    moduleTypes: list[str]
    sanCheck: RoguelikeSanCheckModuleData | None
    dice: RoguelikeDiceModuleData | None
    chaos: RoguelikeChaosModuleData | None
    totemBuff: RoguelikeTotemBuffModuleData | None
    vision: RoguelikeVisionModuleData | None


class RoguelikeTopicDisplayItem(BaseModel):
    displayType: str
    displayNum: int
    displayForm: str
    tokenDesc: str
    sortId: int


class RoguelikeTopicDev(BaseModel):
    buffId: str
    sortId: int
    nodeType: str
    nextNodeId: list[str]
    frontNodeId: list[str]
    tokenCost: int
    buffName: str
    buffIconId: str
    buffTypeName: str
    buffDisplayInfo: list[RoguelikeTopicDisplayItem]


class RoguelikeTopicDevToken(BaseModel):
    sortId: int
    displayForm: str
    tokenDesc: str


class RL01EndingText(BaseModel):
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


class RL01CustomizeData(BaseModel):
    developments: dict[str, RoguelikeTopicDev]
    developmentTokens: dict[str, RoguelikeTopicDevToken]
    endingText: RL01EndingText


class RL02Development(BaseModel):
    buffId: str
    nodeType: str
    frontNodeId: list[str]
    nextNodeId: list[str]
    positionP: int
    positionR: int
    tokenCost: int
    buffName: str
    buffIconId: str
    effectType: str
    rawDesc: str
    buffDisplayInfo: list[RoguelikeTopicDisplayItem]
    enrollId: str | None


class RL02DevRawTextBuffGroup(BaseModel):
    nodeIdList: list[str]
    useLevelMark: bool
    groupIconId: str
    useUpBreak: bool
    sortId: int


class RL02DevelopmentLine(BaseModel):
    fromNode: str
    toNode: str
    fromNodeP: int
    fromNodeR: int
    toNodeP: int
    toNodeR: int
    enrollId: str | None


class RL02EndingText(BaseModel):
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


class RL02CustomizeData(BaseModel):
    developments: dict[str, RL02Development]
    developmentTokens: dict[str, RoguelikeTopicDevToken]
    developmentRawTextGroup: list[RL02DevRawTextBuffGroup]
    developmentLines: list[RL02DevelopmentLine]
    endingText: RL02EndingText


class RL03Development(BaseModel):
    buffId: str
    nodeType: str
    frontNodeId: list[str]
    nextNodeId: list[str]
    positionRow: int
    positionOrder: int
    tokenCost: int
    buffName: str
    buffIconId: str
    effectType: str
    rawDesc: list[str]
    buffDisplayInfo: list[RoguelikeTopicDisplayItem]
    groupId: str
    enrollId: str | None


class RL03DevRawTextBuffGroup(BaseModel):
    nodeIdList: list[str]
    useLevelMark: bool
    groupIconId: str
    sortId: int


class RL03DevDifficultyNodePairInfo(BaseModel):
    frontNode: str
    nextNode: str


class RL03DevDifficultyNodeInfo(BaseModel):
    buffId: str
    nodeMap: list[RL03DevDifficultyNodePairInfo]
    enableGrade: int


class RL03EndingText(BaseModel):
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


class RL03DifficultyExt(BaseModel):
    modeDifficulty: str
    grade: int
    totemProb: int | float
    relicDevLevel: str
    buffs: list[str] | None
    buffDesc: list[str]


class RL03CustomizeData(BaseModel):
    developments: dict[str, RL03Development]
    developmentsTokens: dict[str, RoguelikeTopicDevToken]
    developmentRawTextGroup: list[RL03DevRawTextBuffGroup]
    developmentsDifficultyNodeInfos: dict[str, RL03DevDifficultyNodeInfo]
    endingText: RL03EndingText
    difficulties: list[RL03DifficultyExt]


class RoguelikeTopicCustomizeData(BaseModel):
    rogue_1: RL01CustomizeData
    rogue_2: RL02CustomizeData
    rogue_3: RL03CustomizeData | None = None


class RoguelikeTopicTable(BaseModel):
    __version__ = '23-04-23-15-07-53-24a81c'

    topics: dict[str, RoguelikeTopicBasicData]
    constant: RoguelikeTopicConst
    details: dict[str, RoguelikeTopicDetail]
    modules: dict[str, RoguelikeModule]
    customizeData: RoguelikeTopicCustomizeData

    class Config:
        extra = 'allow'
