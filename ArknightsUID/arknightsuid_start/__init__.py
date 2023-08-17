import asyncio
import threading

from loguru import logger

from ..arknightsuid_resource import startup


async def all_start():
    try:
        pass
        await startup()
    except Exception as e:
        logger.exception(e)


threading.Thread(target=lambda: asyncio.run(all_start()), daemon=True).start()
