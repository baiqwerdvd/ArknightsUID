from typing import cast

from ..arknightsuid_config.ark_config import ArkConfig

PREFIX = cast(str, ArkConfig.get_config("ArknightsPrefix").data)
