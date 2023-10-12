from typing import Dict, List

from msgspec import field

from ..common import BaseStruct


class ItemBundle(BaseStruct):
    id_: str = field(name='id')
    count: int
    type_: str = field(name='type')


class ReplicateData(BaseStruct):
    item: ItemBundle
    replicateTokenItem: ItemBundle


class ReplicateList(BaseStruct):
    replicateList: List[ReplicateData]


class ReplicateTable(BaseStruct):
    __version__ = '23-10-08-17-52-18-288259'

    replicate: Dict[str, ReplicateList]
