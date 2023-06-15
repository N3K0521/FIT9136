"""
Creation Date: 27th May 2023
Last Modified Date: 3rd June 2023

Student Name: Huixin Wang
Student ID: 31552544
"""

import re

class User:
    """
    A class used to represent a user, which is the base class for Customer and Admin

    Attributes
    ----------
    user_id : str
        a string to store the user id in the format of u_10digits
    user_name : str
        a string to store the user's name
    user_password : str
        a string to store the user's password
    user_register_time : str
        a string to store the user's register time in the format “DD-MM-YYYY_HH:MM:SS”
    user_role : str
        a string to store the user's role

    Methods
    -------
    __init__():
        Constructs a user object
    __str__():
        Return the user Information as a formatted string.
    """

    # All positional arguments of the constructor have default values
    def __init__(self, user_id="u_0000000000", user_name="user", user_password="password", user_register_time="00-00-0000_00:00:00",
                 user_role="customer"):
        """
        Constructs a user object.
        :param user_id: str
            The id of the user (default is u_0000000000)
            Format: u_10 digits
            Must be unique
        :param user_name: str
            A string ro store the user's name (default is "user")
        :param user_password: str
            A string to store the user's password (default is "password")
        :param user_register_time: str
            A string to store the user's register time (default is 00-00-0000_00:00:00)
            Format: DD-MM-YYYY_HH:MM:SS
        :param user_role: str
            A string to store the user's role (default is "customer")
        """
        # the re expression matching mode: 10 numbers after u_
        u_id_re = re.compile(r'^u_\d{10}$')
        # the matching mode of the re expression: 00-00-0000_00:00:00
        u_time_re = re.compile(r'^\d{2}-\d{2}-\d{4}_\d{2}:\d{2}:\d{2}$')
        # if does not match:
        if not u_id_re.match(user_id):
            raise ValueError("The user_id is invalid!")
        if not u_time_re.match(user_register_time):
            raise ValueError("The user_register_time is invalid!")
        self.user_id = user_id
        self.user_name = user_name
        self.user_password = user_password
        self.user_register_time = user_register_time
        self.user_role = user_role

    def __str__(self):
        """
        Return the user information as a formatted string
        :return: String returned in the format of:
                “{‘user_id’:’u_1234567890’, ‘user_name’:’xxx’,
                ‘user_password’:’xxx’, ‘user_register_time’:’xxx’,
                ‘user_role’:’customer’}”
        """
        return "{" + f"'user_id':'{self.user_id}', " \
                     f"'user_name':'{self.user_name}', " \
                     f"'user_password':'{self.user_password}', " \
                     f"'user_register_time':'{self.user_register_time}', " \
                     f"'user_role':'{self.user_role}'" + "}"


