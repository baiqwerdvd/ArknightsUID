from typing import Dict, List, Union

from ..common import BaseStruct

from msgspec import field


class ItemBundle(BaseStruct):
    id_: str = field(name='id')
    count: int
    type_: str = field(name='type')


class UniEquipData(BaseStruct):
    uniEquipId: str
    uniEquipName: str
    uniEquipIcon: str
    uniEquipDesc: str
    typeIcon: str
    typeName1: str
    typeName2: Union[str, None]
    equipShiningColor: str
    showEvolvePhase: int
    unlockEvolvePhase: int
    charId: str
    tmplId: Union[str, None]
    showLevel: int
    unlockLevel: int
    unlockFavorPoint: int
    missionList: List[str]
    itemCost: Union[Dict[str, List[ItemBundle]], None]
    type_: str = field(name='type')
    uniEquipGetTime: int
    charEquipOrder: int


class UniEquipMissionData(BaseStruct):
    template: str
    desc: str
    paramList: List[str]
    uniEquipMissionId: str
    uniEquipMissionSort: int
    uniEquipId: str
    jumpStageId: Union[str, None]


class SubProfessionData(BaseStruct):
    subProfessionId: str
    subProfessionName: str
    subProfessionCatagory: int


class UniEquipTrack(BaseStruct):
    charId: str
    equipId: str


class UniEquipTimeInfo(BaseStruct):
    timeStamp: int
    trackList: List[UniEquipTrack]


class UniEquipTable(BaseStruct):
    __version__ = '23-12-02-09-28-50-918524'

    equipDict: Dict[str, UniEquipData]
    missionList: Dict[str, UniEquipMissionData]
    subProfDict: Dict[str, SubProfessionData]
    charEquip: Dict[str, List[str]]
    equipTrackDict: List[UniEquipTimeInfo]
