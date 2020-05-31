def name_shuffler(string):
    """Write a function that returns a string in which
        firstname is swapped with last name.
        Examples:
        >>> name_shuffler('John McClane')
        'McClane John'
        >>> name_shuffler('Vasile Virlan')
        'Virlan Vasile'
        >>> name_shuffler('one two')
        'two one'
    """
    # First split the string into words
    words = string.split(' ')

    # Secoind reverse the split words
    reverse_string = ' '.join(reversed(words))

    return reverse_string
