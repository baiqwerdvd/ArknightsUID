from pydantic import BaseModel


class PlayerAvatarGroupData(BaseModel):
    avatarType: str
    typeName: str
    avatarIdList: list[str]


class PlayerAvatarPerData(BaseModel):
    avatarId: str
    avatarType: str
    avatarIdSort: int
    avatarIdDesc: str
    avatarItemName: str
    avatarItemDesc: str
    avatarItemUsage: str
    obtainApproach: str


class PlayerAvatarTable(BaseModel):
    __version__ = '23-07-27-18-50-06-aeb568'

    avatarList: list[PlayerAvatarPerData]
    avatarTypeData: dict[str, PlayerAvatarGroupData]
    defaultAvatarId: str
