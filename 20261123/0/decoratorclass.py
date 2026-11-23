class istype:
    def __init__(self, typ):
        self.typ = typ
    def __call__(self, function):
        typ = self.typ
        def newfun(*args, **kwargs):
            for arg in args:
                if not isinstance(arg, typ):
                    raise TypeError(f"Аргумент {arg!r} не является {typ.__name__}")
            for v in kwargs.values():
                if not isinstance(v, typ):
                    raise TypeError(f"Аргумент {v!r} не является {typ.__name__}")
            return function(*args, **kwargs)
        return newfun

@istype(int)
def fun(a, b):
    return a + b

print(fun(1, 2))
