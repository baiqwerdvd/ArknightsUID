from typing import Dict, List
from ..common import BaseStruct
from msgspec import field
from msgspec import json as msgjson


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
    __version__ = '23-07-27-18-50-06-aeb568'

    replicate: Dict[str, ReplicateList]
