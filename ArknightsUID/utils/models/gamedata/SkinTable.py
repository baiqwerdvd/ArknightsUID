from typing import Dict, List, Union

from ..common import BaseStruct


class CharSkinDataTokenSkinInfo(BaseStruct):
    tokenId: str
    tokenSkinId: str


class CharSkinDataBattleSkin(BaseStruct):
    overwritePrefab: bool
    skinOrPrefabId: Union[str, None]


class CharSkinDataDisplaySkin(BaseStruct):
    skinName: Union[str, None]
    colorList: Union[List[str], None]
    titleList: Union[List[str], None]
    modelName: Union[str, None]
    drawerList: Union[List[str], None]
    designerList: Union[List[str], None]
    skinGroupId: Union[str, None]
    skinGroupName: Union[str, None]
    skinGroupSortIndex: int
    content: Union[str, None]
    dialog: Union[str, None]
    usage: Union[str, None]
    description: Union[str, None]
    obtainApproach: Union[str, None]
    sortId: int
    displayTagId: Union[str, None]
    getTime: int
    onYear: int
    onPeriod: int


class CharSkinData(BaseStruct):
    skinId: str
    charId: str
    tokenSkinMap: Union[List[CharSkinDataTokenSkinInfo], None]
    illustId: Union[str, None]
    dynIllustId: Union[str, None]
    avatarId: str
    portraitId: Union[str, None]
    dynPortraitId: Union[str, None]
    dynEntranceId: Union[str, None]
    buildingId: Union[str, None]
    battleSkin: CharSkinDataBattleSkin
    isBuySkin: bool
    tmplId: Union[str, None]
    voiceId: Union[str, None]
    voiceType: str
    displaySkin: CharSkinDataDisplaySkin


class CharSkinGroupInfo(BaseStruct):
    skinGroupId: str
    publishTime: int


class CharSkinKvImgInfo(BaseStruct):
    kvImgId: str
    linkedSkinGroupId: str


class CharSkinBrandInfo(BaseStruct):
    brandId: str
    groupList: List[CharSkinGroupInfo]
    kvImgIdList: List[CharSkinKvImgInfo]
    brandName: str
    brandCapitalName: str
    description: str
    publishTime: int
    sortId: int


class SpecialSkinInfo(BaseStruct):
    skinId: str
    startTime: int
    endTime: int


class SkinTable(BaseStruct):
    __version__ = '23-10-31-11-47-45-d410ff'

    charSkins: Dict[str, CharSkinData]
    buildinEvolveMap: Dict[str, Dict[str, str]]
    buildinPatchMap: Dict[str, Dict[str, str]]
    brandList: Dict[str, CharSkinBrandInfo]
    specialSkinInfoList: List[SpecialSkinInfo]
