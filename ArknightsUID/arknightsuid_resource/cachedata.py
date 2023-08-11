import json
from functools import cache
from pathlib import Path
from time import time
from typing import Any, ClassVar

from loguru import logger

from ..utils.file import read_json


class StoreData:
    data: dict[Any, Any]
    modification_time: float

    def __init__(self, data: dict[Any, Any], modification_time: float) -> None:
        self.data = data
        self.modification_time = modification_time


class CacheData:
    cached_data: ClassVar[dict[str, StoreData]] = {}

    @classmethod
    @cache
    def get_cache(cls, local_path: Path) -> dict[Any, Any]:
        data_name = local_path.stem
        if data_name in cls.cached_data:
            current_modification_time = local_path.stat().st_mtime
            if current_modification_time == cls.cached_data[data_name].modification_time:
                logger.debug(f'hit cached: {data_name}')
                return cls.cached_data[data_name].data
        return cls.set_cache(local_path, data_name)

    @classmethod
    def set_cache(
        cls, local_path: Path | None, data_name: str, memory_data: dict | None = None
    ) -> dict[Any, Any]:
        data = read_json(local_path) if local_path else memory_data
        if data is None:
            raise FileNotFoundError
        modification_time = local_path.stat().st_mtime if local_path else time()
        cls.cached_data[data_name] = StoreData(data, modification_time)
        logger.debug(f'cached: {data_name}')
        return cls.cached_data[data_name].data

    @classmethod
    def readFile(cls, local_path: Path) -> dict[Any, Any]:
        try:
            if isinstance(local_path, str):
                local_path = Path(local_path)
            logger.debug(f'loading: {local_path.stem}')
            return cls.get_cache(local_path)
        except json.decoder.JSONDecodeError as e:
            logger.error(f'Could not load file "{local_path}".')
            raise FileNotFoundError from e

    @classmethod
    def readExcel(cls, table_name: str) -> dict[Any, Any]:
        logger.debug(f'loading: {table_name}.json')
        if table_name not in cls.cached_data:
            return {}
        return cls.cached_data[table_name].data
