from gsuid_core.utils.plugins_config.models import (
    GSC,
    GsBoolConfig,
    GsStrConfig,
)

CONIFG_DEFAULT: dict[str, GSC] = {
    'ArknightsPrefix': GsStrConfig(
        '插件命令前缀(确认无冲突再修改)',
        '用于本插件的前缀设定',
        'ark',
    ),
    'CrazyNotice': GsBoolConfig(
        '催命模式',
        '开启后当达到推送阈值将会一直推送',
        False,
    ),
}
