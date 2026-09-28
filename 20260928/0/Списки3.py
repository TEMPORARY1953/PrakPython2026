lst = list(map(int, input().split()))
s = lst[len(lst)//2:]
res = s[1::2][::-1]
print(res)
