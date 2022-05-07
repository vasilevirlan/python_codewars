def letter_order(l1: str, l2: str, l3: str, step=1) -> bool:
    """
    Create a function that will verify if the letters are consecutive.
    Thestep parameter will allow to change the step of consecutivness.
    Where touse this boylshit.
    >>> letter_order('a', 'b', 'c')
    True
    >>> letter_order('a', 'c', 'b')
    False
    """

    if ord(l1) + step == ord(l2) and ord(l2) + step == ord(l3):
        return True

    return False


if __name__ == "__main__":
    from doctest import testmod as tm
    tm(verbose=True)
