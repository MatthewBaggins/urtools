from __future__ import annotations
from typing import Callable, Generic, Iterable, Protocol, TypeVar, cast
from typing_extensions import reveal_type

# T = TypeVar('T')
# class Iter(Generic[T], Iterable[T]):
#     def __init__(self, *args, **kwargs):
#         super().__init__(*args, **kwargs)


T = TypeVar('T', covariant=True)
class _Iter(Iterable, Protocol[T]):
    pass
    
#TODO: test fmap
In = TypeVar('In')
Out = TypeVar('Out')
Iter = TypeVar('Iter', bound=_Iter)
# Iter = TypeVar('Iter', list, tuple, set, frozenset, dict, str, bytes, bytearray, range)
def fmap(f: Callable[[In], Out], xs: Iter[In]) -> Iter[Out]:
    if not isinstance(f, Callable):
        raise TypeError(f'`f` should be `Callable` but is {type(f)} {f.__name__ = }')
    if not isinstance(xs, Iterable):
        raise TypeError(f'`xs` should be `Iterable` but is {type(xs)}')

    xs_type = type(xs)
    try:
        ys: Iter[Out] = xs_type(map(f, list(xs))) #type:ignore
        return ys
    except Exception as e:
        raise e

xs = 1,2,3
from math import sqrt
ys = fmap(lambda x: sqrt(x), xs)
