import base64
import json
from collections.abc import Callable, Iterable, Iterator
from copy import copy, deepcopy
from typing import Any, Dict, List, Tuple, Type, TypeVar, Union

from msgspec import Meta, Struct, UnsetType, convert, field
from msgspec import json as mscjson
from typing_extensions import dataclass_transform

Model = TypeVar('Model', bound='BaseStruct')
T = TypeVar("T")


def transUnset(v: Union[T, UnsetType], d: Any = None) -> Union[T, Any]:
    return v if not isinstance(v, UnsetType) else d


@dataclass_transform(field_specifiers=(field,))
class BaseStruct(Struct, forbid_unknown_fields=True, omit_defaults=True, gc=False):
    class Config:
        encoder = mscjson.Encoder()

    @classmethod
    def json_schema(cls) -> str:
        return (
            f"```json\n{json.dumps(mscjson.schema(cls), ensure_ascii=False, indent=2)}"
        )

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
            str_keys=str_keys
        )

    def __post_init__(
        self,
        validate_whitespace: Union[List[str], None] = None,
        validate_num_with_range: Union[List[Tuple[str, Meta]], None] = None,
        validate_optional: Union[List[Tuple[str, Meta]], None] = None,
        validate_int: Union[List[str], None] = None,
        validate_base64: Union[List[str], None] = None,
    ) -> None:
        if validate_base64 is None:
            validate_base64 = []
        if validate_int is None:
            validate_int = []
        if validate_optional is None:
            validate_optional = []
        if validate_num_with_range is None:
            validate_num_with_range = []
        if validate_whitespace is None:
            validate_whitespace = []
        for field_name in validate_whitespace:
            if (field_value := getattr(self, field_name)) is not None:
                if isinstance(field_value, str) and not field_value.strip():
                    raise ValueError(
                        f'child "{field_name}" fails because ["{field_name}" is not allowed to be empty]'
                    )

        for field_group in validate_num_with_range:
            if (field_value := getattr(self, field_group[0])) is not None:
                if field_value > (le := field_group[1].le or field_value):
                    raise ValueError(f'"{field_group[0]}" must be less than {le}')
                if field_value < (ge := field_group[1].ge or field_value):
                    raise ValueError(f'"{field_group[0]}" must be greater than {ge}')

        for field_group in validate_optional:
            if (field_value := getattr(self, field_group[0])) is not None:
                if field_value not in field_group[1].examples:
                    raise ValueError(
                        f'"{field_group[0]}" must be one of {field_group[1]}'
                    )

        for field_name in validate_int:
            if (field_value := getattr(self, field_name)) is not None:
                if not field_value.isdigit():
                    raise ValueError(
                        f'child "{field_name}" fails because ["{field_name}" must be a number]'
                    )

        for field_name in validate_base64:
            try:
                base64.b64decode(getattr(self, field_name))
            except Exception as e:
                raise ValueError(
                    f'child "{field_name}" fails because ["{field_name}" must be a valid base64 string]'
                ) from e

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
