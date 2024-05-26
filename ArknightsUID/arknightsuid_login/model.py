from typing import Dict, Union

from msgspec import UNSET, Struct, UnsetType, field


class GeneralGeetestData(Struct):
    geetest_challenge: str
    geetest_seccode: str
    geetest_validate: str


class GeneralV1SendPhoneCodeRequest(Struct):
    phone: str
    type: int
    captcha: Union[GeneralGeetestData, UnsetType] = field(default=UNSET)


class CaptchaItemModel(Struct):
    success: int
    gt: str
    challenge: str
    new_captcha: bool


class GeneralV1SendPhoneCodeData(Struct):
    captcha: CaptchaItemModel


class GeneralV1SendPhoneCodeResponse(Struct):
    status: int
    msg: Union[str, UnsetType] = field(default=UNSET)
    type: Union[str, UnsetType] = field(default=UNSET)
    data: Union[GeneralV1SendPhoneCodeData, UnsetType] = field(default=UNSET)


class TokenData(Struct):
    token: str


class UserAuthV2TokenByPhoneCodeRequest(Struct):
    code: str
    phone: str


class UserAuthV2TokenByPhoneCodeResponse(Struct):
    status: int
    msg: Union[str, UnsetType] = field(default=UNSET)
    data: Union[TokenData, UnsetType] = field(default=UNSET)
    type: Union[str, UnsetType] = field(default=UNSET)


class AccountInfoHGRequest(Struct):
    content: str


class AccountInfoHGResponse(Struct):
    code: int
    msg: str
    data: Dict


class GeetestData(Struct):
    gt: str
    challenge: str
    validate: str
    type: str


class FuckMysGeetestPassResponse(Struct):
    code: int
    info: str
    data: GeetestData
    times: int


class Oauth2V2GrantRequest(Struct):
    appCode: str
    token: str
    type: int


class Oauth2V2CodeDataItemResponse(Struct):
    hgId: Union[str, UnsetType] = field(default=UNSET)
    token: Union[str, UnsetType] = field(default=UNSET)
    code: Union[str, UnsetType] = field(default=UNSET)
    uid: Union[str, UnsetType] = field(default=UNSET)
    delete_commit_ts: Union[int, UnsetType] = field(default=UNSET)
    delete_request_ts: Union[int, UnsetType] = field(default=UNSET)


class Oauth2V2GrantResponse(Struct):
    status: int
    msg: str
    data: Union[Oauth2V2CodeDataItemResponse, UnsetType] = field(default=UNSET)
    type: Union[str, UnsetType] = field(default=UNSET)


class ZonaiSklandWebUserGenerateCredByCodeRequest(Struct):
    kind: int
    code: str


class ZonaiSklandWebUserData(Struct):
    cred: str
    userId: str
    token: str


class ZonaiSklandWebUserGenerateCredByCodeResponse(Struct):
    code: int
    message: str
    timestamp: str
    data: ZonaiSklandWebUserData
