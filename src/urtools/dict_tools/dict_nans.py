from urtools.type_tools import is_non_val

def filter_dict_nans(d: dict) -> dict:
    return {k: v for k, v in d.items() if not is_non_val(v)}

def dict_has_nans(d: dict) -> bool:
    return any(is_non_val(v) for v in d.values())
