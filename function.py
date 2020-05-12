# All about function
'''
def display_message():
    print("I learned about function in this chapetr")
display_message()
'''
'''
def display_message():
    message = input('Write your message here: ')
    print(message)
display_message()
'''
'''
#Another display_message function
def display_message():
    user_name = input('Tell me your name: ')
    message = input(user_name.title()+ ' write your message here: ')
    print(user_name.title() + '' + ' wrotte: ' + message.upper())
display_message()
'''
'''
#Favorite_book function
def favorite_book(title):
    text = 'One of my favorite books is '
    print(text + title)
favorite_book(' Alice in Wonderland ')
'''


def kg_to_lbs(weight):
    return weight / 0.45


def lbs_to_kg(weight):
    return weight * 0.45


# This function fin maximum number in a list 22-10-2019
def find_max(nums):
    max = nums[0]
    for number in nums:
        if number > max:
            max = number
    return max


# This exemple is(with recursion) from:
# https://stackoverflow.com/questions/699866/python-int-to-binary-string.
def binary(num):
    if num == 0:
        return ''
    return binary(num//2) + str(num % 2)

# print([binary(i) for i in range(100)])

# This function will reverse a string


def reverse(x):
    return x[::-1]


# This function will say you hello as many times as letters
# in your name added 24.10.2019
def special_greeting():
    name = input('tell me your name: ' + '\n')
    name_len = len(name)
    return name + ' hello ' * name_len


# Hand made sqrt function
def s_root(num):
    return num ** 0.5


def max2(x, y):
    if x > y:
        return x
    return y


def max3(x, y, z):
    return max2(x, max2(y, z))


# Feet to meters function
def feet_to_meters(feets):
    return feets * 0.3048


# Calculates square roots
def sroot(number):
    return number ** 0.5


def square_root(num):
    """Newton's method implementation.
    """
    root = num/2      # initial guess will be 1/2 of num
    for i in range(num + 1):
        root = (1/2)*(root + (num / root))

    return root


def fizz_buzz(num):
    for num in range(num + 1):
        if num % 5 == 0 and num % 3 == 0:
            print('FizzBuzz')
        elif num % 3 == 0:
            print('Fizz')
        elif num % 5 == 0:
            print('Buzz')
        else:
            print(num)


def nospaces(sentence):
    '''This function remove the all spcaaces'''
    return sentence.replace(' ', '')
