from itertools import filterfalse

n = int(input())
a = filterfalse(lambda x: x % n, range(1, 1000))
print(*a)
