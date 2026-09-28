lst = list(map(int, input().split()))
c = 0
for i in lst:
	if i % 2 == 1:
		print(i)
		c = 1
		break
if c == 0:
	print(0)
