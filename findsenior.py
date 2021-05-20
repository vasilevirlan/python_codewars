
from collections import Counter
def find_senior(lst):
    """
        This kata is from Coding Meetup series
        Coding Meetup @#1 - Higher order Functions Series - Count the numbers
        of JavaScript developers coming from Europe.

        You wil be given an array of objects (hashes in ruby) representing data
        about developers who have signed up to attend the coding meetup that
        you are organising for the first time.

        Your task is to return the a sequence which includes the developer who
        is the oldest. In case of a tie, include all same-age developers lested
        in the same order as they  appeared in the original input array.

        Example:
        >>> find_senior([
        {'firstname': 'Dan', 'continent': 'Europe', 'country': 'Hub', 'age': 10, 'language': 'JavaScript'},
        {'firstname': 'Van', 'continent': 'Europe', 'country': 'Rub', 'age': 18, 'language': 'Java'},
        {'firstname': 'Ian', 'continent': 'Europe', 'country': 'Rub', 'age': 18, 'language': 'Python'},
        {'firstname': 'Van', 'continent': 'Europe', 'country': 'Rub', 'age': 20, 'language': 'R'},
        {'firstname': 'Van', 'continent': 'Europe', 'country': 'Rub', 'age': 20, 'language': 'Ruby'},
        {'firstname': 'Van', 'continent': 'Europe', 'country': 'Rub', 'age': 34, 'language': 'C'},
        {'firstname': 'Van', 'continent': 'Europe', 'country': 'Rub', 'age': 45, 'language': 'C++'},
        {'firstname': 'Tan', 'continent': 'Europe', 'country': 'Rub', 'age': 56, 'language': 'JavaScript'},
        ]) == [{'firstname': 'Tan', 'continent': 'Europe', 'country': 'Rub', 'age': 56, 'language': 'JavaScript'}]
        True
        >>> find_senior([
        {'firstname': 'Dan', 'continent': 'Europe', 'country': 'Hub', 'age': 16,'language': 'Python'},
        {'firstname': 'Van', 'continent': 'Europe', 'country': 'Rub', 'age': 18,'language': 'Python'},
        {'firstname': 'Ian', 'continent': 'Europe', 'country': 'Rub', 'age': 18,'language': 'Python'},
        {'firstname': 'Van', 'continent': 'Europe', 'country': 'Rub', 'age': 20,'language': 'Python'},
        {'firstname': 'Van', 'continent': 'Europe', 'country': 'Rub', 'age': 30,'language': 'Python'},
        {'firstname': 'Van', 'continent': 'Europe', 'country': 'Rub', 'age': 44,'language': 'Python'},
        {'firstname': 'Van', 'continent': 'Europe', 'country': 'Rub', 'age': 65,'language': 'Python'},
        ]) == [{'firstname': 'Van', 'continent': 'Europe', 'country': 'Rub', 'age': 65,'language': 'Python'}]
        True
        >>> find_senior([
                {'firstname': 'Dan', 'continent': 'Europe', 'country': 'Hub', 'age': 15,'language': 'JavaScript'},
                {'firstname': 'Van', 'continent': 'Europe', 'country': 'Rub', 'age': 16,'language': 'Javascript'},
                {'firstname': 'Ian', 'continent': 'Europe', 'country': 'Rub', 'age': 19,'language': 'JavaScript'},
                {'firstname': 'Van', 'continent': 'Europe', 'country': 'Rub', 'age': 20,'language': 'JavaScript'}
                {'firstname': 'Van', 'continent': 'Europe', 'country': 'Rub', 'age': 20,'language': 'JavaScript'},
                {'firstname': 'Van', 'continent': 'Europe', 'country': 'Rub', 'age': 34,'language': 'JavaScript'},
                {'firstname': 'Tan', 'continent': 'Europe', 'country': 'Rub', 'age': 55,'language': 'JavaScript'},
        ]) == [{'firstname': 'Tan', 'continent': 'Europe', 'country': 'Rub', 'age': 55,'language': 'JavaScript'}])
        True
    """
    maximum = max([lst[i]['age'] for i in range(len(lst))])
    return [lst[i] for i in range(len(lst)) if lst[i]['age'] == maximum]


if __name__ =="__main__":
        print(find_senior([
        {'firstname': 'Dan', 'continent': 'Europe', 'country': 'Hub', 'age': 15,'language': 'JavaScript'},
        {'firstname': 'Van', 'continent': 'Europe', 'country': 'Rub', 'age': 16,'language': 'Javascript'},
        {'firstname': 'Ian', 'continent': 'Europe', 'country': 'Rub', 'age': 19,'language': 'JavaScript'},
        {'firstname': 'Van', 'continent': 'Europe', 'country': 'Rub', 'age': 20,'language': 'JavaScript'},
        {'firstname': 'Van', 'continent': 'Europe', 'country': 'Rub', 'age': 20,'language': 'JavaScript'},
        {'firstname': 'Van', 'continent': 'Europe', 'country': 'Rub', 'age': 34,'language': 'JavaScript'},
        {'firstname': 'Tan', 'continent': 'Europe', 'country': 'Rub', 'age': 55,'language': 'JavaScript'},
        {'firstname': 'Wan', 'continent': 'Europe', 'country': 'Pub', 'age': 55,'language': 'JavaScript'},]))
