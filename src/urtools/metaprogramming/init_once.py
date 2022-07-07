def init_once(var_name: str, init_code: str) -> object:
    if var_name not in globals():
        code = f'globals()["{var_name}"] = {init_code}'
        exec(code)
    assert var_name in globals()
    return globals()[var_name]
