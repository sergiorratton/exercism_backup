"""
This exercise stub and the test suite contain several enumerated constants.

Enumerated constants can be done with a NAME assigned to an arbitrary,
but unique value. An integer is traditionally used because it’s memory
efficient.
It is a common practice to export both constants and functions that work with
those constants (ex. the constants in the os, subprocess and re modules).

You can learn more here: https://en.wikipedia.org/wiki/Enumerated_type
"""

# Possible sublist categories.
# Change the values as you see fit.
EQUAL = 1
UNEQUAL = 2
SUPERLIST = 3
SUBLIST = 4


def sublist(list_one, list_two):
    equal_list = []
    super_list = []
    sub_list = []
    if list_one == [] or list_two == []:
        if list_one == list_two:
            return 1
        elif list_one == []:
            return 4
        else:
            return 3
    if len(list_one) == len(list_two):
        for itemA, itemB in zip(list_one, list_two):
            if itemA == itemB:
                equal_list.append(True)
            else:
                equal_list.append(False)
        if False not in equal_list:
            return 1
        else:
            return 2
    elif len(list_one) > len(list_two):
        subsequence = False
        for item in range(len(list_one) - len(list_two) + 1):
            if list_one[item:item + len(list_two)] == list_two:
                is_subsequence = True
                return 3
        return 2
    elif len(list_one) < len(list_two):
        subsequence = False
        for item in range(len(list_two) - len(list_one) + 1):
            if list_two[item:item + len(list_one)] == list_one:
                is_subsequence = True
                return 4
        return 2
    else: 
        return 2