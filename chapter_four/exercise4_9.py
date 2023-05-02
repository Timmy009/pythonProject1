import math


def radiant (degrees):
    rad = round(degrees * math.pi / 180, 2)
    return rad

print("\t\tDegrees\tRadiant")
for degrees in range(1, 181):
    print(f"{degrees: >10} {radiant(degrees) :>10}")
