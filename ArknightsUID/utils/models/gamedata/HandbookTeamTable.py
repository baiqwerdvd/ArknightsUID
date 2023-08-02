from pydantic import BaseModel


class HandbookTeam(BaseModel):
    powerId: str
    orderNum: int
    powerLevel: int
    powerName: str
    powerCode: str
    color: str
    isLimited: bool
    isRaw: bool


class HandbookTeamTable(BaseModel):
    __version__ = '23-07-27-18-50-06-aeb568'

    team: dict[str, HandbookTeam]

    def __init__(self, **data):
        super().__init__(team=data)
