import keyword

def check_keyword():
    """
    This function check if the word is or not a keyword.

    """
    word = input("enter a word to check: ")

    if keyword.iskeyword(word):
        print('Sorry it is a reserved keyword')
    else:
        print("it's ok you can use: " + word)

if __name__ == '__main__':
    check_keyword()
