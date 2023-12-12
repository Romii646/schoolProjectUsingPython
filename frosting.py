#!/usr/bin/env python3

"""This program calculates needed amount of frosting per size of cake
   and displays pricing for frosting"""

__author__ = 'Aaron Cortina'
__date__ = '03/23/2023'


import math
import locale as lc
from decimal import Decimal, ROUND_HALF_UP


TUB = 60
PRICE = Decimal('1.25')


def cal(diameter, height, layers):
    """Calculate the area of a cake by the side of a cake and height.
       then totals area and divides by TUB amount to find each container unit.
       Then using the variable frost_tub to find the total price per tub.

    Args:
        diameter (int): half the circumference of a circle
        height (int): The length of the cake
        layers (int): Amount of layers a cake has

    Returns:
        total_price, forst_tub
   """
    radius = diameter / 2
    area_layer = round(Decimal(math.pi * (math.pow(radius, 2))), 4)
    area_side = round(Decimal(math.pi * (diameter * height)), 4)
    total_area = area_layer * layers + area_side
    frost_tub = math.ceil(total_area / TUB)
    total_price = Decimal(PRICE * frost_tub).quantize(Decimal('.01'),
                                                      ROUND_HALF_UP)
    return total_price, frost_tub


def main():
    """Ask user for values to calculate the amount of frosting needed for
       a cake.

    Args:
        None

    Returns:
        None
    """
    diameter = int(input('Diameter? '))
    print()
    height = int(input('Height? '))
    print()
    layers = int(input('Layers? '))
    print()

# call to function cal
    total_price, frost_tub = cal(diameter, height, layers)

# setting currency to local if cant be found set to U.S currency
    result = lc.setlocale(lc.LC_ALL, "")
    if result == 'C':
        lc.setlocale(lc.LC_ALL, 'en_US')

# print to display answers in f strings
    print(f"{'Num tubs:':5} {frost_tub:>5}")
    print(f"{'Price:':8}", end='')
    print('{:>7}'.format(lc.currency(total_price, grouping=True)))


if __name__ == '__main__':
    main()
