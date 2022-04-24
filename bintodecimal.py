"""
Complete the function which converts a binary number given as a string to a
decima number.
Examples:
>>> bin_to_decimal('0')
0
>>> bin_to_decimal('1')
1
>>> bin_to_decimal('1010')
10
>>> bin_to_decimal('1001001')
73

"""
bin_to_decimal = lambda i: int(i, base=2)


if __name__ == "__main__":
    import doctest as dt
    dt.testmod(verbose=True)
