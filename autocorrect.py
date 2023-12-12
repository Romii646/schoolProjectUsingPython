#!/usr/bin/env python3

"""This program autocorrects on a set of words read from a file.
   then displays it on screen."""

__author__ = 'Aaron Cortina'
__date__ = '04/14/2024'


import pathlib
import sys


def read(filename):
    """This function is used to read text files.

    Args:
        filename(string): variable used to pass name of text file.

    Return:
        list1, list2
    """
    try:
        if pathlib.Path(filename).exists():
            with open(filename) as file:
                words = file.read()
                words = words.replace('=', ' ')
                words = words.lower().split()
                list1 = words[::2]
                list2 = words[1::2]
    except FileNotFoundError:
        print('Could not open file')
        sys.exit()
    except OSError:
        print('Could not open file - exiting')
        sys.exit()
    return list1, list2


def merge(list1, list2):
    """This function is used to read text files.

    Args:
        list1(list): containing the key values from text file for a dictionary.
        list2(list): containing strings for the value side of a dictionary.

    Return:
        auto_correct
    """
    # declared dictionary variable
    auto_correct = {}
    count = 0
    for word in list1:
        auto_correct[word] = list2[count]
        count += 1
    return auto_correct


def main():
    """The main program calls function read to get file name for text files.
       After main program will call function merge to grab text file spilt
       into two list to be merged into one variable dictionary. Then display
       correct sentence on screen.
    Args:
       None

    Return:
       None
    """

    # start of main program
    file = input('File? ')
    print()

    # function read to get the file by user
    list1, list2 = read(file)
    # function to merge split words into a dictionary
    auto_correct = merge(list1, list2)

    # variable to get user's sentence
    line = input('Line? ')
    print()

    # for loop to find key value words in dictionary auto_correct and
    # replace miss spelled word with correct word
    for bad_word in auto_correct:
        correct_word = auto_correct.get(bad_word)
        line = line.replace(bad_word, correct_word)
    print(line)


if __name__ == '__main__':
    main()
