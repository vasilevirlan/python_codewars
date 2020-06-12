def reject(seq: list, predicate = lambda x: x % 2 == 0):
    ''' 7 kyu KATA. Implement a function which filter out list value
        which satisfy the given predicate.
        >>> reject([1, 2, 3, 4, 5, 6, 7, 8])
        [1, 3, 5, 7]
    '''
    unwanted = list(filter(predicate, seq))
    return [el for el in seq if el not in unwanted]
