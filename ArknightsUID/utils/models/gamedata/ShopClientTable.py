from typing import Dict, List, Union

from ..common import BaseStruct

from msgspec import field


class ShopRecommendData(BaseStruct):
    imgId: str
    slotIndex: int
    cmd: str
    param1: Union[str, None]
    param2: Union[str, None]
    skinId: Union[str, None]


class ShopRecommendGroup(BaseStruct):
    recommendGroup: List[int]
    dataList: List[ShopRecommendData]


class ShopKeeperWord(BaseStruct):
    id_: str = field(name='id')
    text: str


class ShopRecommendTemplateNormalGiftParam(BaseStruct):
    showStartTs: int
    showEndTs: int
    goodId: str
    giftPackageName: str
    price: int
    logoId: str
    color: str
    haveMark: bool


class ShopRecommendTemplateNormalSkinParam(BaseStruct):
    showStartTs: int
    showEndTs: int
    skinIds: List[str]
    skinGroupName: str
    brandIconId: str
    colorBack: str
    colorText: str
    text: str


class ShopRecommendTemplateNormalFurnParam(BaseStruct):
    showStartTs: int
    showEndTs: int
    furnPackId: str
    isNew: bool
    isPackSell: bool
    count: int
    colorBack: str
    colorText: str
    actId: Union[str, None] = None


class ShopRecommendTemplateReturnSkinParam(BaseStruct):
    showStartTs: int
    showEndTs: int


class ShopRecommendTemplateParam(BaseStruct):
    normalGiftParam: Union[ShopRecommendTemplateNormalGiftParam, None] = None
    normalSkinParam: Union[ShopRecommendTemplateNormalSkinParam, None] = None
    normalFurnParam: Union[ShopRecommendTemplateNormalFurnParam, None] = None
    returnSkinParam: Union[ShopRecommendTemplateReturnSkinParam, None] = None


class ShopRecommendItem(BaseStruct):
    tagId: str
    displayType: str
    tagName: str
    itemTag: str
    orderNum: int
    startDatetime: int
    endDatetime: int
    groupList: List[ShopRecommendGroup]
    tagWord: ShopKeeperWord
    templateType: str
    templateParam: Union[ShopRecommendTemplateParam, None]


class ShopCreditUnlockItem(BaseStruct):
    sortId: int
    unlockNum: int
    charId: str


class ShopCreditUnlockGroup(BaseStruct):
    id_: str = field(name='id')
    index: str
    startDateTime: int
    charDict: List[ShopCreditUnlockItem]


class ShopClientDataShopKeeperData(BaseStruct):
    welcomeWords: List[ShopKeeperWord]
    clickWords: List[ShopKeeperWord]


class ShopCarouselDataItem(BaseStruct):
    spriteId: str
    startTime: int
    endTime: int
    cmd: str
    param1: Union[str, None]
    skinId: str
    furniId: str


class ShopCarouselData(BaseStruct):
    items: List[ShopCarouselDataItem]


class ChooseShopRelation(BaseStruct):
    goodId: str
    optionList: List[str]


class ShopClientGPData(BaseStruct):
    goodId: str
    displayName: str
    condTrigPackageType: str


class LMTGSShopSchedule(BaseStruct):
    gachaPoolId: str
    LMTGSId: str
    iconColor: str
    iconBackColor: str
    startTime: int
    endTime: int
    storeTextColor: Union[str, None] = None


class LMTGSShopOverlaySchedule(BaseStruct):
    gachaPoolId1: str
    gachaPoolId2: str
    picId: str


class ShopClientTable(BaseStruct):
    __version__ = '23-09-29-15-41-03-569cae'

    recommendList: List[ShopRecommendItem]
    creditUnlockGroup: Dict[str, ShopCreditUnlockGroup]
    shopKeeperData: ShopClientDataShopKeeperData
    carousels: List[ShopCarouselData]
    chooseShopRelations: List[ChooseShopRelation]
    shopUnlockDict: Dict[str, str]
    extraQCShopRule: List[str]
    repQCShopRule: List[str]
    shopGPDataDict: Dict[str, ShopClientGPData]
    shopMonthlySubGoodId: str
    ls: List[LMTGSShopSchedule]
    os: List[LMTGSShopOverlaySchedule]
