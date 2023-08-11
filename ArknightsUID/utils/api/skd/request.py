from copy import deepcopy
from typing import Any, Literal

import msgspec
from aiohttp import ClientSession, ContentTypeError, TCPConnector
from gsuid_core.logger import logger

from ...database.models import ArknightsUser
from ...models.skland.models import ArknightsUserMeModel
from .api import ARK_USER_ME


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
            arkUser = await ArknightsUser.base_select_data(ArknightsUser, Cred=Cred)
            if arkUser is None:
                return -61
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
