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


p1 = Point(2, 3)
print(p1)
print(p1.point_from_one())