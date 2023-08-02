from pydantic import BaseModel, Field


class ItemBundle(BaseModel):
    id_: str = Field(alias='id')
    count: int
    type_: str = Field(alias='type')


class MonthlySignInData(BaseModel):
    itemId: str
    itemType: str
    count: int


class MonthlySignInGroupData(BaseModel):
    groupId: str
    title: str
    description: str
    signStartTime: int
    signEndTime: int
    items: list[MonthlySignInData]


class MonthlyDailyBonusGroup(BaseModel):
    groupId: str
    startTime: int
    endTime: int
    items: list[ItemBundle]
    imgId: str
    backId: str


class CheckinTable(BaseModel):
    __version__ = '23-07-27-18-50-06-aeb568'

    groups: dict[str, MonthlySignInGroupData]
    monthlySubItem: dict[str, list[MonthlyDailyBonusGroup]]
    currentMonthlySubId: str

    class Config:
        extra = 'allow'
