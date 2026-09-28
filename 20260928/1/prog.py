M, N = map(int, input().split(', '))
print([x for x in range(M, N) if x > 1 and all(x % j for j in range(2, x))])
