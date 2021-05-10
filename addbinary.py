import math as m
def addbinary(n1: int, n2: int) -> str:
    """
        Implements a function that add two number together and returns their 
        in binary. The returned binary nuber should be a string.
        Examples:
        >>> addbinary(1, 1) == '10'
        True
        >>> addbinary(1, 2) == '11'
        True
    """
    return bin(n1 + n2)[2::]

if __name__ == "__main__":
