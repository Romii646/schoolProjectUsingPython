#!/usr/bin/env python3

"""Exercise program that calulate distance and
   displays how many steps and city blocks you've walked
"""

__author__ = 'Aaron Cortina'
__date__ = '02/10/2023'

import math


def cal_dist(pt_one, pt_two):
    """This function is used to calculate the distance

    Args:
        pt_one(float) pt_two(float): variables from prompted user. Variables
        gets converted into values and then calulated for distance on city
        map

    Return:
        blocks
    """
    # variables pt_one and pt_two are converted into values
    x1 = ord(pt_one[0])
    y1 = ord(pt_one[1])
    x2 = ord(pt_two[0])
    y2 = ord(pt_two[1])
    # Calculated with absolute value function
    loc1 = abs(x1 - y2)
    loc2 = abs(y1 - x2)
    # function to help calculate the distance of pt_one and pt_two
    blocks = math.dist([loc1], [loc2])
    return blocks


def convert(total):
    """This function is used to convert amount of city blocks into miles and
       steps

    Args:
        total(float): variable is used to help convert blocks to miles and
        total amount of steps

    Return:
        miles, step
    """
    step = total * 250
    mile = step / 2000
    return mile, step


# start of main program
def main():
    """This the main function to grab user locations and call functions
       cal_distance and convert. After called functions main will then
       display the total amount walked in steps, miles , city blocks

    Args:
        None

    Return:
        None
    """
# local variable to store total city blocks

    total = 0
    pt_one = input("Home? ")
    print()
    pt_two = input("Next? ")
    print()

# local variable to store original user starting point
    home = pt_one

# loop is used to continue taking user locations until sentinel word home
#  is used
    while home.lower() != 'home':
        blocks = cal_dist(pt_one, pt_two)
        total += blocks
        pt_one = pt_two
        pt_two = input("Next? ")
        print()

# once sentinel word is input then if statement will be activated to end loop
        if pt_two.lower() == 'home':
            pt_two = home
            blocks = cal_dist(pt_one, pt_two)
            total += blocks
            home = 'home'
    mile, step = convert(total)
    print("Trip is " + str(int(total))
          + " city blocks\nwhich is "
          + str(round(mile, 1))
          + " miles\nor " + str(round(step, 1))
          + " steps")


if __name__ == '__main__':
    main()
