from collections import Counter
def can_make_note(article: str, note: str) -> bool:
    return (Counter(note.split()) - Counter(article.split())) == Counter()
def missing_words(article: str, note: str) -> dict:
    return dict(Counter(note.split()) - Counter(article.split()))
def _test():
    assert can_make_note("abc def abc qwert def", "abc def") is True
    assert can_make_note("abc def", "abc abc") is False
    assert can_make_note("a b c", "a b c") is True
    assert can_make_note("", "") is True
    assert can_make_note("", "a") is False
    assert can_make_note("a b", "a b c") is False
    assert missing_words("a b", "a a b") == {"a": 1}
    print("task09: тесты пройдены ✔")
if __name__ == "__main__":
    _test()
    article = input("Статья: ")
    note = input("Записка: ")
    if can_make_note(article, note):
        print("Можно сделать записку")
    else:
        print("Нельзя, не хватает:", missing_words(article, note))
