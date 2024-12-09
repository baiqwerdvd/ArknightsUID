from typing import Dict, List, Union

from msgspec import Struct, field


################
# ArknightsAttendanceCalendar Start
################
class ArknightsAttendanceRecord(Struct):
    ts: str
    resourceId: str
    type_: str = field(name="type")
    count: int


class ArknightsAttendanceCalendar(Struct):
    resourceId: str
    type_: str = field(name="type")
    count: int
    available: bool
    done: bool


class ArknightsAttendanceStageDropListItem(Struct):
    stageId: str
    occPer: int


class ArknightsAttendanceBuildingProductListItem(Struct):
    formulaId: str
    roomType: str


class ArknightsAttendanceAwardResource(Struct):
    id_: str = field(name="id")
    type_: str = field(name="type")
    name: str
    rarity: int
    sortId: int
    otherSource: List[str]
    classifyType: str
    stageDropList: List[ArknightsAttendanceStageDropListItem]
    buildingProductList: List[ArknightsAttendanceBuildingProductListItem]

class ArknightsAttendanceCalendarModel(Struct):
    currentTs: str
    calendar: List[ArknightsAttendanceCalendar]
    records: List[Union[ArknightsAttendanceRecord, None]]
    resourceInfoMap: Dict[str, ArknightsAttendanceAwardResource]


################
# ArknightsAttendance Start
################
class ArknightsAttendanceAward(Struct):
    resource: ArknightsAttendanceAwardResource
    count: int
    type_: str = field(name="type")


class ArknightsAttendanceModel(Struct):
    ts: str
    awards: List[ArknightsAttendanceAward]
    resourceInfoMap: dict


################
# ArknightsAttendance End
################


################
# ArknightsUserMeModel Start
################


class UserMeInfoApply(Struct):
    nickname: str
    profile: str


class UserMeModerator(Struct):
    isModerator: bool


class UserGameStatusAp(Struct):
    current: int
    max_: int = field(name="max")
    lastApAddTime: int
    completeRecoveryTime: int


class UserGameStatusSecretary(Struct):
    charId: str
    skinId: str


class UserGameStatusAvatar(Struct):
    type_: str = field(name="type")
    id_: str = field(name="id")


class UserGameStatus(Struct):
    uid: str
    name: str
    level: int
    registerTs: int
    mainStageProgress: str
    secretary: UserGameStatusSecretary
    resume: str
    subscriptionEnd: int
    ap: UserGameStatusAp
    storeTs: int
    lastOnlineTs: int
    charCnt: int
    furnitureCnt: int
    skinCnt: int
    avatar: Union[UserGameStatusAvatar, None] = None


class UserMeInfoRts(Struct):
    liked: str
    collect: str
    comment: str
    follow: str
    fans: str
    black: str
    pub: str


class UserMeInfo(Struct):
    id_: str = field(name="id")
    nickname: str
    profile: str
    avatarCode: int
    avatar: str
    backgroundCode: int
    isCreator: bool
    creatorIdentifiers: List[str]
    status: int
    operationStatus: int
    identity: int
    kind: int
    latestIpLocation: str
    moderatorStatus: int
    moderatorChangeTime: int
    gender: int
    birthday: str


class ArknightsUserMeModel(Struct, omit_defaults=True):
    user: UserMeInfo
    userRts: UserMeInfoRts
    userSanctionList: List[str]
    gameStatus: UserGameStatus
    moderator: UserMeModerator
    userInfoApply: UserMeInfoApply


################
# ArknightsUserMeModel End
################


################
# ArknightsPlayerInfoModel Start
################


class PlayerManufactureFormulaInfo(Struct):
    id_: str = field(name="id")
    itemId: str
    count: int
    weight: int
    costPoint: int
    costs: Union[List[str], None] = None


class PlayerEquipmentInfo(Struct):
    id_: str = field(name="id")
    name: str
    typeIcon: str
    shiningColor: str
    desc: Union[str, None] = None
    typeName1: Union[str, None] = None


class PlayerCampaignZoneInfo(Struct):
    id_: str = field(name="id")
    name: str


class PlayerMedalInfo(Struct):
    pass


class PlayerCampaignInfo(Struct):
    id_: str = field(name="id")
    name: str
    campaignZoneId: str


class PlayerRogueInfo(Struct):
    id_: str = field(name="id")
    name: str
    sort: int


class PlayerTowerInfo(Struct):
    id_: str = field(name="id")
    name: str
    subName: str
    hasHard: Union[bool, None] = None
    stageNum: Union[int, None] = None


class PlayerZoneInfo(Struct):
    id_: str = field(name="id")
    name: str


class PlayerActivityInfo(Struct):
    id_: str = field(name="id")
    name: str
    startTime: int
    endTime: int
    rewardEndTime: int
    isReplicate: bool
    type_: str = field(name="type")


class PlayerStageInfo(Struct):
    id_: str = field(name="id")
    code: str
    name: str


class PlayerSkinInfo(Struct):
    id_: str = field(name="id")
    brandId: str
    sortId: int
    displayTagId: str
    name: Union[str, None] = None
    brandName: Union[str, None] = None
    brandCapitalName: Union[str, None] = None
    illustId: Union[str, None] = None
    dynIllustId: Union[str, None] = None
    avatarId: Union[str, None] = None
    portraitId: Union[str, None] = None
    skinGroupId: Union[str, None] = None


class PlayerCharInfo(Struct):
    id_: str = field(name="id")
    name: str
    nationId: str
    groupId: str
    displayNumber: str
    rarity: int
    profession: str
    subProfessionId: str


class ActivityZoneStageStatus(Struct):
    stageId: str
    completed: bool


class ActivityZone(Struct):
    zoneId: str
    zoneReplicaId: str
    clearedStage: int
    totalStage: int
    stageStatus: Union[List[ActivityZoneStageStatus], None] = None


class PlayerActivity(Struct):
    actId: str
    actReplicaId: str
    zones: List[ActivityZone]
    type_: Union[str, None] = field(name="type", default=None)


class RewoardItem(Struct):
    current: int
    total: int


class PlayerRoutine(Struct):
    daily: RewoardItem
    weekly: RewoardItem


class BankItem(Struct):
    current: int
    record: int


class RogueRecord(Struct):
    rogueId: str
    relicCnt: int
    bank: BankItem
    mission: Union[RewoardItem, None] = None
    clearTime: Union[int, None] = None


class PlayerRogue(Struct):
    records: List[RogueRecord]


class TowerReward(Struct):
    higherItem: RewoardItem
    lowerItem: RewoardItem
    termTs: int


class TowerRecord(Struct):
    towerId: str
    best: int
    hasHard: Union[bool, None] = None
    stageNum: Union[int, None] = None
    unlockHard: Union[bool, None] = None
    hardBest: Union[int, None] = None


class PlayerTower(Struct):
    records: List[TowerRecord]
    reward: TowerReward


class CampaignReward(Struct):
    current: int
    total: int


class CampaignRecord(Struct):
    campaignId: str
    maxKills: int


class PlayerCampaign(Struct):
    records: List[CampaignRecord]
    reward: CampaignReward


class RecruitTag(Struct):
    tagId: int
    pick: int


class PlayerRecruit(Struct):
    startTs: int
    finishTs: int
    state: int
    duration: Union[int, None] = None
    selectTags: Union[List[RecruitTag], None] = None


class BuildingTrainingTrainee(Struct):
    charId: str
    targetSkill: int
    ap: int
    lastApAddTime: int


class BuildingTrainingTrainer(Struct):
    charId: str
    ap: int
    lastApAddTime: int


class BuildingClue(Struct):
    own: int
    received: int
    dailyReward: bool
    needReceive: int
    board: List[str]
    sharing: bool
    shareCompleteTime: int


class BuildingCharBubbleInfo(Struct):
    add: int
    ts: int


class BuildingCharBubble(Struct):
    normal: BuildingCharBubbleInfo
    assist: BuildingCharBubbleInfo


class BuildingChar(Struct):
    charId: str
    ap: int
    lastApAddTime: int
    index: int
    bubble: BuildingCharBubble
    workTime: int


class BuildingControl(Struct):
    slotId: str
    slotState: int
    level: int
    chars: List[BuildingChar]


class BuildingCorridor(Struct):
    slotId: str
    slotState: int
    level: int


class BuildingElevator(Struct):
    slotId: str
    slotState: int
    level: int


class BuildingFurniture(Struct):
    total: int


class BuildingLabor(Struct):
    maxValue: int
    value: int
    lastUpdateTime: int
    remainSecs: int


class BuildingTraining(Struct):
    slotId: str
    level: int
    remainPoint: float
    speed: float
    lastUpdateTime: int
    remainSecs: int
    slotState: int
    trainee: Union[BuildingTrainingTrainee, None]
    trainer: Union[BuildingTrainingTrainer, None]


class BuildingHire(Struct):
    slotId: str
    level: int
    chars: List[BuildingChar]
    state: int
    refreshCount: int
    completeWorkTime: int
    slotState: int


class BuildingMeeting(Struct):
    slotId: str
    level: int
    chars: List[BuildingChar]
    clue: BuildingClue
    lastUpdateTime: int
    completeWorkTime: int


class BuildingDormitories(Struct):
    slotId: str
    level: int
    chars: List[BuildingChar]
    comfort: int


class BuildingStockDelivery(Struct):
    id_: str = field(name="id")
    count: int
    type_: str = field(name="type")


class BuildingStock(Struct):
    instId: int
    type_: str = field(name="type")
    delivery: List[BuildingStockDelivery]
    gain: BuildingStockDelivery
    isViolated: bool


class BuildingTradings(Struct):
    slotId: str
    level: int
    chars: List[BuildingChar]
    completeWorkTime: int
    lastUpdateTime: int
    strategy: str
    stock: List[BuildingStock]
    stockLimit: int


class BuildingManufactures(Struct):
    slotId: str
    level: int
    chars: List[BuildingChar]
    completeWorkTime: int
    lastUpdateTime: int
    formulaId: str
    capacity: int
    weight: int
    complete: int
    remain: int
    speed: float


class BuildingPower(Struct):
    slotId: str
    level: int
    chars: List[BuildingChar]


class BuildingTiredChar(Struct):
    charId: str
    ap: int
    lastApAddTime: int
    roomSlotId: str
    index: int
    bubble: BuildingCharBubble
    workTime: int


class PlayerBuilding(Struct):
    tiredChars: Union[List[BuildingTiredChar], None]
    powers: Union[List[BuildingPower], None]
    manufactures: Union[List[BuildingManufactures], None]
    tradings: Union[List[BuildingTradings], None]
    dormitories: Union[List[BuildingDormitories], None]
    meeting: Union[BuildingMeeting, None]
    hire: Union[BuildingHire, None]
    labor: BuildingLabor
    furniture: BuildingFurniture
    elevators: List[BuildingElevator]
    corridors: Union[List[BuildingCorridor], None]
    control: BuildingControl
    training: Union[BuildingTraining, None] = None


class PlayerInfoSkin(Struct):
    id_: str = field(name="id")
    ts: int


class PlayerInfoCharSkill(Struct):
    id_: str = field(name="id")
    specializeLevel: int


class PlayerInfoCharEquip(Struct):
    id_: str = field(name="id")
    level: int


class PlayerInfoChar(Struct):
    charId: str
    skinId: str
    level: int
    evolvePhase: int
    potentialRank: int
    mainSkillLvl: int
    skills: Union[List[PlayerInfoCharSkill], None]
    equip: Union[List[PlayerInfoCharEquip], None]
    favorPercent: int
    defaultSkillId: str
    gainTime: int
    defaultEquipId: str
    specializeLevelCount: Union[int, None] = 0


class PlayerAssistCharEquip(Struct):
    id_: str = field(name="id")
    level: int


class PlayerAssistChar(Struct):
    charId: str
    skinId: str
    level: int
    evolvePhase: int
    potentialRank: int
    skillId: str
    mainSkillLvl: int
    specializeLevel: int
    equip: Union[PlayerAssistCharEquip, None]


class PlayerMedal(Struct):
    type_: str = field(name="type")
    template: str
    templateMedalList: List[str]
    customMedalLayout: List[Union[str, None]]
    total: int


class PlayerStatusAp(Struct):
    current: int
    max: int
    lastApAddTime: int
    completeRecoveryTime: int


class PlayerStatusSecretary(Struct):
    charId: str
    skinId: str


class PlayerStatusAvatar(Struct):
    type_: str = field(name="type")
    id_: str = field(name="id")
    url: str


class PlayerStatusExp(Struct):
    current: int
    max: int


class PlayerStatus(Struct):
    uid: str
    name: str
    level: int
    registerTs: int
    mainStageProgress: str
    secretary: PlayerStatusSecretary
    resume: str
    subscriptionEnd: int
    ap: PlayerStatusAp
    storeTs: int
    lastOnlineTs: int
    charCnt: int
    furnitureCnt: int
    skinCnt: int
    avatar: Union[PlayerStatusAvatar, None] = None
    exp: PlayerStatusExp


class DisplayShowConfig(Struct):
    charSwitch: bool
    skinSwitch: bool
    standingsSwitch: bool


class PlayerActivityBannerList(Struct):
    activityId: str
    imgUrl: str
    url: str
    startTs: int
    endTs: int


class ArknightsPlayerInfoModel(Struct, omit_defaults=True, gc=False):
    currentTs: int
    showConfig: DisplayShowConfig
    status: PlayerStatus
    assistChars: List[PlayerAssistChar]
    chars: List[PlayerInfoChar]
    skins: List[PlayerInfoSkin]
    building: PlayerBuilding
    recruit: List[PlayerRecruit]
    campaign: PlayerCampaign
    tower: PlayerTower
    rogue: PlayerRogue
    routine: PlayerRoutine
    activity: List[PlayerActivity]
    charInfoMap: Dict[str, PlayerCharInfo]
    skinInfoMap: Dict[str, PlayerSkinInfo]
    stageInfoMap: Dict[str, PlayerStageInfo]
    activityInfoMap: Dict[str, PlayerActivityInfo]
    towerInfoMap: Dict[str, PlayerTowerInfo]
    rogueInfoMap: Dict[str, PlayerRogueInfo]
    campaignInfoMap: Dict[str, PlayerCampaignInfo]
    campaignZoneInfoMap: Dict[str, PlayerCampaignZoneInfo]
    equipmentInfoMap: Dict[str, PlayerEquipmentInfo]
    manufactureFormulaInfoMap: Dict[str, PlayerManufactureFormulaInfo]
    charAssets: List[Union[str, None]]
    skinAssets: List[Union[str, None]]
    activityBannerList: Dict[str, List[PlayerActivityBannerList]]
    medal: Union[PlayerMedal, None] = None
    zoneInfoMap: Union[Dict[str, PlayerZoneInfo], None] = None
    medalInfoMap: Union[Dict[str, PlayerMedalInfo], None] = None


################
# ArknightsPlayerInfoModel End
################
