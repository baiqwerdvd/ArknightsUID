from typing import Dict, List

from ..common import BaseStruct

from msgspec import field


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
    __version__ = '23-10-31-11-47-45-d410ff'

    replicate: Dict[str, ReplicateList]
