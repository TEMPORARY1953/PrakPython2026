c = []
q = -1
w = 0
while (s := list(map(int, input().split()))):
	if q > 0 and q != len(s):
		print("Разное число элементов в строках")
		exit(404)
	else:
		q = len(s)
		c.append(s)
		w += 1
if w != len(c[0]):
	exit("Матрица не квадратная")
for i in range(len(c[0])):
	for j in range(i + 1, len(c[0])):
		c[i][j], c[j][i] = c[j][i], c[i][j]
for i in range(len(c[0])):
	for j in range(len(c[0])):
		print(c[i][j], end=' ')
	print()
