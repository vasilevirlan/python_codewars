def largest_pair_sum(numbers: list)->int:
    """
        Gven a seuence of numbers, find the larest pair sum in the sequence.
        Examples:
        >>> largest_pair_sum([11, 2, 3, 5]) == 16
        True
        >>> largest_pair_sum([1, 2, 34, 6]) == 40
        True
    """
    numbers = sorted(numbers)
    return numbers.pop() + numbers.pop()
