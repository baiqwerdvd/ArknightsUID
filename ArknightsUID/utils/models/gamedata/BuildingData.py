from pydantic import BaseModel, Field


class BuildingDataRoomUnlockCondCondItem(BaseModel):
    type_: str = Field(alias='type')
    level: int
    count: int


class BuildingDataRoomUnlockCond(BaseModel):
    id_: str = Field(alias='id')
    number: dict[str, BuildingDataRoomUnlockCondCondItem]


class GridPosition(BaseModel):
    row: int
    col: int


class ItemBundle(BaseModel):
    id_: str = Field(alias='id')
    count: int
    type_: str = Field(alias='type')


class BuildingDataRoomDataBuildCost(BaseModel):
    items: list[ItemBundle]
    time: int
    labor: int


class BuildingDataRoomDataPhaseData(BaseModel):
    overrideName: str | None
    overridePrefabId: str | None
    unlockCondId: str
    buildCost: BuildingDataRoomDataBuildCost
    electricity: int
    maxStationedNum: int
    manpowerCost: int


class BuildingDataRoomData(BaseModel):
    id_: str = Field(alias='id')
    name: str
    description: str | None
    defaultPrefabId: str
    canLevelDown: bool
    maxCount: int
    category: str
    size: GridPosition
    phases: list[BuildingDataRoomDataPhaseData]


class BuildingDataLayoutDataRoomSlot(BaseModel):
    id_: str = Field(alias='id')
    cleanCostId: str
    costLabor: int
    provideLabor: int
    size: GridPosition
    offset: GridPosition
    category: str
    storeyId: str


class BuildingDataLayoutDataSlotCleanCostCountCost(BaseModel):
    items: list[ItemBundle]


class BuildingDataLayoutDataSlotCleanCost(BaseModel):
    id_: str = Field(alias='id')
    number: dict[str, BuildingDataLayoutDataSlotCleanCostCountCost]


class BuildingDataLayoutDataStoreyData(BaseModel):
    id_: str = Field(alias='id')
    yOffset: int
    unlockControlLevel: int
    type_: str = Field(alias='type')


class BuildingDataLayoutData(BaseModel):
    id_: str = Field(alias='id')
    slots: dict[str, BuildingDataLayoutDataRoomSlot]
    cleanCosts: dict[str, BuildingDataLayoutDataSlotCleanCost]
    storeys: dict[str, BuildingDataLayoutDataStoreyData]


class BuildingDataPrefabInfo(BaseModel):
    id_: str = Field(alias='id')
    blueprintRoomOverrideId: str | None
    size: GridPosition
    floorGridSize: GridPosition
    backWallGridSize: GridPosition
    obstacleId: str | None


class BuildingDataManufactPhase(BaseModel):
    speed: float | int
    outputCapacity: int


class BuildingDataShopPhase(BaseModel):
    counterNum: int
    speed: float | int
    moneyCapacity: int


class BuildingDataHirePhase(BaseModel):
    economizeRate: float
    resSpeed: int
    refreshTimes: int


class BuildingDataDormPhase(BaseModel):
    manpowerRecover: int
    decorationLimit: int


class BuildingDataMeetingPhase(BaseModel):
    friendSlotInc: int
    maxVisitorNum: int
    gatheringSpeed: int


class BuildingDataTradingPhase(BaseModel):
    orderSpeed: float | int
    orderLimit: int
    orderRarity: int


class BuildingDataWorkshopPhase(BaseModel):
    manpowerFactor: float | int


class BuildingDataTrainingPhase(BaseModel):
    specSkillLvlLimit: int


class BuildingDataRoomBean(BaseModel):
    phases: list[BuildingDataManufactPhase | BuildingDataShopPhase | BuildingDataHirePhase | BuildingDataDormPhase | BuildingDataMeetingPhase | BuildingDataTradingPhase | BuildingDataWorkshopPhase | BuildingDataTrainingPhase] | None  # noqa: E501


class BuildingDataControlRoomBean(BuildingDataRoomBean):
    basicCostBuff: int


class BuildingDataManufactRoomBean(BuildingDataRoomBean):
    basicSpeedBuff: float


class BuildingDataHireRoomBean(BuildingDataRoomBean):
    basicSpeedBuff: float


class BuildingDataMeetingRoomBean(BuildingDataRoomBean):
    basicSpeedBuff: float


class BuildingDataTradingRoomBean(BuildingDataRoomBean):
    basicSpeedBuff: float


class BuildingDataTrainingBean(BuildingDataRoomBean):
    basicSpeedBuff: float


class BuildingDataPowerRoomBean(BuildingDataRoomBean):
    basicSpeedBuff: float


class CharacterDataUnlockCondition(BaseModel):
    phase: int
    level: int


class BuildingDataBuildingBuffCharSlotSlotItem(BaseModel):
    buffId: str
    cond: CharacterDataUnlockCondition


class BuildingDataBuildingBuffCharSlot(BaseModel):
    buffData: list[BuildingDataBuildingBuffCharSlotSlotItem]


class BuildingDataBuildingCharacter(BaseModel):
    charId: str
    maxManpower: int
    buffChar: list[BuildingDataBuildingBuffCharSlot]


class BuildingDataBuildingBuff(BaseModel):
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


class BuildingDataCustomDataFurnitureData(BaseModel):
    id_: str = Field(alias='id')
    sortId: int
    name: str
    iconId: str
    interactType: str | None = None
    type_: str = Field(alias='type')
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
    processedByProductGroup: list
    canBeDestroy: bool
    isOnly: int
    quantity: int


class BuildingDataCustomDataThemeQuickSetupItem(BaseModel):
    furnitureId: str
    pos0: int
    pos1: int
    dir_: int = Field(alias='dir')


class BuildingDataCustomDataThemeData(BaseModel):
    id_: str = Field(alias='id')
    sortId: int
    name: str
    themeType: str
    desc: str
    quickSetup: list[BuildingDataCustomDataThemeQuickSetupItem]
    groups: list[str]
    furnitures: list[str]


class BuildingDataCustomDataGroupData(BaseModel):
    id_: str = Field(alias='id')
    sortId: int
    name: str
    themeId: str
    comfort: int
    count: int
    furniture: list[str]


class BuildingDataCustomDataFurnitureTypeData(BaseModel):
    type_: str = Field(alias='type')
    name: str


class BuildingDataCustomDataFurnitureSubTypeData(BaseModel):
    subType: str
    name: str
    type_: str = Field(alias='type')
    sortId: int


class BuildingDataCustomDataDormitoryDefaultFurnitureItem(BaseModel):
    furnitureId: str
    xOffset: int
    yOffset: int
    defaultPrefabId: str


class BuildingDataCustomDataInteractItem(BaseModel):
    skinId: str


class BuildingDataCustomDataDiyUISortTemplateListDataDiyUISortTemplateData(BaseModel):
    name: str
    sequences: list[str]
    stableSequence: str
    stableSequenceOrder: str


class BuildingDataCustomDataDiyUISortTemplateListData(BaseModel):
    diyUIType: str
    expandState: str
    defaultTemplateIndex: int
    defaultTemplateOrder: str
    templates: list[BuildingDataCustomDataDiyUISortTemplateListDataDiyUISortTemplateData]


class BuildingDataCustomData(BaseModel):
    furnitures: dict[str, BuildingDataCustomDataFurnitureData]
    themes: dict[str, BuildingDataCustomDataThemeData]
    groups: dict[str, BuildingDataCustomDataGroupData]
    types: dict[str, BuildingDataCustomDataFurnitureTypeData]
    subTypes: dict[str, BuildingDataCustomDataFurnitureSubTypeData]
    defaultFurnitures: dict[str, list[BuildingDataCustomDataDormitoryDefaultFurnitureItem]]
    interactGroups: dict[str, list[BuildingDataCustomDataInteractItem]]
    diyUISortTemplates: dict[str, dict[str, BuildingDataCustomDataDiyUISortTemplateListData]]


class BuildingDataManufactFormulaUnlockRoom(BaseModel):
    roomId: str
    roomLevel: int
    roomCount: int


class BuildingDataManufactFormulaUnlockStage(BaseModel):
    stageId: str
    rank: int


class BuildingDataManufactFormula(BaseModel):
    formulaId: str
    itemId: str
    count: int
    weight: int
    costPoint: int
    formulaType: str
    buffType: str
    costs: list[ItemBundle]
    requireRooms: list[BuildingDataManufactFormulaUnlockRoom]
    requireStages: list[BuildingDataManufactFormulaUnlockStage]


class BuildingDataShopFormulaUnlockRoom(BaseModel):
    roomId: str
    roomLevel: int


class BuildingDataShopFormula(BaseModel):
    formulaId: str
    itemId: str
    formulaType: str
    costPoint: int
    gainItem: ItemBundle
    requireRooms: list[BuildingDataShopFormulaUnlockRoom]


class BuildingDataWorkshopExtraWeightItem(BaseModel):
    weight: int
    itemId: str
    itemCount: int


class BuildingDataWorkshopFormulaUnlockRoom(BaseModel):
    roomId: str
    roomLevel: int
    roomCount: int


class BuildingDataWorkshopFormulaUnlockStage(BaseModel):
    stageId: str
    rank: int


class BuildingDataWorkshopFormula(BaseModel):
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
    extraOutcomeGroup: list[BuildingDataWorkshopExtraWeightItem]
    costs: list[ItemBundle]
    requireRooms: list[BuildingDataWorkshopFormulaUnlockRoom]
    requireStages: list[BuildingDataWorkshopFormulaUnlockStage]


class BuildingDataCreditFormulaValueModel(BaseModel):
    basic: int
    addition: int


class BuildingDataCreditFormula(BaseModel):
    initiative: BuildingDataCreditFormulaValueModel | dict
    passive: BuildingDataCreditFormulaValueModel | dict


class BuildingData(BaseModel):
    __version__ = '23-07-27-18-50-06-aeb568'

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
    shopOutputRatio: dict[str, int] | None
    shopStackRatio: dict[str, int] | None
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
    manufactManpowerCostByNum: list[int]
    tradingManpowerCostByNum: list[int]
    roomUnlockConds: dict[str, BuildingDataRoomUnlockCond]
    rooms: dict[str, BuildingDataRoomData]
    layouts: dict[str, BuildingDataLayoutData]
    prefabs: dict[str, BuildingDataPrefabInfo]
    controlData: BuildingDataControlRoomBean
    manufactData: BuildingDataManufactRoomBean
    shopData: BuildingDataRoomBean
    hireData: BuildingDataHireRoomBean
    dormData: BuildingDataRoomBean
    meetingData: BuildingDataMeetingRoomBean
    tradingData: BuildingDataTradingRoomBean
    workshopData: BuildingDataRoomBean
    trainingData: BuildingDataTrainingBean
    powerData: BuildingDataPowerRoomBean
    chars: dict[str, BuildingDataBuildingCharacter]
    buffs: dict[str, BuildingDataBuildingBuff]
    workshopBonus: dict[str, list[str]]
    customData: BuildingDataCustomData
    manufactFormulas: dict[str, BuildingDataManufactFormula]
    shopFormulas: dict[str, BuildingDataShopFormula]
    workshopFormulas: dict[str, BuildingDataWorkshopFormula]
    creditFormula: BuildingDataCreditFormula
    goldItems: dict[str, int]
    assistantUnlock: list[int]

    class Config:
        extra = 'allow'
