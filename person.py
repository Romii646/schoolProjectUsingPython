#!/usr/bin/env python3

"""Person class for program heart."""

__author__ = 'Aaron Cortina'
__date__ = '4/21/2023'


class Person:
    """Class to place data in a range of ages to determine heart beat.

    Attributes:
        name (string): name will default to ''
        age (int): age will default to 21

       Constructor.

       Args:
       month (int): month number
          day (int): day number

       Returns:
          None
    """
    def __init__(self, name='', age=21):
        self.name = name
        self.age = age

    def __str__(self):
        """Converts object to a string.

            Args:
               None

            Returns:
               string (str): string version of the object
         """
        return '{0} ({1} years old)'.format(self.name, self.age)

    @property
    def name(self):
        """nameday getter.

            Args:
               None

            Returns:
               name (string): string name
        """
        return self._name

    @name.setter
    def name(self, name):
        """day setter.

              Args:
                 name (string): string name

              Returns:
                 None
         """
        self._name = name

    @property
    def age(self,):
        """age getter.

            Args:
                none

              Returns:
                age int: a number
         """
        return self._age

    @age.setter
    def age(self, age):
        """age setter.

             Args:
                age (int): age number

              Returns:
                None

              Raises:
                ValueError: if age is out of range
         """
        if age >= 20:
            self._age = age
        else:
            raise ValueError('invalid age')

    def get_target_rate(self):
        """Move to the next day.

            Args:
              none

           Returns:
              target_rate (tuple): passing min heart rate and max
        """
        if 20 <= self.age <= 29:
            target_rate = (100, 170)
        elif 30 <= self.age <= 34:
            target_rate = (95, 162)
        elif 35 <= self.age <= 39:
            target_rate = (93, 157)
        elif 40 <= self.age <= 44:
            target_rate = (90, 153)
        elif 45 <= self.age <= 49:
            target_rate = (88, 149)
        elif 50 <= self.age <= 54:
            target_rate = (85, 145)
        elif 55 <= self.age <= 59:
            target_rate = (83, 140)
        elif 60 <= self.age <= 64:
            target_rate = (80, 136)
        elif 65 <= self.age <= 69:
            target_rate = (78, 132)
        else:
            target_rate = (75, 128)
            
        return target_rate
