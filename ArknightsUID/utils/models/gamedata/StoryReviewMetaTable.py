from typing import Dict, List, Union

from ..common import BaseStruct

from msgspec import field


class MiniActTrialDataRuleData(BaseStruct):
    ruleType: str
    ruleText: str


class ItemBundle(BaseStruct):
    id_: str = field(name='id')
    count: int
    type_: str = field(name='type')


class MiniActTrialDataMiniActTrialRewardData(BaseStruct):
    trialRewardId: str
    orderId: int
    actId: str
    targetStoryCount: int
    item: ItemBundle


class MiniActTrialDataMiniActTrialSingleData(BaseStruct):
    actId: str
    rewardStartTime: int
    themeColor: str
    rewardList: List[MiniActTrialDataMiniActTrialRewardData]


class MiniActTrialData(BaseStruct):
    preShowDays: int
    ruleDataList: List[MiniActTrialDataRuleData]
    miniActTrialDataMap: Dict[str, MiniActTrialDataMiniActTrialSingleData]


class ActArchiveResDataPicArchiveResItemData(BaseStruct):
    id_: str = field(name='id')
    desc: str
    assetPath: str
    type_: str = field(name='type')
    subType: Union[str, None]
    picDescription: str
    kvId: Union[str, None]


class ActArchiveResDataAudioArchiveResItemData(BaseStruct):
    id_: str = field(name='id')
    desc: str
    name: str


class ActArchiveResDataAvgArchiveResItemData(BaseStruct):
    id_: str = field(name='id')
    desc: str
    breifPath: Union[str, None]
    contentPath: str
    imagePath: str
    rawBrief: Union[str, None]
    titleIconPath: Union[str, None]


class ActArchiveResDataStoryArchiveResItemData(BaseStruct):
    id_: str = field(name='id')
    desc: str
    date: Union[str, None]
    pic: str
    text: str
    titlePic: Union[str, None]


class ActArchiveResDataNewsFormatData(BaseStruct):
    typeId: str
    typeName: str
    typeLogo: str
    typeMainLogo: str
    typeMainSealing: str


class ActArchiveResDataActivityNewsLine(BaseStruct):
    lineType: int
    content: str


class ActArchiveResDataNewsArchiveResItemData(BaseStruct):
    id_: str = field(name='id')
    desc: str
    newsType: str
    newsFormat: ActArchiveResDataNewsFormatData
    newsText: str
    newsAuthor: str
    paramP0: int
    paramK: int
    paramR: float
    newsLines: List[ActArchiveResDataActivityNewsLine]


class ActArchiveResDataLandmarkArchiveResItemData(BaseStruct):
    landmarkId: str
    landmarkName: str
    landmarkPic: str
    landmarkDesc: str
    landmarkEngName: str


class ActArchiveResDataLogArchiveResItemData(BaseStruct):
    logId: str
    logDesc: str


class ActArchiveResData(BaseStruct):
    pics: Dict[str, ActArchiveResDataPicArchiveResItemData]
    audios: Dict[str, ActArchiveResDataAudioArchiveResItemData]
    avgs: Dict[str, ActArchiveResDataAvgArchiveResItemData]
    stories: Dict[str, ActArchiveResDataStoryArchiveResItemData]
    news: Dict[str, ActArchiveResDataNewsArchiveResItemData]
    landmarks: Dict[str, ActArchiveResDataLandmarkArchiveResItemData]
    logs: Dict[str, ActArchiveResDataLogArchiveResItemData]


class ActArchiveTimelineItemData(BaseStruct):
    timelineId: str
    timelineSortId: int
    timelineTitle: str
    timelineDes: str
    picIdList: Union[List[str], None] = None
    audioIdList: Union[List[str], None] = None
    avgIdList: Union[List[str], None] = None
    storyIdList: Union[List[str], None] = None
    newsIdList: Union[List[str], None] = None


class ActArchiveTimelineData(BaseStruct):
    timelineList: List[ActArchiveTimelineItemData]


class ActArchiveMusicItemData(BaseStruct):
    musicId: str
    musicSortId: int


class ActArchiveMusicData(BaseStruct):
    musics: Dict[str, ActArchiveMusicItemData]


class ActArchivePicItemData(BaseStruct):
    picId: str
    picSortId: int


class ActArchivePicData(BaseStruct):
    pics: Dict[str, ActArchivePicItemData]


class ActArchiveStoryItemData(BaseStruct):
    storyId: str
    storySortId: int


class ActArchiveStoryData(BaseStruct):
    stories: Dict[str, ActArchiveStoryItemData]


class ActArchiveAvgItemData(BaseStruct):
    avgId: str
    avgSortId: int


class ActArchiveAvgData(BaseStruct):
    avgs: Dict[str, ActArchiveAvgItemData]


class ActArchiveNewsItemData(BaseStruct):
    newsId: str
    newsSortId: int


class ActArchiveNewsData(BaseStruct):
    news: Dict[str, ActArchiveNewsItemData]


class ActArchiveLandmarkItemData(BaseStruct):
    landmarkId: str
    landmarkSortId: int


class ActArchiveChapterLogData(BaseStruct):
    chapterName: str
    displayId: str
    unlockDes: str
    logs: List[str]
    chapterIcon: str


class ActArchiveComponentData(BaseStruct):
    pic: ActArchivePicData
    timeline: Union[ActArchiveTimelineData, None] = None
    music: Union[ActArchiveMusicData, None] = None
    story: Union[ActArchiveStoryData, None] = None
    avg: Union[ActArchiveAvgData, None] = None
    news: Union[ActArchiveNewsData, None] = None
    landmark: Union[Dict[str, ActArchiveLandmarkItemData], None] = None
    log: Union[Dict[str, ActArchiveChapterLogData], None] = None


class ActArchiveComponentTable(BaseStruct):
    components: Dict[str, ActArchiveComponentData]


class StoryReviewMetaTable(BaseStruct):
    __version__ = '23-09-29-15-41-03-569cae'

    miniActTrialData: MiniActTrialData
    actArchiveResData: ActArchiveResData
    actArchiveData: ActArchiveComponentTable
