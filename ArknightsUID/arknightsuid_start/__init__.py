import asyncio

# import threading
from loguru import logger

from ..arknightsuid_resource import startup
from ..utils.database.startup import ark_adapter


async def all_start():
    await startup()
    await ark_adapter()


# asyncio.run(all_start())
