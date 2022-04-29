def is_narcissistic(i):
    """
    A Narcissistic Number is a number of length n in which the sum of its
    digits to the power of n is equal to the original number. If this seems
    confusing,
    refer to the example below.

    Ex: 153 where n = 3 (number of digits in 153)
    13 + 53 + 33 = 153

    >>> is_narcissistic(153)
    True
    >>>	is_narcissistic(201)
    False
    >>>	is_narcissistic(259)
    False
    >>>	is_narcissistic(371)
    True
    >>>	is_narcissistic(407)
    True
    >>>	is_narcissistic(595)
    False
    >>>	is_narcissistic(825)
    False
    >>>	is_narcissistic(1634)
    True
    """
    if i == sum([int(x)**len(str(i)) for x in str(i).strip(' ')]):
        return True
    return False


if __name__ == "__main__":
    from doctest import testfile as tf
    tf('nt.txt', verbose=True)
