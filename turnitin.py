#!/usr/bin/env python3

"""This program takes two strings from the user and removes minor
   differences and then compares to see if they're the same."""

__author__ = 'Aaron Cortina'
__date__ = '04/07/2024'


def removal(f_string, s_string):
    """Function is used to removal all commas and periods as well as seperating
       each word with a dash.

    Args:
        f_string (string): contains users first string
        s_string (string): contains users second string

    Returns:
        word_one, word_two
    """
    # stripping commas and periods
    f_string = f_string.replace(',', '')
    f_string = f_string.replace('.', '')
    s_string = s_string.replace(',', '')
    s_string = s_string.replace('.', '')

    # split strings by words seperated by dashes
    word_one = f_string.split()
    word_one = "-".join(word_one)
    word_two = s_string.split()
    word_two = "-".join(word_two)

    return word_one, word_two


def compare(word_one, word_two):
    """Function is used to compare both strings to see if they're the same.

    Args:
        word_one(string): contains users first string
        word_two(string): contains users second string

    Returns:
        compared
    """
    compared = "SAME"
    count = 0
    for letter in word_one:
        if letter != word_two[count]:
            compared = "DIFFERENT"
            break
        count += 1
    return compared


def main():
    """Ask user for two strings after removing differences from the
       two strings it will then print and compare.

    Args:
        None

    Returns:
        None
    """
    # start of program
    # prompt user for string 1 and 2
    first_string = input("String 1? ").strip()
    word_one = first_string
    word_one = word_one.lower()
    print()
    second_string = input("String 2? ").strip()
    word_two = second_string
    word_two = word_two.lower()
    print()

    # call to function removal to remove commas and periods
    # as well as seperate each with with a dash
    word_one, word_two = removal(word_one, word_two)

    # call to function to compare if same or different function
    # will return a veriable with a sting stating same or not
    compared = compare(word_one, word_two)

    # print section
    print(f"{first_string} simplifies to {word_one}")
    print(f"{second_string} simplifies to {word_two}")
    print(compared)


if __name__ == '__main__':
    main()
