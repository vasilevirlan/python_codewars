def small_enough(array, limit):
    """
        From codewars.com 7kyu kata
        You will be given an array and a limit value. You must check if all 
        value in the array are below or equal to the limit value.
        If the y are return True, else False.
        Here are some examples:
        >>> small_enough([1, 2, 3, 4], 5) == True
        True
        >>> small_enough([1, 22, 333, 4444, 4], 5) == False
        True
        >>> small_enough([1, 2, 3, 400], 5) == False
        True
        >>> small_enough([1, 2, 3, 2.3], 5) == True
        True
    """
    return True if all([num <= limit for num in array]) else False

if __name__ == "__main__":
    print(small_enough([1, 2, 3, 4], 5))
    print(small_enough([1, 2, 3, 4, 5, 6, 7], 5))
    print(small_enough([1, 2, 3, 400], 5))
    print(small_enough([1, 2, 3, 4], 5))
