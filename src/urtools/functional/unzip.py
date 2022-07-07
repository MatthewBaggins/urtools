from __future__ import annotations

from typing import Iterable, TypeVar

#TODO: write tests for unzip
T = TypeVar('T')
def unzip(zipped: Iterable[Iterable[T]]) -> tuple[Iterable[T], ...]:
    inner_len = len(list(next((x for x in zipped))))
    if not all (len(list(x)) == inner_len for x in zipped):
        raise ValueError('All inner iterables must have the same length')
    unzipped: tuple[list[T]] = tuple(
        [list(x)[i] for x in zipped]
        for i in range(inner_len)
        )
    return unzipped
