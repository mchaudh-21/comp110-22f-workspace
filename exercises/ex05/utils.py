"""Building list utility functions."""
__author__ = "730550997"


def only_evens(list1: list[int]) -> list[int]:
    """Given a list of integers, only return the even numbers."""
    even_num = []
    for num in list1:
        if num % 2 == 0:
            even_num.append(num)
    return even_num


def concat(list1: list[int], list2: list[int]) -> list[int]:
    """Given two lists, concatenate them."""
    lists = [list1, list2]
    final = []
    for i in lists:
        for num in i:
            final.append(num)
    return final


def sub(list1: list[int], start: int, end: int) -> list[int]:
    """Take a list and make a subset of that list based on the given index range."""
    new = []
    for i in list1:
        if list1.index(i) >= start and list1.index(i) < end:
            new.append(i)
    return new