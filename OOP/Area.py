import math


def get_area(radious):
    if radious < 0:
        raise ValueError
    area = math.pi * (radious ** 2)
    return area


def get_perimeter(self):
    perimeter = 2 * math.pi * self.radious ** 2
    return f"The perimeter is {perimeter : .2f}"

# @classmethod
# def blue_eye(cls):
#     pass
