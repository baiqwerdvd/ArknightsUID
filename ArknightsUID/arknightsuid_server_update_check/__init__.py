import asyncio
import random
import time

from gsuid_core.aps import scheduler
from gsuid_core.bot import Bot
from gsuid_core.logger import logger
from gsuid_core.models import Event
from gsuid_core.subscribe import gs_subscribe
from gsuid_core.sv import SV

from .apk_monitor import apk_monitor, human_readable_size
from .arknights_monitor import ark_monitor

CONFIG = {
    "VERSION_URL": "https://ak-conf.hypergryph.com/config/prod/official/Android/version",
    "SERVER_STATUS_URL": "https://ak-webview.hypergryph.com/api/gate/meta/Android",
    "CHECK_INTERVAL": 5,
    "REQUEST_TIMEOUT": 10,
    "RETRY_COUNT": 3,
    "RETRY_DELAY": 5,
}

SERVER_STATUS_MAP = {
    1: "Under Maintenance",
    2: "Active",
}

sv_server_check = SV("明日方舟版本更新")
sv_server_check_sub = SV("订阅明日方舟版本更新", pm=3)
sv_game_server_check = SV("明日方舟服务器状态更新")
sv_game_server_check_sub = SV("订阅明日方舟服务器状态更新", pm=3)
sv_apk_check = SV("明日方舟APK更新检查")
sv_apk_check_sub = SV("订阅明日方舟APK更新", pm=3)

TASK_NAME_APK_CHECK = "订阅明日方舟APK更新"
TASK_NAME_SERVER_CHECK = "订阅明日方舟版本更新"
TASK_NAME_GAME_SERVER_CHECK = "订阅明日方舟服务器状态更新"


@sv_server_check.on_command("取明日方舟最新版本")
async def get_latest_version(bot: Bot, ev: Event):
    """获取最新版本信息"""
    try:
        result = await ark_monitor.check_version_update()
        message = f"clientVersion: {result.version.clientVersion}\nresVersion: {result.version.resVersion}"
        await bot.send(message)
    except Exception as e:
        logger.error(f"获取版本信息失败: {e}")
        await bot.send("获取版本信息失败，请稍后再试")


@sv_server_check_sub.on_fullmatch("订阅版本更新")
async def subscribe_version_update(bot: Bot, ev: Event):
    """订阅版本更新"""
    if ev.group_id is None:
        return await bot.send("请在群聊中订阅")

    try:
        data = await gs_subscribe.get_subscribe(TASK_NAME_SERVER_CHECK)
        if data:
            for subscribe in data:
                if subscribe.group_id == ev.group_id:
                    return await bot.send("已经订阅了明日方舟版本更新！")

        await gs_subscribe.add_subscribe(
            "session",
            task_name=TASK_NAME_SERVER_CHECK,
            event=ev,
            extra_message="",
        )

        logger.info(f"新增版本更新订阅: {ev.group_id}")
        await bot.send("成功订阅明日方舟版本更新!")

    except Exception as e:
        logger.error(f"订阅版本更新失败: {e}")
        await bot.send("订阅失败，请稍后再试")


@sv_game_server_check.on_command("取明日方舟服务器状态")
async def get_game_server_status(bot: Bot, ev: Event):
    """获取游戏服务器状态"""
    try:
        result = await ark_monitor.check_server_status()
        status_text = ark_monitor.get_status_text(result.current_status)
        await bot.send(f"明日方舟服务器状态: {status_text}")
    except Exception as e:
        logger.error(f"获取服务器状态失败: {e}")
        await bot.send("获取服务器状态失败，请稍后再试")


@sv_game_server_check_sub.on_fullmatch("订阅服务器状态更新")
async def subscribe_server_status(bot: Bot, ev: Event):
    """订阅服务器状态更新"""
    if ev.group_id is None:
        return await bot.send("请在群聊中订阅")

    try:
        data = await gs_subscribe.get_subscribe(TASK_NAME_GAME_SERVER_CHECK)
        if data:
            for subscribe in data:
                if subscribe.group_id == ev.group_id:
                    return await bot.send("已经订阅了明日方舟服务器状态更新！")

        await gs_subscribe.add_subscribe(
            "session",
            task_name=TASK_NAME_GAME_SERVER_CHECK,
            event=ev,
            extra_message="",
        )

        logger.info(f"新增服务器状态订阅: {ev.group_id}")
        await bot.send("成功订阅明日方舟服务器状态更新!")

    except Exception as e:
        logger.error(f"订阅服务器状态失败: {e}")
        await bot.send("订阅失败，请稍后再试")


async def _notify_subscribers(task_name: str, message: str):
    """通知订阅者"""
    try:
        subscribers = await gs_subscribe.get_subscribe(task_name)
        if not subscribers:
            logger.info(f"[{task_name}] 暂无群订阅")
            return

        for subscribe in subscribers:
            try:
                await subscribe.send(message)
                await asyncio.sleep(random.uniform(1, 3))
            except Exception as e:
                logger.error(f"发送通知失败: {subscribe.group_id}, 错误: {e}")

    except Exception as e:
        logger.error(f"获取订阅列表失败: {e}")


@scheduler.scheduled_job("interval", seconds=CONFIG["CHECK_INTERVAL"], id="check_version_update")
async def version_update_checker():
    """定时检查版本更新"""
    logger.trace("检查明日方舟版本更新")

    try:
        result = await ark_monitor.check_version_update()

        if not result.client_updated and not result.res_updated:
            logger.trace("无版本更新")
            return

        message = None
        if result.client_updated:
            logger.warning("检测到明日方舟客户端版本更新")
            if result.old_version:
                message = (
                    f"🔄 明日方舟客户端版本更新\n"
                    f"客户端版本: {result.old_version.clientVersion} → {result.version.clientVersion}\n"
                    f"资源版本: {result.old_version.resVersion} → {result.version.resVersion}"
                )
            else:
                message = (
                    f"🔄 明日方舟客户端版本更新\n"
                    f"客户端版本: {result.version.clientVersion}\n"
                    f"资源版本: {result.version.resVersion}"
                )
        elif result.res_updated:
            logger.warning("检测到明日方舟资源版本更新")
            if result.old_version:
                message = (
                    f"📦 明日方舟资源版本更新\n"
                    f"客户端版本: {result.version.clientVersion}\n"
                    f"资源版本: {result.old_version.resVersion} → {result.version.resVersion}"
                )
            else:
                message = (
                    f"📦 明日方舟资源版本更新\n"
                    f"客户端版本: {result.version.clientVersion}\n"
                    f"资源版本: {result.version.resVersion}"
                )

        if message:
            await _notify_subscribers(TASK_NAME_SERVER_CHECK, message)

    except Exception as e:
        logger.error(f"版本更新检查失败: {e}")


@scheduler.scheduled_job("interval", seconds=CONFIG["CHECK_INTERVAL"], id="check_server_status")
async def server_status_checker():
    """定时检查服务器状态"""
    logger.trace("检查明日方舟服务器状态")

    try:
        result = await ark_monitor.check_server_status()

        if not result.status_changed:
            logger.trace("服务器状态无变化")
            return

        current_text = ark_monitor.get_status_text(result.current_status)
        previous_text = ark_monitor.get_status_text(result.previous_status) if result.previous_status else "Unknown"

        if result.current_status == 2:  # Active
            logger.info("游戏服务器恢复正常")
            message = f"✅ 明日方舟服务器状态变更: {previous_text} → {current_text}"
        elif result.current_status == 1:  # Under Maintenance
            logger.warning("游戏服务器进入维护")
            message = f"🔧 明日方舟服务器状态变更: {previous_text} → {current_text}"
        else:
            logger.warning(f"游戏服务器状态异常: {result.current_status}")
            message = f"⚠️ 明日方舟服务器状态变更: {previous_text} → {current_text}"

        await _notify_subscribers(TASK_NAME_GAME_SERVER_CHECK, message)

    except Exception as e:
        logger.error(f"服务器状态检查失败: {e}")


@sv_apk_check.on_command("检查APK更新")
async def check_apk_update(bot: Bot, ev: Event):
    try:
        await bot.send("正在检查APK更新...")

        update_info, _ = await apk_monitor.check_and_extract_apk()

        if update_info:
            message = "最新APK信息：\n"
            message += f"url: {update_info.apk_url}\n"
            message += f"updateTime: {time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(update_info.update_time))}\n"
            message += f"versionName: {update_info.version_info.version_name}\n"
            message += f"versionCode: {update_info.version_info.version_code}\n"
            message += f"versionId: {update_info.version_info.version_id}\n"
            message += f"manifestName: {update_info.version_info.manifest_name}\n"
            message += f"manifestVersion: {update_info.version_info.manifest_version}\n"
            message += f"il2cppSize: {human_readable_size(update_info.version_info.il2cpp_size)}\n"
            message += f"globalMetadataSize: {human_readable_size(update_info.version_info.global_metadata_size)}\n"

            await bot.send(message)
        else:
            await bot.send("检查APK更新失败，请查看日志")

    except Exception as e:
        logger.error(f"检查APK更新失败: {e}")
        await bot.send("检查APK更新失败，请稍后再试")


@sv_apk_check_sub.on_fullmatch("订阅APK更新")
async def subscribe_apk_update(bot: Bot, ev: Event):
    """订阅APK更新"""
    if ev.group_id is None:
        return await bot.send("请在群聊中订阅")

    try:
        data = await gs_subscribe.get_subscribe(TASK_NAME_APK_CHECK)
        if data:
            for subscribe in data:
                if subscribe.group_id == ev.group_id:
                    return await bot.send("已经订阅了明日方舟APK更新！")

        await gs_subscribe.add_subscribe(
            "session",
            task_name=TASK_NAME_APK_CHECK,
            event=ev,
            extra_message="",
        )

        logger.info(f"新增APK更新订阅: {ev.group_id}")
        await bot.send("成功订阅明日方舟APK更新!")

    except Exception as e:
        logger.error(f"订阅APK更新失败: {e}")
        await bot.send("订阅失败，请稍后再试")


@scheduler.scheduled_job("interval", seconds=CONFIG["CHECK_INTERVAL"], id="check_apk_update")
async def apk_update_checker():
    """定时检查APK更新"""
    logger.trace("检查明日方舟APK更新")
    try:
        update_info, is_updated = await apk_monitor.check_and_extract_apk()

        if update_info and is_updated:
            message = "检测到明日方舟APK更新\n"
            message += f"url: {update_info.apk_url}\n"
            message += f"updateTime: {time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(update_info.update_time))}\n"

            message += f"versionName: {update_info.version_info.version_name}\n"
            message += f"versionCode: {update_info.version_info.version_code}\n"
            message += f"versionId: {update_info.version_info.version_id}\n"
            message += f"manifestName: {update_info.version_info.manifest_name}\n"
            message += f"manifestVersion: {update_info.version_info.manifest_version}\n"
            message += f"il2cppSize: {human_readable_size(update_info.version_info.il2cpp_size)}\n"
            message += f"globalMetadataSize: {human_readable_size(update_info.version_info.global_metadata_size)}\n"

            await _notify_subscribers(TASK_NAME_APK_CHECK, message)
    except Exception as e:
        logger.error(f"APK更新检查失败: {e}")
        await _notify_subscribers(TASK_NAME_APK_CHECK, "明日方舟APK更新检查失败，请查看日志")
