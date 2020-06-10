def vowels_indices(word):
    """Find the vowels 7kiu Kata.
        We want to find the index of the vowels in the word
        super (the second and the forth letter).
        So given a string "super" we should return a list of [2,4].
        Examples:
        vowels_indices('Mmmm') => []
        vowels_indices('super') => [2.4]
        NOTE: this is indexed from [1...] ( npt 0 !!!.
    """
    vowels = 'aeiouyAEIOUY'
    return [i + 1 for i in range(len(word)) if word[i] in vowels]
