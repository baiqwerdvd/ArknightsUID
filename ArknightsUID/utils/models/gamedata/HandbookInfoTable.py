from pydantic import BaseModel, Field


class HandbookUnlockParam(BaseModel):
    unlockType: int
    unlockParam1: str
    unlockParam2: str | None
    unlockParam3: str | None


class ItemBundle(BaseModel):
    id_: str = Field(alias='id')
    count: int
    type_: str = Field(alias='type')


class HandbookStageTimeData(BaseModel):
    timestamp: int
    charSet: list[str]


class HandbookStoryStageData(BaseModel):
    charId: str
    code: str
    description: str
    levelId: str
    loadingPicId: str
    name: str
    picId: str
    rewardItem: list[ItemBundle]
    stageGetTime: int
    stageId: str
    stageNameForShow: str
    unlockParam: list[HandbookUnlockParam]
    zoneId: str
    zoneNameForShow: str


class HandbookDisplayCondition(BaseModel):
    charId: str
    conditionCharId: str
    type_: str = Field(alias='type')


class HandbookTeamMission(BaseModel):
    id_: str = Field(alias='id')
    sort: int
    powerId: str
    powerName: str
    item: ItemBundle
    favorPoint: int


class NPCUnlock(BaseModel):
    unLockType: int
    unLockParam: str
    unLockString: str | None = None


class NPCData(BaseModel):
    appellation: str
    cv: str
    designerList: list[str] | None
    displayNumber: str
    groupId: str | None
    illustList: list[str]
    name: str
    nationId: str
    npcId: str
    npcShowAudioInfoFlag: bool
    profession: str
    resType: str
    teamId: None
    unlockDict: dict[str, NPCUnlock]
    minPowerId: str


class HandbookAvgData(BaseModel):
    storyId: str
    storySetId: str
    storySort: int
    storyCanShow: bool
    storyIntro: str
    storyInfo: str
    storyTxt: str


class HandbookAvgGroupData(BaseModel):
    storySetId: str
    storySetName: str
    sortId: int
    storyGetTime: int
    rewardItem: list[ItemBundle]
    unlockParam: list[HandbookUnlockParam]
    avgList: list[HandbookAvgData]
    charId: str


class HandbookStoryData(BaseModel):
    storyText: str
    unLockType: int
    unLockParam: str
    unLockString: str


class HandBookStoryViewData(BaseModel):
    stories: list[HandbookStoryData]
    storyTitle: str
    unLockorNot: bool


class HandbookInfoData(BaseModel):
    charID: str
    infoName: str
    storyTextAudio: list[HandBookStoryViewData]
    handbookAvgList: list[HandbookAvgGroupData]
    isLimited: bool | None = None


class HandbookInfoTable(BaseModel):
    __version__ = '23-07-27-18-50-06-aeb568'

    handbookDict: dict[str, HandbookInfoData]
    npcDict: dict[str, NPCData]
    teamMissionList: dict[str, HandbookTeamMission]
    handbookDisplayConditionList: dict[str, HandbookDisplayCondition]
    handbookStageData: dict[str, HandbookStoryStageData]
    handbookStageTime: list[HandbookStageTimeData]

    class Config:
        extra = 'allow'
