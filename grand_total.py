#!/usr/bin/env python3

"""This program is created to read files and add any numbers within the file
    and throw exception if its a non float"""

__author__ = 'Aaron Cortina'
__date__ = '03/09/2023'

import sys


def read(file):
    """This function is used to read text files.

    Args:
        file(string): variable used to capture text data

    Return:
        num
    """
    try:
        with open(file, 'r') as t_file:
            num = t_file.readlines()
    except FileNotFoundError:
        print('Could not open file - exiting')
        sys.exit()
    except OSError:
        print('Could not open file - exiting')
        sys.exit()
    return num


# Start of main program
def main():
    """The main program calls function to get file name for text files.
        After main program will calculate numbers in file and throw exception
        once encounter a non number.
    Args:
        None

    Return:
        None
    """
    file = input('File? ')
    print()
    nums = read(file)
    total = 0
    for num in nums:
        try:
            total += float(num)
        except ValueError:
            print('Invalid number: ' + str(num), end='')
    print(f"Grand total: {total}")


if __name__ == '__main__':
    main()
