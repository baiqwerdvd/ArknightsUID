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
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/129.0.0.0 Safari/537.36 Edg/129.0.0.0",  # noqa: E501
        "content-type": "application/json;charset=UTF-8",
        "origin": "https://www.skland.com",
        "referer": "https://www.skland.com",
    }

    def __init__(self, phone: str, geetest_token: Union[str, None] = None):
        self.phone = phone
        self.client = httpx.Client(
            headers=self._HEADER,
            verify=False,
        )
        self.geetest_token = geetest_token

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
                type=1,
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
            self.send_phone_code(
                override_geetest=GeneralGeetestData(
                    geetest_challenge=geetest_pass_data.data.challenge,
                    geetest_validate=geetest_pass_data.data.validate,
                    geetest_seccode=f"{geetest_pass_data.data.validate}|jordan",
                )
            )
        elif result.status != 0:
            return result.msg

    def token_by_phone_code(self, code: str):
        data = UserAuthV2TokenByPhoneCodeRequest(
            phone=self.phone,
            code=code,
        )
        data = {
            "phone": self.phone,
            "code": code,
        }
        data = mscjson.decode(mscjson.encode(data))
        print(data)
        response = self.client.post(
            ARK_TOKEN_BY_PHONE_CODE,
            json=data,
        )
        response.raise_for_status()
        result = convert(response.json(), UserAuthV2TokenByPhoneCodeResponse)
        status = result.status
        if status == 101:
            msg = transUnset(result.msg)
            assert msg is not None
            raise SklandLoginError(ARK_TOKEN_BY_PHONE_CODE, msg)
        data = transUnset(result.data)
        assert data is not None
        self.token = data.token

    def post_account_info_hg(self):
        if self.token is None:
            raise SklandLoginError(ARK_ACCONUT_INFO_HG, "token not set!")
        data = AccountInfoHGRequest(
            content=self.token,
        )
        response = self.client.post(
            ARK_ACCONUT_INFO_HG,
            json=mscjson.decode(mscjson.encode(data)),
        )
        set_cookie = response.headers.get("set-cookie")
        matches = re.findall(r"ACCOUNT=([^;]+)", set_cookie)
        account_cookie = matches[0]
        self.client = httpx.Client(
            headers=self._HEADER,
            verify=False,
            cookies={"ACCOUNT": account_cookie},
        )
        response.raise_for_status()
        result = convert(response.json(), AccountInfoHGResponse)
        if result.code != 0:
            raise SklandLoginError(ARK_ACCONUT_INFO_HG, result.msg)
        self.get_account_info_hg()

    def get_account_info_hg(self):
        if self.token is None:
            raise SklandLoginError(ARK_ACCONUT_INFO_HG, "token not set!")
        data = AccountInfoHGRequest(
            content=self.token,
        )
        response = self.client.post(
            ARK_ACCONUT_INFO_HG,
            json=mscjson.decode(mscjson.encode(data)),
        )
        response.raise_for_status()
        result = convert(response.json(), AccountInfoHGResponse)
        if result.code != 0:
            raise SklandLoginError(ARK_ACCONUT_INFO_HG, result.msg)

    def user_oauth2_v2_grant(self):
        data = Oauth2V2GrantRequest(
            token=self.token,
            appCode="4ca99fa6b56cc2ba",
            type=0,
        )
        self.client.headers["dId"] = get_d_id()
        response = self.client.post(
            ARK_USER_OAUTH2_V2_GRANT,
            json=mscjson.decode(mscjson.encode(data)),
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
        self.uid = uid
        self.code = code

    def generate_cred_by_code(self):
        data = ZonaiSklandWebUserGenerateCredByCodeRequest(
            kind=1,
            code=self.code,
        )
        self.client.headers["platform"] = "3"
        self.client.headers["vName"] = "1.0.0"
        self.client.headers["timestamp"] = str(int(datetime.now().timestamp()))
        self.client.headers["dId"] = get_d_id()
        response = self.client.post(
            GENERATE_CRED_BY_CODE,
            json=json.dumps(mscjson.decode(mscjson.encode(data))),
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
        return (self.skland_cred, self.skland_token, self.skland_userId)
