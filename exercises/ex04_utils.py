"""EX04 -- List Utility Functions."""
__author__ = "730550997"


def all(list1: list[int], num: int) -> bool:
    """Function that figures out if all of the integers in a given list are the same as a given integer."""
    if len(list1) == 0:
        return False
    index_num = 0
    valid = True
    while index_num < len(list1) and valid is True:
        if num != list1[index_num]:
            valid = False
        index_num += 1

    return valid


def max(list1: list[int]) -> int:
    """Function that finds max value in list."""
    if len(list1) == 0:
        raise ValueError("max() arg is an empty List")

    index_num = 0
    max_num = list1[0]
    while index_num < len(list1):
        if max_num < list1[index_num]:
            max_num = list1[index_num]
        index_num += 1
    return max_num


def is_equal(list1: list[int], list2: list[int]) -> bool:
    """Function that checks if two lists have deep equality."""
    # check length
    if len(list1) != len(list2):
        return False
    else:
        equal = True
        index_num = 0
        # check indices
        while index_num < len(list1) and equal is True:
            if list1[index_num] != list2[index_num]:
                equal = False
            index_num += 1
    return equal