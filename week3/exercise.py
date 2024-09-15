#!/usr/bin/env python

# Week 3 Exercises: Functions

# EXERCISE 1:

# Implement FizzBuzz using function(s) with Clean Code standards

# -----FIZZBUZZ CODE HERE-----


def print_fizzbuzz(last_number):
    """Print FIZZBUZZ outputs from 1 to the specified number.

    Take a number as an input and print FIZZBUZZ outputs from 1 to the number.
    
    Args:
        last_number (int): A last number of FIZZBUZZ inputs.
    """
    for number in range(1, last_number + 1):
        if number % 3 == 0 and number % 5 == 0:
            print("FIZZBUZZ")
        if number % 3 == 0:
            print("FIZZ")
        if number % 5 == 0:
            print("BUZZ")
        else:
            print(number)


if __name__ == "__main__":
    print("Enter the last number for FIZZBUZZ game")
    last_number = int(input())
    print_fizzbuzz(last_number)

# -----END FIZZBUZZ CODE-----

# EXERCISE 2:

# Review the payroll.java code in Listing 3-4 in the book

# Re-implement it as clean Python code. See Listing 3-5 for guidance.

# -----PAYROLL CODE HERE-----


# -----END PAYROLL CODE-----
