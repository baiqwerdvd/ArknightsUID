from pydantic import BaseModel, Field


class MiniActTrialDataRuleData(BaseModel):
    ruleType: str
    ruleText: str


class ItemBundle(BaseModel):
    id_: str = Field(alias='id')
    count: int
    type_: str = Field(alias='type')


class MiniActTrialDataMiniActTrialRewardData(BaseModel):
    trialRewardId: str
    orderId: int
    actId: str
    targetStoryCount: int
    item: ItemBundle


class MiniActTrialDataMiniActTrialSingleData(BaseModel):
    actId: str
    rewardStartTime: int
    themeColor: str
    rewardList: list[MiniActTrialDataMiniActTrialRewardData]


class MiniActTrialData(BaseModel):
    preShowDays: int
    ruleDataList: list[MiniActTrialDataRuleData]
    miniActTrialDataMap: dict[str, MiniActTrialDataMiniActTrialSingleData]


class ActArchiveResDataPicArchiveResItemData(BaseModel):
    id_: str = Field(alias='id')
    desc: str
    assetPath: str
    type_: str = Field(alias='type')
    subType: str | None
    picDescription: str
    kvId: str | None


class ActArchiveResDataAudioArchiveResItemData(BaseModel):
    id_: str = Field(alias='id')
    desc: str
    name: str


class ActArchiveResDataAvgArchiveResItemData(BaseModel):
    id_: str = Field(alias='id')
    desc: str
    breifPath: str | None
    contentPath: str
    imagePath: str
    rawBrief: str | None
    titleIconPath: str | None


class ActArchiveResDataStoryArchiveResItemData(BaseModel):
    id_: str = Field(alias='id')
    desc: str
    date: str | None
    pic: str
    text: str
    titlePic: str | None


class ActArchiveResDataNewsFormatData(BaseModel):
    typeId: str
    typeName: str
    typeLogo: str
    typeMainLogo: str
    typeMainSealing: str


class ActArchiveResDataActivityNewsLine(BaseModel):
    lineType: int
    content: str


class ActArchiveResDataNewsArchiveResItemData(BaseModel):
    id_: str = Field(alias='id')
    desc: str
    newsType: str
    newsFormat: ActArchiveResDataNewsFormatData
    newsText: str
    newsAuthor: str
    paramP0: int
    paramK: int
    paramR: float
    newsLines: list[ActArchiveResDataActivityNewsLine]


class ActArchiveResDataLandmarkArchiveResItemData(BaseModel):
    landmarkId: str
    landmarkName: str
    landmarkPic: str
    landmarkDesc: str
    landmarkEngName: str


class ActArchiveResDataLogArchiveResItemData(BaseModel):
    logId: str
    logDesc: str


class ActArchiveResData(BaseModel):
    pics: dict[str, ActArchiveResDataPicArchiveResItemData]
    audios: dict[str, ActArchiveResDataAudioArchiveResItemData]
    avgs: dict[str, ActArchiveResDataAvgArchiveResItemData]
    stories: dict[str, ActArchiveResDataStoryArchiveResItemData]
    news: dict[str, ActArchiveResDataNewsArchiveResItemData]
    landmarks: dict[str, ActArchiveResDataLandmarkArchiveResItemData]
    logs: dict[str, ActArchiveResDataLogArchiveResItemData]


class ActArchiveTimelineItemData(BaseModel):
    timelineId: str
    timelineSortId: int
    timelineTitle: str
    timelineDes: str
    picIdList: list[str] | None = None
    audioIdList: list[str] | None = None
    avgIdList: list[str] | None = None
    storyIdList: list[str] | None = None
    newsIdList: list[str] | None = None


class ActArchiveTimelineData(BaseModel):
    timelineList: list[ActArchiveTimelineItemData]


class ActArchiveMusicItemData(BaseModel):
    musicId: str
    musicSortId: int


class ActArchiveMusicData(BaseModel):
    musics: dict[str, ActArchiveMusicItemData]


class ActArchivePicItemData(BaseModel):
    picId: str
    picSortId: int


class ActArchivePicData(BaseModel):
    pics: dict[str, ActArchivePicItemData]


class ActArchiveStoryItemData(BaseModel):
    storyId: str
    storySortId: int


class ActArchiveStoryData(BaseModel):
    stories: dict[str, ActArchiveStoryItemData]


class ActArchiveAvgItemData(BaseModel):
    avgId: str
    avgSortId: int


class ActArchiveAvgData(BaseModel):
    avgs: dict[str, ActArchiveAvgItemData]


class ActArchiveNewsItemData(BaseModel):
    newsId: str
    newsSortId: int


class ActArchiveNewsData(BaseModel):
    news: dict[str, ActArchiveNewsItemData]


class ActArchiveLandmarkItemData(BaseModel):
    landmarkId: str
    landmarkSortId: int


class ActArchiveChapterLogData(BaseModel):
    chapterName: str
    displayId: str
    unlockDes: str
    logs: list[str]
    chapterIcon: str


class ActArchiveComponentData(BaseModel):
    timeline: ActArchiveTimelineData | None = None
    music: ActArchiveMusicData | None = None
    pic: ActArchivePicData
    story: ActArchiveStoryData | None = None
    avg: ActArchiveAvgData | None = None
    news: ActArchiveNewsData | None = None
    landmark: dict[str, ActArchiveLandmarkItemData] | None = None
    log: dict[str, ActArchiveChapterLogData] | None = None


class ActArchiveComponentTable(BaseModel):
    components: dict[str, ActArchiveComponentData]


class StoryReviewMetaTable(BaseModel):
    __version__ = '23-07-27-18-50-06-aeb568'

    miniActTrialData: MiniActTrialData
    actArchiveResData: ActArchiveResData
    actArchiveData: ActArchiveComponentTable
