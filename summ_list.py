def sum_mix(arr):
    """Given an list of integers as string.
        Return a summ of all list value.
        Examples: sum_mix(['1', '1']) --> 2.
    """
    return sum(map(int, arr))
