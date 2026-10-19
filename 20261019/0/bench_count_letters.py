from timeit import Timer
VOWELS = set("aeiou")
CONSONANTS = set("bcdfghjklmnpqrstvwxyz")
def count_letters_n(s: str):
    letters = set(s)
    return len(letters & VOWELS), len(letters & CONSONANTS)
def benchmark(s: str):
    t = Timer(lambda: count_letters_n(s))
    number, total = t.autorange()
    return number, total, total / number
def _test():
    assert count_letters_n("aabABbcD123") == (1, 2)
    assert count_letters_n("") == (0, 0)
    assert count_letters_n("aeiou") == (5, 0)
    n, tot, per = benchmark("aabABbcD123" * 100)
    assert n > 0 and tot > 0 and per > 0
    print("task03: тесты пройдены ✔")
if __name__ == "__main__":
    _test()
    s = "aabABbcD123" * 100
    n, tot, per = benchmark(s)
    print(f"строка длиной {len(s)}")
    print(f"number   = {n}")
    print(f"total    = {tot:.6f} s")
    print(f"per call = {per * 1e6:.3f} µs")
