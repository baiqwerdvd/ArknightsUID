from pydantic import BaseModel, Field


class ShopRecommendData(BaseModel):
    imgId: str
    slotIndex: int
    cmd: str
    param1: str | None
    param2: str | None
    skinId: str | None


class ShopRecommendGroup(BaseModel):
    recommendGroup: list[int]
    dataList: list[ShopRecommendData]


class ShopKeeperWord(BaseModel):
    id_: str = Field(alias='id')
    text: str


class ShopRecommendItem(BaseModel):
    tagId: str
    displayType: str
    tagName: str
    itemTag: str
    orderNum: int
    startDatetime: int
    endDatetime: int
    groupList: list[ShopRecommendGroup]
    tagWord: ShopKeeperWord


class ShopCreditUnlockItem(BaseModel):
    sortId: int
    unlockNum: int
    charId: str


class ShopCreditUnlockGroup(BaseModel):
    id_: str = Field(alias='id')
    index: str
    startDateTime: int
    charDict: list[ShopCreditUnlockItem]


class ShopClientDataShopKeeperData(BaseModel):
    welcomeWords: list[ShopKeeperWord]
    clickWords: list[ShopKeeperWord]


class ShopCarouselDataItem(BaseModel):
    spriteId: str
    startTime: int
    endTime: int
    cmd: str
    param1: str | None
    skinId: str
    furniId: str


class ShopCarouselData(BaseModel):
    items: list[ShopCarouselDataItem]


class ChooseShopRelation(BaseModel):
    goodId: str
    optionList: list[str]


class ShopClientGPData(BaseModel):
    goodId: str
    displayName: str
    condTrigPackageType: str


class LMTGSShopSchedule(BaseModel):
    gachaPoolId: str
    LMTGSId: str
    iconColor: str
    iconBackColor: str
    storeTextColor: str | None = None
    startTime: int
    endTime: int


class LMTGSShopOverlaySchedule(BaseModel):
    gachaPoolId1: str
    gachaPoolId2: str
    picId: str


class ShopClientTable(BaseModel):
    __version__ = '23-07-27-18-50-06-aeb568'

    recommendList: list[ShopRecommendItem]
    creditUnlockGroup: dict[str, ShopCreditUnlockGroup]
    shopKeeperData: ShopClientDataShopKeeperData
    carousels: list[ShopCarouselData]
    chooseShopRelations: list[ChooseShopRelation]
    shopUnlockDict: dict[str, str]
    extraQCShopRule: list[str]
    repQCShopRule: list[str]
    shopGPDataDict: dict[str, ShopClientGPData]
    shopMonthlySubGoodId: str
    ls: list[LMTGSShopSchedule]
    os: list[LMTGSShopOverlaySchedule]
