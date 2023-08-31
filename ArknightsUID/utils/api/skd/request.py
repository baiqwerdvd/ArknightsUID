from copy import deepcopy
from typing import Any, ClassVar, Literal

import msgspec
from aiohttp import ClientSession, ContentTypeError, TCPConnector
from gsuid_core.logger import logger
from gsuid_core.utils.plugins_config.gs_config import core_plugins_config

from ...database.models import ArknightsUser
from ...models.skland.models import (
    ArknightsAttendanceCalendarModel,
    ArknightsAttendanceModel,
    ArknightsPlayerInfoModel,
    ArknightsUserMeModel,
)
from .api import ARK_PLAYER_INFO, ARK_SKD_SIGN, ARK_USER_ME

proxy_url = core_plugins_config.get_config('proxy').data
ssl_verify = core_plugins_config.get_config('MhySSLVerify').data


class BaseArkApi:
    proxy_url: str | None = proxy_url if proxy_url else None
    _HEADER: ClassVar[dict[str, str]] = {
        'Host': 'zonai.skland.com',
        'Origin': 'https://www.skland.com',
        'Referer': 'https://www.skland.com/',
        'content-type': 'application/json; charset=UTF-8',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) \
            AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36',
    }

    async def _pass(self, gt: str, ch: str) -> tuple[str | None, str | None]:
        _pass_api = core_plugins_config.get_config('_pass_API').data
        if _pass_api:
            data = await self._ark_request(
                url=f'{_pass_api}&gt={gt}&challenge={ch}',
                method='GET',
            )
            if isinstance(data, int):
                return None, None
            else:
                validate = data['data']['validate']
                ch = data['data']['challenge']
        else:
            validate = None

        return validate, ch

    async def get_game_player_info(self, uid: str) -> int | ArknightsPlayerInfoModel:
        cred: str | None  = await ArknightsUser.get_user_attr_by_uid(uid=uid, attr='cred')
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
            return msgspec.convert(unpack_data, type=ArknightsPlayerInfoModel)

    async def skd_sign(self, uid: str) -> int | ArknightsAttendanceModel:
        cred: str | None = await ArknightsUser.get_user_attr_by_uid(uid=uid, attr='cred')
        if cred is None:
            return -61
        is_vaild = await self.check_cred_valid(cred)
        if isinstance(is_vaild, bool):
            await ArknightsUser.delete_user_data_by_uid(uid)
            return -61
        header = deepcopy(self._HEADER)
        header['Cred'] = cred
        raw_data = await self._ark_request(
            url=ARK_SKD_SIGN,
            method='POST',
            data={
                'uid': uid,
                'gameId': 1
            },
        )
        unpack_data = self.unpack(raw_data)
        if isinstance(unpack_data, int):
            return unpack_data
        else:
            return msgspec.convert(unpack_data, ArknightsAttendanceModel)

    async def get_sign_info(self, uid: str) -> int | ArknightsAttendanceCalendarModel:
        cred: str | None = await ArknightsUser.get_user_attr_by_uid(uid=uid, attr='cred')
        if cred is None:
            return -61
        is_vaild = await self.check_cred_valid(cred)
        if isinstance(is_vaild, bool):
            await ArknightsUser.delete_user_data_by_uid(uid)
            return -61
        header = deepcopy(self._HEADER)
        header['Cred'] = cred
        raw_data = await self._ark_request(
            url=ARK_SKD_SIGN,
            method='GET',
            params={
                'uid': uid,
                'gameId': 1
            },
        )
        unpack_data = self.unpack(raw_data)
        if isinstance(unpack_data, int):
            return unpack_data
        else:
            return msgspec.convert(unpack_data, ArknightsAttendanceCalendarModel)

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
        use_proxy: bool | None = False,
    ) -> dict | int:
        async with ClientSession(
            connector=TCPConnector(verify_ssl=ssl_verify)
        ) as client:
            raw_data = {}
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
                header['Cred'] = Cred

            for _ in range(3):
                async with client.request(
                    method,
                    url=url,
                    headers=header,
                    params=params,
                    json=data,
                    proxy=self.proxy_url if use_proxy else None,
                    timeout=300,
                ) as resp:
                    try:
                        raw_data = await resp.json()
                    except ContentTypeError:
                        _raw_data = await resp.text()
                        raw_data = {'retcode': -999, 'data': _raw_data}
                    logger.debug(raw_data)

                    # 判断status
                    if 'status' in raw_data and 'msg' in raw_data:
                        retcode = 1
                    else:
                        retcode = 0

                    if retcode == 1 and data:
                        vl, ch = await self._pass(
                            gt=raw_data['data']['captcha']['gt'],
                            ch=raw_data['data']['captcha']['challenge']
                        )
                        data['captcha'] = {}
                        data['captcha']['geetest_challenge'] = ch
                        data['captcha']['geetest_validate'] = vl
                        data['captcha']['geetest_seccode'] = f'{vl}|jordan'
                    elif retcode != 0:
                        return retcode
                    else:
                        return raw_data
            return -999
