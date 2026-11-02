from itertools import product
a = (x + y for x, y in product('abcdefgh', '12345678'))
print(*a)