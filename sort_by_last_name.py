def sort_by_last_name(name):
    """This function will sort a list of names(2 words)
        by last name.
    """
    return sorted(name, key=lambda last_name: last_name.split()[-1])
