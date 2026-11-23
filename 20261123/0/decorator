def dumper(f):
    def newfun(*args):
        for arg in args:
            if not isinstance(arg, int):
                raise TypeError(f"Аргумент {arg!r} не является int")
        return f(*args)
    return newfun
def fun(a,b):
    return a*2+b
print(fun(2,3))
