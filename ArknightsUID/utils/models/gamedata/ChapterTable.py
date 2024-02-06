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
    __version__ = '24-02-02-10-18-07-831ad8'

    chapters: Dict[str, ChapterData]
