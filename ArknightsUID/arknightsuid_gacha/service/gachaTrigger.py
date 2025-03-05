import json
import random
from pathlib import Path

from msgspec import convert

from .models import (
    GachaDetailTable,
    GachaTable,
    LinkageRuleType,
    PlayerDataDetail,
    PoolWeightItem,
    RuleType,
)
from .poolGenerator import PoolGenerator

cur_path = Path(__file__).resolve().parent

with cur_path.joinpath("gacha_table.json").open(encoding="UTF-8") as f:
    Excel = convert(json.load(f), GachaTable)
with cur_path.joinpath("gacha_detail_table.json").open(encoding="UTF-8") as f:
    Server = convert(json.load(f), GachaDetailTable)


class GachaTrigger:
    @classmethod
    async def postAdvancedGacha(cls, poolId: str, charHit: PoolWeightItem, player_data: PlayerDataDetail) -> None:
        if poolId not in [p.gachaPoolId for p in Excel.newbeeGachaPoolClient]:
            poolClient = next(p for p in Excel.gachaPoolClient if p.gachaPoolId == poolId)
            if poolClient.gachaRuleType == RuleType.LINKAGE:
                await cls._trigLinkageType(poolId, charHit, player_data)
            elif poolClient.gachaRuleType == RuleType.NORMAL:
                await cls._trigNoramlType(poolId, player_data)
            elif poolClient.gachaRuleType == RuleType.ATTAIN:
                await cls._trigAttainType(poolId, charHit, player_data)
            elif poolClient.gachaRuleType == RuleType.CLASSIC:
                await cls._trigClassicType(poolId, charHit, player_data)
            elif poolClient.gachaRuleType == RuleType.SINGLE:
                await cls._trigSingleType(poolId, charHit, player_data)
            elif poolClient.gachaRuleType == RuleType.FESCLASSIC:
                await cls._trigFesClassicType(poolId, charHit, player_data)
            elif poolClient.gachaRuleType == RuleType.CLASSIC_ATTAIN:
                await cls._trigClassicAttainType(poolId, charHit, player_data)

            curPool = player_data.user.gacha.normal[poolId]
            curPool.cnt += 1
            if curPool.avail and charHit.rarity >= curPool.rarity:
                curPool.avail = False

    # def _tryGetTrackState(poolId: str) -> GachaPoolInfo:
    #     self.track.pool.setdefault(poolId, GachaPoolInfo())
    #     return self.track.pool[poolId]

    @staticmethod
    async def _trigLinkageType(poolId: str, charHit: PoolWeightItem, player_data: PlayerDataDetail) -> None:
        pool = Server.details[poolId]
        poolClient = next(p for p in Excel.gachaPoolClient if p.gachaPoolId == poolId)
        track = player_data.track.gacha.pool[poolId]

        if not (linkageGroup := player_data.user.gacha.linkage):
            return
        if not (upCharInfo := pool.upCharInfo):
            return

        linkage_rule_id = poolClient.linkageRuleId
        if linkage_rule_id == LinkageRuleType.LINKAGE_R6_01:
            level5CharIdList = upCharInfo.perCharList[-1].charIdList
            linkage = linkageGroup[poolId][linkage_rule_id]
            if linkage.must6:
                linkage.must6Count -= 1
                if linkage.must6Count <= 0:
                    charHit.id_ = linkage.must6Char
                    charHit.rarity = linkage.must6Level
            if charHit.rarity == 5 and charHit.id_ == linkage.must6Char:
                linkage.must6 = False
                linkage.must6Char = ""
                linkage.must6Count = 0
            if charHit.rarity == 4 and charHit.id_ in level5CharIdList:
                if linkage.next5 and linkage.next5Char != "":
                    charHit.id_ = linkage.next5Char
                if charHit.id_ in level5CharIdList:
                    if next5Chars := [c for c in level5CharIdList if c not in track.gain5Star]:
                        linkage.next5Char = next5Chars[0]
                    else:
                        linkage.next5 = False
                        linkage.next5Char = ""
        elif linkage_rule_id == LinkageRuleType.LINKAGE_MH_01:
            linkage = linkageGroup[poolId][linkage_rule_id]
            if linkage.must6:
                linkage.must6Count -= 1
                if linkage.must6Count <= 0:
                    charHit.id_ = linkage.must6Char
                    charHit.rarity = linkage.must6Level
            if charHit.rarity == 5 and charHit.id_ == linkage.must6Char:
                linkage.must6 = False
                linkage.must6Char = ""
                linkage.must6Count = 0
        else:
            raise ValueError("invalid linkage pool rule type")

    @staticmethod
    async def _trigNoramlType(poolId: str, player_data: PlayerDataDetail) -> None:
        track = player_data.track.gacha.pool[poolId]
        player_data.track.gacha.nonNormal6StarCnt = track.non6StarCnt

    @staticmethod
    async def _trigAttainType(poolId: str, charHit: PoolWeightItem, player_data: PlayerDataDetail) -> None:
        pool = Server.details[poolId]
        weightPool = await PoolGenerator.build(pool)
        attain = player_data.user.gacha.attain[poolId]

        if not attain.attain6Count or charHit.rarity != 5:
            return
        attainPool = []
        for item in weightPool[charHit.rarity][0][1]:
            # if any(c.charId == item.id_ for c in userChars.values()):
            #     continue
            attainPool.append(item.id_)
        if attainPool:
            charHit.id_ = random.choice(attainPool)
        attain.attain6Count -= 1

    @staticmethod
    async def _trigClassicType(poolId: str, charHit: PoolWeightItem, player_data: PlayerDataDetail) -> None:
        track = player_data.track.gacha.pool[poolId]
        player_data.track.gacha.nonClassic6StarCnt = track.non6StarCnt
        charHit.isClassic = True

    @staticmethod
    async def _trigSingleType(poolId: str, charHit: PoolWeightItem, player_data: PlayerDataDetail) -> None:
        pool = Server.details[poolId]
        single = player_data.user.gacha.single[poolId]
        charHit.singleEnsureCnt = 150 if single.singleEnsureCnt < 0 else single.singleEnsureCnt
        charHit.isSingleEnsure = False

        if single.singleEnsureUse or not pool.upCharInfo:
            return
        must6Char = pool.upCharInfo.perCharList[0].charIdList[0]
        if single.singleEnsureCnt >= 0:
            if single.singleEnsureCnt + 1 < 150:
                if charHit.id_ != must6Char:
                    single.singleEnsureCnt += 1
                else:
                    single.singleEnsureCnt = 0
            elif charHit.id_ != must6Char:
                single.singleEnsureCnt -= 1
            else:
                single.singleEnsureCnt = 0
        elif charHit.rarity == 5:
            charHit.id_ = single.singleEnsureChar
            single.singleEnsureUse = True
            charHit.isSingleEnsure = True

    @staticmethod
    async def _trigFesClassicType(poolId: str, charHit: PoolWeightItem, player_data: PlayerDataDetail) -> None:
        track = player_data.track.gacha.pool[poolId]
        player_data.track.gacha.nonClassic6StarCnt = track.non6StarCnt
        charHit.isClassic = True

    @staticmethod
    async def _trigClassicAttainType(poolId: str, charHit: PoolWeightItem, player_data: PlayerDataDetail) -> None:
        pool = Server.details[poolId]
        weightPool = await PoolGenerator.build(pool)
        attain = player_data.user.gacha.attain[poolId]
        charHit.isClassic = True

        if not attain.attain6Count or charHit.rarity != 5:
            return
        attainPool = []
        for item in weightPool[charHit.rarity][0][1]:
            # if any(c.charId == item.id_ for c in userChars.values()):
            #     continue
            attainPool.append(item.id_)
        if attainPool:
            charHit.id_ = random.choice(attainPool)
        attain.attain6Count -= 1
