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
    __version__ = '23-10-31-11-47-45-d410ff'

    chapters: Dict[str, ChapterData]
