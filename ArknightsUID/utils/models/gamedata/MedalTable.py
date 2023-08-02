from pydantic import BaseModel, Field


class MedalExpireTime(BaseModel):
    start: int
    end: int
    type_: str = Field(alias='type')


class ItemBundle(BaseModel):
    id_: str = Field(alias='id')
    count: int
    type_: str = Field(alias='type')


class MedalGroupData(BaseModel):
    groupId: str
    groupName: str
    groupDesc: str
    medalId: list[str]
    sortId: int
    groupBackColor: str
    groupGetTime: int
    sharedExpireTimes: list[MedalExpireTime] | None


class MedalRewardGroupData(BaseModel):
    groupId: str
    slotId: int
    itemList: list[ItemBundle]


class MedalTypeData(BaseModel):
    medalGroupId: str
    sortId: int
    medalName: str
    groupData: list[MedalGroupData]


class MedalPerData(BaseModel):
    medalId: str | None
    medalName: str | None
    medalType: str | None
    slotId: int | None
    preMedalIdList: list[str] | None
    rarity: int
    template: str | None
    unlockParam: list[str]
    getMethod: str | None
    description: str | None
    advancedMedal: str | None
    originMedal: str | None
    displayTime: int
    expireTimes: list[MedalExpireTime]
    medalRewardGroup: list[MedalRewardGroupData]


class MedalTable(BaseModel):
    __version__ = '23-07-27-18-50-06-aeb568'

    medalList: list[MedalPerData]
    medalTypeData: dict[str, MedalTypeData]

    class Config:
        extra = 'allow'
