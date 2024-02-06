from typing import Dict, List, Union

from ..common import BaseStruct

from msgspec import field


class MissionDisplayRewards(BaseStruct):
    type_: str = field(name='type')
    id_: str = field(name='id')
    count: int


class DailyMissionGroupInfoperiodInfo(BaseStruct):
    missionGroupId: str
    period: List[int]
    rewardGroupId: str


class DailyMissionGroupInfo(BaseStruct):
    endTime: int
    periodList: List[DailyMissionGroupInfoperiodInfo]
    startTime: int
    tagState: Union[str, None]


class MissionWeeklyRewardConf(BaseStruct):
    beginTime: int
    endTime: int
    groupId: str
    id_: str = field(name='id')
    periodicalPointCost: int
    type_: str = field(name='type')
    sortIndex: int
    rewards: List[MissionDisplayRewards]


class MissionDailyRewardConf(BaseStruct):
    groupId: str
    id_: str = field(name='id')
    periodicalPointCost: int
    type_: str = field(name='type')
    sortIndex: int
    rewards: List[MissionDisplayRewards]


class MissionGroup(BaseStruct):
    id_: str = field(name='id')
    title: Union[str, None]
    type_: str = field(name='type')
    preMissionGroup: Union[str, None]
    period: Union[List[int], None]
    rewards: Union[List[MissionDisplayRewards], None]
    missionIds: List[str]
    startTs: int
    endTs: int


class MissionData(BaseStruct):
    id_: str = field(name='id')
    sortId: int
    description: str
    type_: str = field(name='type')
    itemBgType: str
    preMissionIds: Union[List[str], None]
    template: str
    templateType: str
    param: List[str]
    unlockCondition: Union[str, None]
    unlockParam: Union[List[str], None]
    missionGroup: str
    toPage: None
    periodicalPoint: int
    rewards: Union[List[MissionDisplayRewards], None]
    backImagePath: Union[str, None]
    foldId: Union[str, None]
    haveSubMissionToUnlock: bool


class CrossAppShareMissions(BaseStruct):
    shareMissionId: str
    missionType: str
    relateActivityId: Union[str, None]
    startTime: int
    endTime: int
    limitCount: int
    condTemplate: Union[str, None]
    condParam: List[Union[str, None]]
    rewardsList: Union[List[str], None]


class MissionTable(BaseStruct):
    __version__ = '24-02-02-10-18-07-831ad8'

    missions: Dict[str, MissionData]
    missionGroups: Dict[str, MissionGroup]
    periodicalRewards: Dict[str, MissionDailyRewardConf]
    weeklyRewards: Dict[str, MissionWeeklyRewardConf]
    dailyMissionGroupInfo: Dict[str, DailyMissionGroupInfo]
    dailyMissionPeriodInfo: List[DailyMissionGroupInfo]
    crossAppShareMissions: Dict[str, CrossAppShareMissions]
    crossAppShareMissionConst: Dict[str, str]
