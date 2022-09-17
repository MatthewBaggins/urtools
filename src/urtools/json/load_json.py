#pylint:disable=missing-function-docstring
import json
from typing import List, Literal, Optional, overload, Type, Union

JsonType = Union[Type[list], Type[dict]]
JsonMode = Literal['r', 'w', 'x']

@overload
def load_json(path: str, json_type=dict) ->  dict: 
    ...

@overload
def load_json(path: str, json_type=list) ->  list: 
    ... 

def load_json(path: str, json_type: JsonType=dict, *, 
              mode: JsonMode = 'r', encoding: Optional[str] = 'utf-8') -> Union[list, dict]:
    """Load the file into JSON in one line with context manager.
    """
    with open(path, mode, encoding=encoding) as f:
        loaded = json.load(f)
    if not isinstance(loaded, json_type):
        raise AssertionError(f'{path} is {type(loaded)}, should be {json_type}')
    return loaded

def load_dict(path: str) -> dict:
    return load_json(path, dict)

def load_list(path: str) -> list:
    return load_json(path, list)

def load_list_of_dicts(path: str) -> List[dict]:
    loaded = load_list(path)
    assert all(isinstance(x, dict) for x in loaded)
    return loaded
