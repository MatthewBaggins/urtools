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
    if not xs:
        return xs
    type_count = Counter(type(x) for x in xs)
    assert len(type_count) == 1 and isinstance((xs_type := list(type_count)[0]), Iterable)
    if issubclass(xs_type, dict):
        return join_dicts(*cast(Iterable[dict], xs))
    if xs_type is set:
        return reduce(or_, xs)
    return reduce(add, xs)
