from typing import Dict, List

from ..common import BaseStruct


class PlayerAvatarGroupData(BaseStruct):
    avatarType: str
    typeName: str
    avatarIdList: List[str]


class PlayerAvatarPerData(BaseStruct):
    avatarId: str
    avatarType: str
    avatarIdSort: int
    avatarIdDesc: str
    avatarItemName: str
    avatarItemDesc: str
    avatarItemUsage: str
    obtainApproach: str


class PlayerAvatarTable(BaseStruct):
    __version__ = '23-10-08-17-52-18-288259'

    avatarList: List[PlayerAvatarPerData]
    avatarTypeData: Dict[str, PlayerAvatarGroupData]
    defaultAvatarId: str
