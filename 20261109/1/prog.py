class Omnibus:
	_c = {}
	def __init__(s):
		s._a = set()
	def __getattr__(s, n):
		if n in s._a:
			return Omnibus._c[n]
		raise AttributeError(n)
	def __setattr__(s, n, v):
		if n[0] == "_":
			s.__dict__[n] = v
		elif n not in s._a:
			s._a.add(n)
			if n not in Omnibus._c:
				Omnibus._c[n] = 0
			Omnibus._c[n] += 1
	def __delattr__(s, n):
		if n[0] == "_":
			del s.__dict__[n]
		elif n in s._a:
			s._a.remove(n)
			Omnibus._c[n] -= 1

import sys
exec(sys.stdin.read())
