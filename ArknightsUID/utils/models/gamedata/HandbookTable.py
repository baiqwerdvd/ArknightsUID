from typing import List, Union

from ..common import BaseStruct


class HandBookInfoTextViewDataInfoTextAudio(BaseStruct):
    infoText: str
    audioName: str


class StoryTextAudioInfoListItem(BaseStruct):
    storyText: Union[str, None]
    storyTitle: Union[str, None]


class StoryTextAudioItem(BaseStruct):
    stories: List[StoryTextAudioInfoListItem]
    unLockorNot: bool
    unLockType: int
    unLockParam: str
    unLockString: str


class HandBookInfoTextViewData(BaseStruct):
    infoList: List[HandBookInfoTextViewDataInfoTextAudio]
    unLockorNot: bool
    unLockType: int
    unLockParam: str
    unLockLevel: int
    unLockLevelAdditive: int
    unLockString: str


class CharHandbook(BaseStruct):
    charID: str
    drawName: str
    infoName: str
    infoTextAudio: List[HandBookInfoTextViewData]
    storyTextAudio: List[StoryTextAudioItem]


class HandbookTable(BaseStruct):
    __version__ = '23-09-29-15-41-03-569cae'

    char_102_texas: CharHandbook
