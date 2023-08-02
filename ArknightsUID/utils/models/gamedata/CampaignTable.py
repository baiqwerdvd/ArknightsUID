from pydantic import BaseModel, Field


class ItemBundle(BaseModel):
    id_: str = Field(alias='id')
    count: int
    type_: str = Field(alias='type')


class CampaignDataBreakRewardLadder(BaseModel):
    killCnt: int
    breakFeeAdd: int
    rewards: list[ItemBundle]


class WeightItemBundle(BaseModel):
    id_: str = Field(alias='id')
    type_: str = Field(alias='type')
    dropType: str
    count: int
    weight: int


class StageDataDisplayRewards_(BaseModel):
    type_: str = Field(alias='type')
    id_: str = Field(alias='id')
    dropType: int


class StageDataDisplayDetailRewards_(StageDataDisplayRewards_):
    occPercent: int
    GetPercent: float
    CannotGetPercent: float


class CampaignDataCampaignDropInfo(BaseModel):
    firstPassRewards: list[ItemBundle] | None
    passRewards: list[list[WeightItemBundle]] | None
    displayDetailRewards: list[StageDataDisplayDetailRewards_] | None


class CampaignDataDropLadder(BaseModel):
    killCnt: int
    dropInfo: CampaignDataCampaignDropInfo


class CampaignDataGainLadder(BaseModel):
    killCnt: int
    apFailReturn: int
    favor: int
    expGain: int
    goldGain: int
    displayDiamondShdNum: int


class StageDataDisplayRewards(BaseModel):
    type_: str = Field(alias='type')
    id_: str = Field(alias='id')
    dropType: int


class StageDataDisplayDetailRewards(BaseModel):
    occPercent: int
    type_: str = Field(alias='type')
    id_: str = Field(alias='id')
    dropType: int


class CampaignDataDropGainInfo(BaseModel):
    dropLadders: list[CampaignDataDropLadder]
    gainLadders: list[CampaignDataGainLadder]
    displayRewards: list[StageDataDisplayRewards]
    displayDetailRewards: list[StageDataDisplayDetailRewards]


class CampaignData(BaseModel):
    stageId: str
    isSmallScale: int
    breakLadders: list[CampaignDataBreakRewardLadder]
    isCustomized: bool
    dropGains: dict[str, CampaignDataDropGainInfo]


class CampaignGroupData(BaseModel):
    groupId: str
    activeCamps: list[str]
    startTs: int
    endTs: int


class CampaignRegionData(BaseModel):
    id_: str = Field(alias='id')
    isUnknwon: int


class CampaignZoneData(BaseModel):
    id_: str = Field(alias='id')
    name: str
    regionId: str
    templateId: str


class CampaignMissionData(BaseModel):
    id_: str = Field(alias='id')
    sortId: int
    param: list[str]
    description: str
    breakFeeAdd: int


class CampaignConstTable(BaseModel):
    systemPreposedStage: str
    rotateStartTime: int
    rotatePreposedStage: str
    zoneUnlockStage: str
    firstRotateRegion: str
    sweepStartTime: int


class CampaignRotateOpenTimeData(BaseModel):
    groupId: str
    stageId: str
    mapId: str
    unknownRegions: list[str]
    duration: int
    startTs: int
    endTs: int


class CampaignTrainingOpenTimeData(BaseModel):
    groupId: str
    stages: list[str]
    startTs: int
    endTs: int


class CampaignTrainingAllOpenTimeData(BaseModel):
    groupId: str
    startTs: int
    endTs: int


class CampaignTable(BaseModel):
    __version__ = '23-07-27-18-50-06-aeb568'

    campaigns: dict[str, CampaignData]
    campaignGroups: dict[str, CampaignGroupData]
    campaignRegions: dict[str, CampaignRegionData]
    campaignZones: dict[str, CampaignZoneData]
    campaignMissions: dict[str, CampaignMissionData]
    stageIndexInZoneMap: dict[str, int]
    campaignConstTable: CampaignConstTable
    campaignRotateStageOpenTimes: list[CampaignRotateOpenTimeData]
    campaignTrainingStageOpenTimes: list[CampaignTrainingOpenTimeData]
    campaignTrainingAllOpenTimes: list[CampaignTrainingAllOpenTimeData]

    class Config:
        extra = 'allow'
