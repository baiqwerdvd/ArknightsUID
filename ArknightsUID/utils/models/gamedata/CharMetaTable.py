from pydantic import BaseModel, Field


class ItemBundle(BaseModel):
    id_: str = Field(alias='id')
    count: int
    type_: str = Field(alias='type')


class SpCharMissionData(BaseModel):
    charId: str
    missionId: str
    sortId: int
    condType: str
    param: list[str]
    rewards: list[ItemBundle]


class CharMetaTable(BaseModel):
    __version__ = '23-07-27-18-50-06-aeb568'

    class Config:
        extra = 'allow'

    spCharGroups: dict[str, list[str]]
    spCharMissions: dict[str, dict[str, SpCharMissionData]]
    spCharVoucherSkinTime: dict[str, int]
