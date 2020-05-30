def vowels_index(word):
    vowels = 'aeiouyAEIOUY'
    return [x + 1 for x in range(len(word)) if word[x] in vowels]
