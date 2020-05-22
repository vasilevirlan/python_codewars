import math as m
"""Complete the fucntion that calculate the area
        of hte red square (image available on codewars.com),
        when the length of circular arc A is given as the input.
        Return the result rounded by two decimals.
"""


def square_area(A):
    area_square = ((4 * A) / m.pi / 2) ** 2
    return round(area_square, 2)
