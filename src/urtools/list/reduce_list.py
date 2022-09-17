from __future__ import annotations

from typing import Iterable, TypeVar

from urtools.func.flatten import flatten

T = TypeVar('T')

def reduce_list(ll: Iterable[list[T]]) -> list[T]:
    """Reduce a list - remove one level of nesting.
    """
    return flatten(ll)
