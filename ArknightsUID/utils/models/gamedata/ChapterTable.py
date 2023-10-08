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
    __version__ = '23-09-29-15-41-03-569cae'

    chapters: Dict[str, ChapterData]
