def istype(typ):
    def decorator(fun):
        def newfun(*args, **kwargs):
            for arg in args:
                if not isinstance(arg, typ):
                    raise TypeError(f"Аргумент {arg!r} не является {typ.__name__}")
            for v in kwargs.values():
                if not isinstance(v, typ):
                    raise TypeError(f"Аргумент {v!r} не является {typ.__name__}")
            return fun(*args, **kwargs)
        return newfun
    return decorator

@istype(int)
def simplefun(N, m=1):
    return N * 2 + m

print(simplefun(2, 3))
print(simplefun(9, 18))
print(simplefun(90, 180))
print(simplefun(-5, 1))
print(simplefun(6, 7))
print(simplefun(9, 99))
print(simplefun(8, 90))










