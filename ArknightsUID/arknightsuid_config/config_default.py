from typing import Dict

from gsuid_core.utils.plugins_config.models import (
    GSC,
    GsBoolConfig,
    GsIntConfig,
    GsListStrConfig,
    GsStrConfig,
)

CONIFG_DEFAULT: Dict[str, GSC] = {
    "SignTime": GsListStrConfig(
        "每晚签到时间设置", "每晚森空岛签到时间设置(时,分)", ["0", "38"]
    ),
    "SignReportSimple": GsBoolConfig(
        "简洁签到报告",
        "开启后可以大大减少每日签到报告字数",
        True,
    ),
    "SchedSignin": GsBoolConfig(
        "定时签到",
        "开启后每晚00:30将开始自动签到任务",
        True,
    ),
    "ArknightsPrefix": GsStrConfig(
        "插件命令前缀(确认无冲突再修改)",
        "用于本插件的前缀设定",
        "ark",
    ),
    "CrazyNotice": GsBoolConfig(
        "催命模式",
        "开启后当达到推送阈值将会一直推送",
        False,
    ),
    "ArkPrefix": GsStrConfig(
        "插件命令前缀（确认无冲突再修改）",
        "用于设置ArknightsUID前缀的配置",
        "ark",
    ),
    "AnnMinuteCheck": GsIntConfig(
        "公告推送时间检测（单位min）", "公告推送时间检测（单位min）", 1, 60
    ),
}
