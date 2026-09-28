c = []
while (s := list(map(int, input().split()))):
	c.append(s)
for i in range(len(c[0])):
	for j in range(i + 1, len(c[0])):
		c[i][j], c[j][i] = c[j][i], c[i][j]
for i in range(len(c[0])):
	for j in range(len(c[0])):
		print(c[i][j], end=' ')
	print()
