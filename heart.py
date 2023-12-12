#!/usr/bin/env python3

"""Module to print heart rate information for a person."""

__author__ = 'Karen Peterson'
__date__ = '7/20/2020'

from person import Person


def main():
    """Gather info about a person, then print heart rates.

    Args:
        None

    Returns:
        None
    """
    name = input('Name? ')
    print()
    age = int(input('Age? '))
    print()

    exerciser = Person()
    try:
        exerciser.name = name
        exerciser.age = age
    except ValueError as val_err:
        print(val_err)
    print(exerciser)

    target_rate = exerciser.get_target_rate()
    print('{0} should aim for {1} to {2} bpm'.format(
        exerciser.name, target_rate[0], target_rate[1]))


if __name__ == '__main__':
    main()
