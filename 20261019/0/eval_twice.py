def eval_twice(expr: str, a, b):
    first = eval(expr, {}, {"x": a, "y": b})
    second = eval(expr, {}, {"x": b, "y": a})
    return first, second
def _test():
    assert eval_twice("x*2+y", 3, 4) == (10, 11)
    assert eval_twice("x+y", 1, 2) == (3, 3)
    assert eval_twice("x-y", 10, 3) == (7, -7)
    assert eval_twice("x*y", 2, 5) == (10, 10)
    print("task08: тесты пройдены ✔")
if __name__ == "__main__":
    _test()
    expr = input("Выражение: ")
    a, b = map(int, input("a, b: ").split(","))
    r1, r2 = eval_twice(expr, a, b)
    print(r1)
    print(r2)
