#Differrent imported functions for funnn!!!

#Fibonacci numbers!
def fib(num):
    '''This function print Fibonacci Numbers to num. 
        From python .org
    '''
    a, b = 0, 1
    while a < num:
        print(a, end=' ')
        a, b = b, a + b
    print()


def fib2(n):
    if n < 2:
        return 1
    return fib2(n-1) + fib2(n-2)


#Power function
def power_function(num):
    return num * num

#Cube functions
def cube(num):
    return num * num * num

#rectangle area function
def rectangle_area():
    length = int(input("enter length:"))
    width = int(input("Enter width: "))
    return length * width
#sum function
def sum(a:"int,>0", b:"int,>0") ->int:
    return a + b


#Fibonacci numbers from python.org
def fibonacci(number):
    a, b = 0, 1
    while a < number:
        print(a, end=' ')
        a, b = b, a + b

#from codewars.com

def generate_integers(m, n):
    """Generate a list of positive integers
        from m to n.
        From codewars.com
    """
    return[x for x in range(m, n+1)]


def array_madness(a, b):
    if sum([x*x for x in range(2, a+1)]) > sum([x*x*x for x in range(2, b+1)]):
        return True
    else:
        False



def abbrev_name(name):
    """Write a function to convert a name into initials.
        This kata strictly takes two words with one space in between them.
        The output should be two capital lettesrs with a dot separating them.

        This solution is from stackoverflow.com - using list comprehension.
    """
    return '.'.join([word[0].upper() for word in name.split(' ')])


def build_quadranic_function(a, b, c):
    """Return the function f(x) = ax^2 + bx + c.
        From socratica channel on youtube.com
    """
    return lambda x: a*x**2 + b*x + c


def expressions_matters(a, b, c):
    """Try every combination of a, b, c with * + and () and return the maximumobtained.
    """
    sum1 = a *(b+c)
    sum2 = (a + b) * c
    sum3 = (a + c) * b
    sum4 = a * b * c
    return max(sum1, sum2, sum3, sum4)


def str_count(string, letter):
    """All star code chalenge #18
        Create a function that accept 2 string arguments and returns an integer of the count of 
        occurence the 2nd argument is found in the firs one.
        If no occurence can be found a count 0 should be returned.

        str_count('Hello', 'o') // => 1
        str_count('Hello', 'l') // => 2
    """
    return string.count(letter)


def fizz_buzz_list(num):
    """
    Print a list of numbers divided by 3, 5 and 3, 5 at the same time in range of num
    """
    buzz = [x for x in range (1, num + 1) if x %3==0]
    fizz = [x for x in range (1, num + 1) if x % 5 == 0]
    fizzbuzz = [x for x in range (1, num + 1) if (x % 3 ==0 and x % 5 == 0)]
    print('Divide by 3:{}\nDivide by 5:{}\nDivide by 3 and by 5:{}'.format(buzz, fizz, fizzbuzz))


def convert_to_base(number, base):
    """Convert a number to base
    """

    digits = '01234567890ABCDEF'
    if number < base:
        return digits[number]
    return convert_to_base(number // base, base) + digits[number % base]


def is_even(number):
    """Determine if the number passssed is even
    """
    return True  if number %2==0 else False

#from codewars.com 
#8kyu
#Take the derivative

def derive(coefficient, exponent):
    """This function takes two  numbers as parameters, the first number 
        beng the coefficient, and the secpnd number being the exponent.

        Your function shoud multiply the two numbers, and then subtract 1 from
        the exponent. THen, it has to print out an expression (like 28x^7).
        "^1" shoud not be truncated when exponent =2.

        For example:
        derive(7, 8) --> "56x^7"
        derive(5, 9) --> "45x^8"

    """
    return str(coefficient * exponent) + "x^" + str(exponent - 1)

#From codewars.com
#8kyu Begginer series #2 Clock

def past(h, m, s):
    """Clock shows 'h' hoours, 'm' seconds, 's' seonds.
        
        Your task is to make 'past' function which returns
        time converted in miliseconds.
        Example:
        psat(1, 1, 1) --> 61000.

        Input constraints: 0 <= h <= 23, 0<= m<= 59, 0 <= 59.
    """
    if h < 0 and h > 59:
        raise RuntimeError("Inadmissible time")
    elif m < 0 and m > 59:
        raise RuntimeError("Inadmisibile time")
    elif s < 0 and s > 59:
        raise RuntimeError("Inadmisible time")
    else:
        return h * 3600000 + m * 60000 + s * 1000


#From codewars.com
#8kyu kata Find the diference in Age between Oldest and youngest Family Memebers

def difference_in_age(ages):

    """You will be given an array of all the family members' ages. In any order.
        The ages will be given in whole numbers, Return a new array (a tuple in Python)
         with [youngest age,  oldest age, difference between the youngest and oldest age].
    """
    return min(ages), max(ages), max(ages) - min(ages)

def getascii(mystring):
    """This function returns a list of ASCII order of th character from opened file.
    """
    mystring = open(input("enter fille name: "))
    mystring = mystring.read()
    return [ ord(ch) for ch in mystring ]
    
print('{} \nSorted{}'.format(getascii(), sorted(getascii())))
