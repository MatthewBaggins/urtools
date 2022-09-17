from typing import Callable, Iterable, List, Tuple, overload, TypeVar

A = TypeVar("A")

@overload
def filter_(f: Callable[[str], bool], xs: str,
            /) -> str:...
@overload
def filter_(f: Callable[[A], bool], xs: List[A],
            /) -> List[A]:...
@overload
def filter_(f: Callable[[A], bool], xs: Tuple[A, ...],
            /) -> Tuple[A, ...]:...
@overload
def filter_(f: Callable[[A], bool], xs: Iterable[A],
            /) -> Iterable[A]:...

def filter_(f: Callable[[A], bool], xs: Iterable[A], /) -> Iterable:
    """Like built-in `filter` but retains type and uses comprehension 
    under the hood.
    """
    _return_type = type(xs)
    if _return_type is str:
        return "".join([x for x in xs if f(x)]) #type:ignore
    return _return_type([x for x in xs if f(x)]) #type:ignore
