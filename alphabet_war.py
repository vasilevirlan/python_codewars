def alphabet_war(fight: str) -> str:
    """
    There is  a war and nobody knows- the alphabet war.
    Write a funcion that accepts a string consists of only small letters and
    returns who wins the fight. There is two sides left and right. The letter
    from that sides has power, the other letter has no power.
    In one word sum the values of letters from those two dictionaries.
        >>> alphabet_war('z')
        'Right side wins!'
        >>> alphabet_war('zdqmwpbs')
        "Let\'s fight again!"
        >>> alphabet_war('wq')
        'Left side wins!'
    """
    left_side = dict(zip(['w', 'p', 'b', 's'], [4, 3, 2, 1]))
    right_side = dict(zip(['m', 'q', 'd', 'z'], [4, 3, 2, 1]))
    remain_letters = ['a', 'c', 'e', 'f', 'g', 'h', 'i', 'l',
                      'n', 'o', 'r', 't', 'u', 'v', 'x', 'y']
    lefsidescore = []
    rightsidescore = []

    for i in fight:
        if i in left_side and i not in remain_letters:
            lefsidescore.append(left_side[i])
        elif i in right_side and i not in remain_letters:
            rightsidescore.append(right_side[i])

    if sum(lefsidescore) > sum(rightsidescore):
        return 'Left side wins!'

    elif sum(lefsidescore) < sum(rightsidescore):
        return 'Right side wins!'

    else:
        return "Let's fight again!"


if __name__ == "__main__":
    from doctest import testmod as tm
    tm(verbose=True)
