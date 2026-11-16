while True:
	try:
		n = int(input("> "))
	except ValueError:
		print("Это не целое число")
	else:
		print("Спс!");
		break
