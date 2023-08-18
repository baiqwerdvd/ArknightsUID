from copy import deepcopy
from typing import Any, Literal

import msgspec
from aiohttp import ClientSession, ContentTypeError, TCPConnector
from gsuid_core.logger import logger

from ...database.models import ArknightsUser
from ...models.skland.models import ArknightsPlayerInfoModel, ArknightsUserMeModel
from .api import ARK_PLAYER_INFO, ARK_USER_ME


class BaseArkApi:
    ssl_verify = True
    _HEADER = {
        'Host': 'zonai.skland.com',
        'Origin': 'https://www.skland.com',
        'Referer': 'https://www.skland.com/',
        'content-type': 'application/json; charset=UTF-8',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) \
            AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36',
    }

    async def get_game_player_info(self, uid: str) -> int | ArknightsPlayerInfoModel:
        cred = await ArknightsUser.get_user_attr_by_uid(uid=uid, attr='cred')
        if cred is None:
            return -61
        is_vaild = await self.check_cred_valid(cred)
        if isinstance(is_vaild, bool):
            await ArknightsUser.delete_user_data_by_uid(uid)
            return -61
        header = deepcopy(self._HEADER)
        header['Cred'] = cred
        raw_data = await self._ark_request(
            url=ARK_PLAYER_INFO,
            params={'uid': uid},
            header=header,
        )
        unpack_data = self.unpack(raw_data)
        if isinstance(unpack_data, int):
            return unpack_data
        else:
            import json
            with open('test.json', 'w', encoding='utf-8') as f:
                json.dump(unpack_data, f, ensure_ascii=False, indent=4)
            return msgspec.convert(unpack_data, type=ArknightsPlayerInfoModel)

    async def check_cred_valid(self, Cred: str) -> bool | ArknightsUserMeModel:
        header = deepcopy(self._HEADER)
        header['Cred'] = Cred
        raw_data = await self._ark_request(ARK_USER_ME, header=header)
        unpack_data = self.unpack(raw_data)
        if isinstance(unpack_data, int):
            return False
        else:
            return msgspec.convert(unpack_data, type=ArknightsUserMeModel)

    def unpack(self, raw_data: dict | int) -> dict | int:
        if isinstance(raw_data, dict):
            return raw_data['data']
        else:
            return raw_data

    async def _ark_request(
        self,
        url: str,
        method: Literal['GET', 'POST'] = 'GET',
        header: dict[str, Any] = _HEADER,
        params: dict[str, Any] | None = None,
        data: dict[str, Any] | None = None,
    ) -> dict | int:
        if 'Cred' not in header:
            target_user_id = (
                data['friendUserId']
                if data and 'friendUserId' in data
                else None
            )
            Cred: str | None = await ArknightsUser.get_random_cookie(
            target_user_id if target_user_id else '18888888'
            )
            if Cred is None:
                return -61
            arkUser = await ArknightsUser.base_select_data(Cred=Cred)
            if arkUser is None:
                return -61
            print(Cred)
            header['Cred'] = Cred

        async with ClientSession(
            connector=TCPConnector(verify_ssl=self.ssl_verify)
        ) as client:
            async with client.request(
                method,
                url=url,
                headers=header,
                params=params,
                json=data,
                timeout=300,
            ) as resp:
                try:
                    raw_data = await resp.json()
                    with open('test.json', 'w', encoding='utf-8') as f:
                        import json
                        json.dump(raw_data, f, ensure_ascii=False, indent=4)
                except ContentTypeError:
                    _raw_data = await resp.text()
                    raw_data = {'code': -999, 'data': _raw_data}
                if (
                    raw_data
                    and 'code' in raw_data
                    and raw_data['code'] != 0
                ):
                    return raw_data['code']
                logger.debug(raw_data)
                return raw_data