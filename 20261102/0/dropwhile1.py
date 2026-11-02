from itertools import dropwhile, islice

def summm():
    s = 0
    n = 1
    while 1:
        s += 1 / (n**2)
        yield s
        n += 1
gener = summm()
a = dropwhile(lambda x: x <= 1.6, gener)
b = islice(a, 10)
for i in b:
    print(i)
