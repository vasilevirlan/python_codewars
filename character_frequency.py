def char_freq(line: str):
    """return a dictionary with a keys as character and
        as a value frequency of a character.
        Example:
        >>> char_freq('myy string')
        {'m': 1, 'y': 2, 's': 1, 't': 1, 'r': 1,'i': 1, 'n': 1, 'g': 1}
    """
    my_dictionary = {}  # Create a new dictionary

    for i in line:
        my_dictionary[i] = my_dictionary.get(i, 0) + 1
    return my_dictionary
