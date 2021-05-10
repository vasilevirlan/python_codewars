
from maketriangular import triangular
def sum_triangular_numbers(n):
    """
        From codewars.com
        Trangular number sum with map() function.
         Triangular number are 1,3,6,10, 15.
        Triangular number are given by the folowing formula: (n*(n + 1))/2. See 
        details on wikipedia.THIS IMPLEMENTATION ARE MADE WITH map() function.
        >>> sum_triangular_numbers(6) == 56
        True
        >>> sum_triangular_numbers(34) == 7140
        True
        >>> sum_triangular_numbers(-1) == 0
        True
        >>> sum_triangular_numbers(0) == 0
        True
    """
    if n <= 0:
        return 0
    return sum(list(map(triangular, range(1, n + 1))))
