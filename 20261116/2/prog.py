class InvalidInput(Exception):
	pass

class BadTriangle(Exception):
	pass

def triangleSquare(inStr):
	try:
		(x1, y1), (x2, y2), (x3, y3) = eval(inStr)
	except Exception:
		raise InvalidInput
	try:
		a = (x2 - x1) * (y3 - y1)
		b = (x3 - x1) * (y2 - y1)
		s = a - b
		if s < 0:
			s = -s
		s = s / 2
		if not (0 < s < float("inf")):
			raise BadTriangle
	except Exception:
		raise BadTriangle
	return s

while True:
	s = input()
	try:
		area = triangleSquare(s)
	except InvalidInput:
		print("Invalid input")
	except BadTriangle:
		print("Not a triangle")
	else:
		print(f"{area:.2f}")
		break
