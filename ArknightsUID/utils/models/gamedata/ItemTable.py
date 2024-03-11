from typing import ClassVar, Dict, List, Union

from ..common import BaseStruct

from msgspec import field


class ItemDataStageDropInfo(BaseStruct):
    stageId: str
    occPer: str


class ItemDataBuildingProductInfo(BaseStruct):
    roomType: str
    formulaId: str


class ItemBundle(BaseStruct):
    id_: str = field(name="id")
    count: int
    type_: str = field(name="type")


class FavorCharacterInfo(BaseStruct):
    itemId: str
    charId: str
    favorAddAmt: int


class ActivityPotentialCharacterInfo(BaseStruct):
    charId: str


class FullPotentialCharacterInfo(BaseStruct):
    itemId: str
    ts: int


class ItemPackInfo(BaseStruct):
    packId: str
    content: List[ItemBundle]


class UniCollectionInfo(BaseStruct):
    uniCollectionItemId: str
    uniqueItem: List[ItemBundle]


class ApSupplyFeature(BaseStruct):
    id_: str = field(name="id")
    ap: int
    hasTs: bool


class ExpItemFeature(BaseStruct):
    id_: str = field(name="id")
    gainExp: int


class ItemDataVoucherRelateInfo(BaseStruct):
    voucherId: str
    voucherItemType: str


class ItemData(BaseStruct):
    itemId: str
    name: str
    rarity: int
    iconId: str
    sortId: int
    classifyType: str
    itemType: str
    stageDropList: ClassVar[List[Union[ItemDataStageDropInfo, None]]] = []
    buildingProductList: ClassVar[List[Union[ItemDataBuildingProductInfo, None]]] = []
    voucherRelateList: ClassVar[List[Union[ItemDataVoucherRelateInfo, None]]] = []
    overrideBkg: Union[str, None] = None
    usage: Union[str, None] = None
    description: Union[str, None] = None
    stackIconId: Union[str, None] = None
    obtainApproach: Union[str, None] = None
    hideInItemGet: Union[bool, None] = None


class CharVoucherItemFeature(BaseStruct):
    displayType: int
    id_: str = field(name="id")


class ServerItemReminderMailData(BaseStruct):
    content: str
    sender: str
    title: str


class ServerItemReminderInfo(BaseStruct):
    paidItemIdList: List[str]
    paidReminderMail: ServerItemReminderMailData


class ItemTable(BaseStruct):
    __version__ = "24-02-02-10-18-07-831ad8"

    activityPotentialCharacters: Dict[str, ActivityPotentialCharacterInfo]
    apSupplies: Dict[str, ApSupplyFeature]
    expItems: Dict[str, ExpItemFeature]
    favorCharacters: Dict[str, FavorCharacterInfo]
    fullPotentialCharacters: Dict[str, FullPotentialCharacterInfo]
    itemPackInfos: Dict[str, ItemPackInfo]
    items: Dict[str, ItemData]
    itemTimeLimit: Dict[str, int]
    potentialItems: Dict[str, Dict[str, str]]
    uniCollectionInfo: Dict[str, UniCollectionInfo]
    uniqueInfo: Dict[str, int]
    reminderInfo: Union[ServerItemReminderInfo, None] = None
    charVoucherItems: Union[Dict[str, CharVoucherItemFeature], None] = None
