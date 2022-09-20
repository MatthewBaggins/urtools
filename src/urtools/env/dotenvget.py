import os

from dotenv import load_dotenv

def dotenvget(name: str) -> str:
    """Load `.env` and return the value of the given variable.
    """
    load_dotenv()
    val = os.getenv(name)
    if val is None:
        raise ValueError(f'{name} is not set. Set it in the `.env` file.')
    return val
