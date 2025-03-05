from msgspec import UNSET, Struct, UnsetType, field


class GeneralGeetestData(Struct):
    geetest_challenge: str
    geetest_seccode: str
    geetest_validate: str


class GeneralV1SendPhoneCodeRequest(Struct):
    phone: str
    type: int
    captcha: GeneralGeetestData | UnsetType = field(default=UNSET)


class CaptchaItemModel(Struct):
    success: int
    gt: str
    challenge: str
    new_captcha: bool


class GeneralV1SendPhoneCodeData(Struct):
    captcha: CaptchaItemModel


class GeneralV1SendPhoneCodeResponse(Struct):
    status: int
    msg: str | UnsetType = field(default=UNSET)
    type: str | UnsetType = field(default=UNSET)
    data: GeneralV1SendPhoneCodeData | UnsetType = field(default=UNSET)


class TokenData(Struct):
    token: str


class UserAuthV2TokenByPhoneCodeRequest(Struct):
    code: str
    phone: str


class UserAuthV2TokenByPhoneCodeResponse(Struct):
    status: int
    msg: str | UnsetType = field(default=UNSET)
    data: TokenData | UnsetType = field(default=UNSET)
    type: str | UnsetType = field(default=UNSET)


class AccountInfoHGRequest(Struct):
    content: str


class AccountInfoHGResponse(Struct):
    code: int
    msg: str
    data: dict


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
    hgId: str | UnsetType = field(default=UNSET)
    token: str | UnsetType = field(default=UNSET)
    code: str | UnsetType = field(default=UNSET)
    uid: str | UnsetType = field(default=UNSET)
    delete_commit_ts: int | UnsetType = field(default=UNSET)
    delete_request_ts: int | UnsetType = field(default=UNSET)


class Oauth2V2GrantResponse(Struct):
    status: int
    msg: str
    data: Oauth2V2CodeDataItemResponse | UnsetType = field(default=UNSET)
    type: str | UnsetType = field(default=UNSET)


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
