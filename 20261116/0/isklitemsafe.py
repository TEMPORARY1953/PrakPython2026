def itemget(c, i):
	return c[i]
def safeindex(f, *a):
	try:
		return f(*a)
	except IndexError:
		return None

list(safeindex(itemget, "qwe", i) for i in range(5))
safeindex(itemget, "qwe", "qwe")
