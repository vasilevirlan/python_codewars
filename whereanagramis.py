def anagrams(word: str, words: list) -> list:
    return [i for i in words if sorted(i) == sorted(word)]


if __name__ == "__main__":
    print(anagrams('abba', ['aabb', 'abcd', 'bbaa', 'dada']))
