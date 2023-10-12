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
    __version__ = '23-10-08-17-52-18-288259'

    team: Dict[str, HandbookTeam]
