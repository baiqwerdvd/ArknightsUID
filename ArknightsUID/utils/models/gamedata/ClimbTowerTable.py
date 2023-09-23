from typing import Dict, List, Union
from ..common import BaseStruct
from msgspec import field


class ItemBundle(BaseStruct):
    id_: str = field(name='id')
    count: int
    type_: str = field(name='type')


class ClimbTowerSingleTowerDataClimbTowerTaskRewardData(BaseStruct):
    levelNum: int
    rewards: List[ItemBundle]


class ClimbTowerSingleTowerData(BaseStruct):
    id_: str = field(name='id')
    sortId: int
    stageNum: int
    name: str
    subName: str
    desc: str
    towerType: str
    levels: List[str]
    hardLevels: Union[List[str], None]
    taskInfo: Union[List[ClimbTowerSingleTowerDataClimbTowerTaskRewardData], None]
    preTowerId: Union[str, None]
    medalId: Union[str, None]
    hiddenMedalId: Union[str, None]
    hardModeMedalId: Union[str, None]
    bossId: Union[str, None]
    cardId: Union[str, None]
    curseCardIds: List[str]
    dangerDesc: str
    hardModeDesc: Union[str, None]


class WeightItemBundle(BaseStruct):
    id_: str = field(name='id')
    type_: str = field(name='type')
    dropType: str
    count: int
    weight: int


class StageDataDisplayRewards(BaseStruct):
    type_: str = field(name='type')
    id_: str = field(name='id')
    dropType: int


class StageDataDisplayDetailRewards(BaseStruct):
    occPercent: int
    type_: str = field(name='type')
    id_: str = field(name='id')
    dropType: int


class ClimbTowerDropDisplayInfo(BaseStruct):
    itemId: str
    type_: int = field(name='type')
    maxCount: int
    minCount: int


class ClimbTowerLevelDropInfo(BaseStruct):
    displayRewards: Union[List[StageDataDisplayRewards], None]
    displayDetailRewards: Union[List[StageDataDisplayDetailRewards], None]
    passRewards: Union[List[List[WeightItemBundle]], None] = None
    displayDropInfo: Union[Dict[str, ClimbTowerDropDisplayInfo], None] = None


class ClimbTowerSingleLevelData(BaseStruct):
    id_: str = field(name='id')
    levelId: str
    towerId: str
    layerNum: int
    code: str
    name: str
    desc: str
    levelType: str
    loadingPicId: str
    dropInfo: ClimbTowerLevelDropInfo


class ClimbTowerTacticalBuffData(BaseStruct):
    id_: str = field(name='id')
    desc: str
    profession: str
    isDefaultActive: bool
    sortId: int
    buffType: str


class RuneDataSelector(BaseStruct):
    professionMask: Union[int, str]
    buildableMask: int
    charIdFilter: Union[List[str], None]
    enemyIdFilter: Union[List[str], None]
    enemyIdExcludeFilter: Union[List[str], None]
    skillIdFilter: Union[List[str], None]
    tileKeyFilter: Union[List[str], None]
    groupTagFilter: Union[List[str], None]
    filterTagFilter: Union[List[str], None]
    subProfessionExcludeFilter: Union[List[str], None]


class Blackboard(BaseStruct):
    key: str
    value: Union[float, None] = None
    valueStr: Union[str, None] = None


class RuneData(BaseStruct):
    key: str
    selector: RuneDataSelector
    blackboard: List[Blackboard]


class RuneTablePackedRuneData(BaseStruct):
    id_: str = field(name='id')
    points: float
    mutexGroupKey: Union[str, None]
    description: str
    runes: List[RuneData]


class ClimbTowerMainCardData(BaseStruct):
    id_: str = field(name='id')
    type_: str = field(name='type')
    linkedTowerId: Union[str, None]
    sortId: int
    name: str
    desc: str
    subCardIds: List[str]
    runeData: RuneTablePackedRuneData
    trapIds: List[str]


class ClimbTowerSubCardData(BaseStruct):
    id_: str = field(name='id')
    mainCardId: str
    sortId: int
    name: str
    desc: str
    runeData: RuneTablePackedRuneData
    trapIds: List[str]


class ClimbTowerCurseCardData(BaseStruct):
    id_: str = field(name='id')
    towerIdList: List[str]
    name: str
    desc: str
    trapId: str


class ClimbTowerSeasonInfoData(BaseStruct):
    id_: str = field(name='id')
    name: str
    startTs: int
    endTs: int
    towers: List[str]
    seasonCards: List[str]
    seasonColor: str


class ClimbTowerDetailConst(BaseStruct):
    unlockLevelId: str
    unlockModuleNumRequirement: int
    lowerItemId: str
    lowerItemLimit: int
    higherItemId: str
    higherItemLimit: int
    initCharCount: int
    charRecruitTimes: int
    charRecruitChoiceCount: int
    subcardStageSort: int
    assistCharLimit: int
    firstClearTaskDesc: str
    subCardObtainDesc: str
    subGodCardUnlockDesc: str
    recruitStageSort: Union[List[int], None] = None


class ClimbTowerRewardInfo(BaseStruct):
    stageSort: int
    lowerItemCount: int
    higherItemCount: int


class MissionDisplayRewards(BaseStruct):
    type_: str = field(name='type')
    id_: str = field(name='id')
    count: int


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
    toPage: Union[str, None]
    periodicalPoint: int
    rewards: Union[List[MissionDisplayRewards], None]
    backImagePath: Union[str, None]
    foldId: Union[str, None]
    haveSubMissionToUnlock: bool


class ClimbTowerMissionData(MissionData):
    bindGodCardId: Union[str, None]
    missionBkg: str


class MissionGroup(BaseStruct):
    id_: str = field(name='id')
    title: Union[str, None]
    type_: str = field(name='type')
    preMissionGroup: Union[str, None]
    period: Union[List[int], None]
    rewards: List[MissionDisplayRewards]
    missionIds: List[str]
    startTs: int
    endTs: int


class ClimbTowerTable(BaseStruct):
    __version__ = '23-07-27-18-50-06-aeb568'

    towers: Dict[str, ClimbTowerSingleTowerData]
    levels: Dict[str, ClimbTowerSingleLevelData]
    tacticalBuffs: Dict[str, ClimbTowerTacticalBuffData]
    mainCards: Dict[str, ClimbTowerMainCardData]
    subCards: Dict[str, ClimbTowerSubCardData]
    curseCards: Dict[str, ClimbTowerCurseCardData]
    seasonInfos: Dict[str, ClimbTowerSeasonInfoData]
    detailConst: ClimbTowerDetailConst
    rewardInfoList: List[ClimbTowerRewardInfo]
    missionData: Dict[str, ClimbTowerMissionData]
    missionGroup: Dict[str, MissionGroup]
