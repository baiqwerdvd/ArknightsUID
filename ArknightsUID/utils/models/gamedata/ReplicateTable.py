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
    __version__ = '23-09-29-15-41-03-569cae'

    replicate: Dict[str, ReplicateList]
