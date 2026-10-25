s = input().lower()
p1 = []
for i in range(len(s) - 1):
	if s[i].isalpha() and s[i+1].isalpha():
		p1.append(s[i] + s[i+1])
p2 = []
for p in p1:
	if p not in p2:
		p2.append(p)
print(len(p2))
