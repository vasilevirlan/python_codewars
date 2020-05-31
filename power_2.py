def powers_of_two(number):
    """This function takes non-negative integer n as input
        and returns a list of all the powers of 2 with the
        exponent ranging from 0 to n in clusive.
        Examples:
        >>> powers_of_two(0)
        [1]
        >>> powers_of_two(1)
        [1, 2]
        >>> powers_of_two(2)
        [1, 2, 4]
        >>> powers_of_two(4)
        [1, 2, 4, 8, 16]
    """
    return [2 ** x for x in range(number + 1)]
