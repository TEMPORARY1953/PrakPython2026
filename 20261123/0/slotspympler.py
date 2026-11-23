from pympler import asizeof
from string import ascii_letters

class Trad:
    def __init__(self):
        for attr in ascii_letters:
            setattr(self, attr, attr)

class Slotter:
    __slots__ = tuple(ascii_letters)
    def __init__(self):
        for attr in ascii_letters:
            setattr(self, attr, attr)

lst_trad = [Trad() for _ in range(1000)]
lst_slot = [Slotter() for _ in range(1000)]
print("1000 Trad:   ", asizeof.asizeof(lst_trad))
print("1000 Slotter:", asizeof.asizeof(lst_slot))
