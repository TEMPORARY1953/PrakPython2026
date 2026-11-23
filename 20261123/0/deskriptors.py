class Counter:
    def __init__(self):
        self.value = 0
    def __get__(self, obj, objtype=None):
        return self.value
    def __set__(self, obj, value):
        self.value = value
    def __delete__(self, obj):
        self.value = 0

class C:
    counter = Counter()
    def __init__(self):
        self.counter += 1
    def __del__(self):
        self.counter -= 1

c = C()
print(c.counter)
d = C()
print(d.counter)
del c
print(d.counter)
