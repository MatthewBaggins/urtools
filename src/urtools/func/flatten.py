from __future__ import annotations

from collections import Counter
from functools import reduce
from operator import add, or_
from typing import Iterable, TypeVar, cast, overload

from urtools.dict.join_dicts import join_dicts

T = TypeVar("T")

@overload
def flatten(xs: Iterable[list[T]]) -> list[T]:...
@overload
def flatten(xs: Iterable[tuple[T]]) -> tuple[T, ...]:...
@overload
def flatten(xs: Iterable[dict]) -> dict:...
@overload
def flatten(xs: Iterable[str]) -> str:...
@overload
def flatten(xs: Iterable[set[T]]) -> set[T]:...
@overload
def flatten(xs: Iterable[Iterable[T]]) -> Iterable[T]:...

def flatten(xs: Iterable[Iterable]) -> Iterable:
    """Flatten the container/`Iterable`, i.e. remove one dimension/level of nesting."""
    if not issubclass(outer_type := type(xs), Iterable):
        raise OuterNotSubclassOfIterableError(
            f"The outer type {outer_type} is not a subclass of Iterable")
    if outer_type == str:
        raise OuterTypeIsStrError("The outer type is `string`.")
    if not xs:
        return xs
    type_count = Counter(type(x) for x in xs)
    if len(type_count) != 1:
        raise MoreThanOneTypeError(
            f"There is more than one type in the iterable.\n"
            f"There are {len(type_count)} types: {list(type_count)}")
    if not issubclass(inner_type := list(type_count)[0], Iterable):
        raise InnerNotSubclassOfIterableError(
            f"The inner type {inner_type} is not a subclass of Iterable")
    if issubclass(inner_type, dict):
        return join_dicts(*cast(Iterable[dict], xs))
    if inner_type is set:
        return reduce(or_, xs)
    return reduce(add, xs)

class OuterNotSubclassOfIterableError(TypeError):
    """OuterNotSubclassOfIterableError"""

class OuterTypeIsStrError(TypeError):
    """OuterTypeIsStrError"""

class MoreThanOneTypeError(TypeError):
    """MoreThanOneTypeError"""

class InnerNotSubclassOfIterableError(TypeError):
    """InnerNotSubclassOfIterableError"""
