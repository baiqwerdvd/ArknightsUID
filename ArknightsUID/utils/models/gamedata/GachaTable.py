from typing import Dict, List, Union

from ..common import BaseStruct

from msgspec import field


class GachaDataLinkageTenGachaTkt(BaseStruct):
    itemId: str
    endTime: int
    gachaPoolId: str


class GachaDataLimitTenGachaTkt(BaseStruct):
    itemId: str
    endTime: int


class GachaDataFreeLimitGachaData(BaseStruct):
    poolId: str
    openTime: int
    endTime: int
    freeCount: int


class GachaDataCarouselData(BaseStruct):
    poolId: str
    index: int
    startTime: int
    endTime: int
    spriteId: str


class ItemBundle(BaseStruct):
    id_: str = field(name="id")
    count: int
    type_: str = field(name="type")


class GachaDataRecruitRange(BaseStruct):
    rarityStart: int
    rarityEnd: int


class PotentialMaterialConverterConfig(BaseStruct):
    items: Dict[str, ItemBundle]


class RecruitPoolRecruitTime(BaseStruct):
    timeLength: int
    recruitPrice: int
    accumRate: Union[float, None] = None


class RecruitConstantsData(BaseStruct):
    tagPriceList: Dict[str, int]
    maxRecruitTime: int
    rarityWeights: None = None
    recruitTimeFactorList: None = None


class RecruitPool(BaseStruct):
    recruitTimeTable: List[RecruitPoolRecruitTime]
    recruitConstants: RecruitConstantsData
    recruitCharacterList: None = None
    maskTypeWeightTable: None = None


class NewbeeGachaPoolClientData(BaseStruct):
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


class GachaPoolClientData(BaseStruct):
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
    dynMeta: Union[Dict[str, object], None] = None
    linkageParam: Union[Dict[str, object], None] = None
    linkageRuleId: Union[str, None] = None


class GachaTag(BaseStruct):
    tagId: int
    tagName: str
    tagGroup: int


class SpecialRecruitPoolSpecialRecruitCostData(BaseStruct):
    itemCosts: ItemBundle
    recruitPrice: int
    timeLength: int


class SpecialRecruitPool(BaseStruct):
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


class GachaDataFesGachaPoolRelateItem(BaseStruct):
    rarityRank5ItemId: str
    rarityRank6ItemId: str


class GachaTable(BaseStruct):
    __version__ = "23-10-31-11-47-45-d410ff"

    gachaTags: List[GachaTag]
    carousel: List[GachaDataCarouselData]
    classicPotentialMaterialConverter: PotentialMaterialConverterConfig
    dicRecruit6StarHint: Union[Dict[str, str], None]
    fesGachaPoolRelateItem: Union[
        Dict[str, GachaDataFesGachaPoolRelateItem],
        None,
    ]
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
