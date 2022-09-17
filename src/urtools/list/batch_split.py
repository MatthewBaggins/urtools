from __future__ import annotations

from typing import TypeVar

T = TypeVar('T')
def batch_split(data: list[T], batch_size: int = 20) -> list[list[T]]:
    """Split the list into a number of batches (smaller lists)."""
    return [data[i*batch_size : (i+1)*batch_size] for i in range((len(data) // batch_size) + 1)]
