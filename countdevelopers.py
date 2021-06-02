from collections import Counter
def count_languages(lst):
    """
        This kata is from Coding Meetup series
        Coding Meetup @#1 - Higher order Functions Series - Count the numbers
        of JavaScript developers coming from Europe.

        You wil be given an array of objects (hashes in ruby) representing data
        about developers who have signed up to attend the coding meetup that
        you are organising for the first time.

        Your task is to return  a dictionary that contains the count of languages.

        Example:
        >>> count_languages([
        {'firstname': 'Dan', 'continent': 'Europe', 'country': 'Hub', 'language': 'JavaScript'},
        {'firstname': 'Van', 'continent': 'Europe', 'country': 'Rub', 'language': 'Java'},
        {'firstname': 'Ian', 'continent': 'Europe', 'country': 'Rub', 'language': 'Python'},
        {'firstname': 'Van', 'continent': 'Europe', 'country': 'Rub', 'language': 'R'},
        {'firstname': 'Van', 'continent': 'Europe', 'country': 'Rub', 'language': 'Ruby'},
        {'firstname': 'Van', 'continent': 'Europe', 'country': 'Rub', 'language': 'C'},
        {'firstname': 'Van', 'continent': 'Europe', 'country': 'Rub', 'language': 'C++'},
        {'firstname': 'Tan', 'continent': 'Europe', 'country': 'Rub', 'language': 'JavaScript'},
        ]) == {'JavaScript': 2, 'Java': 1, 'Python': 1, 'Ruby': 1, 'C': 1, 'C++': 1}
        True
        >>> count_languages([
        {'firstname': 'Dan', 'continent': 'Europe', 'country': 'Hub', 'language': 'Python'},
        {'firstname': 'Van', 'continent': 'Europe', 'country': 'Rub', 'language': 'Python'},
        {'firstname': 'Ian', 'continent': 'Europe', 'country': 'Rub', 'language': 'Python'},
        {'firstname': 'Van', 'continent': 'Europe', 'country': 'Rub', 'language': 'Python'},
        {'firstname': 'Van', 'continent': 'Europe', 'country': 'Rub', 'language': 'Python'},
        {'firstname': 'Van', 'continent': 'Europe', 'country': 'Rub', 'language': 'Python'},
        {'firstname': 'Van', 'continent': 'Europe', 'country': 'Rub', 'language': 'Python'},
        ]) == {'Python': 7}
        True
        >>> count_languages([
        {'firstname': 'Dan', 'continent': 'Europe', 'country': 'Hub', 'language': 'JavaScript'},
        {'firstname': 'Van', 'continent': 'Europe', 'country': 'Rub', 'language': 'Javascript'},
        {'firstname': 'Ian', 'continent': 'Europe', 'country': 'Rub', 'language': 'JavaScript'},
        {'firstname': 'Van', 'continent': 'Europe', 'country': 'Rub', 'language': 'JavaScript'}
        {'firstname': 'Van', 'continent': 'Europe', 'country': 'Rub', 'language': 'JavaScript'},
        {'firstname': 'Van', 'continent': 'Europe', 'country': 'Rub', 'language': 'JavaScript'},
        {'firstname': 'Tan', 'continent': 'Europe', 'country': 'Rub', 'language': 'JavaScript'},
        ]) == {'JavaScript': 7}
        True
    """

    return Counter(lst[i]['language'] for i in range(len(lst)))

if __name__ =="__main__":
        print(count_languages([
        {'firstname': 'Dan', 'continent': 'Europe', 'country': 'Hub', 'language': 'JavaScript'},
        {'firstname': 'Van', 'continent': 'Europe', 'country': 'Rub', 'language': 'Java'},
        {'firstname': 'Ian', 'continent': 'Europe', 'country': 'Rub', 'language': 'Python'},
        {'firstname': 'Van', 'continent': 'Europe', 'country': 'Rub', 'language': 'R'},
        {'firstname': 'Van', 'continent': 'Europe', 'country': 'Rub', 'language': 'Ruby'},
        {'firstname': 'Van', 'continent': 'Europe', 'country': 'Rub', 'language': 'C'},
        {'firstname': 'Van', 'continent': 'Europe', 'country': 'Rub', 'language': 'C++'},
        {'firstname': 'Tan', 'continent': 'Europe', 'country': 'Rub', 'language': 'JavaScript'},
        ]))
        print(count_languages([
        {'firstname': 'Dan', 'continent': 'Europe', 'country': 'Hub', 'language': 'Python'},
        {'firstname': 'Van', 'continent': 'Europe', 'country': 'Rub', 'language': 'Python'},
        {'firstname': 'Ian', 'continent': 'Europe', 'country': 'Rub', 'language': 'Python'},
        {'firstname': 'Van', 'continent': 'Europe', 'country': 'Rub', 'language': 'Python'},
        {'firstname': 'Van', 'continent': 'Europe', 'country': 'Rub', 'language': 'Python'},
        {'firstname': 'Van', 'continent': 'Europe', 'country': 'Rub', 'language': 'Python'},
        {'firstname': 'Van', 'continent': 'Europe', 'country': 'Rub', 'language': 'Python'},
        ]))
        print(count_languages([
        {'firstname': 'Dan', 'continent': 'Europe', 'country': 'Hub', 'language': 'JavaScript'},
        {'firstname': 'Van', 'continent': 'Europe', 'country': 'Rub', 'language': 'JavaScript'},
        {'firstname': 'Ian', 'continent': 'Europe', 'country': 'Rub', 'language': 'JavaScript'},
        {'firstname': 'Van', 'continent': 'Europe', 'country': 'Rub', 'language': 'JavaScript'},
        {'firstname': 'Van', 'continent': 'Europe', 'country': 'Rub', 'language': 'JavaScript'},
        {'firstname': 'Van', 'continent': 'Europe', 'country': 'Rub', 'language': 'JavaScript'},
        {'firstname': 'Tan', 'continent': 'Europe', 'country': 'Rub', 'language': 'JavaScript'}
    ]))
