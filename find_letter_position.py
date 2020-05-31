def position(letter: str) -> str:
    """this function will return the position pf letter in alphabet.
        >>> position('a')
        'Position of alphabet: 1'
        >>> position('z')
        'Position of alphabet: 26'
        >>> position('e')
        'Position of alphabet: 5'
    """
    return'{} {}'.format('Position of alphabet:', ord(letter) - 96)
print(type(position('a')))
