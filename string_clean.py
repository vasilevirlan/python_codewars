def string_clean(string):
    """Function will return clean string without digits.
    """
    return ''.join([digit for digit in string if not digit.isdigit()])
print(string_clean('1vasile4sal5u8t'))
