from pydantic import BaseModel, Field


class CharWordUnlockParam(BaseModel):
    valueStr: str | None
    valueInt: int


class CharWordData(BaseModel):
    charWordId: str
    wordKey: str
    charId: str
    voiceId: str
    voiceText: str
    voiceTitle: str
    voiceIndex: int
    voiceType: str
    unlockType: str
    unlockParam: list[CharWordUnlockParam]
    lockDescription: str | None
    placeType: str
    voiceAsset: str


class VoiceLangInfoData(BaseModel):
    wordkey: str
    voiceLangType: str
    cvName: list[str]


class VoiceLangData(BaseModel):
    wordkeys: list[str]
    charId: str
    dict_: dict[str, VoiceLangInfoData] = Field(alias='dict')


class VoiceLangTypeData(BaseModel):
    name: str
    groupType: str


class VoiceLangGroupData(BaseModel):
    name: str
    members: list[str]


class NewVoiceTimeData(BaseModel):
    timestamp: int
    charSet: list[str]


class CharwordTable(BaseModel):
    __version__ = '23-07-27-18-50-06-aeb568'

    charWords: dict[str, CharWordData]
    voiceLangDict: dict[str, VoiceLangData]
    defaultLangType: str
    newTagList: list[str]
    voiceLangTypeDict: dict[str, VoiceLangTypeData]
    voiceLangGroupTypeDict: dict[str, VoiceLangGroupData]
    charDefaultTypeDict: dict[str, str]
    startTimeWithTypeDict: dict[str, list[NewVoiceTimeData]]
    displayGroupTypeList: list[str]
    displayTypeList: list[str]
    playVoiceRange: str

    class Config:
        extra = 'allow'
