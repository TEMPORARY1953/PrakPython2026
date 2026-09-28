n = list(range(5, 16))
l = [chr(c) for c in range(ord('a'), ord('k') + 1)]
n[3:7] = l[-5:]
print(n)
