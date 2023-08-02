from pydantic import BaseModel


class HandBookInfoTextViewDataInfoTextAudio(BaseModel):
    infoText: str
    audioName: str


class StoryTextAudioInfoListItem(BaseModel):
    storyText: str | None
    storyTitle: str | None


class StoryTextAudioItem(BaseModel):
    stories: list[StoryTextAudioInfoListItem]
    unLockorNot: bool
    unLockType: int
    unLockParam: str
    unLockString: str


class HandBookInfoTextViewData(BaseModel):
    infoList: list[HandBookInfoTextViewDataInfoTextAudio]
    unLockorNot: bool
    unLockType: int
    unLockParam: str
    unLockLevel: int
    unLockLevelAdditive: int
    unLockString: str


class CharHandbook(BaseModel):
    charID: str
    drawName: str
    infoName: str
    infoTextAudio: list[HandBookInfoTextViewData]
    storyTextAudio: list[StoryTextAudioItem]


class HandbookTable(BaseModel):
    __version__ = '23-07-27-18-50-06-aeb568'

    char_102_texas: CharHandbook
