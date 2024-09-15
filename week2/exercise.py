#!/usr/bin/env python

# Week 2 Exercises: Naming

# Rewrite the two functions below.

# In your commit message, explain what was wrong and how you fixed it.

# FUNCTION 1: Check for a specific value in a list


def checkNums(l):
    if 1 in l:
        print "There is a 1"
        return
    else:
        for o in l:
            print o
        return


# FUNCTION 2: Pick out even numbers


def evenStevens(thing):
    thanos = []
    for avenger in thing:
        if (avenger % 2) == 0:
            thanos.append(avenger)
    print "I AM INEVITABLE"
    print thanos
    return thanos

# Fixed functions
def collect_even_numbers(number_list):
    even_list = []
    for number in number_list:
        if (number % 2) == 0:
            even_list.append(number):

    print(even_list)
    return even_list


def check_numbers(number_list):
    if 1 in number_list:
        print("There is a 1 in a list")
        return
    else:
        for number in number_list:
            print(number)
        return