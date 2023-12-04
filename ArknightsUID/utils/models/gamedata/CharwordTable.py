from typing import Dict, List, Union

from ..common import BaseStruct

from msgspec import field


class CharWordUnlockParam(BaseStruct):
    valueStr: Union[str, None]
    valueInt: int


class CharWordData(BaseStruct):
    charWordId: str
    wordKey: str
    charId: str
    voiceId: str
    voiceText: str
    voiceTitle: str
    voiceIndex: int
    voiceType: str
    unlockType: str
    unlockParam: List[CharWordUnlockParam]
    lockDescription: Union[str, None]
    placeType: str
    voiceAsset: str


class VoiceLangInfoData(BaseStruct):
    wordkey: str
    voiceLangType: str
    cvName: List[str]
    voicePath: Union[str, None] = None


class VoiceLangData(BaseStruct):
    wordkeys: List[str]
    charId: str
    dict_: Dict[str, VoiceLangInfoData] = field(name='dict')


class VoiceLangTypeData(BaseStruct):
    name: str
    groupType: str


class VoiceLangGroupData(BaseStruct):
    name: str
    members: List[str]


class NewVoiceTimeData(BaseStruct):
    timestamp: int
    charSet: List[str]


class CharwordTable(BaseStruct):
    __version__ = '23-10-31-11-47-45-d410ff'

    charWords: Dict[str, CharWordData]
    voiceLangDict: Dict[str, VoiceLangData]
    defaultLangType: str
    newTagList: List[str]
    voiceLangTypeDict: Dict[str, VoiceLangTypeData]
    voiceLangGroupTypeDict: Dict[str, VoiceLangGroupData]
    charDefaultTypeDict: Dict[str, str]
    startTimeWithTypeDict: Dict[str, List[NewVoiceTimeData]]
    displayGroupTypeList: List[str]
    displayTypeList: List[str]
    playVoiceRange: str
