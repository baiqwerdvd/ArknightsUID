from typing import List, Union

from msgspec import field

from ..common import BaseStruct


class RuneDataSelector(BaseStruct):
    professionMask: Union[int, str]
    buildableMask: int
    charIdFilter: Union[List[str], None]
    enemyIdFilter: Union[List[str], None]
    enemyIdExcludeFilter: Union[List[str], None]
    enemyLevelTypeFilter: Union[List[str], None]
    skillIdFilter: Union[List[str], None]
    tileKeyFilter: Union[List[str], None]
    groupTagFilter: Union[List[str], None]
    filterTagFilter: Union[List[str], None]
    filterTagExcludeFilter: Union[List[str], None]
    subProfessionExcludeFilter: Union[List[str], None]
    mapTagFilter: Union[List[str], None]


class Blackboard(BaseStruct):
    key: str
    value: Union[float, None] = None
    valueStr: Union[str, None] = None


class RuneData(BaseStruct):
    key: str
    selector: RuneDataSelector
    blackboard: List[Blackboard]


class RuneTablePackedRuneData(BaseStruct):
    id_: str = field(name="id")
    points: float
    mutexGroupKey: Union[str, None]
    description: str
    runes: List[RuneData]


class CharmItemData(BaseStruct):
    id_: str = field(name="id")
    sort: int
    name: str
    icon: str
    itemUsage: str
    itemDesc: str
    itemObtainApproach: str
    rarity: int
    desc: str
    price: int
    specialObtainApproach: Union[str, None]
    charmType: str
    obtainInRandom: bool
    dropStages: List[str]
    runeData: RuneTablePackedRuneData
    charmEffect: str


class CharmTable(BaseStruct):
    __version__ = "24-02-02-10-18-07-831ad8"

    charmList: List[CharmItemData]
