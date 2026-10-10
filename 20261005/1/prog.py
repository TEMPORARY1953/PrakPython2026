def Pareto(*d):
	res = []
	for p in d:
		dom = 0
		for q in d:
			if q[0] >= p[0] and q[1] >= p[1] and (q[0] > p[0] or q[1] > p[1]):
				dom = 1
				break
		if dom == 0:
			res.append(p)
	return tuple(res)
d = eval(input())
print(Pareto(*d))
