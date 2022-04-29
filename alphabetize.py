def alphabetize(s):
    """Re-order the characters of a string, so that they are concatenated into
    a new string in "case-insensitively-alphabetical-order-of-appearance"
    order. Whitespace and punctuation shall simply be removed!

    The input is restricted to contain no numerals and only words containing
    the
    english alphabet letters.

    Example:
    >>> alphabetize("The Holy Bible")
    'BbeehHilloTy'

    """
    if s != s.isalpha():
        ms = ''.join(filter(str.isalnum, s))
        return ''.join(sorted(ms, key=str.lower)).lstrip()
    return ("".join(sorted(s, key=str.lower))).lstrip()


if __name__ == "__main__":
    from doctest import testmod as tm
    tm(verbose=True)
