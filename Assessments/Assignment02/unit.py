"""
Creation Date: 19th April 2023
Last Modified Date: 09th May 2023

Group number: App03-Group41

Group number 1:
    Name: Huixin Wang
    Student ID: 31552544

Group number 2:
    Name:Enze Dong
    Student ID:33038937

Group number 3:
    Name:Nikita Bhararia
    Student ID:32708246
"""

import os
import random

# Unit Class
class Unit:
    """
    A class used to represent a unit

    Attributes
    ----------
    unit_id : int
        an integer to store the unit id
    unit_code : str
        a string to store the unit code
    unit_name : str
        a string to store the unit name
    unit_capacity : int
        the maximum enrol capacity of the unit

    Methods
    -------
    generate_unit_id():
        Randomly generate a unique unit id (7 digits)
    """
    def __init__(self, unit_id=None, unit_code=None, unit_name=None, unit_capacity=None):
        """
        Constructs a unit object

        :param unit_id: int
            The id of the unit (default is None)
            Must be unique integer
        :param unit_code: str
            The unit code of the unit (e.g. FIT9136)
            Must be unique
        :param unit_name: str
            The unit name
        :param unit_capacity: int
            Each unit has a maximum enrol capacity
        """
        self.unit_id = unit_id if unit_id else self.generate_unit_id()
        self.unit_code = unit_code
        self.unit_name = unit_name
        self.unit_capacity = unit_capacity

    def __str__(self):
        """
        Return the unit information as a formatted string

        :return: str
            a string in the following format: "unit_id, unit_code, unit_name, unit_capacity"
        """
        return f"{self.unit_id}, {self.unit_code}, {self.unit_name}, {self.unit_capacity}"


    def generate_unit_id(self):
        """
        Return a unique unit id (7 digits number)
        :return: int
            an integer number consisting of 7 digits
        """
        with open('data/unit.txt', 'r') as f:
            unit_ids = [int(line.strip().split(', ')[0]) for line in f.readlines()]
        unit_id = random.randint(1000000, 9999999)
        while unit_id in unit_ids:
            unit_id = random.randint(1000000, 9999999)
        return unit_id

