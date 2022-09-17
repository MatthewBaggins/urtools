from typing import Iterable

def has_nulls(l: Iterable) -> bool:
    return any(x is None or x != x or str(x).lower() == 'nan' for x in l)
