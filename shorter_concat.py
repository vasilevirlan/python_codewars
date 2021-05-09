from reversestring import reverse_string

def shorter_reverse_longer(a: str, b: str) -> str:
    """
        From codewars  7kyu kata. Given 2 strings a, b. return the string of the
        form: shorte + reverse(longer) + shorter. If a and b are equal, treat
        a as the longer producing b+reverse(a)+b.
        examples:
        >>> shorter_reverse_longer('first', 'abcde') == 'abcdetsrifabcde'
        True
        >>> shorter_reverse_longer('abc', 'four') == 'abcruofabc'
        True
        >>> shorter_reverse_longer('four', 'one') == 'oneruofone'
        True
    """
    if len(a) >= len(b):
        return b + reverse_string(a) + b
    return a + reverse_string(b) + a

if __name__ == "__main__":
    import doctest
    doctest.testmod()
