from typing import Dict, List, Union

from ..common import BaseStruct

from msgspec import field


class Blackboard(BaseStruct):
    key: str
    value: Union[float, None] = None
    valueStr: Union[str, None] = None


class RoguelikeBuff(BaseStruct):
    key: str
    blackboard: List[Blackboard]


class RoguelikeOuterBuff(BaseStruct):
    level: int
    name: str
    iconId: str
    description: str
    usage: str
    key: str
    blackboard: List[Blackboard]
    buffId: Union[str, None] = None


class RoguelikeOutBuffData(BaseStruct):
    id_: str = field(name="id")
    buffs: Dict[str, RoguelikeOuterBuff]


class RoguelikeEndingData(BaseStruct):
    id_: str = field(name="id")
    backgroundId: str
    name: str
    description: str
    priority: int
    unlockItemId: Union[str, None]
    changeEndingDesc: None


class RoguelikeModeData(BaseStruct):
    id_: str = field(name="id")
    name: str
    canUnlockItem: int
    scoreFactor: float
    itemPools: List[str]
    difficultyDesc: str
    ruleDesc: str
    sortId: int
    unlockMode: str
    color: str


class RoguelikeChoiceSceneData(BaseStruct):
    id_: str = field(name="id")
    title: str
    description: str
    background: str


class RoguelikeChoiceData(BaseStruct):
    id_: str = field(name="id")
    title: str
    description: Union[str, None]
    type_: str = field(name="type")
    nextSceneId: Union[str, None]
    icon: Union[str, None]
    param: Dict[str, object]


class RoguelikeZoneData(BaseStruct):
    id_: str = field(name="id")
    name: str
    description: str
    endingDescription: str
    backgroundId: str
    subIconId: str


class RoguelikeStageData(BaseStruct):
    id_: str = field(name="id")
    linkedStageId: str
    levelId: str
    code: str
    name: str
    loadingPicId: str
    description: str
    eliteDesc: Union[str, None]
    isBoss: int
    isElite: int
    difficulty: str


class RoguelikeRelicFeature(BaseStruct):
    id_: str = field(name="id")
    buffs: List[RoguelikeBuff]


class RoguelikeUpgradeTicketFeature(BaseStruct):
    id_: str = field(name="id")
    profession: int
    rarity: int
    professionList: List[str]
    rarityList: List[int]


class RoguelikeRecruitTicketFeature(BaseStruct):
    id_: str = field(name="id")
    profession: int
    rarity: int
    professionList: List[str]
    rarityList: List[int]
    extraEliteNum: int
    extraFreeRarity: List[Union[int, None]]
    extraCharIds: List[str]


class RelicStableUnlockParam(BaseStruct):
    unlockCondDetail: str
    unlockCnt: int


class RoguelikeItemData(BaseStruct):
    id_: str = field(name="id")
    name: str
    description: Union[str, None]
    usage: str
    obtainApproach: str
    iconId: str
    type_: str = field(name="type")
    rarity: str
    value: int
    sortId: int
    unlockCond: Union[str, None]
    unlockCondDesc: Union[str, None]
    unlockCondParams: List[Union[str, None]]
    stableUnlockCond: Union[RelicStableUnlockParam, None]


class RoguelikeItemTable(BaseStruct):
    items: Dict[str, RoguelikeItemData]
    recruitTickets: Dict[str, RoguelikeRecruitTicketFeature]
    upgradeTickets: Dict[str, RoguelikeUpgradeTicketFeature]
    relics: Dict[str, RoguelikeRelicFeature]


class RoguelikeConstTableEventTypeData(BaseStruct):
    name: str
    description: str


class RoguelikeConstTableCharUpgradeData(BaseStruct):
    evolvePhase: int
    skillLevel: int
    skillSpecializeLevel: int


class RoguelikeConstTableRecruitData(BaseStruct):
    recruitPopulation: int
    upgradePopulation: int


class RoguelikeConstTablePlayerLevelData(BaseStruct):
    exp: int
    populationUp: int
    squadCapacityUp: int
    battleCharLimitUp: int


class RoguelikeConstTable(BaseStruct):
    playerLevelTable: Dict[str, RoguelikeConstTablePlayerLevelData]
    recruitPopulationTable: Dict[str, RoguelikeConstTableRecruitData]
    charUpgradeTable: Dict[str, RoguelikeConstTableCharUpgradeData]
    eventTypeTable: Dict[str, RoguelikeConstTableEventTypeData]
    shopDialogs: List[str]
    shopRelicDialogs: List[str]
    shopTicketDialogs: List[str]
    mimicEnemyIds: List[str]
    clearZoneScores: List[int]
    moveToNodeScore: int
    clearNormalBattleScore: int
    clearEliteBattleScore: int
    clearBossBattleScore: int
    gainRelicScore: int
    gainCharacterScore: int
    unlockRelicSpecialScore: int
    squadCapacityMax: int
    bossIds: List[str]


class RoguelikeTable(BaseStruct):
    __version__ = "24-02-02-10-18-07-831ad8"

    constTable: RoguelikeConstTable
    itemTable: RoguelikeItemTable
    stages: Dict[str, RoguelikeStageData]
    zones: Dict[str, RoguelikeZoneData]
    choices: Dict[str, RoguelikeChoiceData]
    choiceScenes: Dict[str, RoguelikeChoiceSceneData]
    modes: Dict[str, RoguelikeModeData]
    endings: Dict[str, RoguelikeEndingData]
    outBuffs: Dict[str, RoguelikeOutBuffData]
