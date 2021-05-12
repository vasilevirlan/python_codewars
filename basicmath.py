def calculate(s):
    """
        In this kata, you will do addition and substraction on a given string.
        The return value must be also a string. Input will not be empty.
        Examples:
        >>> calculate('1plus2plus3plud4') == '10'
        True
        >>> calculate(1minus2minus3minus4') == '-8'
        True
    """
    if 'plus' in s or 'minus' in s:
        s = s.replace('plus', '+')
        s = s.replace('minus', '-')
        return str(eval(s))


if __name__=="__main__":
    print(calculate('1plus2plus3'))
    print(calculate('1plus2minus3'))
    print(calculate('10minus1minus1'))
    print(calculate('10minus1plus1'))
