a = int(input())
b = int(input())
res = [n for n in range(a, b + 1) if n % 2 != 0 and '3' not in str(n)]
print(res)
