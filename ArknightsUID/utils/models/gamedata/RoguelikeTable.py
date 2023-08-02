from pydantic import BaseModel, Field


class Blackboard(BaseModel):
    key: str
    value: float | None = None
    valueStr: str | None = None


class RoguelikeBuff(BaseModel):
    key: str
    blackboard: list[Blackboard]


class RoguelikeOuterBuff(BaseModel):
    buffId: str | None = None
    level: int
    name: str
    iconId: str
    description: str
    usage: str
    key: str
    blackboard: list[Blackboard]


class RoguelikeOutBuffData(BaseModel):
    id_: str = Field(alias='id')
    buffs: dict[str, RoguelikeOuterBuff]


class RoguelikeEndingData(BaseModel):
    id_: str = Field(alias='id')
    backgroundId: str
    name: str
    description: str
    priority: int
    unlockItemId: str | None
    changeEndingDesc: None


class RoguelikeModeData(BaseModel):
    id_: str = Field(alias='id')
    name: str
    canUnlockItem: int
    scoreFactor: float
    itemPools: list[str]
    difficultyDesc: str
    ruleDesc: str
    sortId: int
    unlockMode: str
    color: str


class RoguelikeChoiceSceneData(BaseModel):
    id_: str = Field(alias='id')
    title: str
    description: str
    background: str


class RoguelikeChoiceData(BaseModel):
    id_: str = Field(alias='id')
    title: str
    description: str | None
    type_: str = Field(alias='type')
    nextSceneId: str | None
    icon: str | None
    param: dict[str, object]


class RoguelikeZoneData(BaseModel):
    id_: str = Field(alias='id')
    name: str
    description: str
    endingDescription: str
    backgroundId: str
    subIconId: str


class RoguelikeStageData(BaseModel):
    id_: str = Field(alias='id')
    linkedStageId: str
    levelId: str
    code: str
    name: str
    loadingPicId: str
    description: str
    eliteDesc: str | None
    isBoss: int
    isElite: int
    difficulty: str


class RoguelikeRelicFeature(BaseModel):
    id_: str = Field(alias='id')
    buffs: list[RoguelikeBuff]


class RoguelikeUpgradeTicketFeature(BaseModel):
    id_: str = Field(alias='id')
    profession: int
    rarity: int
    professionList: list[str]
    rarityList: list[int]


class RoguelikeRecruitTicketFeature(BaseModel):
    id_: str = Field(alias='id')
    profession: int
    rarity: int
    professionList: list[str]
    rarityList: list[int]
    extraEliteNum: int
    extraFreeRarity: list[int | None]
    extraCharIds: list[str]


class RelicStableUnlockParam(BaseModel):
    unlockCondDetail: str
    unlockCnt: int


class RoguelikeItemData(BaseModel):
    id_: str = Field(alias='id')
    name: str
    description: str | None
    usage: str
    obtainApproach: str
    iconId: str
    type_: str = Field(alias='type')
    rarity: str
    value: int
    sortId: int
    unlockCond: str | None
    unlockCondDesc: str | None
    unlockCondParams: list[str | None]
    stableUnlockCond: RelicStableUnlockParam | None


class RoguelikeItemTable(BaseModel):
    items: dict[str, RoguelikeItemData]
    recruitTickets: dict[str, RoguelikeRecruitTicketFeature]
    upgradeTickets: dict[str, RoguelikeUpgradeTicketFeature]
    relics: dict[str, RoguelikeRelicFeature]


class RoguelikeConstTableEventTypeData(BaseModel):
    name: str
    description: str


class RoguelikeConstTableCharUpgradeData(BaseModel):
    evolvePhase: int
    skillLevel: int
    skillSpecializeLevel: int


class RoguelikeConstTableRecruitData(BaseModel):
    recruitPopulation: int
    upgradePopulation: int


class RoguelikeConstTablePlayerLevelData(BaseModel):
    exp: int
    populationUp: int
    squadCapacityUp: int
    battleCharLimitUp: int


class RoguelikeConstTable(BaseModel):
    playerLevelTable: dict[str, RoguelikeConstTablePlayerLevelData]
    recruitPopulationTable: dict[str, RoguelikeConstTableRecruitData]
    charUpgradeTable: dict[str, RoguelikeConstTableCharUpgradeData]
    eventTypeTable: dict[str, RoguelikeConstTableEventTypeData]
    shopDialogs: list[str]
    shopRelicDialogs: list[str]
    shopTicketDialogs: list[str]
    mimicEnemyIds: list[str]
    clearZoneScores: list[int]
    moveToNodeScore: int
    clearNormalBattleScore: int
    clearEliteBattleScore: int
    clearBossBattleScore: int
    gainRelicScore: int
    gainCharacterScore: int
    unlockRelicSpecialScore: int
    squadCapacityMax: int
    bossIds: list[str]


class RoguelikeTable(BaseModel):
    __version__ = '23-07-27-18-50-06-aeb568'

    constTable: RoguelikeConstTable
    itemTable: RoguelikeItemTable
    stages: dict[str, RoguelikeStageData]
    zones: dict[str, RoguelikeZoneData]
    choices: dict[str, RoguelikeChoiceData]
    choiceScenes: dict[str, RoguelikeChoiceSceneData]
    modes: dict[str, RoguelikeModeData]
    endings: dict[str, RoguelikeEndingData]
    outBuffs: dict[str, RoguelikeOutBuffData]

    class Config:
        extra = 'allow'
