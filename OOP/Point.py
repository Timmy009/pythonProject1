class Point:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def draw(self):
        print("drawing...")

    def __str__(self):
        return f"({self.a}, {self.b})"

    @classmethod
    def point_from_one(cls):
        return cls(1, 1)

    def __eq__(self, other):
        return self.a == other.a and self.b == other.b

    def __lt__(self, other):
        return self.a < other.a and self.b < other.b


p1 = Point(2, 3)
print(p1)
print(p1.point_from_one())
p4 = Point(1, 3)
p8 = Point(6, 6)
print(p4 < p8)
