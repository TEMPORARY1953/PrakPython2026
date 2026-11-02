def travel(n):
    for i in range(n):
        yield 'по кочкам'
    return 'и в яму'
def travelwrap(n):
    res = yield from travel(n)
    yield res

n = int(input())
it = travelwrap(n)
for i in range(n + 1):
    print(next(it))