import asyncio
import threading

from gsuid_core.logger import logger

# from ..arknightsuid_resource import startup
from ..utils.database.startup import ark_adapter


async def all_start():
    try:
        # await startup()
        await ark_adapter()
    except Exception as e:
        logger.exception(e)


threading.Thread(target=lambda: asyncio.run(all_start()), daemon=True).start()
