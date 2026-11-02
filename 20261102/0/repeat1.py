from itertools import repeat
def repeater(seq, n):
    for x in seq:
        yield from repeat(x, n)
print(*repeater([1, 2, 3], 8))