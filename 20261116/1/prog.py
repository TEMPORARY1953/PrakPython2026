import collections

class DivStr(collections.UserString):
	def __init__(self, s=""):
		super().__init__(s)
	def __mod__(self, n):
		k = len(self.data) // n
		a = n * k
		return DivStr(self.data[a:])
	def __floordiv__(self, n):
		k = len(self.data) // n
		res = []
		for i in range(n):
			a = i * k
			b = (i + 1) * k
			res.append(DivStr(self.data[a:b]))
		return iter(res)

import sys
exec(sys.stdin.read())
