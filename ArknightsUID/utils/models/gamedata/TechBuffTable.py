from typing import List, Union

from msgspec import field

from ..common import BaseStruct


class RuneDataSelector(BaseStruct):
    professionMask: int
    buildableMask: int
    charIdFilter: Union[List[str], None]
    enemyIdFilter: Union[List[str], None]
    skillIdFilter: Union[List[str], None]
    tileKeyFilter: Union[List[str], None]


class Blackboard(BaseStruct):
    key: str
    value: Union[float, None] = None
    valueStr: Union[str, None] = None


class RuneData(BaseStruct):
    key: str
    selector: RuneDataSelector
    blackboard: List[Blackboard]


class PackedRuneData(BaseStruct):
    id_: str = field(name="id")
    points: float
    mutexGroupKey: Union[str, None]
    description: str
    runes: List[RuneData]


class TechBuffTable(BaseStruct):
    __version__ = "24-02-02-10-18-07-831ad8"

    runes: List[PackedRuneData]
