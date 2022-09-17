from typing import Callable, Iterable, List, Optional, Tuple, overload, Type, TypeVar

A = TypeVar("A")

def filter_(f: Callable[[A], bool], xs: Iterable[A], /) -> Iterable[A]:
    """Like built-in `filter` but retains type and uses comprehension 
    under the hood.
    """
    _return_type = type(xs)
    if _return_type is str:
        return "".join([x for x in xs if f(x)]) #type:ignore
    return _return_type([x for x in xs if f(x)]) #type:ignore
