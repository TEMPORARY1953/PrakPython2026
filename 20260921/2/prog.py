summ = 0
while (x := int(input())) > 0:
	summ += x
	if summ > 21:
		print(summ)
		break
else:
	print(x)
