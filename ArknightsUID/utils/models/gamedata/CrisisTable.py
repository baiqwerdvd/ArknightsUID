from pydantic import BaseModel, Field


class ItemBundle(BaseModel):
    id_: str = Field(alias='id')
    count: int
    type_: str = Field(alias='type')


class StringKeyFrames(BaseModel):
    level: int
    data: str


class CrisisClientDataSeasonInfo(BaseModel):
    seasonId: str
    startTs: int
    endTs: int
    name: str
    crisisRuneCoinUnlockItem: ItemBundle
    permBgm: str
    medalGroupId: str | None
    bgmHardPoint: int
    permBgmHard: str | None


class CrisisMapRankInfo(BaseModel):
    rewards: list[ItemBundle]
    unlockPoint: int


class CrisisTable(BaseModel):
    __version__ = '23-07-27-18-50-06-aeb568'

    seasonInfo: list[CrisisClientDataSeasonInfo]
    tempAppraise: list[StringKeyFrames]
    permAppraise: list[StringKeyFrames]
    mapRankInfo: dict[str, CrisisMapRankInfo]
    meta: str
    unlockCoinLv3: int
    hardPointPerm: int
    hardPointTemp: int
    voiceGrade: int
    crisisRuneCoinUnlockItemTitle: str
    crisisRuneCoinUnlockItemDesc: str

    class Config:
        extra = 'allow'
