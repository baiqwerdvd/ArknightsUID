from typing import Dict, List, Union

from ..common import BaseStruct

from msgspec import field


class BuildingDataRoomUnlockCondCondItem(BaseStruct):
    type_: str = field(name='type')
    level: int
    count: int


class BuildingDataRoomUnlockCond(BaseStruct):
    id_: str = field(name='id')
    number: Dict[str, BuildingDataRoomUnlockCondCondItem]


class GridPosition(BaseStruct):
    row: int
    col: int


class ItemBundle(BaseStruct):
    id_: str = field(name='id')
    count: int
    type_: str = field(name='type')


class BuildingDataRoomDataBuildCost(BaseStruct):
    items: List[ItemBundle]
    time: int
    labor: int


class BuildingDataRoomDataPhaseData(BaseStruct):
    overrideName: Union[str, None]
    overridePrefabId: Union[str, None]
    unlockCondId: str
    buildCost: BuildingDataRoomDataBuildCost
    electricity: int
    maxStationedNum: int
    manpowerCost: int


class BuildingDataRoomData(BaseStruct):
    id_: str = field(name='id')
    name: str
    description: Union[str, None]
    defaultPrefabId: str
    canLevelDown: bool
    maxCount: int
    category: str
    size: GridPosition
    phases: List[BuildingDataRoomDataPhaseData]


class BuildingDataLayoutDataRoomSlot(BaseStruct):
    id_: str = field(name='id')
    cleanCostId: str
    costLabor: int
    provideLabor: int
    size: GridPosition
    offset: GridPosition
    category: str
    storeyId: str


class BuildingDataLayoutDataSlotCleanCostCountCost(BaseStruct):
    items: List[ItemBundle]


class BuildingDataLayoutDataSlotCleanCost(BaseStruct):
    id_: str = field(name='id')
    number: Dict[str, BuildingDataLayoutDataSlotCleanCostCountCost]


class BuildingDataLayoutDataStoreyData(BaseStruct):
    id_: str = field(name='id')
    yOffset: int
    unlockControlLevel: int
    type_: str = field(name='type')


class BuildingDataLayoutData(BaseStruct):
    id_: str = field(name='id')
    slots: Dict[str, BuildingDataLayoutDataRoomSlot]
    cleanCosts: Dict[str, BuildingDataLayoutDataSlotCleanCost]
    storeys: Dict[str, BuildingDataLayoutDataStoreyData]


class BuildingDataPrefabInfo(BaseStruct):
    id_: str = field(name='id')
    blueprintRoomOverrideId: Union[str, None]
    size: GridPosition
    floorGridSize: GridPosition
    backWallGridSize: GridPosition
    obstacleId: Union[str, None]


class BuildingDataManufactPhase(BaseStruct, tag='BuildingDataManufactPhase'):
    speed: Union[float, int]
    outputCapacity: int


class BuildingDataShopPhase(BaseStruct, tag='BuildingDataShopPhase'):
    counterNum: int
    speed: Union[float, int]
    moneyCapacity: int


class BuildingDataHirePhase(BaseStruct, tag='BuildingDataHirePhase'):
    economizeRate: float
    resSpeed: int
    refreshTimes: int


class BuildingDataDormPhase(BaseStruct, tag='BuildingDataDormPhase'):
    manpowerRecover: int
    decorationLimit: int


class BuildingDataMeetingPhase(BaseStruct, tag='BuildingDataMeetingPhase'):
    friendSlotInc: int
    maxVisitorNum: int
    gatheringSpeed: int


class BuildingDataTradingPhase(BaseStruct, tag='BuildingDataTradingPhase'):
    orderSpeed: Union[float, int]
    orderLimit: int
    orderRarity: int


class BuildingDataWorkshopPhase(BaseStruct, tag='BuildingDataWorkshopPhase'):
    manpowerFactor: Union[float, int]


class BuildingDataTrainingPhase(BaseStruct, tag='BuildingDataTrainingPhase'):
    specSkillLvlLimit: int


class BuildingDataShopRoomBean(BaseStruct):
    phases: None = None
    # phases: Union[List[Union[Union[Union[Union[Union[Union[Union[BuildingDataManufactPhase, BuildingDataShopPhase], BuildingDataHirePhase], BuildingDataDormPhase], BuildingDataMeetingPhase], BuildingDataTradingPhase], BuildingDataWorkshopPhase], BuildingDataTrainingPhase]], None]  # noqa: E501


class BuildingDataControlRoomBean(BaseStruct):
    basicCostBuff: int
    phases: None = None


class BuildingDataManufactRoomBean(BaseStruct):
    basicSpeedBuff: float
    phases: List[BuildingDataManufactPhase]


class BuildingDataHireRoomBean(BaseStruct):
    basicSpeedBuff: float
    phases: List[BuildingDataHirePhase]


class BuildingDataDormRoomBean(BaseStruct):
    phases: List[BuildingDataDormPhase]


class BuildingDataMeetingRoomBean(BaseStruct):
    basicSpeedBuff: float
    phases: List[BuildingDataMeetingPhase]


class BuildingDataTradingRoomBean(BaseStruct):
    basicSpeedBuff: float
    phases: List[BuildingDataTradingPhase]


class BuildingDataWorkShopRoomBean(BaseStruct):
    phases: List[BuildingDataWorkshopPhase]


class BuildingDataTrainingBean(BaseStruct):
    basicSpeedBuff: float
    phases: List[BuildingDataTrainingPhase]


class BuildingDataPowerRoomBean(BaseStruct):
    basicSpeedBuff: float
    phases: None = None


class CharacterDataUnlockCondition(BaseStruct):
    phase: int
    level: int


class BuildingDataBuildingBuffCharSlotSlotItem(BaseStruct):
    buffId: str
    cond: CharacterDataUnlockCondition


class BuildingDataBuildingBuffCharSlot(BaseStruct):
    buffData: List[BuildingDataBuildingBuffCharSlotSlotItem]


class BuildingDataBuildingCharacter(BaseStruct):
    charId: str
    maxManpower: int
    buffChar: List[BuildingDataBuildingBuffCharSlot]


class BuildingDataBuildingBuff(BaseStruct):
    buffId: str
    buffName: str
    buffIcon: str
    skillIcon: str
    sortId: int
    buffColor: str
    textColor: str
    buffCategory: str
    roomType: str
    description: str


class BuildingDataCustomDataFurnitureData(BaseStruct):
    id_: str = field(name='id')
    sortId: int
    name: str
    iconId: str
    type_: str = field(name='type')
    subType: str
    location: str
    category: str
    validOnRotate: bool
    enableRotate: bool
    rarity: int
    themeId: str
    groupId: str
    width: int
    depth: int
    height: int
    comfort: int
    usage: str
    description: str
    obtainApproach: str
    processedProductId: str
    processedProductCount: int
    processedByProductPercentage: int
    processedByProductGroup: List
    canBeDestroy: bool
    isOnly: int
    quantity: int
    musicId: str
    interactType: Union[str, None] = None


class BuildingDataCustomDataThemeQuickSetupItem(BaseStruct):
    furnitureId: str
    pos0: int
    pos1: int
    dir_: int = field(name='dir')


class BuildingDataCustomDataThemeData(BaseStruct):
    id_: str = field(name='id')
    sortId: int
    name: str
    themeType: str
    desc: str
    quickSetup: List[BuildingDataCustomDataThemeQuickSetupItem]
    groups: List[str]
    furnitures: List[str]


class BuildingDataCustomDataGroupData(BaseStruct):
    id_: str = field(name='id')
    sortId: int
    name: str
    themeId: str
    comfort: int
    count: int
    furniture: List[str]


class BuildingDataCustomDataFurnitureTypeData(BaseStruct):
    type_: str = field(name='type')
    name: str


class BuildingDataCustomDataFurnitureSubTypeData(BaseStruct):
    subType: str
    name: str
    type_: str = field(name='type')
    sortId: int


class BuildingDataCustomDataDormitoryDefaultFurnitureItem(BaseStruct):
    furnitureId: str
    xOffset: int
    yOffset: int
    defaultPrefabId: str


class BuildingDataCustomDataInteractItem(BaseStruct):
    skinId: str


class BuildingDataCustomDataDiyUISortTemplateListDataDiyUISortTemplateData(
    BaseStruct,
):
    name: str
    sequences: List[str]
    stableSequence: str
    stableSequenceOrder: str


class BuildingDataCustomDataDiyUISortTemplateListData(BaseStruct):
    diyUIType: str
    expandState: str
    defaultTemplateIndex: int
    defaultTemplateOrder: str
    templates: List[BuildingDataCustomDataDiyUISortTemplateListDataDiyUISortTemplateData]


class BuildingDataCustomData(BaseStruct):
    furnitures: Dict[str, BuildingDataCustomDataFurnitureData]
    themes: Dict[str, BuildingDataCustomDataThemeData]
    groups: Dict[str, BuildingDataCustomDataGroupData]
    types: Dict[str, BuildingDataCustomDataFurnitureTypeData]
    subTypes: Dict[str, BuildingDataCustomDataFurnitureSubTypeData]
    defaultFurnitures: Dict[
        str,
        List[BuildingDataCustomDataDormitoryDefaultFurnitureItem],
    ]
    interactGroups: Dict[str, List[BuildingDataCustomDataInteractItem]]
    diyUISortTemplates: Dict[
        str,
        Dict[str, BuildingDataCustomDataDiyUISortTemplateListData],
    ]


class BuildingDataManufactFormulaUnlockRoom(BaseStruct):
    roomId: str
    roomLevel: int
    roomCount: int


class BuildingDataManufactFormulaUnlockStage(BaseStruct):
    stageId: str
    rank: int


class BuildingDataManufactFormula(BaseStruct):
    formulaId: str
    itemId: str
    count: int
    weight: int
    costPoint: int
    formulaType: str
    buffType: str
    costs: List[ItemBundle]
    requireRooms: List[BuildingDataManufactFormulaUnlockRoom]
    requireStages: List[BuildingDataManufactFormulaUnlockStage]


class BuildingDataShopFormulaUnlockRoom(BaseStruct):
    roomId: str
    roomLevel: int


class BuildingDataShopFormula(BaseStruct):
    formulaId: str
    itemId: str
    formulaType: str
    costPoint: int
    gainItem: ItemBundle
    requireRooms: List[BuildingDataShopFormulaUnlockRoom]


class BuildingDataWorkshopExtraWeightItem(BaseStruct):
    weight: int
    itemId: str
    itemCount: int


class BuildingDataWorkshopFormulaUnlockRoom(BaseStruct):
    roomId: str
    roomLevel: int
    roomCount: int


class BuildingDataWorkshopFormulaUnlockStage(BaseStruct):
    stageId: str
    rank: int


class BuildingDataWorkshopFormula(BaseStruct):
    sortId: int
    formulaId: str
    rarity: int
    itemId: str
    count: int
    goldCost: int
    apCost: int
    formulaType: str
    buffType: str
    extraOutcomeRate: float
    extraOutcomeGroup: List[BuildingDataWorkshopExtraWeightItem]
    costs: List[ItemBundle]
    requireRooms: List[BuildingDataWorkshopFormulaUnlockRoom]
    requireStages: List[BuildingDataWorkshopFormulaUnlockStage]


class BuildingDataCreditFormulaValueModel(BaseStruct):
    basic: int
    addition: int


class BuildingDataCreditFormula(BaseStruct):
    initiative: Dict
    passive: Dict


class BuildingData(BaseStruct):
    __version__ = '23-10-31-11-47-45-d410ff'

    controlSlotId: str
    meetingSlotId: str
    initMaxLabor: int
    laborRecoverTime: int
    manufactInputCapacity: int
    shopCounterCapacity: int
    comfortLimit: int
    creditInitiativeLimit: int
    creditPassiveLimit: int
    creditComfortFactor: int
    creditGuaranteed: int
    creditCeiling: int
    manufactUnlockTips: str
    shopUnlockTips: str
    manufactStationBuff: float
    comfortManpowerRecoverFactor: int
    manpowerDisplayFactor: int
    shopOutputRatio: Union[Dict[str, int], None]
    shopStackRatio: Union[Dict[str, int], None]
    basicFavorPerDay: int
    humanResourceLimit: int
    tiredApThreshold: int
    processedCountRatio: int
    tradingStrategyUnlockLevel: int
    tradingReduceTimeUnit: int
    tradingLaborCostUnit: int
    manufactReduceTimeUnit: int
    manufactLaborCostUnit: int
    laborAssistUnlockLevel: int
    apToLaborUnlockLevel: int
    apToLaborRatio: int
    socialResourceLimit: int
    socialSlotNum: int
    furniDuplicationLimit: int
    assistFavorReport: int
    manufactManpowerCostByNum: List[int]
    tradingManpowerCostByNum: List[int]
    roomUnlockConds: Dict[str, BuildingDataRoomUnlockCond]
    rooms: Dict[str, BuildingDataRoomData]
    layouts: Dict[str, BuildingDataLayoutData]
    prefabs: Dict[str, BuildingDataPrefabInfo]
    controlData: BuildingDataControlRoomBean
    manufactData: BuildingDataManufactRoomBean
    shopData: BuildingDataShopRoomBean
    hireData: BuildingDataHireRoomBean
    dormData: BuildingDataDormRoomBean
    meetingData: BuildingDataMeetingRoomBean
    tradingData: BuildingDataTradingRoomBean
    workshopData: BuildingDataWorkShopRoomBean
    trainingData: BuildingDataTrainingBean
    powerData: BuildingDataPowerRoomBean
    chars: Dict[str, BuildingDataBuildingCharacter]
    buffs: Dict[str, BuildingDataBuildingBuff]
    workshopBonus: Dict[str, List[str]]
    customData: BuildingDataCustomData
    manufactFormulas: Dict[str, BuildingDataManufactFormula]
    shopFormulas: Dict[str, BuildingDataShopFormula]
    workshopFormulas: Dict[str, BuildingDataWorkshopFormula]
    creditFormula: BuildingDataCreditFormula
    goldItems: Dict[str, int]
    assistantUnlock: List[int]
