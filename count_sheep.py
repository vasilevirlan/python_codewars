def count_sheep(number):
    """Given a non-negative integer 3 for example, return a string with
        murmus: 1 sheep ...2 sheep...3 sheep... .
        >>> number = 3
        >>> count_sheep(number)
        '1 sheep...2 sheep... 3 sheep...
    """
    return ''.join([str(i) + ' sheep...' for i in range(1, number + 1)])
