def Sb(a, b):
	if isinstance(a, (tuple, list)) and isinstance(b, (tuple, list)):
		res = []
		for x in a:
			if x not in b:
				res.append(x)
		return type(a)(res)
	return a - b

args = eval(input())
print(Sb(*args))
