from typing import Dict, List, Union

from msgspec import field

from ..common import BaseStruct


class ItemBundle(BaseStruct):
    id_: str = field(name="id")
    count: int
    type_: str = field(name="type")


class GameDataConstsCharAssistRefreshTimeState(BaseStruct):
    Hour: int
    Minute: int


class TermDescriptionData(BaseStruct):
    termId: str
    termName: str
    description: str


class GamedataConst(BaseStruct):
    __version__ = "24-02-02-10-18-07-831ad8"

    addedRewardDisplayZone: str
    advancedGachaCrystalCost: int
    announceWebBusType: str
    apBuyCost: int
    apBuyThreshold: int
    assistBeUsedSocialPt: Dict[str, int]
    attackMax: float
    baseMaxFriendNum: int
    buyApTimeNoLimitFlag: bool
    characterExpMap: List[List[int]]
    characterUpgradeCostMap: List[List[int]]
    charAssistRefreshTime: List[GameDataConstsCharAssistRefreshTimeState]
    charmEquipCount: int
    commonPotentialLvlUpCount: int
    completeCrystalBonus: int
    completeGainBonus: float
    continuousActionOpen: bool
    creditLimit: int
    dataVersion: str
    defaultMinContinuousBattleTimes: int
    defaultMaxContinuousBattleTimes: int
    defCDPrimColor: str
    defCDSecColor: str
    defMax: float
    diamondMaterialToShardExchangeRatio: int
    diamondToShdRate: int
    easyCrystalBonus: int
    evolveGoldCost: List[List[int]]
    friendAssistRarityLimit: List[int]
    hardDiamondDrop: int
    hpMax: float
    initCampaignTotalFee: int
    initCharIdList: List[str]
    initPlayerDiamondShard: int
    initPlayerGold: int
    initRecruitTagList: List[int]
    instFinDmdShdCost: int
    isClassicGachaPoolFuncEnabled: bool
    isClassicPotentialItemFuncEnabled: bool
    isClassicQCShopEnabled: bool
    isDynIllustEnabled: bool
    isDynIllustStartEnabled: bool
    isLMGTSEnabled: bool
    isSandboxPermFuncEnabled: bool
    isRoguelikeAvgAchieveFuncEnabled: bool
    isRoguelikeTopicFuncEnabled: bool
    legacyItemList: List[ItemBundle]
    legacyTime: int
    lMTGSDescConstOne: str
    lMTGSDescConstTwo: str
    LMTGSToEPGSRatio: int
    mailBannerType: List[str]
    mainlineCompatibleDesc: str
    mainlineEasyDesc: str
    mainlineNormalDesc: str
    mainlineToughDesc: str
    maxLevel: List[List[int]]
    maxPlayerLevel: int
    maxPracticeTicket: int
    monthlySubRemainTimeLimitDays: int
    monthlySubWarningTime: int
    multiInComeByRank: List[str]
    newBeeGiftEPGS: int
    normalGachaUnlockPrice: List[int]
    normalRecruitLockedString: List[str]
    playerApMap: List[int]
    playerApRegenSpeed: int
    playerExpMap: List[int]
    pullForces: List[float]
    pullForceZeroIndex: int
    pushForces: List[float]
    pushForceZeroIndex: int
    recruitPoolVersion: int
    rejectSpCharMission: int
    reMax: float
    replicateShopStartTime: int
    requestSameFriendCD: int
    resPrefVersion: str
    richTextStyles: Dict[str, str]
    storyReviewUnlockItemLackTip: str
    termDescriptionDict: Dict[str, TermDescriptionData]
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
    classicProtectChar: List[str]
    isVoucherClassicItemDistinguishable: Union[bool, None] = None
    operatorRecordsStartTime: Union[int, None] = None
    subProfessionDamageTypePairs: Union[Dict[str, int], None] = None
    crisisUnlockStage: Union[str, None] = None  # Removed in 2.1.21
