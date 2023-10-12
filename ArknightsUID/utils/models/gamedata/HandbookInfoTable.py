from typing import Dict, List, Union

from msgspec import field

from ..common import BaseStruct


class HandbookUnlockParam(BaseStruct):
    unlockType: int
    unlockParam1: str
    unlockParam2: Union[str, None]
    unlockParam3: Union[str, None]


class ItemBundle(BaseStruct):
    id_: str = field(name='id')
    count: int
    type_: str = field(name='type')


class HandbookStageTimeData(BaseStruct):
    timestamp: int
    charSet: List[str]


class HandbookStoryStageData(BaseStruct):
    charId: str
    code: str
    description: str
    levelId: str
    loadingPicId: str
    name: str
    picId: str
    rewardItem: List[ItemBundle]
    stageGetTime: int
    stageId: str
    stageNameForShow: str
    unlockParam: List[HandbookUnlockParam]
    zoneId: str
    zoneNameForShow: str


class HandbookDisplayCondition(BaseStruct):
    charId: str
    conditionCharId: str
    type_: str = field(name='type')


class HandbookTeamMission(BaseStruct):
    id_: str = field(name='id')
    sort: int
    powerId: str
    powerName: str
    item: ItemBundle
    favorPoint: int


class NPCUnlock(BaseStruct):
    unLockType: int
    unLockParam: str
    unLockString: Union[str, None] = None


class NPCData(BaseStruct):
    appellation: str
    cv: str
    designerList: Union[List[str], None]
    displayNumber: str
    groupId: Union[str, None]
    illustList: List[str]
    name: str
    nationId: str
    npcId: str
    npcShowAudioInfoFlag: bool
    profession: str
    resType: str
    teamId: None
    unlockDict: Dict[str, NPCUnlock]
    minPowerId: str


class HandbookAvgData(BaseStruct):
    storyId: str
    storySetId: str
    storySort: int
    storyCanShow: bool
    storyIntro: str
    storyInfo: str
    storyTxt: str


class HandbookAvgGroupData(BaseStruct):
    storySetId: str
    storySetName: str
    sortId: int
    storyGetTime: int
    rewardItem: List[ItemBundle]
    unlockParam: List[HandbookUnlockParam]
    avgList: List[HandbookAvgData]
    charId: str


class HandbookStoryData(BaseStruct):
    storyText: str
    unLockType: int
    unLockParam: str
    unLockString: str


class HandBookStoryViewData(BaseStruct):
    stories: List[HandbookStoryData]
    storyTitle: str
    unLockorNot: bool


class HandbookInfoData(BaseStruct):
    charID: str
    infoName: str
    storyTextAudio: List[HandBookStoryViewData]
    handbookAvgList: List[HandbookAvgGroupData]
    isLimited: Union[bool, None] = None


class HandbookInfoTable(BaseStruct):
    __version__ = '23-10-08-17-52-18-288259'

    handbookDict: Dict[str, HandbookInfoData]
    npcDict: Dict[str, NPCData]
    teamMissionList: Dict[str, HandbookTeamMission]
    handbookDisplayConditionList: Dict[str, HandbookDisplayCondition]
    handbookStageData: Dict[str, HandbookStoryStageData]
    handbookStageTime: List[HandbookStageTimeData]
