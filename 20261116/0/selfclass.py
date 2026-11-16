class Vector:
    def __init__(self, x, y):
        self.x, self.y = x, y
    def __add__(self, o):
        return self.__class__(self.x + o.x, self.y + o.y)
    def __repr__(self):
        return f"{type(self).__name__}({self.x}, {self.y})"
class Vector3(Vector):
    def __init__(self, x, y, z=0):
        super().__init__(x, y)
        self.z = z
    def __add__(self, o):
        return self.__class__(self.x + o.x, self.y + o.y, self.z + o.z)
print(Vector(1, 2) + Vector(3, 4))
print(Vector3(1, 2, 3) + Vector3(4, 5, 6))
