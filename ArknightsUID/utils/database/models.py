from gsuid_core.utils.database.base_models import (
    Bind,
    User,
)
from gsuid_core.webconsole.mount_app import GsAdminModel, PageSchema, site
from sqlmodel import Field


class ArknightsBind(Bind, table=True):
    uid: str | None = Field(default=None, title='明日方舟UID')


class ArknightsUser(User, table=True):
    uid: str | None = Field(default=None, title='明日方舟UID')
    skd_uid: str | None = Field(default=None, title='SKD用户ID')
    cred: str | None = Field(default=None, title='SKD凭证')


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
