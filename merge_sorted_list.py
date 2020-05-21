
def merge_lists(first, second):
    """Write a function that merge two sorted list
        into a single one.The list only contains integers.
        Also, the final outcome
        must be sorted and not haev any duplicates.
        Examples
        merge_list([1, 3, 5], [2, 4, 6]) --> [1, 2, 3, 4, 5, 6]
    """
    return list(sorted(dict.fromkeys(first + second)))
