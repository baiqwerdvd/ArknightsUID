from typing import Dict, List, Union
from ..common import BaseStruct
from msgspec import field


class ItemDataStageDropInfo(BaseStruct):
    stageId: str
    occPer: str


class ItemDataBuildingProductInfo(BaseStruct):
    roomType: str
    formulaId: str


class ItemBundle(BaseStruct):
    id_: str = field(name='id')
    count: int
    type_: str = field(name='type')


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
    id_: str = field(name='id')
    ap: int
    hasTs: bool


class ExpItemFeature(BaseStruct):
    id_: str = field(name='id')
    gainExp: int


class ItemData(BaseStruct):
    itemId: str
    name: str
    description: Union[str, None]
    rarity: int
    iconId: str
    overrideBkg: None
    stackIconId: Union[str, None]
    sortId: int
    usage: Union[str, None]
    obtainApproach: Union[str, None]
    classifyType: str
    itemType: str
    stageDropList: List[ItemDataStageDropInfo]
    buildingProductList: List[ItemDataBuildingProductInfo]
    hideInItemGet: Union[bool, None] = None


class CharVoucherItemFeature(BaseStruct):
    displayType: int
    id_: str = field(name='id')


class ServerItemReminderMailData(BaseStruct):
    content: str
    sender: str
    title: str


class ServerItemReminderInfo(BaseStruct):
    paidItemIdList: List[str]
    paidReminderMail: ServerItemReminderMailData


class ItemTable(BaseStruct):
    __version__ = '23-07-27-18-50-06-aeb568'

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
