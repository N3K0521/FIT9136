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
from user import User
from user_teacher import UserTeacher
from user_student import UserStudent
class UserAdmin(User):
    """
    A class used to store the Admin details

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
    admin_menu():
        Display admin operations menu
    search_user(user_name):
        Search for a user using user_name in "data/user.txt"
    list_all_users():
        List all users from "data/user.txt"
    list_all_units():
        List all units from "data/unit.txt"
    enable_disable_user(user_name):
        Update user status (enabled/disabled) in "data/user.txt"
    add_user(user_obj):
        Add a user (UserTeacher or UserStudent instance) to "data/user.txt"
    delete_user(user_name):
        Delete a user using user_name from "data/user.txt"
    """
    def __init__(self, user_id=1, user_name="admin", user_password="password", user_role="AD", user_status="enabled"):
        """
        :param user_id: int
            The id of the user (default is 1)
        :param user_name: str
            The name of the user (default is "admin")
        :param user_password: str
            The password of the user (default is "password")
        :param user_role: str
            The  role of the user (default is "AD")
        :param user_status: str
            The stored user status of the user (default is "enabled")

        :return: a string in the format: "user_id, user_name, user_password, user_role, user_status"
        """
        super().__init__(user_id, user_name, user_password, user_role, user_status)
        self.user_name = "AD"
        # create a new list to store the users
        self.users = []
        # read the file
        # alternative:
        # f = open("data/user.txt", "r")
        # lines = f.readlines()
        with open('data/user.txt', 'r') as f:
            lines = f.readlines()
        # split the line
        for line in lines:
            words = line.strip().split(', ')
            # determine the role of the user from the list words: words[3]
            if words[3] == 'AD':
                self.users.append(User(int(words[0]), words[1], words[2], words[3], words[4]))
            # if the user is a student/teacher, the enrolled/teaching units may be added
            elif words[3] == 'TA':
                self.users.append(UserTeacher(int(words[0]), words[1], words[2], words[3], words[4], eval(', '.join(words[5:]))))
            elif words[3] == 'ST':
                self.users.append(UserStudent(int(words[0]), words[1], words[2], words[3], words[4], eval(', '.join(words[5:]))))

    def __str__(self):
        return super().__str__()

    def admin_menu(self):
        """
        Display admin operations menu
        """

        print('-' * 50)
        # Greeting
        print("Hello, welcome to the student information management system. ")

        # Option 1: search user
        print("1. Search User")
        # Option 2: list all users
        print("2. List All Users")
        # Option 3: list all units
        print("3. List All Units")
        # Option 4: enable/disable user
        print("4. Enable/Disable User")
        # Option 5: add user
        print("5. Add User")
        # Option 6: delete user
        print("6. Delete User")
        # Option 7: logout
        print("7. Log out")

    def search_user(self, user_name):
        """
        Display the information of the user found by the search

        :param user_name: str
            A username that needs to be searched in the user.txt
        """
        for user in self.users:
            if user.user_name == user_name:
                print(user)
                break
        print('User not found!')

    def list_all_users(self):
        """
        Display the information of all users currently stored in the system
        :param: None
        :return: None
        """
        for user in self.users:
            print(user)

    def list_all_units(self):
        """
        Display the information of all units currently stored in the system
        :param: None
        :return: None
        """
        # List all units from "data/unit.txt"
        with open("data/unit.txt", "r") as file:
            for line in file:
                print(line.strip())

    def enable_disable_user(self, user_name):
        """
        Update a user's status by changing it from enabled to disabled or
        from disabled to enabled, depending on the user's current status
        :param user_name: str
            A username that needs to be searched in the user.txt
        :return: None
        """
        # Update user status (enabled/disabled) in "data/user.txt"
        updated = False
        for user in self.users:
            if user.user_name == user_name:
                user.user_status = 'enabled' if user.user_status == 'disable' else 'disable'
                print('Done...')
                updated = True
                break
        if updated:
            with open("data/user.txt", "w") as file:
                for user in self.users:
                    file.write(str(user) + "\n")
        else:
            print('User not found!')

    def add_user(self, user_obj):
        """
        Add a user to the system. All the users should be persisted to the user.txt file
        :param user_obj: An instance of the UserTeacher or UserStudent class
        :return: None
        """
        # Add a user (UserTeacher or UserStudent instance) to "data/user.txt"
        self.users.append(user_obj)
        with open("data/user.txt", "a") as file:
            file.write(str(user_obj) + "\n")
        print('New user added!')

    def delete_user(self, user_name):
        """
        Delete the user that was found by the search.
        :param user_name: str
            A username that needs to be searched in the user.txt
        :return: None
        """
        # Delete a user using user_name from "data/user.txt"
        deleted = False
        for user in self.users:
            if user.user_name == user_name:
                self.users.remove(user)
                deleted = True
                break
        if deleted:
            with open("data/user.txt", "w") as file:
                for user in self.users:
                    file.write(str(user) + "\n")
            print('User deleted!')
        else:
            print("User not found.")
