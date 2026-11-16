class A:
	def __init__(self): 
		self.a = 1
class B(A):
	def __init__(self):
		super().__init__()
		self.b = 2
b = B()
print(b.a, b.b)
print(isinstance(b, A))
