from typing import Dict

from ..common import BaseStruct


class HandbookTeam(BaseStruct):
    powerId: str
    orderNum: int
    powerLevel: int
    powerName: str
    powerCode: str
    color: str
    isLimited: bool
    isRaw: bool


class HandbookTeamTable(BaseStruct):
    __version__ = '23-09-29-15-41-03-569cae'

    team: Dict[str, HandbookTeam]
