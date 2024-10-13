from typing import cast

from ..arknightsuid_config.ark_config import arkconfig

PREFIX = cast(str, arkconfig.get_config("ArknightsPrefix").data)
