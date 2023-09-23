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


class HomeBackgroundData(BaseStruct):
    defaultBackgroundId: str
    defaultThemeId: str
    homeBgDataList: List[HomeBackgroundSingleData]
    themeList: List[HomeBackgroundThemeData]
    defaultBgMusicId: str
    themeStartTime: int


class DisplayMetaTable(BaseStruct):
    __version__ = '23-07-27-18-50-06-aeb568'

    playerAvatarData: PlayerAvatarData
    homeBackgroundData: HomeBackgroundData
