from typing import Iterable

from urtools.type_tools import is_non_val

def list_has_nans(l: Iterable) -> bool:
    return any(is_non_val(x) for x in l)