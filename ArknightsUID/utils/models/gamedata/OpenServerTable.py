from typing import Dict, List, Union

from ..common import BaseStruct

from msgspec import field


class RewardItem(BaseStruct):
    type_: str = field(name='type')
    id_: str = field(name='id')
    count: int
    sortId: int


class ItemBundle(BaseStruct):
    type_: str = field(name='type')
    id_: str = field(name='id')
    count: int


class MissionDisplayRewards(BaseStruct):
    type_: str = field(name='type')
    id_: str = field(name='id')
    count: int


class OpenServerItemData(BaseStruct):
    itemId: str
    itemType: str
    count: int


class ReturnIntroData(BaseStruct):
    sort: int
    pubTime: int
    image: str


class ReturnCheckinData(BaseStruct):
    isImportant: bool
    checkinRewardItems: List[ItemBundle]


class ReturnLongTermTaskData(BaseStruct):
    id_: str = field(name='id')
    sortId: int
    template: str
    param: List[str]
    desc: str
    rewards: List[MissionDisplayRewards]
    playPoint: int


class ReturnDailyTaskData(BaseStruct):
    groupId: str
    id_: str = field(name='id')
    groupSortId: int
    taskSortId: int
    template: str
    param: List[str]
    desc: str
    rewards: List[MissionDisplayRewards]
    playPoint: int


class ReturnConst(BaseStruct):
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


class ReturnData(BaseStruct):
    constData: ReturnConst
    onceRewards: List[ItemBundle]
    intro: List[ReturnIntroData]
    returnDailyTaskDic: Dict[str, List[ReturnDailyTaskData]]
    returnLongTermTaskList: List[ReturnLongTermTaskData]
    creditsList: List[ItemBundle]
    checkinRewardList: List[ReturnCheckinData]


class OpenServerConst(BaseStruct):
    firstDiamondShardMailCount: int
    initApMailEndTs: int


class TotalCheckinData(BaseStruct):
    order: int
    item: OpenServerItemData
    colorId: int


class ChainLoginData(BaseStruct):
    order: int
    item: OpenServerItemData
    colorId: int


class MissionData(BaseStruct):
    id_: str = field(name='id')
    sortId: int
    description: str
    type_: str = field(name='type')
    itemBgType: str
    preMissionIds: None
    template: str
    templateType: str
    param: List[str]
    unlockCondition: None
    unlockParam: None
    missionGroup: str
    toPage: None
    periodicalPoint: int
    rewards: List[ItemBundle]
    backImagePath: None
    foldId: None
    haveSubMissionToUnlock: bool


class MissionGroup(BaseStruct):
    id_: str = field(name='id')
    title: None
    type_: str = field(name='type')
    preMissionGroup: None
    period: None
    rewards: None
    missionIds: List[str]
    startTs: int
    endTs: int


class OpenServerData(BaseStruct):
    openServerMissionGroup: MissionGroup
    openServerMissionData: List[MissionData]
    checkInData: List[TotalCheckinData]
    chainLoginData: List[ChainLoginData]


class OpenServerScheduleItem(BaseStruct):
    id_: str = field(name='id')
    startTs: int
    endTs: int
    totalCheckinDescption: str
    chainLoginDescription: str
    charImg: str


class ReturnConstV2(BaseStruct):
    startTime: int
    unlockLv: int
    unlockStage: str
    permMissionTime: int
    pointId: str
    returnPriceDesc: str
    dailySupplyDesc: str


class onceRewardDataV2(BaseStruct):
    groupId: str
    startTime: int
    endTime: int
    rewardList: List[RewardItem]


class ReturnCheckinDataV2RewardList(BaseStruct):
    sortId: int
    isImportant: bool
    rewardList: List[ItemBundle]


class CheckInRewardData(BaseStruct):
    groupId: str
    startTime: int
    endTime: int
    rewardList: List[ReturnCheckinDataV2RewardList]


class PriceRewardDataV2Content(BaseStruct):
    contentId: str
    sortId: int
    pointRequire: int
    desc: str
    iconId: str
    topIconId: str
    rewardList: List[RewardItem]


class PriceRewardDataV2(BaseStruct):
    groupId: str
    startTime: int
    endTime: int
    contentList: List[PriceRewardDataV2Content]


class MissionGroupDataV2Mission(BaseStruct):
    missionId: str
    groupId: str
    sortId: int
    jumpType: str
    jumpParam: Union[str, None]
    desc: str
    rewardList: List[ItemBundle]


class MissionGroupDataV2(BaseStruct):
    groupId: str
    sortId: int
    tabTitle: str
    title: str
    desc: str
    diffMissionCount: int
    startTime: int
    endTime: int
    imageId: str
    iconId: str
    missionList: List[MissionGroupDataV2Mission]


class SailySupplyDataV2(BaseStruct):
    groupId: str
    startTime: int
    endTime: int
    rewardList: List[ItemBundle]


class PackageCheckInRewardDataV2(BaseStruct):
    groupId: str
    startTime: int
    endTime: int
    getTime: int
    bindGPGoodId: str
    totalCheckInDay: int
    iconId: str
    rewardDict: Dict[str, List[RewardItem]]


class ReturnDataV2(BaseStruct):
    constData: ReturnConstV2
    onceRewardData: List[onceRewardDataV2]
    checkInRewardData: List[CheckInRewardData]
    priceRewardData: List[PriceRewardDataV2]
    missionGroupData: List[MissionGroupDataV2]
    dailySupplyData: List[SailySupplyDataV2]
    packageCheckInRewardData: List[PackageCheckInRewardDataV2]


class CheckInRewardItem(BaseStruct):
    orderNum: int
    itemBundle: ItemBundle


class OpenServerNewbieCheckInPackage(BaseStruct):
    groupId: str
    startTime: int
    endTime: int
    bindGPGoodId: str
    checkInDuration: int
    totalCheckInDay: int
    iconId: str
    checkInRewardDict: Dict[str, List[CheckInRewardItem]]


class OpenServerTable(BaseStruct):
    __version__ = '23-12-02-09-28-50-918524'

    schedule: List[OpenServerScheduleItem]
    dataMap: Dict[str, OpenServerData]
    constant: OpenServerConst
    playerReturn: ReturnData
    playerReturnV2: ReturnDataV2
    newbieCheckInPackageList: List[OpenServerNewbieCheckInPackage]
