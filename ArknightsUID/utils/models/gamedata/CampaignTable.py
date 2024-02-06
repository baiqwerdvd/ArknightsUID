from typing import Dict, List, Union

from ..common import BaseStruct

from msgspec import field


class ItemBundle(BaseStruct):
    id_: str = field(name='id')
    count: int
    type_: str = field(name='type')


class CampaignDataBreakRewardLadder(BaseStruct):
    killCnt: int
    breakFeeAdd: int
    rewards: List[ItemBundle]


class WeightItemBundle(BaseStruct):
    id_: str = field(name='id')
    type_: str = field(name='type')
    dropType: str
    count: int
    weight: int


class StageDataDisplayRewards_(BaseStruct):
    type_: str = field(name='type')
    id_: str = field(name='id')
    dropType: int


class StageDataDisplayDetailRewards_(StageDataDisplayRewards_):
    occPercent: int
    GetPercent: float
    CannotGetPercent: float


class CampaignDataCampaignDropInfo(BaseStruct):
    firstPassRewards: Union[List[ItemBundle], None]
    passRewards: Union[List[List[WeightItemBundle]], None]
    displayDetailRewards: Union[List[StageDataDisplayDetailRewards_], None]


class CampaignDataDropLadder(BaseStruct):
    killCnt: int
    dropInfo: CampaignDataCampaignDropInfo


class CampaignDataGainLadder(BaseStruct):
    killCnt: int
    apFailReturn: int
    favor: int
    expGain: int
    goldGain: int
    displayDiamondShdNum: int


class StageDataDisplayRewards(BaseStruct):
    type_: str = field(name='type')
    id_: str = field(name='id')
    dropType: int


class StageDataDisplayDetailRewards(BaseStruct):
    occPercent: int
    type_: str = field(name='type')
    id_: str = field(name='id')
    dropType: int


class CampaignDataDropGainInfo(BaseStruct):
    dropLadders: List[CampaignDataDropLadder]
    gainLadders: List[CampaignDataGainLadder]
    displayRewards: List[StageDataDisplayRewards]
    displayDetailRewards: List[StageDataDisplayDetailRewards]


class CampaignData(BaseStruct):
    stageId: str
    isSmallScale: int
    breakLadders: List[CampaignDataBreakRewardLadder]
    isCustomized: bool
    dropGains: Dict[str, CampaignDataDropGainInfo]


class CampaignGroupData(BaseStruct):
    groupId: str
    activeCamps: List[str]
    startTs: int
    endTs: int


class CampaignRegionData(BaseStruct):
    id_: str = field(name='id')
    isUnknwon: int


class CampaignZoneData(BaseStruct):
    id_: str = field(name='id')
    name: str
    regionId: str
    templateId: str


class CampaignMissionData(BaseStruct):
    id_: str = field(name='id')
    sortId: int
    param: List[str]
    description: str
    breakFeeAdd: int


class CampaignConstTable(BaseStruct):
    systemPreposedStage: str
    rotateStartTime: int
    rotatePreposedStage: str
    zoneUnlockStage: str
    firstRotateRegion: str
    sweepStartTime: int


class CampaignRotateOpenTimeData(BaseStruct):
    groupId: str
    stageId: str
    mapId: str
    unknownRegions: List[str]
    duration: int
    startTs: int
    endTs: int


class CampaignTrainingOpenTimeData(BaseStruct):
    groupId: str
    stages: List[str]
    startTs: int
    endTs: int


class CampaignTrainingAllOpenTimeData(BaseStruct):
    groupId: str
    startTs: int
    endTs: int


class CampaignTable(BaseStruct):
    __version__ = '24-02-02-10-18-07-831ad8'

    campaigns: Dict[str, CampaignData]
    campaignGroups: Dict[str, CampaignGroupData]
    campaignRegions: Dict[str, CampaignRegionData]
    campaignZones: Dict[str, CampaignZoneData]
    campaignMissions: Dict[str, CampaignMissionData]
    stageIndexInZoneMap: Dict[str, int]
    campaignConstTable: CampaignConstTable
    campaignRotateStageOpenTimes: List[CampaignRotateOpenTimeData]
    campaignTrainingStageOpenTimes: List[CampaignTrainingOpenTimeData]
    campaignTrainingAllOpenTimes: List[CampaignTrainingAllOpenTimeData]
