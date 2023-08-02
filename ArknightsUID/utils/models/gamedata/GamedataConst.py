from pydantic import BaseModel, Field


class ItemBundle(BaseModel):
    id_: str = Field(alias='id')
    count: int
    type_: str = Field(alias='type')


class GameDataConstsCharAssistRefreshTimeState(BaseModel):
    Hour: int
    Minute: int


class TermDescriptionData(BaseModel):
    termId: str
    termName: str
    description: str


class GamedataConst(BaseModel):
    __version__ = '23-07-27-18-50-06-aeb568'

    addedRewardDisplayZone: str
    advancedGachaCrystalCost: int
    announceWebBusType: str
    apBuyCost: int
    apBuyThreshold: int
    assistBeUsedSocialPt: dict[str, int]
    attackMax: float
    baseMaxFriendNum: int
    buyApTimeNoLimitFlag: bool
    characterExpMap: list[list[int]]
    characterUpgradeCostMap: list[list[int]]
    charAssistRefreshTime: list[GameDataConstsCharAssistRefreshTimeState]
    charmEquipCount: int
    commonPotentialLvlUpCount: int
    completeCrystalBonus: int
    completeGainBonus: float
    creditLimit: int
    crisisUnlockStage: str
    dataVersion: str
    defCDPrimColor: str
    defCDSecColor: str
    defMax: float
    diamondMaterialToShardExchangeRatio: int
    diamondToShdRate: int
    easyCrystalBonus: int
    evolveGoldCost: list[list[int]]
    friendAssistRarityLimit: list[int]
    hardDiamondDrop: int
    hpMax: float
    initCampaignTotalFee: int
    initCharIdList: list[str]
    initPlayerDiamondShard: int
    initPlayerGold: int
    initRecruitTagList: list[int]
    instFinDmdShdCost: int
    isClassicGachaPoolFuncEnabled: bool
    isClassicPotentialItemFuncEnabled: bool
    isClassicQCShopEnabled: bool
    isDynIllustEnabled: bool
    isDynIllustStartEnabled: bool
    isLMGTSEnabled: bool
    isRoguelikeAvgAchieveFuncEnabled: bool
    isRoguelikeTopicFuncEnabled: bool
    isVoucherClassicItemDistinguishable: bool | None = None
    legacyItemList: list[ItemBundle]
    legacyTime: int
    lMTGSDescConstOne: str
    lMTGSDescConstTwo: str
    LMTGSToEPGSRatio: int
    mailBannerType: list[str]
    mainlineCompatibleDesc: str
    mainlineEasyDesc: str
    mainlineNormalDesc: str
    mainlineToughDesc: str
    maxLevel: list[list[int]]
    maxPlayerLevel: int
    maxPracticeTicket: int
    monthlySubRemainTimeLimitDays: int
    monthlySubWarningTime: int
    multiInComeByRank: list[str]
    newBeeGiftEPGS: int
    normalGachaUnlockPrice: list[int]
    normalRecruitLockedString: list[str]
    operatorRecordsStartTime: int | None = None
    playerApMap: list[int]
    playerApRegenSpeed: int
    playerExpMap: list[int]
    pullForces: list[float]
    pullForceZeroIndex: int
    pushForces: list[float]
    pushForceZeroIndex: int
    recruitPoolVersion: int
    rejectSpCharMission: int
    reMax: float
    replicateShopStartTime: int
    requestSameFriendCD: int
    resPrefVersion: str
    richTextStyles: dict[str, str]
    storyReviewUnlockItemLackTip: str
    subProfessionDamageTypePairs: dict[str, int] | None = None
    termDescriptionDict: dict[str, TermDescriptionData]
    UnlimitSkinOutOfTime: int
    useAssistSocialPt: int
    useAssistSocialPtMaxCount: int
    v006RecruitTimeStep1Refresh: int
    v006RecruitTimeStep2Check: int
    v006RecruitTimeStep2Flush: int
    voucherDiv: int
    voucherSkinDesc: str
    voucherSkinRedeem: int
    weeklyOverrideDesc: str
    TSO: int

    class Config:
        extra = 'allow'
