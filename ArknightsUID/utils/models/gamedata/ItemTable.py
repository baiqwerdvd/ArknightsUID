from pydantic import BaseModel, Field


class ItemDataStageDropInfo(BaseModel):
    stageId: str
    occPer: str


class ItemDataBuildingProductInfo(BaseModel):
    roomType: str
    formulaId: str


class ItemBundle(BaseModel):
    id_: str = Field(alias='id')
    count: int
    type_: str = Field(alias='type')


class FavorCharacterInfo(BaseModel):
    itemId: str
    charId: str
    favorAddAmt: int


class ActivityPotentialCharacterInfo(BaseModel):
    charId: str


class FullPotentialCharacterInfo(BaseModel):
    itemId: str
    ts: int


class ItemPackInfo(BaseModel):
    packId: str
    content: list[ItemBundle]


class UniCollectionInfo(BaseModel):
    uniCollectionItemId: str
    uniqueItem: list[ItemBundle]


class ApSupplyFeature(BaseModel):
    id_: str = Field(alias='id')
    ap: int
    hasTs: bool


class ExpItemFeature(BaseModel):
    id_: str = Field(alias='id')
    gainExp: int


class ItemData(BaseModel):
    itemId: str
    name: str
    description: str | None
    rarity: int
    iconId: str
    overrideBkg: None
    stackIconId: str | None
    sortId: int
    usage: str | None
    obtainApproach: str | None
    classifyType: str
    itemType: str
    stageDropList: list[ItemDataStageDropInfo]
    buildingProductList: list[ItemDataBuildingProductInfo]


class CharVoucherItemFeature(BaseModel):
    displayType: int
    id_: str = Field(alias='id')


class ServerItemReminderMailData(BaseModel):
    content: str
    sender: str
    title: str


class ServerItemReminderInfo(BaseModel):
    paidItemIdList: list[str]
    paidReminderMail: ServerItemReminderMailData


class ItemTable(BaseModel):
    __version__ = '23-07-27-18-50-06-aeb568'

    activityPotentialCharacters: dict[str, ActivityPotentialCharacterInfo]
    apSupplies: dict[str, ApSupplyFeature]
    charVoucherItems: dict[str, CharVoucherItemFeature] | None = None
    expItems: dict[str, ExpItemFeature]
    favorCharacters: dict[str, FavorCharacterInfo]
    fullPotentialCharacters: dict[str, FullPotentialCharacterInfo]
    itemPackInfos: dict[str, ItemPackInfo]
    items: dict[str, ItemData]
    itemTimeLimit: dict[str, int]
    potentialItems: dict[str, dict[str, str]]
    reminderInfo: ServerItemReminderInfo | None = None
    uniCollectionInfo: dict[str, UniCollectionInfo]
    uniqueInfo: dict[str, int]

    class Config:
        extra = 'allow'
