def find_odd_names(lst):
    """
        This kata is from Coding Meetup series
        Coding Meetup @#15 - Higher order Functions Series - Count the numbers
        of JavaScript developers coming from Europe.

        You wil be given an array of objects (hashes in ruby) representing data
        about developers who have signed up to attend the coding meetup that
        you are organising for the first time.

        Your task is to return only the developers where if you add the ASCII 
        representation of all characters in their firstnames, the result will 
        be an odd number.
        Sum of ASCII in name  Abb is 65 + 98 + 98 = 261 which is an odd number.

        Solution description :
        builtin ord() will find out the ASCII representation of a letter;
        make an list with ord(letter), sum that list, put that sum in a condition 
        in list comprehension the condition is that the sum should return an odd 
        number : sum(ord(letter)) % 2 != 0
        Examples:

        >>> find_odd_names([{'firstname': 'Abb', 'age': 15,'language': 'JavaScript'},
        {'firstname': 'Aba', 'age': 16,'language': 'Javascript'}
        ]) == [{'firstname': 'Abb', 'age': 15,'language': 'JavaScript'}]
        True


    """
    return [lst[i] for i in range(len(lst)) 
            if sum([ord(i) for i in lst[i]['firstname']]) % 2 !=0]


if __name__ =="__main__":
        print(find_odd_names([
        {'firstname': 'Abb', 'country': 'Hub', 'age': 15,'language': 'JavaScript'},
        {'firstname': 'Aba', 'country': 'Rub', 'age': 16,'language': 'Javascript'},
        {'firstname': 'Ara', 'country': 'Pub', 'age': 55,'language': 'JavaScript'},]))
