def walk2d():
    x = 0
    y = 0
    while 1:
        dx, dy = yield x, y
        x += dx 
        y += dy

it = walk2d()
print(it.send(None))
print(it.send((1, 2)))
print(it.send((2, -3)))