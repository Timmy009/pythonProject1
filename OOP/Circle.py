import math


class Circle:
    def __init__(self, radious):
        self.radious = radious

    def get_area(self):
        area = math.pi * (self.radious ** 2)
        return f"The area is {area : .2f}"

    def get_perimeter(self):
        perimeter = 2 * math.pi * self.radious ** 2
        return f"The perimeter is {perimeter : .2f}"

    @classmethod
    def blue_eye(cls):
        pass



calculate = Circle(7)
print(calculate.get_perimeter())
print(calculate.get_area())
