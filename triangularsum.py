def sum_triangular_numbers(n):
    """
        From codewars.com
        Your task is to return the sum of Triangular Number up-to-and-including
        the Nth Triangular number. Triangular number are 1,3,6,10, 15. 
        Triangular number are given by the folowing formula: (n*(n + 1))/2. See 
        details on wikipedia.
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
    return sum([(i*(i + 1))// 2 for i in range(1, n + 1)])
