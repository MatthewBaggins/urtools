from typing import Any, TypeVar

def _is_valid_option(option: Any) -> bool:
    if option is None or option != option:
        return False
    return True

#TODO: overload return type depending on `allow_none_default`
T = TypeVar('T')
def alt(*options: T | None, default: T | None = None, allow_none_default: bool = False) -> T | None:
    for option in options:
        if _is_valid_option(option):
            assert option
            return option
    if _is_valid_option(default):
        assert default
        return default
    if allow_none_default:
        return None
    raise StopIteration(f'None of the `options` given are valid and default was not `provided`: {options=}; {default=}')
