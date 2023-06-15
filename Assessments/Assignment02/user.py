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


# User Class
class User:
    """
    A class used to represent a user

    Attributes
    ----------
    user_id : int
        an integer to store the user id
    user_name : str
        a string to store the user's name
    user_password : str
        a string to store the user's password
    user_role : str
        a string to store the user's role
    user_status : str
        a string to store the user's status

    Methods
    -------
    generate_user_id():
        Randomly generate a unique user_id
    encrypt(user_password):
        Return the encrypted user_password
    login(user_name, user_password):
        Allowing the user to log in with their credentials
    """
    def __init__(self, user_id=None, user_name=None, user_password=None, user_role=None, user_status=None):
        """
        :param user_id: int
            The id of the user (default is None)
            Must be unique integer
        :param user_name: str
            The name of the user (default is None)
            Must be unique and can only consist of numbers,
                letters, underscores
        :param user_password: str
            The password of the user (default is None)
            Must be encrypted
        :param user_role: str
            The  role of the user (default is None)
            Can only be: 'AD' for 'admin', 'TA' for 'teacher'
                'ST' for 'student'
        :param user_status: str
            The stored user status of the user (default is None)
            Must be either 'enabled' or 'disabled'. Only users
                with 'enabled' status are allowed to log in
        """
        self.user_id = user_id if user_id else self.generate_user_id()
        self.user_name = user_name
        self.user_password = user_password
        self.user_role = user_role
        self.user_status = "enable" if user_status is None else user_status

    def __str__(self):
        """
        :return: A formatted string containing account details
        """
        return f"{self.user_id}, {self.user_name}, {self.user_password}, {self.user_role}, {self.user_status}"

    def generate_user_id(self):
        """
        Generate a unique user id (use random to generate a
            5 digits int number
        :return: new randomly generated user id as a 5 digits integer
        """
        with open('data/user.txt', 'r') as f:
            user_ids = [int(line.strip().split(', ')[0]) for line in f.readlines()]
        user_id = random.randint(10000, 99999)
        while user_id in user_ids:
            user_id = random.randint(10000, 99999)
        return user_id

    def check_username_exist(self, user_name):
        with open('data/user.txt', 'r') as f:
            user_names = [line.strip().split(', ')[1] for line in f.readlines()]
        return user_name in user_names

    def encrypt(self, user_password):
        """
        Encrypt the user provided password with the 2 provided
        strings str_1 and str_2 as encryption character pools

        Encryption steps:
        For each letter in the user-provided password:
            1. Get the ASCII code number of the letter using ord()
            2. Get the remainder of the ASCII code number divided
                by the length of the str_1
            3. Use the remainder as an index to locate a character
                in str_1
            4. Get the remainder of the letter index in the user-provided
                password divided by the length of the str_2
            5. Use the remainder as an index to locate a character in str_2
            6. The characters obtained from step 3 and 5 are used to
                encrypt the letter
        Finally, add "^^^" at the begining and "$$$" at the end of the
        encrypted password to indicate its beginning and ending respectively

        :param user_password: a string which stores user's provided password
        :return: an encrypted password string

        Examples
        --------
        User-provided password: "password"
        Encrypted password string: "^^^Y!J#2$2%6&X(1)M*$$$"

        User-provided password: "abcd1234"
        Encrypted password string: "^^^J!K#L$M%X&Y(Z)1*$$$"
        """
        if user_password is None:
            return None

        str_1 = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"
        str_2 = "!#$%&()*+-./:;<=>?@^_`{|}~"

        encrypted_password = ["^^^"]

        for i, char in enumerate(user_password):
            ascii_code = ord(char)
            remainder_1 = ascii_code % len(str_1)
            encrypted_char_1 = str_1[remainder_1]

            remainder_2 = i % len(str_2)
            encrypted_char_2 = str_2[remainder_2]

            encrypted_password.append(encrypted_char_1)
            encrypted_password.append(encrypted_char_2)

        encrypted_password.append("$$$")

        return ''.join(encrypted_password)

    def login(self, user_name, user_password):
        """
        Authenticate a user login attempt.

        :param user_name: str
            a string to store the user's name
        :param user_password: str
            a string to store the user's provided password
        :return: a user information string (obtained from the 'user.txt' file)
                * If user doesn't exist/status is 'disabled', return None
        """
        # Read the "user.txt" file
        with open("data/user.txt", "r") as file:
            lines = file.readlines()
        # Iterate through each line in the file and check for a matching user
        for line in lines:
            user_data = line.strip().split(", ")
            stored_user_name, stored_user_password, stored_user_status = user_data[1], user_data[2], user_data[4]

            # Check if the user_name and password match and the user is enabled
            if user_name == stored_user_name and stored_user_status == "enabled" and stored_user_password == self.encrypt(user_password):
                return line.strip()

        # Return None if no matching user is found or the user is disabled
        return None

