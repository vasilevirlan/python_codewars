def day_name(daynumber):

    """..converts an integers number 0 - 6 into the name of the day. Assume day
        0 is Sunday.
        >>> day_name(0) == "Sunday"
        True
        >>> day_name(1) == "Monday"
        True
        >>> day_name(2) == "Tuesday"
        True
        >>> day_name(3) == "Tuesday"
        False
        >>> day_name(5) == "Friday"
        True
        >>> day_name(6) == "Friday"
        False
        >>> day_name(7) == None
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
    return None if daynumber > 6 else days[daynumber]

if __name__ == "__main__":
    import doctest
    doctest.testmod()

