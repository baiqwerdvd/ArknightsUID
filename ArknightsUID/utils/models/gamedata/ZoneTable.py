from typing import Dict, List, Union

from ..common import BaseStruct

from msgspec import field


class ZoneData(BaseStruct):
    zoneID: str
    zoneIndex: int
    type_: str = field(name='type')
    zoneNameFirst: Union[str, None]
    zoneNameSecond: Union[str, None]
    zoneNameTitleCurrent: Union[str, None]
    zoneNameTitleUnCurrent: Union[str, None]
    zoneNameTitleEx: Union[str, None]
    zoneNameThird: Union[str, None]
    lockedText: Union[str, None]
    canPreview: bool


class WeeklyZoneData(BaseStruct):
    daysOfWeek: List[int]
    type_: str = field(name='type')


class ZoneValidInfo(BaseStruct):
    startTs: int
    endTs: int


class MainlineZoneData(BaseStruct):
    zoneId: str
    chapterId: str
    preposedZoneId: Union[str, None]
    zoneIndex: int
    startStageId: str
    endStageId: str
    mainlneBgName: str
    recapId: str
    recapPreStageId: str
    buttonName: str
    buttonStyle: str
    spoilAlert: bool
    zoneOpenTime: int
    diffGroup: List[int]


class ItemBundle(BaseStruct):
    id_: str = field(name='id')
    count: int
    type_: str = field(name='type')


class RecordRewardInfo(BaseStruct):
    bindStageId: str
    stageDiff1: int
    stageDiff: int
    picRes: Union[str, None]
    textPath: Union[str, None]
    textDesc: Union[str, None]
    recordReward: Union[List[ItemBundle], None]


class ZoneRecordData(BaseStruct):
    recordId: str
    zoneId: str
    recordTitleName: str
    preRecordId: Union[str, None]
    nodeTitle1: Union[str, None]
    nodeTitle2: Union[str, None]
    rewards: List[RecordRewardInfo]


class ZoneRecordUnlockData(BaseStruct):
    noteId: str
    zoneId: str
    initialName: str
    finalName: Union[str, None]
    accordingExposeId: Union[str, None]
    initialDes: str
    finalDes: Union[str, None]
    remindDes: Union[str, None]


class ZoneRecordGroupData(BaseStruct):
    zoneId: str
    records: List[ZoneRecordData]
    unlockData: ZoneRecordUnlockData


class ZoneRecordMissionData(BaseStruct):
    missionId: str
    recordStageId: str
    templateDesc: str
    desc: str


class ZoneMetaData(BaseStruct):
    ZoneRecordMissionData: Dict[str, ZoneRecordMissionData]


class ZoneTable(BaseStruct):
    __version__ = '23-09-29-15-41-03-569cae'

    zones: Dict[str, ZoneData]
    weeklyAdditionInfo: Dict[str, WeeklyZoneData]
    zoneValidInfo: Dict[str, ZoneValidInfo]
    mainlineAdditionInfo: Dict[str, MainlineZoneData]
    zoneRecordGroupedData: Dict[str, ZoneRecordGroupData]
    zoneRecordRewardData: Dict[str, List[str]]
    zoneMetaData: ZoneMetaData
