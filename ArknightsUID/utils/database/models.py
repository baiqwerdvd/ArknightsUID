from typing import Literal

from gsuid_core.utils.database.base_models import Bind, Push, T_BaseIDModel, User
from gsuid_core.webconsole.mount_app import GsAdminModel, PageSchema, site
from sqlmodel import Field


class ArknightsBind(Bind, table=True):
    uid: str | None = Field(default=None, title='明日方舟UID')


class ArknightsUser(User, table=True):
    uid: str | None = Field(default=None, title='明日方舟UID')
    skd_uid: str | None = Field(default=None, title='SKD用户ID')
    cred: str | None = Field(default=None, title='SKD凭证')
    token: str | None = Field(default=None, title='SKD令牌')


class ArknightsPush(Push, table=True):
    uid: str | None = Field(default=None, title='明日方舟UID')
    skd_uid: str | None = Field(default=None, title='森空岛用户ID')
    ap_push: bool | None = Field(default=False, title='理智推送')
    ap_value: int | None = Field(default=110, title='理智推送阈值')
    ap_is_push: bool | None = Field(default=False, title='理智是否已经推送')
    training_push: bool | None = Field(default=False, title='训练室推送')
    training_value: int | None = Field(default=30, title='训练室推送阈值')
    training_is_push: bool | None = Field(default=False, title='训练室是否已经推送')

    @classmethod
    async def insert_push_data(cls, uid: str, skd_uid: str):
        await cls.full_insert_data(
            bot_id=cls.bot_id,
            uid=uid,
            skd_uid=skd_uid,
            ap_push=False,
            ap_value=2100,
            ap_is_push=False,
            training_push=True,
            training_value=140,
            training_is_push=False
        )

    @classmethod
    async def update_push_data(cls, uid: str, data: dict) -> bool:
        retcode = -1
        if await cls.data_exist(uid=uid):
            retcode = await cls.update_data_by_uid(
                uid, cls.bot_id, None, **data
            )
        return not bool(retcode)

    @classmethod
    async def change_push_status(
        cls,
        mode: Literal['ap', 'training'],
        uid: str,
        status: str,
    ):
        await cls.update_push_data(uid, {f'{mode}_is_push': status})

    @classmethod
    async def select_push_data(
        cls: type[T_BaseIDModel], uid: str
    ) -> T_BaseIDModel | None:
        return await cls.base_select_data(uid=uid)

    @classmethod
    async def push_exists(cls, uid: str) -> bool:
        return await cls.data_exist(uid=uid)


@site.register_admin
class ArknightsBindadmin(GsAdminModel):
    pk_name = 'id'
    page_schema = PageSchema(label='方舟绑定管理', icon='fa fa-users')  # type: ignore

    # 配置管理模型
    model = ArknightsBind


@site.register_admin
class ArknightsUseradmin(GsAdminModel):
    pk_name = 'id'
    page_schema = PageSchema(label='方舟SKD CRED管理', icon='fa fa-database')  # type: ignore

    # 配置管理模型
    model = ArknightsUser


@site.register_admin
class ArknightsPushadmin(GsAdminModel):
    pk_name = 'id'
    page_schema = PageSchema(label='明日方舟推送管理', icon='fa fa-database')  # type: ignore

    # 配置管理模型
    model = ArknightsPush
