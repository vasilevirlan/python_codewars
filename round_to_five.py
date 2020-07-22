def round_to_five(number):
    """ Given an integer as input, can you round it to the next(meaning,
        "highter")5?
        >>> round_to_five(0)
        0
        >>> round_to_five(2)
        5
        >>> round_to_five(12)
        15
        >>> round_to_five(3)
        5
        >>> round_to_five(21)
        25
        >>> round_to_five(30)
        30
        >>> round_to_five(-2)
        0
        >>> round_to_five(-5)
        -5
    """
    return number + (5 - number) % 5
