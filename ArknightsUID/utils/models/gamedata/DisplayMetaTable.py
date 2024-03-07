from typing import Dict, List

from ..common import BaseStruct

from msgspec import field


class PlayerAvatarPerData(BaseStruct):
    avatarId: str
    avatarType: str
    avatarIdSort: int
    avatarIdDesc: str
    avatarItemName: str
    avatarItemDesc: str
    avatarItemUsage: str
    obtainApproach: str


class PlayerAvatarGroupData(BaseStruct):
    avatarType: str
    typeName: str
    avatarIdList: List[str]


class PlayerAvatarData(BaseStruct):
    defaultAvatarId: str
    avatarList: List[PlayerAvatarPerData]
    avatarTypeData: Dict[str, PlayerAvatarGroupData]


class HomeBackgroundSingleData(BaseStruct):
    bgId: str
    bgType: str
    bgSortId: int
    bgStartTime: int
    bgName: str
    bgMusicId: str
    bgDes: str
    bgUsage: str
    obtainApproach: str
    unlockDesList: List[str]


class HomeBackgroundThemeData(BaseStruct):
    id_: str = field(name='id')
    type_: str = field(name='type')
    sortId: int
    startTime: int
    tmName: str
    tmDes: str
    tmUsage: str
    obtainApproach: str
    unlockDesList: List[str]
    isLimitObtain: bool
    hideWhenLimit: bool


class ThemeLimitInfo(BaseStruct):
    startTime: int
    endTime: int
    invalidObtainDesc: str


class HomeBackgroundThemeLimitData(BaseStruct):
    id_: str = field(name='id')
    limitInfos: List[ThemeLimitInfo]


class HomeBackgroundData(BaseStruct):
    defaultBackgroundId: str
    defaultThemeId: str
    homeBgDataList: List[HomeBackgroundSingleData]
    themeList: List[HomeBackgroundThemeData]
    themeLimitData: Dict[str, HomeBackgroundThemeLimitData]
    defaultBgMusicId: str
    themeStartTime: int

# class

# class NameCardV2Data(BaseStruct):
#     fixedModuleData: Dict[str, Dict[str, str]]
#     removableModuleData: Dict[str, RemovableModule]
#     skinData: Dict[str, NameCardV2DataSkinData]
#     consts: NameCardV2DataConsts


class DisplayMetaTable(BaseStruct):
    __version__ = '24-02-02-10-18-07-831ad8'

    playerAvatarData: PlayerAvatarData
    homeBackgroundData: HomeBackgroundData
    # nameCardV2Data: NameCardV2Data
