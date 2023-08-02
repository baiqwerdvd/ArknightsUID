from pydantic import BaseModel, Field


class ItemBundle(BaseModel):
    type_: str = Field(alias='type')
    id_: str = Field(alias='id')
    count: int


class MissionDisplayRewards(BaseModel):
    type_: str = Field(alias='type')
    id_: str = Field(alias='id')
    count: int


class OpenServerItemData(BaseModel):
    itemId: str
    itemType: str
    count: int


class ReturnIntroData(BaseModel):
    sort: int
    pubTime: int
    image: str


class ReturnCheckinData(BaseModel):
    isImportant: bool
    checkinRewardItems: list[ItemBundle]


class ReturnLongTermTaskData(BaseModel):
    id_: str = Field(alias='id')
    sortId: int
    template: str
    param: list[str]
    desc: str
    rewards: list[MissionDisplayRewards]
    playPoint: int


class ReturnDailyTaskData(BaseModel):
    groupId: str
    id_: str = Field(alias='id')
    groupSortId: int
    taskSortId: int
    template: str
    param: list[str]
    desc: str
    rewards: list[MissionDisplayRewards]
    playPoint: int


class ReturnConst(BaseModel):
    startTime: int
    systemTab_time: int
    afkDays: int
    unlockLv: int
    unlockLevel: str
    juniorClear: bool
    ifvisitor: bool
    permMission_time: int
    needPoints: int
    defaultIntro: str
    pointId: str


class ReturnData(BaseModel):
    constData: ReturnConst
    onceRewards: list[ItemBundle]
    intro: list[ReturnIntroData]
    returnDailyTaskDic: dict[str, list[ReturnDailyTaskData]]
    returnLongTermTaskList: list[ReturnLongTermTaskData]
    creditsList: list[ItemBundle]
    checkinRewardList: list[ReturnCheckinData]


class OpenServerConst(BaseModel):
    firstDiamondShardMailCount: int
    initApMailEndTs: int


class TotalCheckinData(BaseModel):
    order: int
    item: OpenServerItemData
    colorId: int


class ChainLoginData(BaseModel):
    order: int
    item: OpenServerItemData
    colorId: int


class MissionData(BaseModel):
    id_: str = Field(alias='id')
    sortId: int
    description: str
    type_: str = Field(alias='type')
    itemBgType: str
    preMissionIds: None
    template: str
    templateType: str
    param: list[str]
    unlockCondition: None
    unlockParam: None
    missionGroup: str
    toPage: None
    periodicalPoint: int
    rewards: list[ItemBundle]
    backImagePath: None
    foldId: None
    haveSubMissionToUnlock: bool


class MissionGroup(BaseModel):
    id_: str = Field(alias='id')
    title: None
    type_: str = Field(alias='type')
    preMissionGroup: None
    period: None
    rewards: None
    missionIds: list[str]
    startTs: int
    endTs: int


class OpenServerData(BaseModel):
    openServerMissionGroup: MissionGroup
    openServerMissionData: list[MissionData]
    checkInData: list[TotalCheckinData]
    chainLoginData: list[ChainLoginData]


class OpenServerScheduleItem(BaseModel):
    id_: str = Field(alias='id')
    startTs: int
    endTs: int
    totalCheckinDescption: str
    chainLoginDescription: str
    charImg: str


class OpenServerTable(BaseModel):
    __version__ = '23-07-27-18-50-06-aeb568'

    schedule: list[OpenServerScheduleItem]
    dataMap: dict[str, OpenServerData]
    constant: OpenServerConst
    playerReturn: ReturnData

    class Config:
        extra = 'allow'
