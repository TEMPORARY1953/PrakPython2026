from math import *
def Calc(s, t, u):
	def F(x):
		return eval(u, globals(), {"x": eval(s, globals(), {"x": x}), "y": eval(t, globals(), {"x": x})})
	return F
s = eval(input())
x = eval(input())
F = Calc(*s)
print(F(x))
