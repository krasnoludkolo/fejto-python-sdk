def for_all_methods(decorator):
    def decorate(cls):
        for attr in cls.__dict__:
            if callable(getattr(cls, attr)):
                setattr(cls, attr, decorator(getattr(cls, attr)))
        return cls
    return decorate


def return_raw_value(fn):
    def return_raw(*args, **kwargs):
        response = fn(*args, **kwargs)
        if 'raw' in kwargs.keys() and kwargs['raw']:
            return response
        if response and "_embedded" in response:
            return response["_embedded"]["items"]
        return response

    return return_raw
