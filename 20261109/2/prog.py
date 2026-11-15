class Triangle:
	def __init__(s, a, b, c):
		s.p = (tuple(a), tuple(b), tuple(c))
	def __abs__(s):
		a, b, c = s.p
		q1 = (b[0] - a[0]) * (c[1] - a[1])
		q2 = (b[1] - a[1]) * (c[0] - a[0])
		qq = q1 - q2
		if qq == 0:
			return 0
		return abs(qq)/2
	def __bool__(s):
		if abs(s) != 0:
			return True
		else:
			return False
	def __lt__(s, t):
		if abs(s) < abs(t):
			return True
		else:
			return False
	def __contains__(s, t):
		if not t:
			return True
		if not s:
			return False
		for x, y in t.p:
			z = []
			for i in range(1, 4):
				a = s.p[i - 1]
				b = s.p[i % 3]
				q1 = (b[0] - a[0]) * (y - a[1])
				q2 = (b[1] - a[1]) * (x - a[0])
				qq = q1 - q2
				z.append(qq)
			if min(z) < 0 and max(z) > 0:
				return False
		return True
	def __and__(s, t):
		if not s:
			return False
		if not t:
			return False
		for u in (s, t):
			for i in range(1, 4):
				a = u.p[i - 1]
				b = u.p[i % 3]
				x = a[1] - b[1]
				y = b[0] - a[0]
				p = []
				q = []
				for k, j in s.p:
					p.append(x * k + y * j)
				for k, j in t.p:
					q.append(x * k + y * j)
				if max(p) < min(q):
					return False
				if max(q) < min(p):
					return False
		return True

import sys
exec(sys.stdin.read())
