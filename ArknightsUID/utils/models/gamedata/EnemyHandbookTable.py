from typing import Dict, List, Union

from ..common import BaseStruct

from msgspec import field


class EnemyHandBookDataAbilty(BaseStruct):
    text: str
    textFormat: str


class EnemyHandBookData(BaseStruct):
    enemyId: str
    enemyIndex: str
    enemyTags: Union[List[str], None]
    sortId: int
    name: str
    enemyLevel: str
    description: str
    attackType: Union[str, None]
    ability: Union[str, None]
    isInvalidKilled: bool
    overrideKillCntInfos: Dict[str, int]
    hideInHandbook: bool
    abilityList: Union[List[EnemyHandBookDataAbilty], None]
    linkEnemies: Union[List[str], None]
    damageType: Union[List[str], None]
    invisibleDetail: bool
    hideInStage: Union[bool, None] = None


class EnemyHandbookLevelInfoDataRangePair(BaseStruct):
    min_: float = field(name="min")
    max_: float = field(name="max")


class EnemyHandbookLevelInfoData(BaseStruct):
    classLevel: str
    attack: EnemyHandbookLevelInfoDataRangePair
    def_: EnemyHandbookLevelInfoDataRangePair = field(name="def")
    magicRes: EnemyHandbookLevelInfoDataRangePair
    maxHP: EnemyHandbookLevelInfoDataRangePair
    moveSpeed: EnemyHandbookLevelInfoDataRangePair
    attackSpeed: EnemyHandbookLevelInfoDataRangePair
    enemyDamageRes: EnemyHandbookLevelInfoDataRangePair
    enemyRes: EnemyHandbookLevelInfoDataRangePair


class EnemyHandbookRaceData(BaseStruct):
    id_: str = field(name="id")
    raceName: str
    sortId: int


class EnemyHandbookTable(BaseStruct):
    __version__ = "24-02-02-10-18-07-831ad8"

    levelInfoList: List[EnemyHandbookLevelInfoData]
    enemyData: Dict[str, EnemyHandBookData]
    raceData: Dict[str, EnemyHandbookRaceData]
