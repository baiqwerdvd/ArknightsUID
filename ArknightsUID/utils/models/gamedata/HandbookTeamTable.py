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
    __version__ = '24-02-02-10-18-07-831ad8'

    team: Dict[str, HandbookTeam]
