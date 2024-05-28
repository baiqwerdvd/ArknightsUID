from enum import Enum

# from typing_extensions import TypeAlias
from typing import Any, Dict, List, Union

from msgspec import Struct, field


class StrEnum(str, Enum):
    pass


class RuleType(StrEnum):
    NEWBEE = "NEWBEE"
    NORMAL = "NORMAL"
    ATTAIN = "ATTAIN"
    CLASSIC_ATTAIN = "CLASSIC_ATTAIN"
    LINKAGE = "LINKAGE"
    SINGLE = "SINGLE"
    LIMITED = "LIMITED"
    CLASSIC = "CLASSIC"
    FESCLASSIC = "FESCLASSIC"


class LinkageRuleType(StrEnum):
    LINKAGE_R6_01 = "LINKAGE_R6_01"
    LINKAGE_MH_01 = "LINKAGE_MH_01"


class GachaPerAvail(Struct):
    rarityRank: int
    charIdList: List[str]
    totalPercent: float


class GachaAvailChar(Struct):
    perAvailList: List[GachaPerAvail]


class GachaPerChar(Struct):
    rarityRank: int
    charIdList: List[str]
    percent: float
    count: int


class GachaUpChar(Struct):
    perCharList: List[GachaPerChar]


class GachaWeightUpChar(Struct):
    rarityRank: int
    charId: str
    weight: int


class GachaObject(Struct):
    gachaObject: str
    type_: int = field(name="type")
    imageType: int
    param: Union[str, None]


class GachaGroupObject(Struct):
    groupType: int
    startIndex: int
    endIndex: int


class GachaDetailInfo(Struct):
    availCharInfo: GachaAvailChar
    upCharInfo: Union[GachaUpChar, None]
    weightUpCharInfoList: Union[List[GachaWeightUpChar], None]
    limitedChar: Union[List[str], None]
    gachaObjList: List[GachaObject]
    gachaObjGroups: Union[List[GachaGroupObject], None]


class GachaDetailTable(Struct):
    details: Dict[str, GachaDetailInfo]


class GachaDataLinkageTenGachaTkt(Struct):
    itemId: str
    endTime: int
    gachaPoolId: str


class GachaDataLimitTenGachaTkt(Struct):
    itemId: str
    endTime: int


class GachaDataFreeLimitGachaData(Struct):
    poolId: str
    openTime: int
    endTime: int
    freeCount: int


class GachaDataCarouselData(Struct):
    poolId: str
    index: int
    startTime: int
    endTime: int
    spriteId: str


class ItemBundle(Struct):
    id_: str = field(name="id")
    count: int
    type_: str = field(name="type")


class GachaDataRecruitRange(Struct):
    rarityStart: int
    rarityEnd: int


class PotentialMaterialConverterConfig(Struct):
    items: Dict[str, ItemBundle]


class RecruitPoolRecruitTime(Struct):
    timeLength: int
    recruitPrice: int
    accumRate: Union[float, None] = None


class RecruitConstantsData(Struct):
    tagPriceList: Dict[str, int]
    maxRecruitTime: int
    rarityWeights: None = None
    recruitTimeFactorList: None = None


class RecruitPool(Struct):
    recruitTimeTable: List[RecruitPoolRecruitTime]
    recruitConstants: RecruitConstantsData
    recruitCharacterList: None = None
    maskTypeWeightTable: None = None


class NewbeeGachaPoolClientData(Struct):
    gachaPoolId: str
    gachaIndex: int
    gachaPoolName: str
    gachaPoolDetail: str
    gachaPrice: int
    gachaTimes: int
    gachaOffset: Union[str, None] = None
    firstOpenDay: Union[int, None] = None
    reOpenDay: Union[int, None] = None
    gachaPoolItems: None = None
    signUpEarliestTime: Union[int, None] = None


class GachaPoolClientData(Struct):
    CDPrimColor: Union[str, None]
    CDSecColor: Union[str, None]
    endTime: int
    gachaIndex: int
    gachaPoolDetail: Union[str, None]
    gachaPoolId: str
    gachaPoolName: str
    gachaPoolSummary: str
    gachaRuleType: str
    guarantee5Avail: int
    guarantee5Count: int
    LMTGSID: Union[str, None]
    openTime: int
    dynMeta: Union[Dict[str, Any], None] = None
    linkageParam: Union[Dict[str, Any], None] = None
    linkageRuleId: Union[str, None] = None


class GachaTag(Struct):
    tagId: int
    tagName: str
    tagGroup: int


class SpecialRecruitPoolSpecialRecruitCostData(Struct):
    itemCosts: ItemBundle
    recruitPrice: int
    timeLength: int


class SpecialRecruitPool(Struct):
    endDateTime: int
    order: int
    recruitId: str
    recruitTimeTable: List[SpecialRecruitPoolSpecialRecruitCostData]
    startDateTime: int
    tagId: int
    tagName: str
    CDPrimColor: Union[str, None]
    CDSecColor: Union[str, None]
    LMTGSID: Union[str, None]
    gachaRuleType: str


class GachaDataFesGachaPoolRelateItem(Struct):
    rarityRank5ItemId: str
    rarityRank6ItemId: str


class GachaTable(Struct):
    __version__ = "24-03-29-14-33-44-5002d2"

    gachaTags: List[GachaTag]
    carousel: List[GachaDataCarouselData]
    classicPotentialMaterialConverter: PotentialMaterialConverterConfig
    dicRecruit6StarHint: Union[Dict[str, str], None]
    fesGachaPoolRelateItem: Union[Dict[str, GachaDataFesGachaPoolRelateItem], None]
    freeGacha: List[GachaDataFreeLimitGachaData]
    gachaPoolClient: List[GachaPoolClientData]
    limitTenGachaItem: List[GachaDataLimitTenGachaTkt]
    linkageTenGachaItem: List[GachaDataLinkageTenGachaTkt]
    newbeeGachaPoolClient: List[NewbeeGachaPoolClientData]
    potentialMaterialConverter: PotentialMaterialConverterConfig
    recruitDetail: str
    recruitPool: RecruitPool
    recruitRarityTable: Dict[str, GachaDataRecruitRange]
    specialRecruitPool: List[SpecialRecruitPool]
    specialTagRarityTable: Dict[str, List[int]]
    gachaTagMaxValid: Union[int, None] = None
    potentialMats: Union[Dict, None] = None
    classicPotentialMats: Union[Dict, None] = None


class GachaDetailDataPerAvail(Struct):
    rarityRank: int
    charIdList: List[str]
    totalPercent: float


class GachaDetailDataGachaAvailChar(Struct):
    perAvailList: List[GachaDetailDataPerAvail]


class PoolWeightItem(Struct):
    id_: str = field(name="id")
    count: int
    type_: str = field(name="type")
    rarity: int
    isClassic: bool = field(default=False)
    beforeNonHitCnt: Union[int, None] = field(default=None)
    singleEnsureCnt: Union[int, None] = field(default=None)
    isSingleEnsure: Union[bool, None] = field(default=None)

    def bulidLog(self) -> Dict:
        m_log: Dict[str, Union[bool, int]] = {}
        if self.beforeNonHitCnt is not None:
            m_log["beforeNonHitCnt"] = self.beforeNonHitCnt
        if self.singleEnsureCnt is not None:
            m_log["singleEnsureCnt"] = self.singleEnsureCnt
        if self.isSingleEnsure is not None:
            m_log["isSingleEnsure"] = self.isSingleEnsure
        return m_log


class gachaGroupConfig(Struct):
    normalCharCnt: int
    weights: List[float] = field(default_factory=list)
    pool: List[PoolWeightItem] = field(default_factory=list)
    upChars_1: List[str] = field(default_factory=list)
    upChars_2: List[str] = field(default_factory=list)
    perUpWeight_1: float = field(default=0.0)
    perUpWeight_2: float = field(default=0.0)
    totalWeights: float = field(default=1.0)


class GachaPoolInfo(Struct, omit_defaults=False):
    init: int = field(default=0)
    totalCnt: int = field(default=0)
    non6StarCnt: int = field(default=0)
    non5StarCnt: int = field(default=0)
    gain5Star: List[str] = field(default_factory=list)
    gain6Star: List[str] = field(default_factory=list)
    history: List[str] = field(default_factory=list)


class GachaTrackModel(Struct, omit_defaults=False):
    pool: Dict[str, GachaPoolInfo] = field(default_factory=dict)
    nonNormal6StarCnt: int = field(default=0)
    nonClassic6StarCnt: int = field(default=0)


class PlayerGacha(Struct):
    class PlayerNewbeeGachaPool(Struct):
        openFlag: int
        cnt: int
        poolId: str

    class PlayerGachaPool(Struct):
        cnt: int
        maxCnt: int
        rarity: int
        avail: bool

    class PlayerFreeLimitGacha(Struct):
        leastFree: int

    class PlayerLinkageGacha(Struct):
        next5: bool
        next5Char: str
        must6: bool
        must6Char: str
        must6Count: int
        must6Level: int

    class PlayerAttainGacha(Struct):
        attain6Count: int

    class PlayerSingleGacha(Struct):
        singleEnsureCnt: int
        singleEnsureUse: bool
        singleEnsureChar: str
        cnt: Union[int, None] = field(default=None)
        maxCnt: Union[int, None] = field(default=None)
        avail: Union[bool, None] = field(default=None)

    class PlayerFesClassicGacha(Struct):
        upChar: Dict[str, List[str]]

    newbee: PlayerNewbeeGachaPool
    normal: Dict[str, PlayerGachaPool]
    attain: Dict[str, PlayerAttainGacha]
    single: Dict[str, PlayerSingleGacha]
    fesClassic: Dict[str, PlayerFesClassicGacha]
    limit: Dict[str, PlayerFreeLimitGacha]
    linkage: Dict[str, Dict[str, PlayerLinkageGacha]]


class PlayerTrack(Struct):
    gacha: GachaTrackModel


class PlayerData(Struct):
    gacha: PlayerGacha


class PlayerDataDetail(Struct):
    user: PlayerData
    track: PlayerTrack
