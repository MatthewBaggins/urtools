from typing import Dict, TypeVar, Union

V = TypeVar('V')
def json_keys2int(x: Dict[str, V]) -> Dict[Union[str, int], V]:
    """A util to convert json objects' keys from strings to ints (where they should be ints)
    """
    if isinstance(x, dict):
        assert all(str(k).isdigit() and float(k) == int(k) for k in x)
        return {int(k): v for k, v in x.items()}
    return x
