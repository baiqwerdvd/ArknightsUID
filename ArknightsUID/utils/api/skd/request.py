import hashlib
import hmac
import json
import time
from copy import deepcopy
from typing import Any, Dict, Literal, Tuple, Union, cast
from urllib.parse import urlparse

import msgspec
from aiohttp import ClientSession, ContentTypeError, TCPConnector
from gsuid_core.logger import logger
from gsuid_core.utils.plugins_config.gs_config import core_plugins_config

from ...crypto import get_d_id
from ...database.models import ArknightsUser
from ...models.skland.models import (
    ArknightsAttendanceCalendarModel,
    ArknightsAttendanceModel,
    ArknightsPlayerInfoModel,
    ArknightsUserMeModel,
)
from .api import ARK_API_USER, ARK_PLAYER_INFO, ARK_REFRESH_TOKEN, ARK_SKD_SIGN

proxy_url = core_plugins_config.get_config("proxy").data
ssl_verify = core_plugins_config.get_config("MhySSLVerify").data

# dId = get_d_id()

# async def get_header():
#     header = deepcopy(_HEADER)
#     header["dId"] = await get_d_id()
#     return header

_HEADER: Dict[str, str] = {
    "User-Agent": "Skland/1.28.0 (com.hypergryph.skland; build:102800063; Android 35; ) Okhttp/4.11.0",
    "Accept-Encoding": "gzip",
    "Connection": "close",
    "Origin": "https://www.skland.com",
    "Referer": "https://www.skland.com/",
    "Content-Type": "application/json",
    "manufacturer": "Xiaomi",
    "os": "35",
    "dId": "",  # "de9759a5afaa634f",
}


header_for_sign = {
    "platform": "1",
    "timestamp": "",
    "dId": "",
    "vName": "1.28.0",
}


def generate_signature(
    token: str, path: str, body_or_query: str, dId: str = ""
) -> Tuple[str, Dict[str, str]]:
    t = str(int(time.time()) - 2)
    _token = token.encode("utf-8")
    header_ca = header_for_sign.copy()
    header_ca["timestamp"] = t
    header_ca["dId"] = dId
    header_ca_str = json.dumps(header_ca, separators=(",", ":"))
    s = path + body_or_query + t + header_ca_str
    hex_s = hmac.new(_token, s.encode("utf-8"), hashlib.sha256).hexdigest()
    md5 = hashlib.md5(hex_s.encode("utf-8")).hexdigest()
    return md5, header_ca


def get_sign_header(
    token: str,
    url: str,
    method: str,
    body: Union[dict[Any, Any], None],
    old_header: dict[str, str],
):
    h = old_header.copy()
    p = urlparse(url)
    if method.lower() == "get":
        h["sign"], header_ca = generate_signature(token, p.path, p.query)
    else:
        h["sign"], header_ca = generate_signature(token, p.path, json.dumps(body))
    h.update(header_ca)
    return h


class TokenExpiredError(Exception):
    pass


class TokenRefreshFailed(Exception):
    pass


class BaseArkApi:
    proxy_url: Union[str, None] = proxy_url if proxy_url else None

    async def _pass(
        self,
        gt: str,
        ch: str,
    ) -> Tuple[Union[str, None], Union[str, None]]:
        _pass_api = core_plugins_config.get_config("_pass_API").data
        if _pass_api:
            data = await self._ark_request(
                url=f"{_pass_api}&gt={gt}&challenge={ch}",
                method="GET",
            )
            if isinstance(data, int) or not data:
                return None, None
            else:
                validate = data["data"]["validate"]
                ch = data["data"]["challenge"]
        else:
            validate = None

        return validate, ch

    async def get_game_player_info(
        self,
        uid: str,
    ) -> Union[int, ArknightsPlayerInfoModel]:
        cred: Union[str, None] = await ArknightsUser.get_user_attr_by_uid(
            uid=uid,
            attr="cred",
        )
        if cred is None:
            return -60
        token: Union[str, None] = await ArknightsUser.get_user_attr_by_uid(
            uid=uid,
            attr="token",
        )
        if token is None:
            return -60
        is_vaild = await self.check_cred_valid(cred)
        if isinstance(is_vaild, bool):
            await ArknightsUser.delete_user_data_by_uid(uid)
            return -61
        headers = deepcopy(_HEADER)
        headers["cred"] = cred
        headers["dId"] = await get_d_id()
        header = get_sign_header(token, ARK_PLAYER_INFO, "get", None, headers)
        raw_data = await self.ark_request(
            url=ARK_PLAYER_INFO,
            params={"uid": uid},
            header=header,
        )
        if isinstance(raw_data, int):
            return raw_data
        if raw_data is None:
            return -61
        unpack_data = self.unpack(raw_data)
        if isinstance(unpack_data, int):
            return unpack_data
        else:
            return msgspec.convert(unpack_data, type=ArknightsPlayerInfoModel)

    async def skd_sign(self, uid: str) -> Union[int, ArknightsAttendanceModel]:
        cred: Union[str, None] = await ArknightsUser.get_user_attr_by_uid(
            uid=uid,
            attr="cred",
        )
        if cred is None:
            return -60
        token: Union[str, None] = await ArknightsUser.get_user_attr_by_uid(
            uid=uid,
            attr="token",
        )
        if token is None:
            return -60
        # is_vaild = await self.check_cred_valid(cred)
        # if isinstance(is_vaild, bool):
        #     await ArknightsUser.delete_user_data_by_uid(uid)
        #     return -61
        headers = deepcopy(_HEADER)
        headers["cred"] = cred
        # headers["dId"] = await get_d_id()
        data = {"uid": uid, "gameId": 1}
        # header = get_sign_header(token, ARK_SKD_SIGN, "post", data, headers)
        async with ClientSession(
            connector=TCPConnector(),
        ) as client:
            sign_response = await client.post(
                ARK_SKD_SIGN,
                headers=get_sign_header(token, ARK_SKD_SIGN, "post", data, headers),
                json=data,
            )
            sign_response_json = await sign_response.json()
        unpack_data = self.unpack(sign_response_json)
        if isinstance(unpack_data, int):
            return unpack_data
        else:
            logger.info(unpack_data)
            return msgspec.convert(unpack_data, ArknightsAttendanceModel)

    async def get_sign_info(
        self,
        uid: str,
    ) -> Union[int, ArknightsAttendanceCalendarModel]:
        cred: Union[str, None] = await ArknightsUser.get_user_attr_by_uid(
            uid=uid,
            attr="cred",
        )
        if cred is None:
            return -60
        token: Union[str, None] = await ArknightsUser.get_user_attr_by_uid(
            uid=uid,
            attr="token",
        )
        if token is None:
            return -60
        headers = deepcopy(_HEADER)
        headers["cred"] = cred
        headers["dId"] = await get_d_id()
        url = ARK_SKD_SIGN + f"?uid={uid}&gameId=1"
        header = get_sign_header(token, url, "get", None, headers)
        raw_data = await self.ark_request(
            url=url,
            method="GET",
            header=header,
        )
        if isinstance(raw_data, int):
            return raw_data
        if raw_data is None:
            return -61
        unpack_data = self.unpack(raw_data)
        if isinstance(unpack_data, int):
            return unpack_data
        else:
            logger.info(unpack_data)
            return msgspec.convert(unpack_data, ArknightsAttendanceCalendarModel)

    async def check_cred_valid(
        self,
        cred: Union[str, None] = None,
        token: Union[str, None] = None,
        uid: Union[str, None] = None,
    ) -> Union[bool, ArknightsUserMeModel]:
        if uid is not None:
            cred = (
                cred
                if cred
                else await ArknightsUser.get_user_attr_by_uid(
                    uid=uid,
                    attr="cred",
                )
            )
            token = (
                token
                if token
                else await ArknightsUser.get_user_attr_by_uid(
                    uid=uid,
                    attr="token",
                )
            )
        if cred is None:
            return False
        if token is None:
            return False
        header = deepcopy(_HEADER)
        header["cred"] = cred
        header["dId"] = await get_d_id()
        header = get_sign_header(token, ARK_API_USER, "get", None, header)
        raw_data = await self.ark_request(ARK_API_USER, header=header)
        if isinstance(raw_data, int) or not raw_data:
            return False
        if "code" in raw_data and raw_data["code"] == 10001:
            logger.info(f"cred is invalid {raw_data}")
            return False
        unpack_data = self.unpack(raw_data)
        return msgspec.convert(unpack_data, type=ArknightsUserMeModel)

    def unpack(self, raw_data: Dict) -> Dict:
        try:
            data = raw_data["data"]
            return data
        except KeyError:
            return raw_data

    async def refresh_token(self, cred: str, uid: Union[str, None] = None) -> str:
        header = deepcopy(_HEADER)
        header["cred"] = cred
        header["sign_enable"] = "false"
        # header["dId"] = await get_d_id()
        raw_data = await self.ark_request(url=ARK_REFRESH_TOKEN, header=header)
        if isinstance(raw_data, int) or not raw_data:
            raise TokenRefreshFailed
        else:
            token = cast(str, self.unpack(raw_data)["token"])
            uid = await ArknightsUser.get_uid_by_cred(cred)
            if uid is not None:
                _ = await ArknightsUser.update_user_attr_by_uid(
                    uid=uid,
                    attr="token",
                    value=token,
                )
            return token

    async def ark_request(
        self,
        url: str,
        method: Literal["GET", "POST"] = "GET",
        header: Dict[str, Any] = _HEADER,
        params: Union[Dict[str, Any], None] = None,
        data: Union[Dict[str, Any], None] = None,
        use_proxy: Union[bool, None] = False,
    ) -> Union[Dict, Union[int, None]]:
        logger.debug(f"ark_request {url} {method} {header} {params} {data} {use_proxy}")
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
            await self.refresh_token(header["cred"])
            headers = deepcopy(header)
            headers["cred"] = header["cred"]
            headers["dId"] = await get_d_id()
            headers = get_sign_header(headers["cred"], url, method, data, headers)
            raw_data = await self._ark_request(
                url=url,
                method=method,
                header=headers,
                params=params,
                data=data,
                use_proxy=use_proxy,
            )
        return raw_data

    async def _ark_request(
        self,
        url: str,
        method: Literal["GET", "POST"] = "GET",
        header: Dict[str, Any] = _HEADER,
        params: Union[Dict[str, Any], None] = None,
        data: Union[Dict[str, Any], None] = None,
        use_proxy: Union[bool, None] = False,
    ) -> Union[Dict, Union[int, None]]:
        async with ClientSession(
            connector=TCPConnector(verify_ssl=ssl_verify),
        ) as client:
            raw_data = {}
            if "cred" not in header:
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
                    raw_data = {"code": -999, "data": _raw_data}
                logger.info(raw_data)

                # 判断code
                if raw_data["code"] == 0:
                    return raw_data

                if raw_data["code"] == 10000:
                    # 请求异常
                    logger.info(f"{url} {raw_data}")
                    raise TokenExpiredError

                if raw_data["code"] == 10001:
                    # 重复签到
                    return raw_data["code"]
