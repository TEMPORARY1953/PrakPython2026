import math
def scale(a, b, A, B, x):
    return A + (B - A) * (x - a) / (b - a)
W = 60
H = 20
screen = [[' '] * W for _ in range(H)]
for col in range(W):
    x = scale(0, W - 1, 0, 7, col)
    y = math.sin(x)
    row = round(scale(-1, 1, H - 1, 0, y))
    screen[row][col] = '*'
for line in screen:
    print("".join(line))
