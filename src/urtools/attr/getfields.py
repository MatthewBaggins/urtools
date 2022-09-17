from typing import List

def getfields(x: object) -> List[str]:
    """Get a list of all fields of the object."""
    return [f for f in dir(x) if f[0].islower()]
