from pydantic import BaseModel, Field


class ItemBundle(BaseModel):
    id_: str = Field(alias='id')
    count: int
    type_: str = Field(alias='type')


class StoryDataConditionStageCondition(BaseModel):
    stageId: str
    minState: int
    maxState: int


class StoryReviewInfoClientData(BaseModel):
    storyReviewType: int
    storyId: str
    storyGroup: str
    storySort: int
    storyDependence: str | None
    storyCanShow: int
    storyCode: str | None
    storyName: str
    storyPic: str | None
    storyInfo: str
    storyCanEnter: int
    storyTxt: str
    avgTag: str
    unLockType: str
    costItemType: str
    costItemId: str | None
    costItemCount: int
    stageCount: int
    requiredStages: list[StoryDataConditionStageCondition] | None


class StoryReviewGroupClientData(BaseModel):
    id_: str = Field(alias='id')
    name: str
    entryType: str
    actType: str
    startTime: int
    endTime: int
    startShowTime: int
    endShowTime: int
    remakeStartTime: int
    remakeEndTime: int
    storyEntryPicId: str | None
    storyPicId: str | None
    storyMainColor: str | None
    customType: int
    storyCompleteMedalId: str | None
    rewards: list[ItemBundle] | None
    infoUnlockDatas: list[StoryReviewInfoClientData]


class StoryReviewTable(BaseModel):
    __version__ = '23-07-27-18-50-06-aeb568'

    storyreviewtable: dict[str, StoryReviewGroupClientData]

    def __init__(self, data: dict) -> None:
        super().__init__(storyreviewtable=data)
