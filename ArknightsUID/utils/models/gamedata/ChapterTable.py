from pydantic import BaseModel


class ChapterData(BaseModel):
    chapterId: str
    chapterName: str
    chapterName2: str
    chapterIndex: int
    preposedChapterId: str | None
    startZoneId: str
    endZoneId: str
    chapterEndStageId: str


class ChapterTable(BaseModel):
    __version__ = '23-07-27-18-50-06-aeb568'

    chapters: dict[str, ChapterData]

    class Config:
        extra = 'allow'

    def __init__(self, data: dict) -> None:
        super().__init__(chapters=data)
