from typing import Dict, Literal, Optional, Type, Union

from gsuid_core.utils.database.base_models import Bind, Push, T_BaseIDModel, User, with_session, BaseModel
from gsuid_core.webconsole.mount_app import GsAdminModel, PageSchema, site
from sqlmodel import Field
from sqlalchemy.future import select
from sqlalchemy.ext.asyncio import AsyncSession


class ArknightsBind(Bind, table=True):
    uid: Union[str, None] = Field(default=None, title='明日方舟UID')


class ArknightsUser(User, table=True):
    uid: Union[str, None] = Field(default=None, title='明日方舟UID')
    skd_uid: Union[str, None] = Field(default=None, title='SKD用户ID')
    cred: Union[str, None] = Field(default=None, title='SKD凭证')
    token: Union[str, None] = Field(default=None, title='SKD Token')

    @classmethod
    @with_session
    async def select_data_by_cred(
        cls,
        session: AsyncSession,
        cred: str
    ) -> Union[BaseModel, None]:
        sql= select(cls).where(cls.cred == cred)
        result = await session.execute(sql)
        data = result.scalars().all()
        return data[0] if data else None

    @classmethod
    async def get_token_by_cred(cls, cred: str) -> Union[str, None]:
        result =  await cls.select_data_by_cred(cred)
        return getattr(result, 'token') if result else None

    @classmethod
    async def get_uid_by_cred(cls, cred: str) -> Union[str, None]:
        result =  await cls.select_data_by_cred(cred)
        return getattr(result, 'uid') if result else None

    @classmethod
    async def update_user_attr_by_uid(
        cls,
        uid: str,
        attr: str,
        value: str,
    ) -> bool:
        retcode = -1
        if await cls.data_exist(uid=uid):
            retcode = await cls.update_data_by_uid(
                uid, cls.bot_id, None, **{attr: value}
            )
        return not bool(retcode)


class ArknightsPush(Push, table=True):
    uid: Union[str, None] = Field(default=None, title='明日方舟UID')
    skd_uid: Union[str, None] = Field(default=None, title='森空岛用户ID')
    ap_push: Union[bool, None] = Field(default=False, title='理智推送')
    ap_value: Union[int, None] = Field(default=110, title='理智推送阈值')
    ap_is_push: Union[bool, None] = Field(default=False, title='理智是否已经推送')
    training_push: Union[bool, None] = Field(default=False, title='训练室推送')
    training_value: Union[int, None] = Field(default=30, title='训练室推送阈值')
    training_is_push: Union[bool, None] = Field(default=False, title='训练室是否已经推送')

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
    @with_session
    async def base_select_data(
        cls: Type[T_BaseIDModel], session: AsyncSession, **data
    ) -> Optional[T_BaseIDModel]:
        stmt = select(cls)
        for k, v in data.items():
            stmt = stmt.where(getattr(cls, k) == v)
        result = await session.execute(stmt)
        data = result.scalars().all()
        return data[0] if data else None

    @classmethod
    async def update_push_data(cls, uid: str, data: Dict) -> bool:
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
        cls: Type[T_BaseIDModel], uid: str
    ) -> Union[T_BaseIDModel, None]:
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
