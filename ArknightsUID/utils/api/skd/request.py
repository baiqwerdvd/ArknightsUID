from copy import deepcopy
import hashlib
import json
import time
import hmac
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
from .api import ARK_GEN_CRED_BY_CODE, ARK_PLAYER_INFO, ARK_SKD_SIGN, ARK_USER_ME

proxy_url = core_plugins_config.get_config('proxy').data
ssl_verify = core_plugins_config.get_config('MhySSLVerify').data


class BaseArkApi:
    proxy_url: str | None = proxy_url if proxy_url else None
    _HEADER: ClassVar[dict[str, str]] = {
        'Host': 'zonai.skland.com',
        'Platform': '1',
        'Origin': 'https://www.skland.com',
        'Referer': 'https://www.skland.com/',
        'content-type': 'application/json',
        'user-agent': 'Skland/1.0.1 (com.hypergryph.skland; build:100001014; Android 33; ) Okhttp/4.11.0',
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
            return -60
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
        if isinstance(raw_data, int):
            return raw_data
        unpack_data = self.unpack(raw_data)
        if isinstance(unpack_data, int):
            return unpack_data
        else:
            return msgspec.convert(unpack_data, type=ArknightsPlayerInfoModel)

    async def skd_sign(self, uid: str) -> int | ArknightsAttendanceModel:
        cred: str | None = await ArknightsUser.get_user_attr_by_uid(uid=uid, attr='cred')
        if cred is None:
            return -60
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
            header=header,
        )
        if isinstance(raw_data, int):
            return raw_data
        unpack_data = self.unpack(raw_data)
        if isinstance(unpack_data, int):
            return unpack_data
        else:
            return msgspec.convert(unpack_data, ArknightsAttendanceModel)

    async def get_sign_info(self, uid: str) -> int | ArknightsAttendanceCalendarModel:
        cred: str | None = await ArknightsUser.get_user_attr_by_uid(uid=uid, attr='cred')
        if cred is None:
            return -60
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
            header=header,
        )
        if isinstance(raw_data, int):
            return raw_data
        unpack_data = self.unpack(raw_data)
        if isinstance(unpack_data, int):
            return unpack_data
        else:
            return msgspec.convert(unpack_data, ArknightsAttendanceCalendarModel)

    async def check_cred_valid(self, Cred: str) -> bool | ArknightsUserMeModel:
        header = deepcopy(self._HEADER)
        header['Cred'] = Cred
        raw_data = await self._ark_request(ARK_USER_ME, header=header)
        if isinstance(raw_data, int):
            return False
        if 'code' in raw_data and raw_data['code'] == 10001:
            logger.info(f'cred is invalid {raw_data}')
            return False
        unpack_data = self.unpack(raw_data)
        return msgspec.convert(unpack_data, type=ArknightsUserMeModel)

    async def check_code_valid(self, code: str) -> bool | str:
        data = {
            'kind': 1,
            'code': code
        }
        raw_data = await self._ark_request(
            ARK_GEN_CRED_BY_CODE,
            data=data
        )
        if isinstance(raw_data, int):
            return False
        else:
            cred = raw_data['cred']
            return cred

    def unpack(self, raw_data: dict) -> dict:
        return raw_data['data']

    async def refresh_token(self, uid: str) -> int | str:
        pass

    async def set_sign(
        self,
        url: str,
        headers: dict[str, Any],
        data: dict[str, Any] | None = None,
        params: dict[str, Any] | None = None,
    ) -> dict:
        path = url.split("://")[1].split("/")[1]
        timestamp = str(int(time.time()))
        str1=json.dumps(
        {
                "platform":headers.get(['platform'],""),
                'timestamp': timestamp,
                'dId': headers.get(["dId"],""),
                "vName":headers.get(["vName"],"")
            }
            ,separators=(',', ':')
        )
        s2=""
        if params:
            s2+="&".join(["=".join(x) for x in params])
        if data:
            s2+=json.dumps(data,separators=(',', ':'))
        str2=path+s2+headers["timestamp"]+str1
        token: str | None  = await ArknightsUser.get_token_by_cred(headers['Cred'])
        sign=hashlib.md5(hmac.new(token.encode(),str2.encode(), hashlib.sha256).hexdigest().encode()).hexdigest()
        headers["sign"]=sign
        headers["timestamp"]=timestamp
        return headers

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
                return 10001

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
                    raw_data = {'code': -999, 'data': _raw_data}
                logger.info(raw_data)

                # 判断code
                if 'code' in raw_data and raw_data['code'] != 0:
                    logger.info(raw_data)
                    return raw_data
                elif 'code' in raw_data and raw_data['code'] == 10000:
                    #token失效
                    logger.info(raw_data)
                    await self.refresh_token(header['Cred'])


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
            return 10001
