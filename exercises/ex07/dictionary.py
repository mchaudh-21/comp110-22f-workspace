"""Dictionary function code."""
__author__ = "730550997"


def invert(dict1: dict[str,str]) -> dict[str,str]:
    """Function that inverts the keys and values of a dictionary."""
    dict2 = {}
    for key in dict1:
        new_key = dict1[key]
        new_val = key
        
        # Raise key error if the new key alr exists in the new dictionary.
        for key in dict2:
            if new_key == key:
                raise KeyError("Key is repeated.")
        
        # If there is no error, this should run.
        dict2[new_key] = new_val

    return dict2


def favorite_color(dict1: dict[str,str]) -> str:
    """Function that takes a dictionary and returns the colror that occurs with highest frequency."""
    color_list = []
    for name in dict1:
        color_list.append(dict1[name])
    
    # Now sort through the color list to check frequency. 
    frequency_dict = {}
    for color in color_list:
        if color in frequency_dict:
            frequency_dict[color] += 1
        else:
            frequency_dict[color] = 0
    
    # Now find most frequent color.
    max_num = 0
    most_frequent_color = ""
    for color in frequency_dict:
        if max_num < frequency_dict[color]:
            most_frequent_color = color

    return most_frequent_color


def count(list1: list[str]) -> dict[str,int]:
    """Function that makes a dictionary with values from a list as keys and their frequencies as values."""
    result_dict = {}
    for val in list1:
        if val in result_dict:
            result_dict[val] += 1
        else:
            result_dict[val] = 1
    
    return result_dict