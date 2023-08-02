from pydantic import BaseModel, Field


class ZoneData(BaseModel):
    zoneID: str
    zoneIndex: int
    type: str
    zoneNameFirst: str | None
    zoneNameSecond: str | None
    zoneNameTitleCurrent: str | None
    zoneNameTitleUnCurrent: str | None
    zoneNameTitleEx: str | None
    zoneNameThird: str | None
    lockedText: str | None
    canPreview: bool


class WeeklyZoneData(BaseModel):
    daysOfWeek: list[int]
    type_: str = Field(..., alias='type')


class ZoneValidInfo(BaseModel):
    startTs: int
    endTs: int


class MainlineZoneData(BaseModel):
    zoneId: str
    chapterId: str
    preposedZoneId: str | None
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
    diffGroup: list[int]


class ItemBundle(BaseModel):
    id_: str = Field(alias='id')
    count: int
    type_: str = Field(alias='type')


class RecordRewardInfo(BaseModel):
    bindStageId: str
    stageDiff1: int
    stageDiff: int
    picRes: str | None
    textPath: str | None
    textDesc: str | None
    recordReward: list[ItemBundle] | None


class ZoneRecordData(BaseModel):
    recordId: str
    zoneId: str
    recordTitleName: str
    preRecordId: str | None
    nodeTitle1: str | None
    nodeTitle2: str | None
    rewards: list[RecordRewardInfo]


class ZoneRecordUnlockData(BaseModel):
    noteId: str
    zoneId: str
    initialName: str
    finalName: str | None
    accordingExposeId: str | None
    initialDes: str
    finalDes: str | None
    remindDes: str | None


class ZoneRecordGroupData(BaseModel):
    zoneId: str
    records: list[ZoneRecordData]
    unlockData: ZoneRecordUnlockData


class ZoneRecordMissionData(BaseModel):
    missionId: str
    recordStageId: str
    templateDesc: str
    desc: str


class ZoneMetaData(BaseModel):
    ZoneRecordMissionData: dict[str, ZoneRecordMissionData]


class ZoneTable(BaseModel):
    __version__ = '23-07-27-18-50-06-aeb568'

    zones: dict[str, ZoneData]
    weeklyAdditionInfo: dict[str, WeeklyZoneData]
    zoneValidInfo: dict[str, ZoneValidInfo]
    mainlineAdditionInfo: dict[str, MainlineZoneData]
    zoneRecordGroupedData: dict[str, ZoneRecordGroupData]
    zoneRecordRewardData: dict[str, list[str]]
    zoneMetaData: ZoneMetaData
