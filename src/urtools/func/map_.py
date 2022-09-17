from __future__ import annotations

from typing import Callable, Iterable, Optional, overload, Type, TypeVar

A = TypeVar("A")
R = TypeVar("R")
I = TypeVar("I", bound=Iterable)

@overload
def map_(f: Callable[[A], R], xs: list[A], return_type: Optional[Type[I]] = None,
         /) -> list[R]:...
@overload
def map_(f: Callable[[A], R], xs: tuple[A, ...], return_type: Optional[Type[I]] = None,
         /) -> tuple[R, ...]:...
@overload
def map_(f: Callable[[str], R], xs: str, return_type: Optional[Type[I]] = None,
         /) -> str:...
@overload
def map_(f: Callable[[A], R], xs: Iterable[A], return_type: Optional[Type[I]] = None,
         /) -> Iterable[R]:...
@overload
def map_(f: Callable[[A], R], xs: list[A], return_type: Type[I] = None,
         /) -> I:...

def map_(f: Callable[[A], R], xs: Iterable[A], return_type: Optional[Type[I]] = None,
         /) -> Iterable:
    """Like built-in `map` but retains the type and uses comprehension
    under the hood.
    """
    _return_type = return_type or type(xs)
    if _return_type is str:
        return "".join([str(f(x)) for x in xs]) #type:ignore
    return _return_type(f(x) for x in xs) #type:ignore
