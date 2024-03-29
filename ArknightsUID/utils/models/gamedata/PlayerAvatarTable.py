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
    __version__ = "24-02-02-10-18-07-831ad8"

    avatarList: List[PlayerAvatarPerData]
    avatarTypeData: Dict[str, PlayerAvatarGroupData]
    defaultAvatarId: str
