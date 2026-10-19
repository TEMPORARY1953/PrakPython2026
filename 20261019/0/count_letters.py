VOWELS = set("aeiou")
CONSONANTS = set("bcdfghjklmnpqrstvwxyz")
def count_letters(s: str):
    letters = set(s)
    return letters & VOWELS, letters & CONSONANTS
def _test():
    v, c = count_letters("aabABbcD123")
    assert v == {"a"}, v
    assert c == {"b", "c"}, c
    assert count_letters("") == (set(), set())
    assert count_letters("AEIOU") == (set(), set())     # заглавные не считаем
    assert count_letters("aeiou") == (set("aeiou"), set())
    assert count_letters("bcdfg") == (set(), set("bcdfg"))
    print("task02: тесты пройдены ✔")
if __name__ == "__main__":
    _test()
    s = input("Строка: ")
    v, c = count_letters(s)
    print(f"гласных: {len(v)} {v}")
    print(f"согласных: {len(c)} {c}")
