from pydantic import BaseModel, Field


class ItemBundle(BaseModel):
    id_: str = Field(alias='id')
    count: int
    type_: str = Field(alias='type')


class ClimbTowerSingleTowerDataClimbTowerTaskRewardData(BaseModel):
    levelNum: int
    rewards: list[ItemBundle]


class ClimbTowerSingleTowerData(BaseModel):
    id_: str = Field(alias='id')
    sortId: int
    stageNum: int
    name: str
    subName: str
    desc: str
    towerType: str
    levels: list[str]
    hardLevels: list[str] | None
    taskInfo: list[ClimbTowerSingleTowerDataClimbTowerTaskRewardData] | None
    preTowerId: str | None
    medalId: str | None
    hiddenMedalId: str | None
    hardModeMedalId: str | None
    bossId: str | None
    cardId: str | None
    curseCardIds: list[str]
    dangerDesc: str
    hardModeDesc: str | None


class WeightItemBundle(BaseModel):
    id_: str = Field(alias='id')
    type_: str = Field(alias='type')
    dropType: str
    count: int
    weight: int


class StageDataDisplayRewards(BaseModel):
    type_: str = Field(alias='type')
    id_: str = Field(alias='id')
    dropType: int


class StageDataDisplayDetailRewards(BaseModel):
    occPercent: int
    type_: str = Field(alias='type')
    id_: str = Field(alias='id')
    dropType: int


class ClimbTowerDropDisplayInfo(BaseModel):
    itemId: str
    type_: int = Field(alias='type')
    maxCount: int
    minCount: int


class ClimbTowerLevelDropInfo(BaseModel):
    passRewards: list[list[WeightItemBundle]] | None = None
    displayRewards: list[StageDataDisplayRewards] | None
    displayDetailRewards: list[StageDataDisplayDetailRewards] | None
    displayDropInfo: dict[str, ClimbTowerDropDisplayInfo] | None = None


class ClimbTowerSingleLevelData(BaseModel):
    id_: str = Field(alias='id')
    levelId: str
    towerId: str
    layerNum: int
    code: str
    name: str
    desc: str
    levelType: str
    loadingPicId: str
    dropInfo: ClimbTowerLevelDropInfo


class ClimbTowerTacticalBuffData(BaseModel):
    id_: str = Field(alias='id')
    desc: str
    profession: str
    isDefaultActive: bool
    sortId: int
    buffType: str


class RuneDataSelector(BaseModel):
    professionMask: int | str
    buildableMask: int
    charIdFilter: list[str] | None
    enemyIdFilter: list[str] | None
    enemyIdExcludeFilter: list[str] | None
    skillIdFilter: list[str] | None
    tileKeyFilter: list[str] | None
    groupTagFilter: list[str] | None
    filterTagFilter: list[str] | None


class Blackboard(BaseModel):
    key: str
    value: float | None = None
    valueStr: str | None = None


class RuneData(BaseModel):
    key: str
    selector: RuneDataSelector
    blackboard: list[Blackboard]


class RuneTablePackedRuneData(BaseModel):
    id_: str = Field(alias='id')
    points: float
    mutexGroupKey: str | None
    description: str
    runes: list[RuneData]


class ClimbTowerMainCardData(BaseModel):
    id_: str = Field(alias='id')
    type_: str = Field(alias='type')
    linkedTowerId: str | None
    sortId: int
    name: str
    desc: str
    subCardIds: list[str]
    runeData: RuneTablePackedRuneData
    trapIds: list[str]


class ClimbTowerSubCardData(BaseModel):
    id_: str = Field(alias='id')
    mainCardId: str
    sortId: int
    name: str
    desc: str
    runeData: RuneTablePackedRuneData
    trapIds: list[str]


class ClimbTowerCurseCardData(BaseModel):
    id_: str = Field(alias='id')
    towerIdList: list[str]
    name: str
    desc: str
    trapId: str


class ClimbTowerSeasonInfoData(BaseModel):
    id_: str = Field(alias='id')
    name: str
    startTs: int
    endTs: int
    towers: list[str]
    seasonCards: list[str]
    seasonColor: str


class ClimbTowerDetailConst(BaseModel):
    unlockLevelId: str
    unlockModuleNumRequirement: int
    lowerItemId: str
    lowerItemLimit: int
    higherItemId: str
    higherItemLimit: int
    initCharCount: int
    recruitStageSort: list[int] | None = None
    charRecruitTimes: int
    charRecruitChoiceCount: int
    subcardStageSort: int
    assistCharLimit: int
    firstClearTaskDesc: str
    subCardObtainDesc: str
    subGodCardUnlockDesc: str


class ClimbTowerRewardInfo(BaseModel):
    stageSort: int
    lowerItemCount: int
    higherItemCount: int


class MissionDisplayRewards(BaseModel):
    type_: str = Field(alias='type')
    id_: str = Field(alias='id')
    count: int


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
    toPage: str | None
    periodicalPoint: int
    rewards: list[MissionDisplayRewards] | None
    backImagePath: str | None
    foldId: str | None
    haveSubMissionToUnlock: bool


class ClimbTowerMissionData(MissionData):
    bindGodCardId: str | None
    missionBkg: str


class MissionGroup(BaseModel):
    id_: str = Field(alias='id')
    title: str | None
    type_: str = Field(alias='type')
    preMissionGroup: str | None
    period: list[int] | None
    rewards: list[MissionDisplayRewards]
    missionIds: list[str]
    startTs: int
    endTs: int


class ClimbTowerTable(BaseModel):
    __version__ = '23-07-27-18-50-06-aeb568'

    towers: dict[str, ClimbTowerSingleTowerData]
    levels: dict[str, ClimbTowerSingleLevelData]
    tacticalBuffs: dict[str, ClimbTowerTacticalBuffData]
    mainCards: dict[str, ClimbTowerMainCardData]
    subCards: dict[str, ClimbTowerSubCardData]
    curseCards: dict[str, ClimbTowerCurseCardData]
    seasonInfos: dict[str, ClimbTowerSeasonInfoData]
    detailConst: ClimbTowerDetailConst
    rewardInfoList: list[ClimbTowerRewardInfo]
    missionData: dict[str, ClimbTowerMissionData]
    missionGroup: dict[str, MissionGroup]

    class Config:
        extra = 'allow'
