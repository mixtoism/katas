from collections import OrderedDict

__cache__ = {}


def cache(function, *args, **kwargs):
    kwargs_dict = OrderedDict(sorted(kwargs.items(), key=lambda x: x[0]))
    hash_str = "".join([f"{kw}={arg}:{type(arg)}" for kw, arg in kwargs_dict.items()])
    key = (*args, hash_str)

    if result := __cache__.get(key):
        return result

    result = function(*args, **kwargs)
    __cache__[key] = result
    return result
