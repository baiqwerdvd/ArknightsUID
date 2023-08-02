from pydantic import BaseModel, Field


class GachaDataLinkageTenGachaTkt(BaseModel):
    itemId: str
    endTime: int
    gachaPoolId: str


class GachaDataLimitTenGachaTkt(BaseModel):
    itemId: str
    endTime: int


class GachaDataFreeLimitGachaData(BaseModel):
    poolId: str
    openTime: int
    endTime: int
    freeCount: int


class GachaDataCarouselData(BaseModel):
    poolId: str
    index: int
    startTime: int
    endTime: int
    spriteId: str


class ItemBundle(BaseModel):
    id_: str = Field(alias='id')
    count: int
    type_: str = Field(alias='type')


class GachaDataRecruitRange(BaseModel):
    rarityStart: int
    rarityEnd: int


class PotentialMaterialConverterConfig(BaseModel):
    items: dict[str, ItemBundle]


class RecruitPoolRecruitTime(BaseModel):
    timeLength: int
    recruitPrice: int
    accumRate: float | None = None


class RecruitConstantsData(BaseModel):
    rarityWeights: None = None
    tagPriceList: dict[str, int]
    recruitTimeFactorList: None = None
    maxRecruitTime: int


class RecruitPool(BaseModel):
    recruitTimeTable: list[RecruitPoolRecruitTime]
    recruitCharacterList: None = None
    recruitConstants: RecruitConstantsData
    maskTypeWeightTable: None = None


class NewbeeGachaPoolClientData(BaseModel):
    gachaPoolId: str
    gachaIndex: int
    gachaPoolName: str
    gachaPoolDetail: str
    gachaPrice: int
    gachaTimes: int
    gachaOffset: str | None = None
    firstOpenDay: int | None = None
    reOpenDay: int | None = None
    gachaPoolItems: None = None
    signUpEarliestTime: int | None = None


class GachaPoolClientData(BaseModel):
    CDPrimColor: str | None
    CDSecColor: str | None
    dynMeta: dict[str, object] | None = None
    endTime: int
    gachaIndex: int
    gachaPoolDetail: str | None
    gachaPoolId: str
    gachaPoolName: str
    gachaPoolSummary: str
    gachaRuleType: str
    guarantee5Avail: int
    guarantee5Count: int
    linkageParam: dict[str, object] | None = None
    linkageRuleId: str | None = None
    LMTGSID: str | None
    openTime: int


class GachaTag(BaseModel):
    tagId: int
    tagName: str
    tagGroup: int


class SpecialRecruitPoolSpecialRecruitCostData(BaseModel):
    itemCosts: ItemBundle
    recruitPrice: int
    timeLength: int


class SpecialRecruitPool(BaseModel):
    endDateTime: int
    order: int
    recruitId: str
    recruitTimeTable: list[SpecialRecruitPoolSpecialRecruitCostData]
    startDateTime: int
    tagId: int
    tagName: str
    CDPrimColor: str | None
    CDSecColor: str | None
    LMTGSID: str | None
    gachaRuleType: str


class GachaDataFesGachaPoolRelateItem(BaseModel):
    rarityRank5ItemId: str
    rarityRank6ItemId: str


class GachaTable(BaseModel):
    __version__ = '23-07-27-18-50-06-aeb568'

    gachaTags: list[GachaTag]
    carousel: list[GachaDataCarouselData]
    classicPotentialMaterialConverter: PotentialMaterialConverterConfig
    dicRecruit6StarHint: dict[str, str] | None
    fesGachaPoolRelateItem: dict[str, GachaDataFesGachaPoolRelateItem] | None
    freeGacha: list[GachaDataFreeLimitGachaData]
    gachaPoolClient: list[GachaPoolClientData]
    gachaTagMaxValid: int | None = None
    limitTenGachaItem: list[GachaDataLimitTenGachaTkt]
    linkageTenGachaItem: list[GachaDataLinkageTenGachaTkt]
    newbeeGachaPoolClient: list[NewbeeGachaPoolClientData]
    potentialMaterialConverter: PotentialMaterialConverterConfig
    recruitDetail: str
    recruitPool: RecruitPool
    recruitRarityTable: dict[str, GachaDataRecruitRange]
    specialRecruitPool: list[SpecialRecruitPool]
    specialTagRarityTable: dict[str, list[int]]
    potentialMats: dict | None = None
    classicPotentialMats: dict | None = None

    class Config:
        extra = 'allow'
