from math import *


def res():
    x = 0.25
    y = (atan(3 / 4) + (4 / 3) * log(cos(atan(3 / 4)))) / (2 * pi)
    z = (atan(4 / 3) + (3 / 4) * log(cos(atan(4 / 3)))) / (2 * pi)
    print(y, z)
    return x + y + z


def res2():
    x = 0.5
    y = log(sin(2 * atan(3 / 4)) / 2) / (2 * pi)
    return x + y
