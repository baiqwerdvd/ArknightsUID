import json
from functools import cache
from pathlib import Path
from time import time
from typing import Any, ClassVar, Dict, Union

from loguru import logger

from ..utils.file import read_json


class StoreData:
    data: Dict[Any, Any]
    modification_time: float

    def __init__(self, data: Dict[Any, Any], modification_time: float) -> None:
        self.data = data
        self.modification_time = modification_time


class CacheData:
    cached_data: ClassVar[Dict[str, StoreData]] = {}

    @classmethod
    @cache
    def get_cache(cls, local_path: Path) -> Dict[Any, Any]:
        data_name = local_path.stem
        if data_name in cls.cached_data:
            current_modification_time = local_path.stat().st_mtime
            if current_modification_time == cls.cached_data[data_name].modification_time:
                return cls.cached_data[data_name].data
        return cls.set_cache(local_path, data_name)

    @classmethod
    def set_cache(
        cls, local_path: Union[Path, None], data_name: str, memory_data: Union[Dict, None] = None
    ) -> Dict[Any, Any]:
        data = read_json(local_path) if local_path else memory_data
        if data is None:
            raise FileNotFoundError
        modification_time = local_path.stat().st_mtime if local_path else time()
        cls.cached_data[data_name] = StoreData(data, modification_time)
        return cls.cached_data[data_name].data

    @classmethod
    def readFile(cls, local_path: Path) -> Dict[Any, Any]:
        try:
            if isinstance(local_path, str):
                local_path = Path(local_path)
            return cls.get_cache(local_path)
        except json.decoder.JSONDecodeError as e:
            logger.error(f'Could not load file "{local_path}".')
            raise FileNotFoundError from e

    @classmethod
    def readExcel(cls, table_name: str) -> Dict[Any, Any]:
        logger.debug(f'loading: {table_name}.json')
        if table_name not in cls.cached_data:
            return {}
        return cls.cached_data[table_name].data
    
    @classmethod
    def readBytesExcel(cls, table_name: str) -> bytes:
        logger.debug(f'loading: {table_name}.json')
        if table_name not in cls.cached_data:
            return bytes({})
        return json.dumps(cls.cached_data[table_name].data).encode('utf-8')
