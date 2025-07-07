import asyncio
import json
import random
from pathlib import Path

from gsuid_core.aps import scheduler
from gsuid_core.bot import Bot
from gsuid_core.data_store import get_res_path
from gsuid_core.logger import logger
from gsuid_core.models import Event
from gsuid_core.subscribe import gs_subscribe
from gsuid_core.sv import SV

from .ak import ArknightsClient, ServerMaintenanceError

sv_add_server_bot = SV("明日方舟账号池", pm=0)
sv_game_server_monitor = SV("明日方舟游戏服务器状态")
sv_game_server_monitor_sub = SV("订阅明日方舟游戏服务器状态", pm=0)

TASK_NAME_GAME_SERVER_MONITOR = "订阅明日方舟游戏服务器状态"

EXSAMPLE = """ark登陆官服 手机号, 密码
⚠ 提示: 该命令将会使用账密进行登陆, 请[永远]不要使用自己的大号, 否则可能会导致账号被封！
⚠ 请自行使用任何小号, 本插件不为账号被封禁承担任何责任！！
"""


@sv_add_server_bot.on_command("登陆官服")
async def add_server_bot(bot: Bot, ev: Event):
    evt = ev.text.strip()
    if not evt:
        return await bot.send(f"❌ 登陆失败!参考命令:\n{EXSAMPLE}")

    if " " in evt:
        username, password = evt.split(" ")
        if not username or not password:
            return await bot.send("❌ 请输入有效的username和password!")

        try:
            client = ArknightsClient(username=username, password=password)
            await client.login()

            return await bot.send(
                f"✅ Login successful!\nUsername: {client.username}\nUID: {client.uid}\nNickname: {client.nickname}"
            )
        except Exception as e:
            logger.error(f"❌ 登陆失败! 错误信息: {e}")
            return await bot.send(f"❌ 登陆失败! 错误信息: {e}")
    else:
        return await bot.send(f"❌ 登陆失败!参考命令:\n{EXSAMPLE}")


def get_client_session_files():
    session_dir = get_res_path("ArknightsUID") / "session"
    if not session_dir.exists():
        return []

    session_files = list(session_dir.rglob("*.pickle"))
    return session_files


@sv_game_server_monitor.on_command("取明日方舟游戏服务器状态")
async def get_game_server_status(bot: Bot, ev: Event):
    session_files = get_client_session_files()
    if not session_files:
        return await bot.send("❌ 会话文件不存在!")

    for session_file in session_files:
        try:
            client = ArknightsClient.from_session_file(session_file)
            await client.login()

            push_message = await client.get_push_message()
            message = f"✅ 游戏服务器状态正常\nPush Message:\n{push_message}"
            return await bot.send(message)
        except ServerMaintenanceError as e:
            logger.warning(f"⚠️ 游戏服务器正在维护: {e}")
            return await bot.send("⚠️ 游戏服务器正在维护")
        except Exception as e:
            logger.error(f"❌ 获取游戏服务器状态失败! 文件: {session_file} 错误信息: {e}")
            session_file.unlink(missing_ok=True)
    else:
        return await bot.send("❌ 所有会话文件均失效，无法获取游戏服务器状态！")


@sv_game_server_monitor_sub.on_command("订阅明日方舟游戏服务器状态")
async def subscribe_game_server_status(bot: Bot, ev: Event):
    if ev.group_id is None:
        return await bot.send("请在群聊中订阅")

    try:
        data = await gs_subscribe.get_subscribe(TASK_NAME_GAME_SERVER_MONITOR)
        if data:
            for subscribe in data:
                if subscribe.group_id == ev.group_id:
                    return await bot.send("已经订阅了明日方舟游戏服务器状态更新！")

        await gs_subscribe.add_subscribe(
            "session",
            task_name=TASK_NAME_GAME_SERVER_MONITOR,
            event=ev,
            extra_message="",
        )

        logger.info(f"新增游戏服务器状态订阅: {ev.group_id}")
        await bot.send("成功订阅明日方舟游戏服务器状态更新!")

    except Exception as e:
        logger.error(f"订阅游戏服务器状态失败: {e}")
        await bot.send("订阅失败，请稍后再试")


async def _notify_subscribers(task_name: str, message: str):
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


@scheduler.scheduled_job("interval", seconds=60, id="check_game_server_status")
async def check_game_server_status():
    session_files = get_client_session_files()
    if not session_files:
        return

    game_server_status_storage = get_res_path("ArknightsUID") / "game_server_status.json"
    if game_server_status_storage.exists():
        try:
            with Path.open(game_server_status_storage, encoding="utf-8") as f:
                last_status_json = json.load(f)
        except json.JSONDecodeError:
            last_status_json = {"status": "unknown"}
    else:
        last_status_json = {"status": "unknown"}

    last_status = last_status_json.get("status", "unknown")

    for session_file in session_files:
        try:
            client = ArknightsClient.from_session_file(session_file)
            await client.login()

            push_message = await client.get_push_message()
            logger.info(f"获取游戏服务器状态: {session_file}, 推送消息: {push_message}")

            # if the login is successful, we can assume the game server is active
            current_status = "Active"
            if last_status != current_status:
                if current_status == "Active":
                    await _notify_subscribers(
                        TASK_NAME_GAME_SERVER_MONITOR, "✅ Arknights game server status is now active"
                    )
                elif current_status == "Under Maintenance":
                    await _notify_subscribers(
                        TASK_NAME_GAME_SERVER_MONITOR, "⚠️ Arknights game server is under maintenance"
                    )
                with Path.open(game_server_status_storage, "w", encoding="utf-8") as f:
                    json.dump({"status": current_status}, f, ensure_ascii=False)
            elif last_status == "unknown":
                with Path.open(game_server_status_storage, "w", encoding="utf-8") as f:
                    json.dump({"status": current_status}, f, ensure_ascii=False)
            return
        except ServerMaintenanceError as e:
            logger.warning(f"⚠️ 游戏服务器正在维护: {e}")
            return await _notify_subscribers(
                TASK_NAME_GAME_SERVER_MONITOR, "⚠️ Arknights game server is under maintenance"
            )
        except Exception as e:
            logger.error(f"❌ 获取游戏服务器状态失败! 文件: {session_file} 错误信息: {e}")
            session_file.unlink(missing_ok=True)
    else:
        return await _notify_subscribers(
            TASK_NAME_GAME_SERVER_MONITOR, "❌ 所有会话文件均失效，无法获取游戏服务器状态！"
        )
