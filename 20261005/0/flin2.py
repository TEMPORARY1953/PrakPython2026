def make_linear(a, b):
	def f(x):
		return a * x + b
	return f
line = make_linear(2, 3)
print(line(10))
