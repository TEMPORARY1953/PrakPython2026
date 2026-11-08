def fib(m, n):
	a = 1
	b = 1
	i = 0
	while 1:
		if i >= m and i < m + n:
			yield a
		elif i >= m + n:
			return
		t = a
		a = b
		b = t + b
		i += 1

import sys
exec(sys.stdin.read())
