from pydantic import BaseModel, Field


class StoryDataTrigger(BaseModel):
    type_: str = Field(alias='type')
    key: str | None
    useRegex: bool


class StoryDataConditionStageCondition(BaseModel):
    stageId: str
    minState: int
    maxState: int


class StoryDataCondition(BaseModel):
    minProgress: int
    maxProgress: int
    minPlayerLevel: int
    requiredFlags: list[str]
    excludedFlags: list[str]
    requiredStages: list[StoryDataConditionStageCondition]


class ItemBundle(BaseModel):
    id_: str = Field(alias='id')
    count: int
    type_: str = Field(alias='type')


class StoryData(BaseModel):
    id_: str = Field(alias='id')
    needCommit: bool
    repeatable: bool
    disabled: bool
    videoResource: bool
    trigger: StoryDataTrigger
    condition: StoryDataCondition | None
    setProgress: int
    setFlags: list[str] | None
    completedRewards: list[ItemBundle] | None


class StoryTable(BaseModel):
    __version__ = '23-07-27-18-50-06-aeb568'

    stories: dict[str, StoryData]

    def __init__(self, data: dict) -> None:
        super().__init__(stories=data)
