class A:
	pass
class B:
	pass
class C(A, B):
	pass
class D(B, A):
	pass
ok = 0
for other in (A, B, C, D):
	for order in ((C, other), (other, C)):
		try:
			type('E', order, {}); ok += 1
		except TypeError:
			pass
print(ok)
