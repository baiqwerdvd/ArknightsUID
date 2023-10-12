from typing import Dict, List

from msgspec import field

from ..common import BaseStruct


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


class DisplayMetaTable(BaseStruct):
    __version__ = '23-10-08-17-52-18-288259'

    playerAvatarData: PlayerAvatarData
    homeBackgroundData: HomeBackgroundData
