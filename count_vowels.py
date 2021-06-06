def count_vowels(input_string: str) -> int:
    """
        >>> count_vowels('mama') == 2
        True
        >>> count_vowels('vowels') == 2
        True
        >>> count_vowels('vvv') == 0
        True
    """
    vowels = 'aeiou'
    return len([i for i in input_string if i in vowels])

if __name__ == "__main__":
    import string
    print(count_vowels(string.ascii_letters))

