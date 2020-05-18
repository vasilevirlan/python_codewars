def digitize(number):
    """Convert number to reversed array of digits.
       Examples: 348597 => [7, 9, 5, 8, 4, 3]
    """
    my_list = list(map(int, str(number)))
    my_list.reverse()
    return my_list
