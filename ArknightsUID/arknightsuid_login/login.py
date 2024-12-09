import json
import re
from datetime import datetime
from typing import ClassVar, Dict, TypeVar, Union

import httpx
from gsuid_core.utils.plugins_config.gs_config import core_plugins_config
from msgspec import UnsetType, convert
from msgspec import json as mscjson

from ..utils.crypto import get_d_id
from .constant import (
    ARK_ACCONUT_INFO_HG,
    ARK_LOGIN_SEND_PHONE_CODE,
    ARK_TOKEN_BY_PHONE_CODE,
    ARK_USER_OAUTH2_V2_GRANT,
    GENERATE_CRED_BY_CODE,
)
from .model import (
    AccountInfoHGRequest,
    AccountInfoHGResponse,
    FuckMysGeetestPassResponse,
    GeneralGeetestData,
    GeneralV1SendPhoneCodeRequest,
    GeneralV1SendPhoneCodeResponse,
    Oauth2V2GrantRequest,
    Oauth2V2GrantResponse,
    UserAuthV2TokenByPhoneCodeRequest,
    UserAuthV2TokenByPhoneCodeResponse,
    ZonaiSklandWebUserGenerateCredByCodeRequest,
    ZonaiSklandWebUserGenerateCredByCodeResponse,
)

T1 = TypeVar("T1")
T2 = TypeVar("T2")


class SklandLoginError(Exception):
    def __init__(self, url: str, message: str):
        self.url = url
        self.message = message

    def __str__(self):
        return self.url + " " + self.message


def transUnset(v: Union[T1, UnsetType], d: T2 = None) -> Union[T1, T2]:
    return v if not isinstance(v, UnsetType) else d


class SklandLogin:
    _HEADER: ClassVar[Dict[str, str]] = {
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/129.0.0.0 Safari/537.36",  # noqa: E501
        "content-type": "application/json;charset=UTF-8",
        "origin": "https://ak.hypergryph.com",
        "referer": "https://ak.hypergryph.com",
    }

    def __init__(self, phone: str, geetest_token: Union[str, None] = None):
        self.phone = phone
        self.client = httpx.Client(
            headers=self._HEADER,
            verify=False,
        )
        self.geetest_token = geetest_token
        self.token = None
        self.ark_uid = None

    def send_phone_code(
        self,
        override_geetest: Union[GeneralGeetestData, None] = None,
    ):
        if override_geetest:
            data = GeneralV1SendPhoneCodeRequest(
                phone=self.phone,
                type=2,
                captcha=override_geetest,
            )
        else:
            data = GeneralV1SendPhoneCodeRequest(
                phone=self.phone,
                type=2,
            )
        response = self.client.post(
            ARK_LOGIN_SEND_PHONE_CODE,
            json=mscjson.decode(mscjson.encode(data)),
        )
        response.raise_for_status()
        result = convert(response.json(), GeneralV1SendPhoneCodeResponse)
        if result.status == 1:
            captcha_data = transUnset(result.data)
            assert captcha_data is not None
            _pass_api = core_plugins_config.get_config("_pass_API").data
            if _pass_api is None:
                raise SklandLoginError(
                    ARK_LOGIN_SEND_PHONE_CODE,
                    "config _pass_API is None",
                )
            return_data = httpx.post(
                f"{_pass_api}&gt={captcha_data.captcha.gt}&challenge={captcha_data.captcha.challenge}",
                verify=False,
                timeout=100,
            )
            geetest_pass_data = convert(return_data.json(), FuckMysGeetestPassResponse)
            if geetest_pass_data.code != 0:
                raise SklandLoginError(
                    "_pass_API",
                    geetest_pass_data.info,
                )
            _ = self.send_phone_code(
                override_geetest=GeneralGeetestData(
                    geetest_challenge=geetest_pass_data.data.challenge,
                    geetest_validate=geetest_pass_data.data.validate,
                    geetest_seccode=f"{geetest_pass_data.data.validate}|jordan",
                )
            )
        elif result.status != 0:
            return result.msg

    def token_by_phone_code(self, code: str):
        response = self.client.post(
            ARK_TOKEN_BY_PHONE_CODE,
            json={
                "phone": self.phone,
                "code": code,
            },
        )
        result = convert(response.json(), UserAuthV2TokenByPhoneCodeResponse)
        print(result)
        status = result.status
        if status == 101:
            msg = transUnset(result.msg)
            assert msg is not None
            raise SklandLoginError(ARK_TOKEN_BY_PHONE_CODE, msg)
        data = transUnset(result.data)
        assert data is not None
        self.token = data.token
        self.get_ark_uid()

    async def user_oauth2_v2_grant(self):
        self.client.headers["platform"] = "3"
        self.client.headers["vName"] = "1.0.0"
        self.client.headers["origin"] = "https://zonai.skland.com/"
        self.client.headers["referer"] = "https://zonai.skland.com/"
        self.client.headers["dId"] = await get_d_id()
        self.client.headers["timestamp"] = str(int(datetime.now().timestamp()))
        response = self.client.post(
            ARK_USER_OAUTH2_V2_GRANT,
            json={"appCode": "4ca99fa6b56cc2ba", "token": self.token, "type": 0},
        )
        response.raise_for_status()
        result = convert(response.json(), Oauth2V2GrantResponse)
        status = result.status
        if status != 0:
            raise SklandLoginError(ARK_USER_OAUTH2_V2_GRANT, result.msg)
        result_data = transUnset(result.data)
        if not result_data:
            raise SklandLoginError(ARK_USER_OAUTH2_V2_GRANT, "result.data is None")
        uid = transUnset(result_data.uid)
        if not uid:
            raise SklandLoginError(ARK_USER_OAUTH2_V2_GRANT, "result.data.uid is None")
        code = transUnset(result_data.code)
        if not code:
            raise SklandLoginError(ARK_USER_OAUTH2_V2_GRANT, "result.data.code is None")
        # self.uid = uid
        self.code = code

    def get_ark_uid(self):
        url = "https://as.hypergryph.com/u8/user/info/v1/basic"
        response = self.client.post(
            url,
            json={
                "appId": 1,
                "channelMasterId": 1,
                "channelToken": {"token": self.token},
            },
        )
        response.raise_for_status()
        result_data = response.json()
        self.ark_uid: str = result_data["data"]["uid"]

    async def generate_cred_by_code(self):
        headers = {
            "User-Agent": "Skland/1.28.0 (com.hypergryph.skland; build:102800063; Android 35; ) Okhttp/4.11.0",
            "content-type": "application/json;charset=UTF-8",
            "platform": "1",
            "vName": "1.28.0",
            "origin": "https://zonai.skland.com/",
            "referer": "https://zonai.skland.com/",
            "sign_enable": "false",
            "dId": await get_d_id(),
            "timestamp": str(int(datetime.now().timestamp())),
        }
        # self.client.headers = headers
        async with httpx.AsyncClient(headers=headers, verify=False) as client:
            response = await client.post(
                GENERATE_CRED_BY_CODE,
                json={"code": self.code, "kind": 1},
            )
        response.raise_for_status()
        print(response.json())
        result = convert(response.json(), ZonaiSklandWebUserGenerateCredByCodeResponse)
        if result.code != 0:
            raise SklandLoginError(
                GENERATE_CRED_BY_CODE,
                result.message,
            )
        self.skland_cred = result.data.cred
        self.skland_token = result.data.token
        self.skland_userId = result.data.userId
