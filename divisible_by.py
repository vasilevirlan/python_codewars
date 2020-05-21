def divisible_by(numbers, divisor):
    """This function will return all number from numbers which is a list
        that are divisible by divisor.
        Examples:
        divisible_by([1, 2, 3, 4, 5, 6], 2) ==> [2, 4, 6]
    """
    return [x for x in numbers if x % divisor == 0]


