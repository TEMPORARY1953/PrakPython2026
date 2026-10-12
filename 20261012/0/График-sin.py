import math
def scale(a, b, A, B, x):
    return A + (B - A) * (x - a) / (b - a)
W = int(input())
H = int(input())
A = float(input())
B = float(input())
for i in range(H):
    x = scale(0, H - 1, A, B, i)
    y = math.sin(x)
    col = round(scale(-1, 1, 0, W - 1, y))
    print(" " * col + "*")
