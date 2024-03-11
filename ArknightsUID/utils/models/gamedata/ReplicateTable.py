from typing import Dict, List

from ..common import BaseStruct

from msgspec import field


class ItemBundle(BaseStruct):
    id_: str = field(name="id")
    count: int
    type_: str = field(name="type")


class ReplicateData(BaseStruct):
    item: ItemBundle
    replicateTokenItem: ItemBundle


class ReplicateList(BaseStruct):
    replicateList: List[ReplicateData]


class ReplicateTable(BaseStruct):
    __version__ = "24-02-02-10-18-07-831ad8"

    replicate: Dict[str, ReplicateList]
