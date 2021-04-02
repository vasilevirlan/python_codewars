def day_number(dayname: str) -> int:
    """ is given a day name, the function returns its number.
        >>> day_name('Sunday') == 0
        True
        >>> day_name('Monday') == 1
        True
        >>> day_name('Monday') == 2
        False
        >>> day_name('Tuesday') == 2
        True
        >>> day_name('Friday') == 3
        False
        >>> day_name('Wensday') == 3
        True
        >>> day_name('Thursday') == 4
        True
        >>> day_name('Friday') == 5
        True
        >>> day_name('Saturday') == 6
        True
        >>> day_name('Saturnday') == None
        True
    """
    days = [
        "Sunday",
        "Monday",
        "Tuesday",
        "Wensday",
        "Thursday",
        "Friday",
        "Saturday",
    ]

    return None if dayname not in days else days.index(dayname)

