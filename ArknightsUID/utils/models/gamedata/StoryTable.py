from typing import Dict, List, Union

from ..common import BaseStruct

from msgspec import field


class StoryDataTrigger(BaseStruct):
    type_: str = field(name="type")
    key: Union[str, None]
    useRegex: bool


class StoryDataConditionStageCondition(BaseStruct):
    stageId: str
    minState: int
    maxState: int


class StoryDataCondition(BaseStruct):
    minProgress: int
    maxProgress: int
    minPlayerLevel: int
    requiredFlags: List[str]
    excludedFlags: List[str]
    requiredStages: List[StoryDataConditionStageCondition]


class ItemBundle(BaseStruct):
    id_: str = field(name="id")
    count: int
    type_: str = field(name="type")


class StoryData(BaseStruct):
    id_: str = field(name="id")
    needCommit: bool
    repeatable: bool
    disabled: bool
    videoResource: bool
    trigger: StoryDataTrigger
    condition: Union[StoryDataCondition, None]
    setProgress: int
    setFlags: Union[List[str], None]
    completedRewards: Union[List[ItemBundle], None]


class StoryTable(BaseStruct):
    __version__ = "24-02-02-10-18-07-831ad8"

    stories: Dict[str, StoryData]
