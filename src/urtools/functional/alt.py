from dataclasses import dataclass, field
from typing import Any, Iterable, TypeVar, Optional

from urtools.type_tools import is_non_val

@dataclass
class NoValidAlternativesError(StopIteration):
    options: Iterable
    message: str = field(init=False)
    def __post_init__(self) -> None:
        self.message = f'None of the `options` passed to the `alt` function are valid and default was not provided nor allowed to be `None`\n{self.options = }'

#TODO: overload return type depending on `allow_none_default`
#TODO: test it
T = TypeVar('T')
def alt(*options: Optional[T], 
        default: Optional[T] = None, 
        allow_none_default: bool = False) -> Optional[T]:
    for option in options:
        if not is_non_val(option):
            return option
    if not is_non_val(default):
        return default
    if allow_none_default:
        return None
    raise NoValidAlternativesError(options)
