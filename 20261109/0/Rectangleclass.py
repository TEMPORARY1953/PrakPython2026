class Rectangle:
	c = 0
	def __init__(self, x1, y1, x2, y2):
		self.x1, self.y1, self.x2, self.y2 = x1, y1, x2, y2
		Rectangle.c += 1
		setattr(self, f"rect_{Rectangle.c}", Rectangle.c)
	def __str__(self):
		return (f"({self.x1},{self.y1})({self.x1},{self.y2})"f"({self.x2},{self.y2})({self.x2},{self.y1})"f" c={Rectangle.c}")
	def _area(self):
		return (self.x2 - self.x1) * (self.y2 - self.y1)
	def __lt__(self, other):
		return self._area() < other._area()
	def __eq__(self, other):
		return self._area() == other._area()
	def __mul__(self, k):
		return Rectangle(self.x1*k, self.y1*k, self.x2*k, self.y2*k)
	def __rmul__(self, k):
		return self.__mul__(k)
	def __getitem__(self, i):
		pts = [(self.x1, self.y1), (self.x1, self.y2), (self.x2, self.y2), (self.x2, self.y1)]
		return pts[i]
	def __bool__(self):
		return self._area() != 0
	def __iter__(self):
		return iter([(self.x1, self.y1), (self.x1, self.y2), (self.x2, self.y2), (self.x2, self.y1)])
	def __del__(self):
		Rectangle.c -= 1
		print(f"del: c={Rectangle.c}")
