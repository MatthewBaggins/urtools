from __future__ import annotations

import pandas as pd

from urtools.pandas.find_duplicates import find_duplicates

def count_duplicates(df: pd.DataFrame, subset: str | list[str] | None = None) -> int:
    """Count the number of duplicates in the `DataFrame`.
    """
    return len(find_duplicates(df, subset))
