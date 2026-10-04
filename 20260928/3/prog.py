c1 = []
c1.append(list(map(int, input().split(','))))
l = len(c1[0])
for i in range(l - 1):
	c1.append(list(map(int, input().split(','))))
c2 = []
for i in range(l):
	c2.append(list(map(int, input().split(','))))
c3 = []
for i in range(l):
	c3.append([0] * l)
for i in range(l):
	for j in range(l):
		for k in range(l):
			c3[i][j] += c1[i][k] * c2[k][j]
for i in range(l):
	print(','.join(map(str, c3[i])))
