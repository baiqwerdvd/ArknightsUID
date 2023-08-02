from pydantic import BaseModel, Field


class ItemBundle(BaseModel):
    id_: str = Field(alias='id')
    count: int
    type_: str = Field(alias='type')


class ReplicateData(BaseModel):
    item: ItemBundle
    replicateTokenItem: ItemBundle


class ReplicateList(BaseModel):
    replicateList: list[ReplicateData]


class ReplicateTable(BaseModel):
    __version__ = '23-07-27-18-50-06-aeb568'

    replicate: dict[str, ReplicateList]

    class Config:
        extra = 'allow'

    def __init__(self, **data):
        super().__init__(replicate=data)
