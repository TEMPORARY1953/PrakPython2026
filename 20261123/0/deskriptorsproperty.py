class C:
    def __init__(self, age=0):
        self.age = age
    @property
    def age(self):
        if self._age == 42:
            print("secret value!")
            return -1
        return self._age
    @age.setter
    def age(self, value):
        if value > 128:
            print("too old!")
            raise ValueError("too old!")
        self._age = value

c = C(30)
print(c.age)
c.age = 42
print(c.age)
try:
    c.age = 200
except ValueError as e:
    print("Ошибка:", e)
