from typing import List, Tuple, overload

from typing_extensions import TypeAlias

from .models import (
    GachaDetailDataGachaAvailChar,
    GachaDetailInfo,
    PlayerDataDetail,
    PoolWeightItem,
    gachaGroupConfig,
)

PoolResultA: TypeAlias = Tuple[List[float], List[PoolWeightItem]]
PoolResultB: TypeAlias = List[List[Tuple[List[float], List[PoolWeightItem]]]]


class PoolGenerator:
    @staticmethod
    async def buildSimplePool(detail: GachaDetailDataGachaAvailChar) -> PoolResultA:
        weights, pool = [], []
        for group in detail.perAvailList:
            if not group.charIdList:
                continue
            for charId in group.charIdList:
                weightObj = PoolWeightItem(
                    id_=charId, count=1, type_="CHAR", rarity=group.rarityRank
                )
                pool.append(weightObj)
            length = len(group.charIdList)
            weights.extend([group.totalPercent / length] * length)
        return weights, pool

    @overload
    @classmethod
    async def build(cls, detail: GachaDetailInfo) -> PoolResultB: ...

    @overload
    @classmethod
    async def build(
        cls, detail: GachaDetailInfo, poolId: str, player_data: PlayerDataDetail
    ) -> PoolResultB: ...

    @classmethod
    async def build(cls, *args) -> PoolResultB:  # type: ignore[overload-overlap]
        if len(args) == 1:
            return await cls._buildAdvancedPool(*args)
        if len(args) == 3:
            return await cls._buildFesCustomPool(*args)
        raise TypeError("PoolGenerator.build invalid arguments")

    @staticmethod
    async def _buildAdvancedPool(detail: GachaDetailInfo) -> PoolResultB:
        result = [[] for _ in range(6)]
        for group in detail.availCharInfo.perAvailList:
            conf = gachaGroupConfig(normalCharCnt=len(group.charIdList))
            if info := detail.upCharInfo:
                upGroup = next(
                    (x for x in info.perCharList if x.rarityRank == group.rarityRank), None
                )
                if upGroup is not None:
                    conf.upChars_1 = upGroup.charIdList
                    conf.perUpWeight_1 = upGroup.percent
                    conf.normalCharCnt -= len(conf.upChars_1)
                    conf.totalWeights -= conf.perUpWeight_1 * len(conf.upChars_1)
            if info := detail.weightUpCharInfoList:
                conf.upChars_2 = [x.charId for x in info if x.rarityRank == group.rarityRank]
                if conf.upChars_2:
                    conf.perUpWeight_2 = info[0].weight
                    conf.normalCharCnt -= len(conf.upChars_2)
                    rate = conf.perUpWeight_2 // 100
                    conf.perUpWeight_2 = (
                        conf.totalWeights
                        / (conf.normalCharCnt + len(conf.upChars_2) * rate)
                        * rate
                    )
                    conf.totalWeights -= conf.perUpWeight_2 * len(conf.upChars_2)
            for charId in group.charIdList:
                weightObj = PoolWeightItem(
                    id_=charId,
                    count=1,
                    type_="CHAR",
                    rarity=group.rarityRank,
                )
                conf.pool.append(weightObj)
                if charId in conf.upChars_1:
                    conf.weights.append(conf.perUpWeight_1)
                elif charId in conf.upChars_2:
                    conf.weights.append(conf.perUpWeight_2)
                else:
                    conf.weights.append(conf.totalWeights / conf.normalCharCnt)
            result[group.rarityRank].append((conf.weights, conf.pool))
        return result

    @staticmethod
    async def _buildFesCustomPool(
        detail: GachaDetailInfo, poolId: str, player_data: PlayerDataDetail
    ) -> PoolResultB:
        result = [[] for _ in range(6)]
        for group in detail.availCharInfo.perAvailList:
            conf = gachaGroupConfig(normalCharCnt=len(group.charIdList))
            if info := player_data.user.gacha.fesClassic:
                if upGroup := info[poolId].upChar.get(str(group.rarityRank)):
                    conf.upChars_1 = upGroup[:]
                    conf.perUpWeight_1 = 0.25 if group.rarityRank == 5 else 0.166667
                    conf.normalCharCnt -= len(conf.upChars_1)
                    conf.totalWeights -= conf.perUpWeight_1 * len(conf.upChars_1)
            for charId in group.charIdList:
                weightObj = PoolWeightItem(
                    id_=charId,
                    count=1,
                    type_="CHAR",
                    rarity=group.rarityRank,
                )
                conf.pool.append(weightObj)
                if charId in conf.upChars_1:
                    conf.weights.append(conf.perUpWeight_1)
                else:
                    conf.weights.append(conf.totalWeights / conf.normalCharCnt)
            result[group.rarityRank].append((conf.weights, conf.pool))
        return result
