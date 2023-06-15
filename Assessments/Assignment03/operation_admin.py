"""
Creation Date: 1st June 2023
Last Modified Date: 3rd June 2023

Student Name: Huixin Wang
Student ID: 31552544
"""

from operation_user import UserOperation
from model_admin import Admin
import time


class AdminOperation:
    """
    Contains all the operations related to the admin

    Methods
    -------
    register_admin():
        Commonly in a system, the admin account should not allow users to
        register by themselves. We add this function to manually create an
        admin account. This function should be called every time you run the
        system. The same admin account should not be registered multiple
        times. In this method, you need to write the admin account info into
        the database.
    """

    def register_admin(self):
        """
        In this system, users are not allowed to register by themselves.
        Admin aacounts will be created manually.
        This function should be called every time the system runs.
        The same admin account should not be registered multiple times.
        The admin account info is directly written into the database.
        :return: None
        """
        user_operation = UserOperation()
        # In this case -> only one admin
        # Only generate an admin if there is no existing admin account
        # If exist -> don't generate
        # username: admin
        # password: admin
        if user_operation.check_username_exist("admin"):
            return
        user_password = user_operation.encrypt_password("admin")
        # Get the current time and convert it into a fixed-format string
        user_register_time = time.strftime("%d-%m-%Y_%H:%M:%S", time.localtime(time.time()))
        admin = Admin(user_operation.generate_unique_user_id(), "admin", user_password, user_register_time, "admin")
        with open('./data/users.txt', 'a', encoding='utf-8') as f:
            f.write(str(admin) + '\n')

