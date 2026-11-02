def summm():
    s = 0
    n = 1
    while 1:
        s += 1 / (n**2)
        yield s
        n += 1
gener = summm()
for i in range(228):
    print(next(gener))