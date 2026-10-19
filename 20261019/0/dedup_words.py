def dedup_words(text: str) -> str:
    return " ".join(dict.fromkeys(text.split()))
def _test():
    assert dedup_words("abc def abc qwert def") == "abc def qwert"
    assert dedup_words("") == ""
    assert dedup_words("a a a a") == "a"
    assert dedup_words("b a b a c") == "b a c"
    assert dedup_words("x") == "x"
    print("task07: тесты пройдены")
if __name__ == "__main__":
    _test()
    text = input("Текст: ")
    print(dedup_words(text))
