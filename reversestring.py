def reverse_string(s: str):
    """I found this on w3school site.
        >>> reverse_string('reverse') == 'esrever'
        True
        >>> reverse_string('Hello') == 'olleH'
        True
    """
    return s[::-1]

if __name__ == '__main__':
    import doctest
    doctest.testmod()
