from __future__ import annotations

def partition_n(string: str, sep: str, n: int | None=None) -> list[str]:
    if n is not None and (not isinstance(n, int) or n < 0):
        raise AssertionError(f'`n` must be a non-negative integer or `None`; {n=}')
    r1, r2, rest = string.partition(sep)
    if n is None:
        return [r1, r2, *partition_n(rest, sep)]
    if n > 0:
        return [r1, r2, *partition_n(rest, sep, n-1)]
    else: 
        # n == 0
        return [r1, r2, rest]
    