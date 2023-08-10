from msgspec import Struct, field

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
    max_: int = field(name='max')
    lastApAddTime: int
    completeRecoveryTime: int


class UserGameStatusSecretary(Struct):
    charId: str
    skinId: str


class UserGameStatusAvatar(Struct):
    type_: str = field(name='type')
    id_: str = field(name='id')


class UserGameStatus(Struct):
    uid: str
    name: str
    level: int
    avatar: UserGameStatusAvatar
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


class UserMeInfoRts(Struct):
    liked: str
    collect: str
    comment: str
    follow: str
    fans: str
    black: str
    pub: str


class UserMeInfo(Struct):
    id_: str = field(name='id')
    nickname: str
    profile: str
    avatarCode: int
    avatar: str
    backgroundCode: int
    isCreator: bool
    creatorIdentifiers: list[str]
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
    userSanctionList: list[str]
    gameStatus: UserGameStatus
    moderator: UserMeModerator
    userInfoApply: UserMeInfoApply

################
# ArknightsUserMeModel End
################



################
# ArknightsPlayerInfoModel Start
################

class PlayerSkinAsset(Struct):
    pass


class PlayerCharAsset(Struct):
    pass


class PlayerManufactureFormulaInfo(Struct):
    id_: str = field(name='id')
    itemId: str
    count: int
    weight: int
    costs: list[str]
    costPoint: int


class PlayerEquipmentInfo(Struct):
    id_: str = field(name='id')
    name: str
    desc: str
    typeIcon: str
    typeName1: str
    shiningColor: str


class PlayerCampaignZoneInfo(Struct):
    id_: str = field(name='id')
    name: str


class PlayerMedalInfo(Struct):
    pass


class PlayerCampaignInfo(Struct):
    id_: str = field(name='id')
    name: str
    campaignZoneId: str


class PlayerRogueInfo(Struct):
    id_: str = field(name='id')
    name: str
    sort: int


class PlayerTowerInfo(Struct):
    id_: str = field(name='id')
    name: str
    subName: str
    hasHard: bool
    stageNum: int


class PlayerZoneInfo(Struct):
    id_: str = field(name='id')
    name: str


class PlayerActivityInfo(Struct):
    id_: str = field(name='id')
    name: str
    startTime: int
    endTime: int
    rewardEndTime: int
    isReplicate: bool
    type_: str = field(name='type')


class PlayerStageInfo(Struct):
    id_: str = field(name='id')
    code: str
    name: str


class PlayerSkinInfo(Struct):
    id_: str = field(name='id')
    name: str
    brandId: str
    brandName: str
    brandCapitalName: str
    illustId: str
    dynIllustId: str
    avatarId: str
    portraitId: str
    sortId: int
    displayTagId: str
    skinGroupId: str


class PlayerCharInfo(Struct):
    id_: str = field(name='id')
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
    stageStatus: list[ActivityZoneStageStatus]


class PlayerActivity(Struct):
    actId: str
    actReplicaId: str
    type_: str = field(name='type')
    zones: list[ActivityZone]


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
    clearTime: int
    relicCnt: int
    bank: BankItem
    mission: RewoardItem


class PlayerRogue(Struct):
    records: list[RogueRecord]


class TowerReward(Struct):
    higherItem: RewoardItem
    lowerItem: RewoardItem
    termTs: int


class TowerRecord(Struct):
    towerId: str
    best: int
    hasHard: bool
    stageNum: int
    unlockHard: bool
    hardBest: int


class PlayerTower(Struct):
    records: list[TowerRecord]
    reward: TowerReward


class CampaignReward(Struct):
    current: int
    total: int


class CampaignRecord(Struct):
    campaignId: str
    maxKills: int


class PlayerCampaign(Struct):
    records: list[CampaignRecord]
    reward: CampaignReward


class RecruitTag(Struct):
    tagId: int
    pick: int


class PlayerRecruit(Struct):
    startTs: int
    finishTs: int
    duration: int
    selectTags: list[RecruitTag | None]
    state: int


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
    board: list[str]
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
    chars: list[BuildingChar]


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
    trainee: BuildingTrainingTrainee
    trainer: BuildingTrainingTrainer
    remainPoint: float
    speed: float
    lastUpdateTime: int
    remainSecs: int
    slotState: int


class BuildingHire(Struct):
    slotId: str
    level: int
    chars: list[BuildingChar]
    state: int
    refreshCount: int
    completeWorkTime: int
    slotState: int


class BuildingMeeting(Struct):
    slotId: str
    level: int
    chars: list[BuildingChar]
    clue: BuildingClue
    lastUpdateTime: int
    completeWorkTime: int


class BuildingDormitories(Struct):
    slotId: str
    level: int
    chars: list[BuildingChar]
    comfort: int


class BuildingTradings(Struct):
    slotId: str
    level: int
    chars: list[BuildingChar]
    completeWorkTime: int
    lastUpdateTime: int
    strategy: str
    stock: list[int]
    stockLimit: int


class BuildingManufactures(Struct):
    slotId: str
    level: int
    chars: list[BuildingChar]
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
    chars: list[BuildingChar]


class PlayerBuilding(Struct):
    tiredChars: list[str]
    powers: list[BuildingPower]
    manufactures: list[BuildingManufactures]
    tradings: list[BuildingTradings]
    dormitories: list[BuildingDormitories]
    meeting: BuildingMeeting
    hire: BuildingHire
    training: BuildingTraining
    labor: BuildingLabor
    furniture: BuildingFurniture
    elevators: list[BuildingElevator]
    corridors: list[BuildingCorridor]
    control: BuildingControl


class PlayerInfoSkin(Struct):
    id_: str = field(name='id')
    ts: int


class PlayerInfoCharSkill(Struct):
    id_: str = field(name='id')
    specializeLevel: int


class PlayerInfoCharEquip(Struct):
    id_: str = field(name='id')
    level: int


class PlayerInfoChar(Struct):
    charId: str
    skinId: str
    level: int
    evolvePhase: int
    potentialRank: int
    mainSkillLvl: int
    skills: list[PlayerInfoCharSkill] | None
    equip: list[PlayerInfoCharEquip] | None
    favorPercent: int
    defaultSkillId: str
    gainTime: int
    defaultEquipId: str


class PlayerAssistCharEquip(Struct):
    id_: str = field(name='id')
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
    equip: PlayerAssistCharEquip | None


class PlayerMedal(Struct):
    type_: str = field(name='type')
    template: str
    templateMedallist: list[str]
    customMedalLayout: list[str]
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
    type_: str = field(name='type')
    id_: str = field(name='id')


class PlayerStatus(Struct):
    uid: str
    name: str
    level: int
    avatar: PlayerStatusAvatar
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


class DisplayShowConfig(Struct):
    charSwitch: bool
    skinSwitch: bool
    standingsSwitch: bool


class ArknightsPlayerInfoModel(Struct, omit_defaults=True, gc=False):
    currentTs: int
    showConfig: DisplayShowConfig
    status: PlayerStatus
    medal: PlayerMedal
    assistChars: list[PlayerAssistChar]
    chars: list[PlayerInfoChar]
    skins: list[PlayerInfoSkin]
    building: PlayerBuilding
    recruit: list[PlayerRecruit]
    campaign: PlayerCampaign
    tower: PlayerTower
    rogue: PlayerRogue
    routine: PlayerRoutine
    activity: list[PlayerActivity]
    charInfoMap: dict[str, PlayerCharInfo]
    skinInfoMap: dict[str, PlayerSkinInfo]
    stageInfoMap: dict[str, PlayerStageInfo]
    activityInfoMap: dict[str, PlayerActivityInfo]
    zoneInfoMap: dict[str, PlayerZoneInfo]
    towerInfoMap: dict[str, PlayerTowerInfo]
    rogueInfoMap: dict[str, PlayerRogueInfo]
    campaignInfoMap: dict[str, PlayerCampaignInfo]
    medalInfoMap: dict[str, PlayerMedalInfo]
    campaignZoneInfoMap: dict[str, PlayerCampaignZoneInfo]
    equipmentInfoMap: dict[str, PlayerEquipmentInfo]
    manufactureFormulaInfoMap: dict[str, PlayerManufactureFormulaInfo]
    charAssets: list[PlayerCharAsset]
    skinAssets: list[PlayerSkinAsset]


################
# ArknightsPlayerInfoModel End
################
