import asyncio
import threading

from torappu_excel import ExcelTableManager

EXCEL: ExcelTableManager = ExcelTableManager()

threading.Thread(target=lambda: asyncio.run(EXCEL.preload_table()), daemon=True).start()
