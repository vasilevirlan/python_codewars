from string import ascii_lowercase as al

LETTERS = {letter: str(index) for index, letter in enumerate(al, start=1)}

def alphabet_position(text):
    """Returns the position of letter from alphabet in a given string.
    """
    text = text.lower()

    numbers = [LETTERS[character] for character in text if character in LETTERS]

    return list(numbers)
if __name__=='__main__':

    my_string = input("your text please: ")
    print(alphabet_position(my_string))
