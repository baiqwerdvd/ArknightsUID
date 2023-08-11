from gsuid_core.data_store import get_res_path
from gsuid_core.utils.error_reply import get_error
from msgspec import json as msgjson

from ..utils.ark_api import ark_skd_api


async def get_role_img(sr_uid: str):
    player_info = await ark_skd_api.get_game_player_info(sr_uid)
    if isinstance(player_info, int):
        return get_error(player_info)

    current_ts = player_info.currentTs
    status = player_info.status
    uid = status.uid

    player_save_path = get_res_path(['ArknightsUID', 'players'])

    with open(player_save_path / f'{uid}.json', 'wb') as file:
        file.write(msgjson.format(msgjson.encode(player_info), indent=4))
