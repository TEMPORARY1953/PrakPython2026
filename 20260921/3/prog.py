n = int(input())
i = n
while i <= n + 2:
	j = n
	k = 0
	while j <= n + 2:
		k += 1
		if k < 2:
			s = 0
			t = i * j
			while t > 0:
				s += t % 10
				t //= 10
			if s == 6:
				print(i, "*", j, "=", ":=)", end=" ")
			else:
				print(i, "*", j, "=", i * j, end=" ")
		else:
			s = 0
			t = i * j
			while t > 0:
				s += t % 10
				t //= 10
			if s == 6:
				print(i, "*", j, "=", ":=)")
			else:
				print(i, "*", j, "=", i * j)
		j += 1
	i += 1
	
