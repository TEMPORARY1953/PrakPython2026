a = int(input())
if not a % 50:
	print("A + ", end="")
else: 
	print("A - ", end="")
if not a % 25 and a % 2:
	print("B + ", end="")
else: 
	print("B - ", end="")
if not a % 8:
	print("C + ", end="")
else: 
	print("C - ")
