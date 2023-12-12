#!/usr/bin/env python3

"""This program is created to simulate prices and order quantity for groceries
   and multiply for total amount."""

__author__ = 'Aaron Cortina'
__date__ = '03/06/2023'

import pathlib
import csv
# I couldn't figure out the data2.txt but manage to encrpyt data1.txt

def read(txt_file, csv_file):
    """Function to read files.


    Args:
        txt_file, csv_file: variables to read files

    Returns:
           txt_file, key
    """
    if pathlib.Path(txt_file).exists():
        with open(txt_file, 'r') as t_file:
            txt_file = t_file.read()
    if pathlib.Path(csv_file).exists():
        key = []
        with open(csv_file, 'r', newline="") as c_file:
            key_r = csv.reader(c_file)
            for row in key_r:
                key.append(row)
    return txt_file, key


def encrpyt(words, key):
        """Function to encpypt file.


    Args:
        words, key: variables to encrypt message

    Returns:
           words
    """
    # module encrpyts txt_file undervariable name words from
    #csv_file under key
    count = 1
    for word in words:
        index = words.index(word)
        index += 1
        print('index ',index)
        print('count', count)
        if count > 4:
            count = 0
        if count == int(key[0][0]):
            temp = words[index - 1]
            words.pop(index - 1)
            words.insert(0,temp)
        elif count == int(key[0][1]):
            temp = words[index - 1]
            words.pop(index - 1)
            words.insert(1,temp)
        elif count == int(key[0][2]):)
            temp = words[index - 1]
            words.pop(index - 1))
            words.insert(3,temp)
        elif count == int(key[0][3]):
            temp = words[index - 2]
            words.pop(index - 2)
            words.insert(3,temp)               
        count += 1
    print(words)
    return words


# Start of main program
def main():
        """The main program calls function to get file name for txt_file
        and key. After main program will call function read
        to grab information from approcriate files and encrpyt will rearrange
        text.
    Args:
        None

    Return:
        None
    """
    txt_file = input('File? ')
    print()
    csv_file = input('Key? ')
    print()
    
    words, key = read(txt_file, csv_file)
    print(words)
    words = list(words)
    words = encrpyt(words, key)
    print()
    for word in words:
        print(word, end='')


if __name__ == '__main__':
    main()
