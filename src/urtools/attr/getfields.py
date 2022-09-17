from __future__ import annotations

def getfields(x: object) -> list[str]:
    """Get a list of all fields of the object."""
    return [f for f in dir(x) if f[0].islower()]
