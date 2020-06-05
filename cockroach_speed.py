def transf_speed(speed):
    """ takes speed in km/h and returns
        cm/sec rounded down to the integer.
        >>> transf_speed(1.08)
        30
        >>> transf_speed(1.09)
        30
    """
    return int((speed * 100000) / 3600)
