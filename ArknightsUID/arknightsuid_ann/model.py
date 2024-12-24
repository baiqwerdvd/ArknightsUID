from typing import Any

from msgspec import Struct, field


class BulletinTargetDataItem(Struct):
    cid: str
    title: str
    category: int
    displayTime: str
    updatedAt: int
    sticky: bool


class BulletinTargetDataPopup(Struct):
    popupList: list[Any]
    defaultPopup: str


class BulletinTargetData(Struct):
    list_: list[BulletinTargetDataItem] = field(name="list", default_factory=list)
    popup: dict[str, Any] = field(default_factory=dict)


class BulletinTarget(Struct):
    Android: BulletinTargetData = field(default_factory=BulletinTargetData)
    Bilibili: BulletinTargetData = field(default_factory=BulletinTargetData)
    IOS: BulletinTargetData = field(default_factory=BulletinTargetData)


class BulletinData(Struct):
    cid: str
    displayType: int
    title: str
    category: int
    header: str
    content: str
    jumpLink: str
    bannerImageUrl: str
    displayTime: str
    updatedAt: int


class BulletinMeta(Struct):
    data: dict[str, BulletinData] = field(default_factory=dict)
    update: dict[str, BulletinData] = field(default_factory=dict)
    target: BulletinTarget = field(default_factory=BulletinTarget)
