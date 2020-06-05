def find_longest(string):
    """ Returns length of the longest word in a list.
        >>> find_longest('two words')
        5
        >>> find_longest('Sausage chops')
        7
    """
    return max([len(iter) for iter in string.split(" ")])
