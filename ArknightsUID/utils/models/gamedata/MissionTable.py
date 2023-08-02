from pydantic import BaseModel, Field


class MissionDisplayRewards(BaseModel):
    type_: str = Field(alias='type')
    id_: str = Field(alias='id')
    count: int


class DailyMissionGroupInfoperiodInfo(BaseModel):
    missionGroupId: str
    period: list[int]
    rewardGroupId: str


class DailyMissionGroupInfo(BaseModel):
    endTime: int
    periodList: list[DailyMissionGroupInfoperiodInfo]
    startTime: int
    tagState: str | None


class MissionWeeklyRewardConf(BaseModel):
    beginTime: int
    endTime: int
    groupId: str
    id_: str = Field(alias='id')
    periodicalPointCost: int
    type_: str = Field(alias='type')
    sortIndex: int
    rewards: list[MissionDisplayRewards]


class MissionDailyRewardConf(BaseModel):
    groupId: str
    id_: str = Field(alias='id')
    periodicalPointCost: int
    type_: str = Field(alias='type')
    sortIndex: int
    rewards: list[MissionDisplayRewards]


class MissionGroup(BaseModel):
    id_: str = Field(alias='id')
    title: str | None
    type_: str = Field(alias='type')
    preMissionGroup: str | None
    period: list[int] | None
    rewards: list[MissionDisplayRewards] | None
    missionIds: list[str]
    startTs: int
    endTs: int


class MissionData(BaseModel):
    id_: str = Field(alias='id')
    sortId: int
    description: str
    type_: str = Field(alias='type')
    itemBgType: str
    preMissionIds: list[str] | None
    template: str
    templateType: str
    param: list[str]
    unlockCondition: str | None
    unlockParam: list[str] | None
    missionGroup: str
    toPage: None
    periodicalPoint: int
    rewards: list[MissionDisplayRewards] | None
    backImagePath: str | None
    foldId: str | None
    haveSubMissionToUnlock: bool


class MissionTable(BaseModel):
    __version__ = '23-07-27-18-50-06-aeb568'

    missions: dict[str, MissionData]
    missionGroups: dict[str, MissionGroup]
    periodicalRewards: dict[str, MissionDailyRewardConf]
    weeklyRewards: dict[str, MissionWeeklyRewardConf]
    dailyMissionGroupInfo: dict[str, DailyMissionGroupInfo]
    dailyMissionPeriodInfo: list[DailyMissionGroupInfo]

    class Config:
        extra = 'allow'
