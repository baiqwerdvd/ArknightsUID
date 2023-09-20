from copy import deepcopy
import hashlib
import json
import time
import hmac
from typing import Any, ClassVar, Literal, cast
from urllib.parse import urlparse

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
from .api import ARK_PLAYER_INFO, ARK_REFRESH_TOKEN, ARK_SKD_SIGN, ARK_USER_ME

proxy_url = core_plugins_config.get_config('proxy').data
ssl_verify = core_plugins_config.get_config('MhySSLVerify').data


_HEADER: dict[str, str] = {
        'Host': 'zonai.skland.com',
        'platform': '1',
        'Origin': 'https://www.skland.com',
        'Referer': 'https://www.skland.com/',
        'Content-Type': 'application/json',
        'User-Agent': 'Skland/1.1.0 (com.hypergryph.skland; build:100100047; Android 33; ) Okhttp/4.11.0',
        'vName': '1.1.0',
        'vCode': '100100047',
        'nId': '1',
        'os': '33',
        'manufacturer': 'Xiaomi'
    }


class TokenExpiredError(Exception):
    pass


class TokenRefreshFailed(Exception):
    pass


class BaseArkApi:
    proxy_url: str | None = proxy_url if proxy_url else None

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
        header = deepcopy(_HEADER)
        header['cred'] = cred
        header = await self.set_sign(ARK_PLAYER_INFO, header=header)
        raw_data = await self.ark_request(
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
        header = deepcopy(_HEADER)
        header['cred'] = cred
        header = await self.set_sign(ARK_SKD_SIGN, header=header)
        data = {
                'uid': uid,
                'gameId': 1
            }
        header['Content-Type'] = 'application/json'
        header['Content-Length'] = str(len(json.dumps(data)))
        raw_data = await self.ark_request(
            url=ARK_SKD_SIGN,
            method='POST',
            data=data,
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
        header = deepcopy(_HEADER)
        header['cred'] = cred
        header = await self.set_sign(ARK_SKD_SIGN, header=header)
        raw_data = await self.ark_request(
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

    async def check_cred_valid(
        self, cred: str | None = None, token: str | None = None, uid: str | None = None
    ) -> bool | ArknightsUserMeModel:
        if uid is not None:
            cred = cred if cred else await ArknightsUser.get_user_attr_by_uid(uid=uid, attr='cred')
        header = deepcopy(_HEADER)
        if cred is None:
            return False
        header['cred'] = cred
        header = await self.set_sign(ARK_USER_ME, header=header, token=token)
        raw_data = await self.ark_request(ARK_USER_ME, header=header)
        if isinstance(raw_data, int):
            return False
        if 'code' in raw_data and raw_data['code'] == 10001:
            logger.info(f'cred is invalid {raw_data}')
            return False
        unpack_data = self.unpack(raw_data)
        return msgspec.convert(unpack_data, type=ArknightsUserMeModel)

    # async def check_code_valid(self, code: str) -> bool | str:
    #     data = {
    #         'kind': 1,
    #         'code': code
    #     }
    #     raw_data = await self.ark_request(
    #         ARK_GEN_CRED_BY_CODE,
    #         data=data
    #     )
    #     if isinstance(raw_data, int):
    #         return False
    #     else:
    #         cred = raw_data['cred']
    #         return cred

    def unpack(self, raw_data: dict) -> dict:
        return raw_data['data']

    async def refresh_token(self, cred: str, uid: str | None = None) -> str:
        header = deepcopy(_HEADER)
        header['cred'] = cred
        header['sign_enable'] = 'false'
        raw_data = await self.ark_request(url=ARK_REFRESH_TOKEN, header=header)
        if isinstance(raw_data, int):
            raise TokenRefreshFailed
        else:
            token = cast(str, self.unpack(raw_data)['token'])
            uid = await ArknightsUser.get_uid_by_cred(cred)
            if uid is not None:
                await ArknightsUser.update_user_attr_by_uid(uid=uid, attr='token', value=token)
            return token

    async def set_sign(
        self,
        url: str,
        header: dict[str, Any],
        data: dict[str, Any] | None = None,
        params: dict[str, Any] | None = None,
        token: str | None = None,
    ) -> dict:
        parsed_url = urlparse(url)
        path = parsed_url.path
        timestamp = str(int(time.time()) - 1)
        str1=json.dumps(
        {
                'platform': header.get('platform', ''),
                'timestamp': timestamp,
                'dId': header.get('dId', ''),
                'vName': header.get('vName', '')
            },separators=(',', ':')
        )
        s2=''
        if params:
            logger.debug(f'params {params}')
            s2 += '&'.join([str(x) + '=' + str(params[x]) for x in params])
        if data:
            s2 += json.dumps(data,separators=(',', ':'))
        logger.debug(f'{path} {s2} {timestamp} {str1}')
        str2 = path + s2 + timestamp + str1
        token_ = await ArknightsUser.get_token_by_cred(header['cred'])
        logger.debug(f'cred {header["cred"]} token {token} token_ {token_}')
        token = token if token else token_
        if token is None:
            raise Exception("token is None")
        encode_token = token.encode('utf-8')
        hex_s = hmac.new(encode_token, str2.encode('utf-8'), hashlib.sha256).hexdigest()
        sign = hashlib.md5(hex_s.encode('utf-8')).hexdigest()
        header["sign"] = sign
        header["timestamp"] = timestamp
        logger.debug(header)
        return header
    
    async def ark_request(
        self,
        url: str,
        method: Literal['GET', 'POST'] = 'GET',
        header: dict[str, Any] = _HEADER,
        params: dict[str, Any] | None = None,
        data: dict[str, Any] | None = None,
        use_proxy: bool | None = False,
    ) -> dict | int:
        try:
            raw_data = await self._ark_request(
                url=url,
                method=method,
                header=header,
                params=params,
                data=data,
                use_proxy=use_proxy,
            )
        except TokenExpiredError:
            await self.refresh_token(header['cred'])
            header = await self.set_sign(url, header, data, params)
            raw_data = await self._ark_request(
                url=url,
                method=method,
                header=header,
                params=params,
                data=data,
                use_proxy=use_proxy,
            )
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
            if 'cred' not in header:
                return 10001
            
            async with client.request(
                method=method,
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
                if 'code' in raw_data and raw_data['code'] == 10000:
                    #token失效
                    logger.info(f'{url} {raw_data}')
                    raise TokenExpiredError

                return raw_data
                # 判断status
                # if 'status' in raw_data and 'msg' in raw_data:
                #     retcode = 1
                # else:
                #     retcode = 0

                # if retcode == 1 and data:
                #     vl, ch = await self._pass(
                #         gt=raw_data['data']['captcha']['gt'],
                #         ch=raw_data['data']['captcha']['challenge']
                #     )
                #     data['captcha'] = {}
                #     data['captcha']['geetest_challenge'] = ch
                #     data['captcha']['geetest_validate'] = vl
                #     data['captcha']['geetest_seccode'] = f'{vl}|jordan'
                # elif retcode != 0:
                #     return retcode
                # else:
                #     return raw_data
            # return 10001
