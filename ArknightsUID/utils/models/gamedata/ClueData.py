from typing import List

from ..common import BaseStruct


class MeetingClueDataClueData(BaseStruct):
    clueId: str
    clueName: str
    clueType: str
    number: int


class MeetingClueDataClueTypeData(BaseStruct):
    clueType: str
    clueNumber: int


class MeetingClueDataReceiveTimeBonus(BaseStruct):
    receiveTimes: int
    receiveBonus: int


class ClueData(BaseStruct):
    __version__ = '23-12-02-09-28-50-918524'

    clues: List[MeetingClueDataClueData]
    clueTypes: List[MeetingClueDataClueTypeData]
    receiveTimeBonus: List[MeetingClueDataReceiveTimeBonus]
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
