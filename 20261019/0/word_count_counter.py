from collections import Counter
def word_count_counter(text: str) -> Counter:
    return Counter(text.split())
def _test():
    assert word_count_counter("abc def abc qwert def abc") == Counter(
        {"abc": 3, "def": 2, "qwert": 1}
    )
    assert word_count_counter("") == Counter()
    assert word_count_counter("a a a") == Counter({"a": 3})
    # сверка с dict-версией
    from task04_word_count_dict import word_count_dict
    txt = "one two two three three three"
    assert word_count_counter(txt) == word_count_dict(txt)
    print("task05: тесты пройдены ✔")
if __name__ == "__main__":
    _test()
    text = input("Текст: ")
    print(word_count_counter(text))
