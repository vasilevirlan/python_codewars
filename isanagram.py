def is_anagram(test, original):
    """ Test if is  anagram of original.
    """

    if sorted(test.lower()) == sorted(original.lower()):
        return True
    return False
