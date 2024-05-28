import json
import random
import time
from pathlib import Path
from typing import ClassVar, List, Tuple

from loguru import logger
from msgspec import convert
from msgspec import json as mscjson

from .gachaTrigger import GachaTrigger
from .models import (
    GachaDetailTable,
    GachaPoolClientData,
    GachaPoolInfo,
    GachaTable,
    GachaTrackModel,
    LinkageRuleType,
    PlayerDataDetail,
    PlayerGacha,
    PoolWeightItem,
    RuleType,
)
from .poolGenerator import PoolGenerator

cur_path = Path(__file__).resolve().parent
with cur_path.joinpath("gacha_table.json").open(encoding="UTF-8") as f:
    Excel = convert(json.load(f), GachaTable)
with cur_path.joinpath("gacha_detail_table.json").open(encoding="UTF-8") as f:
    Server = convert(json.load(f), GachaDetailTable)


class GachaService:
    RIT5_UP_CNT_1: ClassVar[int] = 15
    RIT5_UP_CNT_2: ClassVar[int] = 20
    RIT6_UP_CNT: ClassVar[int] = 50

    forbiddenGachaPool: ClassVar[List[str]] = []

    @classmethod
    async def doAdvancedGacha(
        cls, poolId: str, ruleType: str, player_data: PlayerDataDetail
    ) -> PoolWeightItem:
        pool = Server.details[poolId]
        state = GachaService._tryGetTrackState(poolId, player_data)

        guaranteed = await cls._getGuaranteedRarity(poolId, player_data)
        rarityHit = cls._getRarityHit(poolId, guaranteed, player_data)
        if "BOOT" in poolId and not state.totalCnt:
            rarityHit = 3

        if ruleType != RuleType.FESCLASSIC:
            gachaPool = await PoolGenerator.build(pool)
        else:
            gachaPool = await PoolGenerator.build(pool, poolId, player_data)

        weightPool = gachaPool[rarityHit]
        charHit = random.choices(weightPool[0][1], weights=weightPool[0][0], k=1)[0]
        charHit.beforeNonHitCnt = state.non6StarCnt

        if ruleType != RuleType.FESCLASSIC and pool.upCharInfo and pool.upCharInfo.perCharList:
            if state.totalCnt + 1 >= 60:
                perChar = pool.upCharInfo.perCharList[-1]
                if charHit.rarity == perChar.rarityRank == 4:
                    if charIdList := [c for c in perChar.charIdList if c not in state.gain5Star]:
                        charHit.id_ = random.choice(charIdList)
            if state.totalCnt + 1 >= 200:
                perChar = pool.upCharInfo.perCharList[0]
                if charHit.rarity == perChar.rarityRank == 5:
                    if charIdList := [c for c in perChar.charIdList if c not in state.gain6Star]:
                        charHit.id_ = random.choice(charIdList)
        await GachaTrigger.postAdvancedGacha(poolId, charHit, player_data)

        if charHit.rarity == 4:
            state.non5StarCnt = 0
            state.gain5Star.append(charHit.id_)
        if charHit.rarity == 5:
            state.non6StarCnt = state.non5StarCnt = 0
            state.gain6Star.append(charHit.id_)
        else:
            state.non5StarCnt += 1
            state.non6StarCnt += 1
        state.totalCnt += 1

        # if self.showLog:
        logger.debug(f"{ruleType}|{poolId}: {mscjson.decode(mscjson.encode(charHit))}")
        return charHit

    @staticmethod
    async def handleNormalGacha(
        poolId: str, useTkt: int, player_data: PlayerDataDetail
    ) -> PoolWeightItem:
        now = time.time()
        poolClient = next(p for p in Excel.gachaPoolClient if p.gachaPoolId == poolId)
        state = GachaService._tryGetTrackState(poolId, player_data)

        if not state.init:
            if poolClient.gachaRuleType == RuleType.NORMAL:
                state.non6StarCnt = player_data.track.gacha.nonNormal6StarCnt
            state.init = 1

        if not poolClient.openTime <= now <= poolClient.endTime:
            raise ValueError("gacha pool not open")

        ## === ↓ ***基础数据校验*** ↓ ===
        # poolClient.openTime <= now <= poolClient.endTime -> gacha pool not open
        # useTkt:1|TKT_GACHA -> useTkt:0|DIAMOND_SHD -> gacha tkt state error
        ## === ↑ ***基础数据校验*** ↑ ===

        return await GachaService.doAdvancedGacha(
            poolId=poolId,
            ruleType=poolClient.gachaRuleType,
            player_data=player_data,
        )

    @staticmethod
    async def handleTenNormalGacha(
        poolId: str, itemId: str, useTkt: int, player_data: PlayerDataDetail
    ) -> List[PoolWeightItem]:
        now = time.time()
        poolClient = next(p for p in Excel.gachaPoolClient if p.gachaPoolId == poolId)
        state = GachaService._tryGetTrackState(poolId, player_data)

        if not state.init:
            if poolClient.gachaRuleType == RuleType.NORMAL:
                state.non6StarCnt = player_data.track.gacha.nonNormal6StarCnt
            state.init = 1

        if not poolClient.openTime <= now <= poolClient.endTime:
            pass
            # raise ValueError("gacha pool not open")

        ## === ↓ ***基础数据校验*** ↓ ===
        # poolClient.openTime <= now <= poolClient.endTime -> gacha pool not open
        # useTkt:4|LINKAGE_TKT_GACHA_10 -> useTkt:2|TKT_GACHA_10 -> useTkt:5|TKT_GACHA -> useTkt:0|DIAMOND_SHD -> gacha tkt state error
        ## === ↑ ***基础数据校验*** ↑ ===

        result: list[PoolWeightItem] = []
        for _ in range(10):
            obj = await GachaService.doAdvancedGacha(
                poolId=poolId,
                ruleType=poolClient.gachaRuleType,
                player_data=player_data,
            )
            result.append(obj)
        return result

    @staticmethod
    async def handleNewbeeGacha(poolId: str, player_data: PlayerDataDetail) -> PoolWeightItem:
        now = time.time()
        poolClient = next(p for p in Excel.newbeeGachaPoolClient if p.gachaPoolId == poolId)
        carousel = next(g for g in Excel.carousel if g.poolId == poolId)
        curPool = player_data.user.gacha.newbee
        state = GachaService._tryGetTrackState(poolId, player_data)

        if not state.init:
            state.init = 1

        if not carousel.startTime <= now <= carousel.endTime or not curPool.openFlag:
            raise ValueError("gacha pool not open")

        ## === ↓ ***基础数据校验*** ↓ ===
        # carousel.startTime <= now <= carousel.endTime | openFlag -> gacha pool not open
        # cnt = 0 -> newbie pool cnt not enough
        ## === ↑ ***基础数据校验*** ↑ ===

        # 调试状态下模拟客户端请求时需强制完成`obt/guide/l0-0/1_recruit_adv`
        curPool.cnt -= 1

        return await GachaService.doAdvancedGacha(
            poolId=poolId, ruleType=RuleType.NEWBEE, player_data=player_data
        )

    @staticmethod
    async def handleTenNewbieGacha(
        poolId: str, player_data: PlayerDataDetail
    ) -> List[PoolWeightItem]:
        now = time.time()
        poolClient = next(p for p in Excel.newbeeGachaPoolClient if p.gachaPoolId == poolId)
        carousel = next(g for g in Excel.carousel if g.poolId == poolId)
        curPool = player_data.user.gacha.newbee
        state = GachaService._tryGetTrackState(poolId, player_data)

        if not state.init:
            state.init = 1

        if not carousel.startTime <= now <= carousel.endTime or not curPool.openFlag:
            raise ValueError("gacha pool not open")

        ## === ↓ ***基础数据校验*** ↓ ===
        # carousel.startTime <= now <= carousel.endTime | openFlag -> gacha pool not open
        # cnt < 10 -> newbie pool cnt not enough
        ## === ↑ ***基础数据校验*** ↑ ===

        curPool.cnt -= 10

        result: List[PoolWeightItem] = []
        for _ in range(10):
            obj = await GachaService.doAdvancedGacha(
                poolId=poolId,
                ruleType=RuleType.NEWBEE,
                player_data=player_data,
            )
            result.append(obj)
        return result

    @staticmethod
    async def handleLimitedGacha(
        poolId: str,
        useTkt: int,
        player_data: PlayerDataDetail,
    ) -> Tuple[PoolWeightItem, List]:
        now = time.time()
        poolClient = next(p for p in Excel.gachaPoolClient if p.gachaPoolId == poolId)
        state = GachaService._tryGetTrackState(poolId, player_data)
        itemGet = []

        if not state.init:
            state.init = 1

        if not poolClient.openTime <= now <= poolClient.endTime:
            raise ValueError("gacha pool not open")

        ## === ↓ ***基础数据校验*** ↓ ===
        # poolClient.openTime <= now <= poolClient.endTime -> gacha pool not open
        # useTkt:3 -> useTkt:1|TKT_GACHA -> useTkt:0|DIAMOND_SHD -> gacha tkt state error
        ## === ↑ ***基础数据校验*** ↑ ===

        if useTkt == 3 and player_data.user.gacha.limit[poolId].leastFree:
            player_data.user.gacha.limit[poolId].leastFree -= 1
        # 处理 lmtgs -> itemGet

        return await GachaService.doAdvancedGacha(
            poolId=poolId,
            ruleType=poolClient.gachaRuleType,
            player_data=player_data,
        ), itemGet

    @staticmethod
    async def handleTenLimitedGacha(
        poolId: str, itemId: str, useTkt: int, player_data: PlayerDataDetail
    ) -> Tuple[List[PoolWeightItem], List[List]]:
        now = time.time()
        poolClient = next(p for p in Excel.gachaPoolClient if p.gachaPoolId == poolId)
        state = GachaService._tryGetTrackState(poolId, player_data)
        itemGet = []

        if not state.init:
            state.init = 1

        if not poolClient.openTime <= now <= poolClient.endTime:
            raise ValueError("gacha pool not open")

        ## === ↓ ***基础数据校验*** ↓ ===
        # poolClient.openTime <= now <= poolClient.endTime -> gacha pool not open
        # useTkt:4|LIMITED_TKT_GACHA_10 -> useTkt:2|TKT_GACHA_10 -> useTkt:5|TKT_GACHA -> useTkt:0|DIAMOND_SHD -> gacha tkt state error
        ## === ↑ ***基础数据校验*** ↑ ===

        # 处理 lmtgs -> itemGet
        result: List[PoolWeightItem] = []

        for _ in range(10):
            obj = await GachaService.doAdvancedGacha(
                poolId=poolId,
                ruleType=poolClient.gachaRuleType,
                player_data=player_data,
            )
            result.append(obj)
        return result, itemGet

    @staticmethod
    async def handleClassicGacha(
        poolId: str,
        useTkt: int,
        player_data: PlayerDataDetail,
    ) -> PoolWeightItem:
        now = time.time()
        poolClient = next(p for p in Excel.gachaPoolClient if p.gachaPoolId == poolId)
        state = GachaService._tryGetTrackState(poolId, player_data)

        if not state.init:
            state.init = 1

        if not poolClient.openTime <= now <= poolClient.endTime:
            pass
            # raise ValueError("gacha pool not open")

        ## === ↓ ***基础数据校验*** ↓ ===
        # poolClient.openTime <= now <= poolClient.endTime -> gacha pool not open
        # useTkt:6|CLASSIC_TKT_GACHA -> useTkt:1|TKT_GACHA -> useTkt:0|DIAMOND_SHD -> gacha tkt state error
        ## === ↑ ***基础数据校验*** ↑ ===

        return await GachaService.doAdvancedGacha(
            poolId=poolId,
            ruleType=poolClient.gachaRuleType,
            player_data=player_data,
        )

    @staticmethod
    async def handleTenClassicGacha(
        poolId: str,
        useTkt: int,
        player_data: PlayerDataDetail,
    ) -> List[PoolWeightItem]:
        now = time.time()
        poolClient = next(p for p in Excel.gachaPoolClient if p.gachaPoolId == poolId)
        state = GachaService._tryGetTrackState(poolId, player_data)

        if not state.init:
            state.init = 1

        if not poolClient.openTime <= now <= poolClient.endTime:
            raise ValueError("gacha pool not open")

        ## === ↓ ***基础数据校验*** ↓ ===
        # poolClient.openTime <= now <= poolClient.endTime -> gacha pool not open
        # useTkt:7|CLASSIC_TKT_GACHA_10 -> useTkt:8|CLASSIC_TKT_GACHA -> useTkt:2|TKT_GACHA_10 -> useTkt:5|TKT_GACHA -> useTkt:0|DIAMOND_SHD -> gacha tkt state error
        ## === ↑ ***基础数据校验*** ↑ ===

        result: List[PoolWeightItem] = []
        for _ in range(10):
            obj = await GachaService.doAdvancedGacha(
                poolId=poolId,
                ruleType=poolClient.gachaRuleType,
                player_data=player_data,
            )
            result.append(obj)
        return result

    @classmethod
    async def tryInitGachaRule(
        cls, poolClient: GachaPoolClientData, player_data: PlayerDataDetail
    ) -> None:
        poolId = poolClient.gachaPoolId
        if poolClient.gachaRuleType in [RuleType.ATTAIN, RuleType.CLASSIC_ATTAIN]:
            await cls._initAttainPoolState(poolId, poolClient, player_data)
        elif poolClient.gachaRuleType == RuleType.LINKAGE:
            await cls._initLinkagePoolState(poolId, poolClient, player_data)
        elif poolClient.gachaRuleType == RuleType.SINGLE:
            await cls._initSinglePoolState(poolId, player_data)
        elif poolClient.gachaRuleType == RuleType.FESCLASSIC:
            await cls._initFesClassicPoolState(poolId, player_data)

    @staticmethod
    def _tryGetTrackState(poolId: str, player_data: PlayerDataDetail) -> GachaPoolInfo:
        player_data.track.gacha.pool.setdefault(poolId, GachaPoolInfo())
        return player_data.track.gacha.pool[poolId]

    @staticmethod
    async def _initAttainPoolState(
        poolId: str, poolClient: GachaPoolClientData, player_data: PlayerDataDetail
    ) -> None:
        if poolId not in player_data.user.gacha.attain:
            attain6Count = (poolClient.dynMeta or {}).get("attainRare6Num", 0)
            poolObj = player_data.user.gacha.PlayerAttainGacha(attain6Count=attain6Count)
            player_data.user.gacha.attain.setdefault(poolId, poolObj)

    @staticmethod
    async def _initLinkagePoolState(
        poolId: str, poolClient: GachaPoolClientData, player_data: PlayerDataDetail
    ) -> None:
        pool = Server.details[poolId]
        if (upCharInfo := pool.upCharInfo) and poolClient.linkageParam:
            rType = poolClient.linkageRuleId
            if rType == LinkageRuleType.LINKAGE_R6_01:
                poolObj = player_data.user.gacha.PlayerLinkageGacha(
                    next5=True,
                    next5Char="",
                    must6=True,
                    must6Char=upCharInfo.perCharList[0].charIdList[0],
                    must6Count=poolClient.linkageParam["guaranteeTarget6Count"],
                    must6Level=5,
                )
            elif rType == LinkageRuleType.LINKAGE_MH_01:
                poolObj = player_data.user.gacha.PlayerLinkageGacha(
                    next5=False,
                    next5Char="",
                    must6=True,
                    must6Char=upCharInfo.perCharList[0].charIdList[0],
                    must6Count=poolClient.linkageParam["guaranteeTarget6Count"],
                    must6Level=5,
                )
            else:
                raise ValueError("invalid linkage gacha rule id")
            player_data.user.gacha.linkage.setdefault(rType, {})
            if poolId not in player_data.user.gacha.linkage:
                player_data.user.gacha.linkage[poolId].setdefault(rType, poolObj)

    @staticmethod
    async def _initSinglePoolState(poolId: str, player_data: PlayerDataDetail) -> None:
        if poolId not in player_data.user.gacha.single:
            pool = Server.details[poolId]
            if upCharInfo := pool.upCharInfo:
                poolObj = player_data.user.gacha.PlayerSingleGacha(
                    singleEnsureCnt=0,
                    singleEnsureUse=False,
                    singleEnsureChar=upCharInfo.perCharList[0].charIdList[0],
                )
                player_data.user.gacha.single.setdefault(poolId, poolObj)

    @staticmethod
    async def _initFesClassicPoolState(poolId: str, player_data: PlayerDataDetail) -> None:
        if poolId not in player_data.user.gacha.fesClassic:
            poolObj = player_data.user.gacha.PlayerFesClassicGacha(upChar={})
            player_data.user.gacha.fesClassic.setdefault(poolId, poolObj)

    @classmethod
    def _getRarityHit(
        cls,
        poolId: str,
        guaranteed: int,
        player_data: PlayerDataDetail,
    ) -> int:
        pool = Server.details[poolId]
        perAvailList = pool.availCharInfo.perAvailList
        state = player_data.track.gacha.pool[poolId]
        rarityWeights = [0.0] * 2 + [i.totalPercent for i in reversed(perAvailList)]

        add6StarWeight = 0
        if state.non6StarCnt >= cls.RIT6_UP_CNT:
            add6StarWeight += rarityWeights[5] * (1 + state.non6StarCnt - cls.RIT6_UP_CNT)
            if rarityWeights[5] + add6StarWeight > 1:
                add6StarWeight = 1 - rarityWeights[5]
            rarityWeights[5] += add6StarWeight

        add5StarWeight = 0
        if (cnt51 := min(1 + state.non5StarCnt - cls.RIT5_UP_CNT_1, 5)) > 0:
            add5StarWeight += rarityWeights[4] * cnt51 * 0.25
        if (cnt52 := 1 + state.non5StarCnt - cls.RIT5_UP_CNT_2) >= 0:
            add5StarWeight += rarityWeights[4] * cnt52 * 0.5
        rarityWeights[4] += add5StarWeight

        totalWeight = 0
        for i in range(5, -1, -1):
            rarityWeights[i] = min(rarityWeights[i], 1 - totalWeight)
            totalWeight += rarityWeights[i]
        rarityWeights[2] = max(0, 1 - sum(rarityWeights[3:6]))

        rarityHit = random.choices(range(6), weights=rarityWeights, k=1)[0]
        return max(rarityHit, guaranteed)

    @staticmethod
    async def _getGuaranteedRarity(poolId: str, player_data: PlayerDataDetail) -> int:
        newbeeGachaIds = [p.gachaPoolId for p in Excel.newbeeGachaPoolClient]
        guaranteedRarity = 2
        if poolId not in newbeeGachaIds:
            poolClient = next(p for p in Excel.gachaPoolClient if p.gachaPoolId == poolId)
            if poolId not in player_data.user.gacha.normal:
                player_data.user.gacha.normal[poolId] = player_data.user.gacha.PlayerGachaPool(
                    cnt=0,
                    maxCnt=poolClient.guarantee5Count,
                    rarity=4,
                    avail=bool(poolClient.guarantee5Avail),
                )
            curPool = player_data.user.gacha.normal[poolId]
            if curPool.avail and curPool.cnt + 1 == curPool.maxCnt:
                guaranteedRarity = curPool.rarity
            await GachaService.tryInitGachaRule(poolClient, player_data)
        else:
            cur = player_data.track.gacha.pool[poolId]
            if not cur.gain6Star and cur.totalCnt + 1 == 10:
                guaranteedRarity = 5
            if not cur.gain5Star and cur.totalCnt + 1 == 21:
                guaranteedRarity = 4
        return guaranteedRarity
