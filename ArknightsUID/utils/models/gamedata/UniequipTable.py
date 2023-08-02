from pydantic import BaseModel, Field


class ItemBundle(BaseModel):
    id_: str = Field(alias='id')
    count: int
    type_: str = Field(alias='type')


class UniEquipData(BaseModel):
    uniEquipId: str
    uniEquipName: str
    uniEquipIcon: str
    uniEquipDesc: str
    typeIcon: str
    typeName1: str
    typeName2: str | None
    equipShiningColor: str
    showEvolvePhase: int
    unlockEvolvePhase: int
    charId: str
    tmplId: str | None
    showLevel: int
    unlockLevel: int
    unlockFavorPoint: int
    missionList: list[str]
    itemCost: dict[str, list[ItemBundle]] | None
    type_: str = Field(..., alias='type')
    uniEquipGetTime: int
    charEquipOrder: int


class UniEquipMissionData(BaseModel):
    template: str
    desc: str
    paramList: list[str]
    uniEquipMissionId: str
    uniEquipMissionSort: int
    uniEquipId: str
    jumpStageId: str | None


class SubProfessionData(BaseModel):
    subProfessionId: str
    subProfessionName: str
    subProfessionCatagory: int


class UniEquipTrack(BaseModel):
    charId: str
    equipId: str


class UniEquipTimeInfo(BaseModel):
    timeStamp: int
    trackList: list[UniEquipTrack]


class UniEquipTable(BaseModel):
    __version__ = '23-07-27-18-50-06-aeb568'

    equipDict: dict[str, UniEquipData]
    missionList: dict[str, UniEquipMissionData]
    subProfDict: dict[str, SubProfessionData]
    charEquip: dict[str, list[str]]
    equipTrackDict: list[UniEquipTimeInfo]
