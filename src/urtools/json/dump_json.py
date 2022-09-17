from typing import Union
import json

def dump_json(obj: Union[list, dict], path: str) -> None:
    """Load data into a JSON file in one line with context manager.
    """
    with open(path, 'w', encoding='utf-8') as f:
        json.dump(obj, f)
