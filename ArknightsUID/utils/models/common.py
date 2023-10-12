from collections.abc import Callable, Iterable, Iterator
from copy import copy, deepcopy
from typing import Any, Dict, Tuple, Type, TypeVar, Union

from msgspec import Struct, UnsetType, convert, field
from msgspec import json as mscjson
from typing_extensions import dataclass_transform

Model = TypeVar('Model', bound='BaseStruct')
T = TypeVar("T")


def transUnset(v: Union[T, UnsetType], d: Any = None) -> Union[T, Any]:
    return v if not isinstance(v, UnsetType) else d


@dataclass_transform(field_specifiers=(field,))
class BaseStruct(
    Struct, forbid_unknown_fields=True, omit_defaults=True, gc=False
):
    class Config:
        encoder = mscjson.Encoder()

    @classmethod
    def convert(
        cls: Type[Model],
        obj: Any,
        *,
        strict: bool = True,
        from_attributes: bool = False,
        dec_hook: Union[Callable[[type, Any], Any], None] = None,
        builtin_types: Union[Iterable[type], None] = None,
        str_keys: bool = False,
    ) -> Model:
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

    def __getattribute__(self, __name: str) -> Union[Any, None]:
        value = super().__getattribute__(__name)
        if isinstance(value, UnsetType):
            return None
        return value

    def keys(self) -> Iterator[str]:
        yield from self.__struct_fields__

    def values(self) -> Iterator[Any]:
        for field_name in self.__struct_fields__:
            yield getattr(self, field_name)

    def model_dump(self) -> Dict[str, Any]:
        return mscjson.decode(mscjson.encode(self))

    def model_copy(self: Model, *, deep: bool = False) -> Model:
        return deepcopy(self) if deep else copy(self)
