def century(year):
    """Given a year return the century itis in.
        The first century spans from year 1 up to and 
        including the year 100. The second century - from the year 101
        up to and including the year 200, ets.
        Examples:
        century(1705) --> 18:
        century(1900) --> 19:
    """

    if year % 100 != 0:
        return year // 100 + 1
    else:
        return year // 100
