from collections import Counter
from timeit import Timer
def word_count_dict(text: str) -> dict:
    d = {}
    for w in text.split():
        d[w] = d.get(w, 0) + 1
    return d
def word_count_counter(text: str) -> Counter:
    return Counter(text.split())
def compare(text: str):
    t1 = Timer(lambda: word_count_dict(text))
    n1, tot1 = t1.autorange()

    t2 = Timer(lambda: word_count_counter(text))
    n2, tot2 = t2.autorange()

    return (tot1 / n1, tot2 / n2)
def _test():
    text = "abc def abc qwert def " * 100
    assert word_count_dict(text) == word_count_counter(text)
    t_dict, t_cnt = compare(text)
    assert t_dict > 0 and t_cnt > 0
    print("task06: тесты пройдены")
if __name__ == "__main__":
    _test()
    text = "abc def abc qwert def " * 1000
    t_dict, t_cnt = compare(text)
    print(f"dict:    {t_dict * 1e6:8.2f} µs/call")
    print(f"Counter: {t_cnt * 1e6:8.2f} µs/call")
    print(f"Counter быстрее в {t_dict / t_cnt:.2f} раз")
