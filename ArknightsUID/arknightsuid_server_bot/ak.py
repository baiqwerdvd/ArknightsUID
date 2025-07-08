import asyncio
import base64
import hashlib
import hmac
import json
import pickle
import uuid
from hashlib import sha1
from pathlib import Path
from typing import Any, ClassVar
from urllib.parse import urlencode

import httpx
from gsuid_core.data_store import get_res_path
from gsuid_core.logger import logger
from gsuid_core.utils.plugins_config.gs_config import core_plugins_config


class ArknightsException(Exception):
    pass


class AuthenticationError(ArknightsException):
    pass


class AccountBannedError(ArknightsException):
    pass


class SessionExpiredError(ArknightsException):
    pass


class ServerMaintenanceError(ArknightsException):
    pass


class Config:
    HEADERS: ClassVar[dict[str, str]] = {
        "Content-Type": "application/json",
        "X-Unity-Version": "2017.4.39f1",
        "User-Agent": "Dalvik/2.1.0 (Linux; U; Android 11; KB2000 Build/RP1A.201005.001)",
        "Connection": "Keep-Alive",
    }

    APP_KEY = b"91240f70c09a08a6bc72af1a5c8d4670"
    AUTH_SERVER = "https://as.hypergryph.com"
    GAME_SERVER = "https://ak-gs-gf.hypergryph.com"
    CONFIG_SERVER = "https://ak-conf.hypergryph.com"

    ENDPOINTS: ClassVar[dict[str, str]] = {
        "version": "/config/prod/official/Android/version",
        "network_config": "/config/prod/official/network_config",
        "token_by_phone": "/user/auth/v1/token_by_phone_password",
        "oauth2_grant": "/user/oauth2/v2/grant",
        "get_token": "/u8/user/v1/getToken",
        "account_login": "/account/login",
        "sync_data": "/account/syncData",
        "sync_push_message": "/account/syncPushMessage",
        "online_ping": "/online/v1/ping",
        "user_info": "/user/info/v1/need_cloud_auth",
        "user_login": "/user/login",
    }


class ArknightsClient:
    def __init__(
        self,
        username: str,
        password: str,
        device_id: str = "",
        device_id2: str = "",
        relogin: bool = False,
        use_cache: bool = True,
        timeout: int = 30,
        polling_interval: int = 60,
    ):
        self.username = username
        self.password = password
        self.device_id = device_id or self._generate_device_id()
        self.device_id2 = device_id2 or self._generate_device_id2()
        self.session_dir = get_res_path("ArknightsUID") / "session"
        self.relogin = relogin
        self.use_cache = use_cache
        self.polling_interval = polling_interval

        self.http = httpx.AsyncClient(
            headers=Config.HEADERS,
            timeout=timeout,
        )

        self.nickname = ""
        self.uid = ""
        self.token = ""
        self.secret = ""
        self.seqnum = 1
        self.challenge = ""
        self.gt = ""
        self.code = ""
        self.access_token = ""

        self.res_version = ""
        self.client_version = ""
        self.major_version = ""
        self.network_version = ""

        self.session_file = self.session_dir / f"{self.username}.pickle"

    @classmethod
    def from_session_file(cls, session_file: Path) -> "ArknightsClient":
        if not session_file.exists():
            raise FileNotFoundError(f"Session file {session_file} does not exist.")
        with session_file.open("rb") as f:
            session_data = pickle.load(f)
            (
                device_id,
                device_id2,
                username,
                password,
                access_token,
                uid,
                nickname,
                proxy,
                secret,
                seqnum,
                res_version,
                client_version,
                network_version,
                major_version,
            ) = session_data
        client = ArknightsClient(
            username=username,
            password=password,
            device_id=device_id,
            device_id2=device_id2,
            relogin=False,
            use_cache=True,
        )
        client.access_token = access_token
        client.uid = uid
        client.nickname = nickname
        client.secret = secret
        client.seqnum = seqnum
        client.res_version = res_version
        client.client_version = client_version
        client.network_version = network_version
        client.session_file = session_file

        return client

    def _generate_device_id(self) -> str:
        return str(uuid.uuid4()).replace("-", "")

    def _generate_device_id2(self) -> str:
        return str(uuid.uuid4()).replace("-", "")[:16]

    async def post_auth_server(self, endpoint: str, data: dict[str, Any] | str) -> dict[str, Any]:
        url = Config.AUTH_SERVER + endpoint
        logger.debug(f"POST {url} with data: {data}")

        try:
            response = await self.http.post(url, json=data, headers=Config.HEADERS)
            response.raise_for_status()
            result = response.json()
            logger.debug(f"Response: {result}")
            return result
        except httpx.HTTPStatusError as e:
            if e.response.status_code == 400:
                logger.error(f"游戏服务器返回400错误，可能正在维护: {e}")
                raise ServerMaintenanceError(f"游戏服务器正在维护: {e.response.text}") from e
            logger.error(f"HTTP请求失败 (状态码: {e.response.status_code}): {e}")
            raise ArknightsException(f"请求失败: {e}") from e
        except httpx.RequestError as e:
            logger.error(f"HTTP请求失败: {e}")
            raise ArknightsException(f"请求失败: {e}") from e
        except json.JSONDecodeError as e:
            logger.error(f"JSON解析失败: {e}")
            raise ArknightsException(f"响应解析失败: {e}") from e

    async def post_game_server(self, endpoint: str, data: dict[str, Any], verify: bool = True) -> dict[str, Any]:
        url = Config.GAME_SERVER + endpoint
        headers = self._get_game_headers()

        try:
            response = await self.http.post(url, json=data, headers=headers)
            response.raise_for_status()
            result = response.json()

            verify_result = None
            if verify:
                verify_result = await self._verify_response(result, endpoint, data)
            if verify_result is not None:
                self._save_session()
                return verify_result

            self._save_session()
            return result
        except httpx.HTTPStatusError as e:
            if e.response.status_code == 400:
                logger.error(f"游戏服务器返回400错误，可能正在维护: {e}")
                raise ServerMaintenanceError(f"游戏服务器正在维护: {e.response.text}") from e
            logger.error(f"HTTP请求失败 (状态码: {e.response.status_code}): {e}")
            raise ArknightsException(f"请求失败: {e}") from e
        except httpx.RequestError as e:
            logger.error(f"HTTP请求失败: {e}")
            raise ArknightsException(f"请求失败: {e}") from e

    async def _verify_response(
        self, result: dict[str, Any], endpoint: str, data: dict[str, Any]
    ) -> dict[str, Any] | None:
        status_code = result.get("statusCode", 0)

        if status_code == 401:
            if self.relogin:
                logger.info("会话过期，尝试重新登录...")
                await asyncio.sleep(15)
                self.relogin = False
                await self.login()
                return await self.post_game_server(endpoint, data)
            else:
                raise SessionExpiredError("会话已过期")
        elif status_code != 0:
            raise ArknightsException(f"API错误: {result}")
        return None

    def _get_game_headers(self) -> dict[str, str]:
        self.seqnum += 1
        headers = Config.HEADERS.copy()
        headers.update(
            {
                "uid": self.uid,
                "secret": self.secret,
                "seqnum": str(self.seqnum),
            }
        )
        return headers

    def verify_secret_info(self, secret: str) -> bool:
        buffer = base64.b64decode(secret)
        if len(buffer) != 24:
            raise ArknightsException(f"无效的secret长度: {len(buffer)}, 期望24字节")

        if version_info := self.brute_force_versions(buffer[:16]):
            client_version, major_version = version_info
            logger.info(f"解析出的版本信息: clientVersion={client_version}, majorVersion={major_version}")
            if client_version != self.client_version:
                return False
            return True
        else:
            raise ArknightsException("无法解析版本信息")

    def verify_versions(self, target_hash: bytes, client_version: str, major_version: int) -> bool:
        md5_hash = hashlib.md5()
        md5_hash.update(client_version.encode("utf-8"))
        md5_hash.update(str(major_version).encode("utf-8"))
        computed_hash = md5_hash.digest()
        return computed_hash == target_hash

    def brute_force_versions(self, target_hash: bytes):
        for major_version in range(100, 1000):
            for i in range(1, 5):
                for j in range(0, 10):
                    for k in range(0, 100):
                        client_version = f"{i}.{j}.{k}"
                        if self.verify_versions(target_hash, client_version, major_version):
                            return client_version, major_version
        return None

    async def _load_session(self) -> bool:
        if not (self.session_file.exists() and self.use_cache):
            return False

        try:
            with self.session_file.open("rb") as f:
                session_data = pickle.load(f)

            (
                self.device_id,
                self.device_id2,
                self.username,
                self.password,
                self.access_token,
                self.uid,
                self.nickname,
                self.proxy,
                self.secret,
                self.seqnum,
                self.res_version,
                self.client_version,
                self.network_version,
                self.major_version,
            ) = session_data

            if not self.verify_secret_info(self.secret):
                logger.warning("缓存的secret信息无效，重新登录")
                self.session_file.unlink()
                return False

            self.seqnum += 1

            session_verify = await self.post_game_server(Config.ENDPOINTS["sync_data"], {"platform": 1}, False)

            status_code = session_verify.get("statusCode", 0)
            if status_code == 401:
                logger.info("会话已过期，删除缓存文件")
                self.session_file.unlink()
                return False
            elif status_code != 0:
                raise ArknightsException(f"会话验证失败: {session_verify}")

            self.nickname = session_verify["user"]["status"]["nickName"]
            logger.info(f"从缓存加载会话成功: {self.nickname}")
            return True

        except Exception as e:
            logger.error(f"加载会话失败: {e}")
            return False

    def _save_session(self) -> None:
        if not self.use_cache:
            return

        try:
            self.session_dir.mkdir(parents=True, exist_ok=True)
            session_data = (
                self.device_id,
                self.device_id2,
                self.username,
                self.password,
                self.access_token,
                self.uid,
                self.nickname,
                getattr(self, "proxy", None),
                self.secret,
                self.seqnum,
                self.res_version,
                self.client_version,
                self.network_version,
                self.major_version,
            )

            with self.session_file.open("wb") as f:
                pickle.dump(session_data, f)
        except Exception as e:
            logger.error(f"保存会话失败: {e}")

    async def _get_version_info(self) -> None:
        try:
            version_url = Config.CONFIG_SERVER + Config.ENDPOINTS["version"]
            response = await self.http.get(version_url)
            response.raise_for_status()
            version_data = response.json()

            self.res_version = version_data["resVersion"]
            self.client_version = version_data["clientVersion"]

            network_url = Config.CONFIG_SERVER + Config.ENDPOINTS["network_config"]
            response = await self.http.get(network_url)
            response.raise_for_status()
            network_data = response.json()

            self.network_version = json.loads(network_data["content"])["configVer"]

        except Exception as e:
            logger.error(f"获取版本信息失败: {e}")
            raise ArknightsException(f"获取版本信息失败: {e}") from e

    async def _user_login(self) -> None:
        data = {
            "phone": self.username,
            "password": self.password,
        }

        response = await self.post_auth_server(Config.ENDPOINTS["token_by_phone"], data)

        if response.get("result") == 8:
            logger.info("遇到验证码，尝试处理...")
            self.challenge = response["captcha"]["challenge"]
            self.gt = response["captcha"]["gt"]
            response = await self._handle_geetest(data, Config.ENDPOINTS["token_by_phone"])
            self.access_token = response["token"]
        else:
            try:
                self.access_token = response["data"]["token"]
                logger.info("用户名密码登录成功")
            except KeyError:
                raise AuthenticationError(f"登录失败: {response}")

    async def _handle_geetest(self, login_data: dict[str, Any], endpoint: str) -> dict[str, Any]:
        _pass_api = core_plugins_config.get_config("_pass_API").data
        if not _pass_api:
            raise AuthenticationError("请配置 _pass_API 以处理验证码")

        try:
            geetest_url = f"{_pass_api}&gt={self.gt}&challenge={self.challenge}"
            response = await self.http.get(geetest_url)
            response.raise_for_status()

            data = response.json()
            geetest_validate = data["data"]["validate"]
            geetest_challenge = data["data"]["challenge"]
            geetest_seccode = f"{geetest_validate}|jordan"

            captcha_data = {
                "geetest_challenge": geetest_challenge,
                "geetest_seccode": geetest_seccode,
                "geetest_validate": geetest_validate,
            }

            login_data["captcha"] = json.dumps(captcha_data)
            logger.info(f"处理验证码数据: {login_data}")
            response = await self.post_auth_server(endpoint, login_data)
            logger.info("验证码处理成功")
            return response

        except Exception as e:
            logger.error(f"验证码处理失败: {e}")
            raise AuthenticationError(f"验证码处理失败: {e}") from e

    async def _auth_login(self) -> bool:
        login_data = {
            "token": self.access_token,
            "appCode": "7318def77669979d",
            "type": 0,
        }

        response = await self.post_auth_server(Config.ENDPOINTS["oauth2_grant"], login_data)

        if response.get("status") == 1:
            logger.info("需要人机验证，尝试处理...")
            self.challenge = response["data"]["captcha"]["challenge"]
            self.gt = response["data"]["captcha"]["gt"]
            data = await self._handle_geetest(login_data, Config.ENDPOINTS["oauth2_grant"])
            self.code = data.get("data", {}).get("code", "")
            if not self.code:
                logger.error("获取code失败，可能是access_token无效或已过期")
                logger.error(f"响应内容: {data}")
                return False
            return True

        if response.get("statusCode", 0) != 0:
            return False

        code = response.get("data", {}).get("code", "")
        if not code:
            logger.error("获取code失败，可能是access_token无效或已过期")
            logger.error(f"响应内容: {response}")
            return False
        self.code = code
        return True

    async def _get_online_status(self) -> None:
        data = {"token": self.access_token}
        data["sign"] = generate_sign({"token": self.access_token})
        await self.post_auth_server(Config.ENDPOINTS["online_ping"], data)

    async def _game_login(self) -> None:
        sign_data = {
            "appId": "1",
            "channelId": "1",
            "deviceId": self.device_id,
            "deviceId2": self.device_id2,
            "deviceId3": "",
            "extension": json.dumps(
                {
                    "code": self.code,
                    "isSuc": True,
                    "type": 1,
                }
            ),
            "platform": 1,
            "subChannel": "308",
            "worldId": "1",
        }

        sign_data["sign"] = generate_sign(sign_data)
        response = await self.post_auth_server(Config.ENDPOINTS["get_token"], sign_data)

        if response.get("result") == 1:
            raise ServerMaintenanceError("服务器正在维护，请稍后再试")
        elif response.get("result") == 2:
            raise AccountBannedError("账号已被封禁，请联系官方客服")
        elif response.get("result") != 0:
            raise ArknightsException(f"获取游戏令牌失败: {response}")

        self.uid = response["uid"]
        self.token = response["token"]

        login_data = {
            "networkVersion": self.network_version,
            "uid": self.uid,
            "token": self.token,
            "assetsVersion": self.res_version,
            "clientVersion": self.client_version,
            "platform": 1,
            "deviceId": self.device_id,
            "deviceId2": self.device_id2,
            "deviceId3": "",
        }

        response = await self.post_game_server(Config.ENDPOINTS["account_login"], login_data, False)
        logger.info(f"游戏登录响应: {response}")

        if "secret" not in response:
            raise ArknightsException(f"游戏登录失败: {response}")

        self.secret = response["secret"]
        self.major_version = response.get("majorVersion", 0)

        if not self.verify_secret_info(self.secret):
            raise ArknightsException("无效的secret信息，可能是版本不匹配或数据损坏")

        sync_response = await self.post_game_server(Config.ENDPOINTS["sync_data"], {"platform": 1}, False)

        if sync_response.get("result") != 0:
            raise ArknightsException(f"数据同步失败: {sync_response}")

        self.nickname = sync_response["user"]["status"]["nickName"]
        logger.info(f"游戏登录成功: {self.nickname}")

    async def login(self, retry: bool = True) -> tuple[str, str, str, str, str]:
        logger.info(f"开始登录: {self.username}")

        await self._get_version_info()

        if await self._load_session():
            return (
                self.username,
                self.uid,
                self.nickname,
                self.access_token,
                self.secret,
            )

        max_retries = 3
        retries = 0

        while retries < max_retries:
            try:
                if self.access_token and not self.relogin:
                    logger.info(f"尝试使用 access_token 登录， {self.access_token}")
                    if not await self._auth_login():
                        logger.info("access_token 验证失败，使用用户名密码登录")
                        await self._user_login()
                        await self._auth_login()
                else:
                    logger.info("使用用户名密码登录 (或重新登录)")
                    await self._user_login()
                    await self._auth_login()

                await self.post_auth_server(Config.ENDPOINTS["user_info"], {"token": self.access_token})
                await self._get_online_status()

                await self._game_login()

                self._save_session()

                return (
                    self.username,
                    self.uid,
                    self.nickname,
                    self.access_token,
                    self.secret,
                )
            except AuthenticationError as e:
                logger.error(f"认证失败，尝试重新登录: {e}")
                self.relogin = True
                self.access_token = ""
                self.code = ""
                retries += 1
                if retries >= max_retries:
                    logger.critical("达到最大重试次数，登录失败。")
                    raise
                await asyncio.sleep(5)
            except ServerMaintenanceError as _:
                logger.warning("登录失败，服务器正在维护")
                self._save_session()
                raise ServerMaintenanceError from _
            except Exception as e:
                logger.error(f"登录过程中发生未知错误: {e}")
                raise

        raise ArknightsException("登录失败，未知错误")

    async def sync_data(self) -> dict[str, Any]:
        return await self.post_game_server(Config.ENDPOINTS["sync_data"], {"platform": 1})

    async def get_push_message(self) -> dict[str, Any]:
        return await self.post_game_server(Config.ENDPOINTS["sync_push_message"], {})

    async def aclose(self) -> None:
        await self.http.aclose()
        self._save_session()

    def __aenter__(self):
        return self

    async def __aexit__(self, exc_type, exc_val, exc_tb):
        await self.aclose()


def generate_sign(data: str | dict[str, Any]) -> str:
    if isinstance(data, dict):
        sorted_items = sorted(data.items())
        query_string = urlencode(sorted_items)
    else:
        query_string = data

    signature = hmac.new(Config.APP_KEY, query_string.encode("utf-8"), sha1).hexdigest().lower()

    return signature
