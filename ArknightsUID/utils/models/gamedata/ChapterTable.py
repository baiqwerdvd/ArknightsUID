from typing import Dict, Union
from ..common import BaseStruct


class ChapterData(BaseStruct):
    chapterId: str
    chapterName: str
    chapterName2: str
    chapterIndex: int
    preposedChapterId: Union[str, None]
    startZoneId: str
    endZoneId: str
    chapterEndStageId: str


class ChapterTable(BaseStruct):
    __version__ = '23-07-27-18-50-06-aeb568'

    chapters: Dict[str, ChapterData]
