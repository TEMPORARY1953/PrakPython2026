def MINF(*funcs):
	return lambda x: min(f(x) for f in funcs)
g = MINF(lambda x: x + 1, lambda x: x * 2, lambda x: 10 - x)
print(g(3))
print(g(0))
