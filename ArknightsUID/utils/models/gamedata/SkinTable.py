
from pydantic import BaseModel


class CharSkinDataTokenSkinInfo(BaseModel):
    tokenId: str
    tokenSkinId: str


class CharSkinDataBattleSkin(BaseModel):
    overwritePrefab: bool
    skinOrPrefabId: str | None


class CharSkinDataDisplaySkin(BaseModel):
    skinName: str | None
    colorList: list[str] | None
    titleList: list[str] | None
    modelName: str | None
    drawerList: list[str] | None
    designerList: list[str] | None
    skinGroupId: str | None
    skinGroupName: str | None
    skinGroupSortIndex: int
    content: str | None
    dialog: str | None
    usage: str | None
    description: str | None
    obtainApproach: str | None
    sortId: int
    displayTagId: str | None
    getTime: int
    onYear: int
    onPeriod: int


class CharSkinData(BaseModel):
    skinId: str
    charId: str
    tokenSkinMap: list[CharSkinDataTokenSkinInfo] | None
    illustId: str | None
    dynIllustId: str | None
    avatarId: str
    portraitId: str | None
    dynPortraitId: str | None
    dynEntranceId: str | None
    buildingId: str | None
    battleSkin: CharSkinDataBattleSkin
    isBuySkin: bool
    tmplId: str | None
    voiceId: str | None
    voiceType: str
    displaySkin: CharSkinDataDisplaySkin


class CharSkinGroupInfo(BaseModel):
    skinGroupId: str
    publishTime: int


class CharSkinKvImgInfo(BaseModel):
    kvImgId: str
    linkedSkinGroupId: str


class CharSkinBrandInfo(BaseModel):
    brandId: str
    groupList: list[CharSkinGroupInfo]
    kvImgIdList: list[CharSkinKvImgInfo]
    brandName: str
    brandCapitalName: str
    description: str
    sortId: int


class SpecialSkinInfo(BaseModel):
    skinId: str
    startTime: int
    endTime: int


class SkinTable(BaseModel):
    __version__ = '23-07-27-18-50-06-aeb568'

    charSkins: dict[str, CharSkinData]
    buildinEvolveMap: dict[str, dict[str, str]]
    buildinPatchMap: dict[str, dict[str, str]]
    brandList: dict[str, CharSkinBrandInfo]
    specialSkinInfoList: list[SpecialSkinInfo]
