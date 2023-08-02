from pydantic import BaseModel, Field


class EnemyHandBookDataAbilty(BaseModel):
    text: str
    textFormat: str


class EnemyHandBookData(BaseModel):
    enemyId: str
    enemyIndex: str
    enemyTags: list[str] | None
    sortId: int
    name: str
    enemyLevel: str
    description: str
    attackType: str | None
    ability: str | None
    isInvalidKilled: bool
    overrideKillCntInfos: dict[str, int]
    hideInHandbook: bool
    abilityList: list[EnemyHandBookDataAbilty] | None
    linkEnemies: list[str] | None
    damageType: list[str] | None
    invisibleDetail: bool


class EnemyHandbookLevelInfoDataRangePair(BaseModel):
    min_: float = Field(alias='min')
    max_: float = Field(alias='max')


class EnemyHandbookLevelInfoData(BaseModel):
    classLevel: str
    attack: EnemyHandbookLevelInfoDataRangePair
    def_: EnemyHandbookLevelInfoDataRangePair = Field(alias='def')
    magicRes: EnemyHandbookLevelInfoDataRangePair
    maxHP: EnemyHandbookLevelInfoDataRangePair
    moveSpeed: EnemyHandbookLevelInfoDataRangePair
    attackSpeed: EnemyHandbookLevelInfoDataRangePair


class EnemyHandbookRaceData(BaseModel):
    id_: str = Field(alias='id')
    raceName: str
    sortId: int


class EnemyHandbookTable(BaseModel):
    __version__ = '23-07-27-18-50-06-aeb568'

    levelInfoList: list[EnemyHandbookLevelInfoData]
    enemyData: dict[str, EnemyHandBookData]
    raceData: dict[str, EnemyHandbookRaceData]

    class Config:
        extra = 'allow'
