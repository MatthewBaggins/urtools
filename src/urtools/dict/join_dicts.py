def join_dicts(*dicts: dict) -> dict:
    """Join dictionaries into one"""
    joined = {}
    for d in dicts:
        joined.update(d)
    return joined
