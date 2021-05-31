from functools import reduce
def odd_or_even(arr):
    """
        Given a list of integers, determine whether the sum of lists elements 
        is odd or  even.
        Give your answer as  a string matching "odd" or "even".
        Examples:
        >>> odd_or_even([0]) == 'even'
        True
        >>> odd_or_even([0, 1, 4]) == 'odd'
        True
        >>> odd_or_even([0, 1, 5]) == 'even'
        True
    """
    return 'even' if reduce(lambda a, b: a+b, arr) % 2 == 0 else 'odd'

