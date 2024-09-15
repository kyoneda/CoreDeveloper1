#!/usr/bin/env python

# Week 4 Exercises: Comments and Formatting

# EXERCISE 1:

# The function below is an implementation of bubble sort
# Rewrite it with proper comments and formatting using Clean Code standards

import copy


def bubble_sort(int_list):
    """Sort a list of integers with bubble sort algorithms.

    Compares adjacent elements and swaps them if they are in the wrong
    order. This push big number from left to right.
    
    Args:
        int_list (list of int): The list of integers to be sorted.
    
    Returns:
        sorted_list (list of int): A sorted list.
    """
    sorted_list = copy.copy(int_list)
    len_list = len(sorted_list)
    for index_a in range(len_list):
        for index_b in range(0, len_list - index_a - 1):
            if sorted_list[index_b] > sorted_list[index_b + 1]:
                sorted_list[index_b], sorted_list[index_b + 1] = sorted_list[
                    index_b + 1], sorted_list[index_b]
    return sorted_list


# EXERCISE 2:

# Create a Python function that find the number of instances of a substring
# within a string. For example given the string "abcda" and the substring "a"
# the function should return 2
# Write a proper multiline docstring for your code


def count_substrings(substring, string):
    """Count number of appearance of substring in a parent string.

    substrings can share the elements.
    Ex. count_substrings("aba","abababa") = 3 but not 2.

    Args:
        string (str): A string to look in.

        substring (str): A string you want to count appearance.
    
    Returns:
        cnt (int): number of substring in a string.
    """
    cnt = 0
    sub_len = len(substring)
    main_len = len(string)

    for i in range(main_len - sub_len + 1):
        if string[i:i + sub_len] == substring:
            cnt = cnt + 1

    return cnt


# - - - - Enter code here or in separate file - - - -
