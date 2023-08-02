from pydantic import BaseModel, Field


class GridPosition(BaseModel):
    row: int
    col: int


class ObscuredRect(BaseModel):
    m_xMin: float
    m_yMin: float
    m_width: float
    m_height: float


class Stage(BaseModel):
    id_: str = Field(alias='id')
    direction: int
    grids: list[GridPosition]
    boundingBoxes: list[ObscuredRect] | None = None


class RangeTable(BaseModel):
    __version__ = '23-07-27-18-50-06-aeb568'

    range: dict[str, Stage]

    def __init__(self, **data):
        super().__init__(range=data)
