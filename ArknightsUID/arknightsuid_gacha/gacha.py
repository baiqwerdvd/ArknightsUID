import json
import time
from pathlib import Path

from msgspec import convert
from msgspec import json as msgjson

from .service.gachaLogic import GachaService
from .service.models import (
    GachaDetailTable,
    GachaPoolClientData,
    GachaTable,
    GachaTrackModel,
    PlayerData,
    PlayerDataDetail,
    PlayerGacha,
    PlayerTrack,
    RuleType,
)

cur_path = Path(__file__).parent
with cur_path.joinpath("gacha_table.json").open(encoding="UTF-8") as f:
    Excel = convert(json.load(f), GachaTable)
with cur_path.joinpath("gacha_detail_table.json").open(encoding="UTF-8") as f:
    Server = convert(json.load(f), GachaDetailTable)


async def gacha(uid: str):
    if not (cur_path / Path(f"{uid}.json")).exists():
        with open(cur_path / Path(f"{uid}.json"), "w") as f:
            data = PlayerDataDetail(
                user=PlayerData(
                    gacha=PlayerGacha(
                        newbee=PlayerGacha.PlayerNewbeeGachaPool(openFlag=1, cnt=21, poolId="BOOT_0_1_2"),
                        normal={},
                        attain={},
                        single={},
                        fesClassic={},
                        limit={},
                        linkage={},
                    )
                ),
                track=PlayerTrack(
                    gacha=GachaTrackModel(),
                ),
            )
            json.dump({"uid": uid, "data": msgjson.decode(msgjson.encode(data))}, f, indent=4)

    with open(cur_path / Path(f"{uid}.json")) as f:
        data = json.load(f)
    data = convert(data["data"], PlayerDataDetail)
    char_get = await testTenAdvancedGacha("CLASSIC_48_0_2", data, 0)
    with open(cur_path / Path(f"{uid}.json"), "w") as f:
        json.dump({"uid": uid, "data": msgjson.decode(msgjson.encode(data))}, f, indent=4)

    return char_get


async def testTenAdvancedGacha(
    poolId: str,
    player_data: PlayerDataDetail,
    useTkt: int = 0,
    itemId: str = "4003",
) -> list[str]:
    now = int(time.time())
    newbeeGachaPoolClient = Excel.newbeeGachaPoolClient
    gachaPoolClient = Excel.gachaPoolClient

    if poolId not in [p.gachaPoolId for p in newbeeGachaPoolClient]:
        if not (pool := next((p for p in gachaPoolClient if p.gachaPoolId == poolId), None)):
            raise ValueError("invalid gacha pool id")
    elif not (pool := next((p for p in newbeeGachaPoolClient if p.gachaPoolId == poolId), None)):
        raise ValueError("invalid gacha pool id")

    if poolId in GachaService.forbiddenGachaPool:
        raise ValueError("当前寻访暂时无法使用, 详情请关注官方公告")

    if isinstance(pool, GachaPoolClientData):
        if pool.gachaRuleType in [RuleType.ATTAIN, RuleType.FESCLASSIC, RuleType.CLASSIC_ATTAIN]:
            raise ValueError("Unsupported gacha rule type")
        elif pool.gachaRuleType in [RuleType.NORMAL, RuleType.SINGLE, RuleType.LINKAGE]:
            result = await GachaService.handleTenNormalGacha(
                poolId,
                itemId,
                useTkt,
                player_data,
            )
        elif pool.gachaRuleType == RuleType.LIMITED:
            result, itemGet = await GachaService.handleTenLimitedGacha(
                poolId,
                itemId,
                useTkt,
                player_data,
            )
        elif pool.gachaRuleType == RuleType.CLASSIC:
            result = await GachaService.handleTenClassicGacha(
                poolId,
                useTkt,
                player_data,
            )
        else:
            raise ValueError(f"invalid gacha rule type: {pool.gachaRuleType}")
    else:
        result = await GachaService.handleTenNewbieGacha(
            poolId,
            player_data,
        )

    char_get = []

    state = player_data.track.gacha.pool[poolId]
    for _, bundle in enumerate(result):
        char_get.append(bundle.id_)
        state.history.append(f"{bundle.id_}&{bundle.rarity}&{now}")  # &{charGet.isNew}")
    return char_get
