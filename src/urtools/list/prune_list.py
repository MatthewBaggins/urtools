from __future__ import annotations

from typing import TypeVar

T = TypeVar("T")


def prune_list(l: list[T]) -> list[T]:
    """Strip the list from repeating elements."""
    return list(dict.fromkeys(l))
