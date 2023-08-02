from pydantic import BaseModel


class MeetingClueDataClueData(BaseModel):
    clueId: str
    clueName: str
    clueType: str
    number: int


class MeetingClueDataClueTypeData(BaseModel):
    clueType: str
    clueNumber: int


class MeetingClueDataReceiveTimeBonus(BaseModel):
    receiveTimes: int
    receiveBonus: int


class ClueData(BaseModel):
    __version__ = '23-07-27-18-50-06-aeb568'

    clues: list[MeetingClueDataClueData]
    clueTypes: list[MeetingClueDataClueTypeData]
    receiveTimeBonus: list[MeetingClueDataReceiveTimeBonus]
    inventoryLimit: int
    outputBasicBonus: int
    outputOperatorsBonus: int
    cluePointLimit: int
    expiredDays: int
    transferBonus: int
    recycleBonus: int
    expiredBonus: int
    communicationDuration: int
    initiatorBonus: int
    participantsBonus: int

    class Config:
        extra = 'allow'
