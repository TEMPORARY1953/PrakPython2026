def word_count_dict(text: str) -> dict:
    d = {}
    for w in text.split():
        d[w] = d.get(w, 0) + 1
    return d
def _test():
    assert word_count_dict("abc def abc qwert def abc") == {
        "abc": 3, "def": 2, "qwert": 1
    }
    assert word_count_dict("") == {}
    assert word_count_dict("a a a") == {"a": 3}
    assert word_count_dict("x y z") == {"x": 1, "y": 1, "z": 1}
    print("task04: тесты пройдены ✔")
if __name__ == "__main__":
    _test()
    text = input("Текст: ")
    print(word_count_dict(text))
