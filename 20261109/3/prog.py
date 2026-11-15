class Maze:
	def __init__(s, n):
		s.n = n
		s.a = []
		for i in range(2 * n + 1):
			s.a.append(["█"] * (2 * n + 1))
		for y in range(n):
			for x in range(n):
				i = 2 * y + 1
				j = 2 * x + 1
				s.a[i][j] = "·"
	def __setitem__(s, k, v):
		x0, t, y1 = k
		y0 = t.start
		x1 = t.stop
		if x0 == x1:
			for y in range(min(y0, y1), max(y0, y1)):
				i = 2 * y + 2
				j = 2 * x0 + 1
				s.a[i][j] = v
		elif y0 == y1:
			for x in range(min(x0, x1), max(x0, x1)):
				i = 2 * y0 + 1
				j = 2 * x + 2
				s.a[i][j] = v
	def __getitem__(s, k):
		x0, t, y1 = k
		y0 = t.start
		x1 = t.stop
		q = [(x0, y0)]
		v = {(x0, y0)}
		while q:
			x, y = q.pop()
			if (x, y) == (x1, y1):
				return True
			for a, b in ((1, 0), (-1, 0), (0, 1), (0, -1)):
				i = x + a
				j = y + b
				if (i, j) in v:
					continue
				if i < 0 or i >= s.n:
					continue
				if j < 0 or j >= s.n:
					continue
				if s.a[y + j + 1][x + i + 1] == "·":
					v.add((i, j))
					q.append((i, j))
		return False
	def __str__(s):
		q = []
		for r in s.a:
			q.append("".join(r))
		return "\n".join(q)


import sys
exec(sys.stdin.read())
