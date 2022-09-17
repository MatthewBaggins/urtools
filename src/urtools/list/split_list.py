from __future__ import annotations

from typing import TypeVar

import numpy as np

T = TypeVar('T')
def split_list(l: list[T], n_splits: int) -> list[list[T]]:
    """Partition a list into `n_splits` sublists of equal size.
    """
    return [a.tolist() for a in np.array_split(l, n_splits)] #type: ignore
