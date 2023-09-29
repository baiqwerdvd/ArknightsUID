from __future__ import annotations
from abc import ABC, abstractmethod
import json

import os
import pickle
import shutil
from datetime import UTC, datetime, timedelta
from pathlib import Path
from tempfile import mkstemp
from typing import Any

import anyio
from anyio import Path as anyioPath
from anyio.to_thread import run_sync
from msgspec import Struct

from gsuid_core.logger import logger


def read_json(file_path: Path, **kwargs) -> dict:
    """
    Read a JSON file and return its contents as a dictionary.
    """
    try:
        with Path.open(file_path, encoding="UTF-8", **kwargs) as file:
            return json.load(file)
    except (FileNotFoundError, json.JSONDecodeError) as e:
        logger.error(f"Error reading JSON file: {e}")
        return {}


class Store(ABC):
    """Thread and process safe asynchronous key/value store."""

    @abstractmethod
    async def set(self, key: str, value: str | bytes, expires_in: int | timedelta | None = None) -> None:
        raise NotImplementedError

    @abstractmethod
    async def get(self, key: str, renew_for: int | timedelta | None = None) -> bytes | None:
        raise NotImplementedError

    @abstractmethod
    async def delete(self, key: str) -> None:
        raise NotImplementedError

    @abstractmethod
    async def delete_all(self) -> None:
        raise NotImplementedError

    @abstractmethod
    async def exists(self, key: str) -> bool:
        raise NotImplementedError

    @abstractmethod
    async def expires_in(self, key: str) -> int | None:
        raise NotImplementedError


class StorageObject(Struct):
    expires_at: datetime | None
    data: Any

    @classmethod
    def new(cls, data: Any, expires_in: int | timedelta | None) -> StorageObject:
        if expires_in is not None and not isinstance(expires_in, timedelta):
            expires_in = timedelta(seconds=expires_in)
        return cls(
            data=data,
            expires_at=(datetime.now(tz=UTC) + expires_in) if expires_in else None,
        )

    @property
    def expired(self) -> bool:
        return self.expires_at is not None and datetime.now(tz=UTC) >= self.expires_at

    @property
    def expires_in(self) -> int:
        if self.expires_at:
            return int(self.expires_at.timestamp() - datetime.now(tz=UTC).timestamp())
        return -1


class StoreService(Store):
    __slots__ = ("store", "lock", "path")

    def __init__(self) -> None:
        self.path: anyioPath = anyioPath('data')
        self.store_: dict[str, StorageObject] = {}
        self.lock: anyio.Lock = anyio.Lock()
        self.last_cleared: datetime = datetime.utcnow()

    @staticmethod
    async def load_from_path(path: anyioPath) -> dict[str, StorageObject]:
        try:
            data = await path.read_bytes()
            return pickle.loads(data)
        except FileNotFoundError:
            return {}

    def _write_sync(self, target_file: anyioPath) -> None:
        try:
            tmp_file_fd, tmp_file_name = mkstemp(dir=self.path, prefix=f"{target_file.name}.cache")
            renamed = False
            try:
                try:
                    os.write(tmp_file_fd, pickle.dumps(self.store_))
                finally:
                    os.close(tmp_file_fd)
                shutil.move(tmp_file_name, target_file)
                renamed = True
            finally:
                if not renamed:
                    Path.unlink(Path(tmp_file_name))
        except OSError:
            pass

    async def write(self, target_file: anyioPath) -> None:
        await run_sync(self._write_sync, target_file)

    async def set(self, key: str, value: Any, expires_in: int | timedelta | None = None) -> None:
        if isinstance(value, str):
            value = value.encode("UTF-8")
        async with self.lock:
            self.store_[key] = StorageObject.new(data=value, expires_in=expires_in)

    async def get(self, key: str, renew_for: int | timedelta | None = None, default: Any = None) -> Any:
        async with self.lock:
            storage_obj = self.store_.get(key)
            if not storage_obj:
                return default
            if storage_obj.expired:
                self.store_.pop(key)
                return None
            if renew_for and storage_obj.expires_at:
                storage_obj = StorageObject.new(data=storage_obj.data, expires_in=renew_for)
                self.store_[key] = storage_obj
            return storage_obj.data

    async def get_excel(self, table_name: str) -> Any:
        return await self.get(table_name, default=None)

    async def get_file(self, local_path: Path, expires_in: int | timedelta | None = None) -> Any:
        if not await self.exists(local_path.stem):
            await self.set(local_path.stem, read_json(local_path), expires_in)
        return await self.get(local_path.stem)

    async def delete(self, key: str) -> None:
        async with self.lock:
            self.store_.pop(key, None)

    async def delete_all(self) -> None:
        async with self.lock:
            self.store_.clear()

    async def delete_expired(self) -> None:
        async with self.lock:
            new_store = {}
            for i, (key, storage_obj) in enumerate(self.store_.items()):
                if not storage_obj.expired:
                    new_store[key] = storage_obj
                if i % 1000 == 0:
                    await anyio.sleep(0)
            self.store_ = new_store

    async def exists(self, key: str) -> bool:
        return key in self.store_

    async def keys(self) -> list[str]:
        return list(self.store_.keys())

    async def expires_in(self, key: str) -> int | None:
        if storage_obj := self.store_.get(key):
            return storage_obj.expires_in
        return None


store = StoreService()
