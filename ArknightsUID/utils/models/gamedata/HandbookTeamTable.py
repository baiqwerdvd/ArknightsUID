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
    __version__ = '23-12-02-09-28-50-918524'

    team: Dict[str, HandbookTeam]
