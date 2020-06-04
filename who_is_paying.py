def who_is_paying(name):
    """This function will return a list that contains
        name and first two letters from name.
        Examples:
        >>> who_is_paying('Vasile')
        ['Vasile', 'Va']
        >>> who_is_paying('Va')
        ['Va']
        >>> who_is_paying('')
        ['']
    """
    my_list = list(name.split(" "))
    if len(name) <= 2:
        return my_list
        return list(''.split(''))
    else:
        return my_list + list((name[0] + name[1]).split( ))
