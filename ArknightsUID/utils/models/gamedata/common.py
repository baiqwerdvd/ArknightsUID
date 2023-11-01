from __future__ import annotations

from collections.abc import Callable, Iterable, Iterator
from copy import copy, deepcopy
from typing import Any, Dict, Tuple, TypeVar, Union
from typing_extensions import dataclass_transform

from msgspec import (
    Struct,
    UnsetType,
    convert,
    field,
    json as mscjson,
)

Model = TypeVar("Model", bound="BaseStruct")
T1 = TypeVar("T1")
T2 = TypeVar("T2")


def transUnset(v: Union[T1, UnsetType], d: T2 = None) -> Union[T1, T2]:
    return v if not isinstance(v, UnsetType) else d


@dataclass_transform(field_specifiers=(field,))
class BaseStruct(
    Struct,
    forbid_unknown_fields=True,
    omit_defaults=True,
    gc=False,
):
    class Config:
        encoder = mscjson.Encoder()

    @classmethod
    def convert(
        cls: type[Model],
        obj: Any,
        *,
        strict: bool = True,
        from_attributes: bool = False,
        dec_hook: Union[Callable[[type, Any], Any], None] = None,
        builtin_types: Union[Iterable[type], None] = None,
        str_keys: bool = False,
    ) -> Model:
        if obj is None:
            return None  # type: ignore
        if isinstance(obj, BaseStruct):
            obj = obj.model_dump()
        return convert(
            obj=obj,
            type=cls,
            strict=strict,
            from_attributes=from_attributes,
            dec_hook=dec_hook,
            builtin_types=builtin_types,
            str_keys=str_keys,
        )

    def __iter__(self) -> Iterator[Tuple[str, Any]]:
        for field_name in self.__struct_fields__:
            yield field_name, getattr(self, field_name)

    def keys(self) -> Iterator[str]:
        yield from self.__struct_fields__

    def values(self) -> Iterator[Any]:
        for field_name in self.__struct_fields__:
            yield getattr(self, field_name)

    def model_dump(self) -> Dict[str, Any]:
        return mscjson.decode(mscjson.encode(self))

    def dump_child(self, target: str) -> Any:
        return self.model_dump()[target]

    def model_copy(self: Model, *, deep: bool = False) -> Model:
        return deepcopy(self) if deep else copy(self)
