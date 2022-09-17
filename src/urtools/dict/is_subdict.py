from __future__ import annotations
from typing import Dict, TypeVar
from typing_extensions import TypeGuard

K = TypeVar('K')
V = TypeVar('V')
def is_subdict(sub_dict: dict, sup_dict: Dict[K, V]) -> TypeGuard[Dict[K, V]]:
    """Check whether all key-value pairs in `sub_dict` occur in `sup_dict`.
    """
    return set(sub_dict.items()).issubset(sup_dict.items())

