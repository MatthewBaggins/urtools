#pylint:disable=missing-function-docstring
from typing import Iterable, Union
from typing_extensions import TypeGuard

def is_str(x: object) -> TypeGuard[str]:
    return isinstance(x, str)

def is_iter(x: object) -> TypeGuard[Iterable]:
    return isinstance(x, Iterable)

def is_str_or_non_iter(x: object) -> TypeGuard[Union[str, Iterable]]:
    return is_str(x) or not is_iter(x)

def is_iter_and_non_str(x: object) -> TypeGuard[Iterable]:
    """Is this an iterable but not a string?
    """
    return not is_str(x) and is_iter(x)
