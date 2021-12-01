def recursively_build_json(val):
    if isinstance(val, list):
        new_val = [recursively_build_json(item) for item in val]
    elif type(val) is dict:
        new_val = {key:recursively_build_json(value) for (key,value) in val.items()}
    elif hasattr(val, '_asdict'):
        new_val = {key:recursively_build_json(value) for (key,value) in val._asdict().items()}
    else:
        new_val = val
    return new_val