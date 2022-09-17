from __future__ import annotations

import pandas as pd

from urtools.dict.dict_nans import filter_dict_nans

def df_to_jsonlist(df: pd.DataFrame) -> list[dict]:
    """Convert a `DataFrame` into a list of rows as dicts.
    """
    return [filter_dict_nans(record) for record in df.to_dict(orient='records')]
