n = list(map(int, input().split(',')))
for i in range(len(n) - 1):
	sw = False
	for j in range(len(n) - i - 1):
		if (n[j + 1] ** 2) % 100 < (n[j] ** 2) % 100:
			n[j + 1], n[j] = n[j], n[j + 1]
			sw = True
	if not sw:
		break
print(n)
