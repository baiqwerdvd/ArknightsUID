from pydantic import BaseModel


class PlayerAvatarPerData(BaseModel):
    avatarId: str
    avatarType: str
    avatarIdSort: int
    avatarIdDesc: str
    avatarItemName: str
    avatarItemDesc: str
    avatarItemUsage: str
    obtainApproach: str


class PlayerAvatarGroupData(BaseModel):
    avatarType: str
    typeName: str
    avatarIdList: list[str]


class PlayerAvatarData(BaseModel):
    defaultAvatarId: str
    avatarList: list[PlayerAvatarPerData]
    avatarTypeData: dict[str, PlayerAvatarGroupData]


class HomeBackgroundSingleData(BaseModel):
    bgId: str
    bgType: str
    bgSortId: int
    bgStartTime: int
    bgName: str
    bgMusicId: str
    bgDes: str
    bgUsage: str
    obtainApproach: str
    unlockDesList: list[str]


class HomeBackgroundData(BaseModel):
    defaultBackgroundId: str
    homeBgDataList: list[HomeBackgroundSingleData]
    defaultBgMusicId: str


class DisplayMetaTable(BaseModel):
    __version__ = '23-07-27-18-50-06-aeb568'

    playerAvatarData: PlayerAvatarData
    homeBackgroundData: HomeBackgroundData

    class Config:
        extra = 'allow'
