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
    __version__ = '23-10-31-11-47-45-d410ff'

    team: Dict[str, HandbookTeam]
