"""
Creation Date: 3rd June 2023
Last Modified Date: 4th June 2023

Student Name: Huixin Wang
Student ID: 31552544
"""

import re
from operation_user import UserOperation
from model_customer import Customer
import time
import math

class CustomerOperation:
    """
    Contains all the operations related to the customer.

    Methods
    -------
    validate_email():
        Validate the provided email address format. An email address
        consists of four parts
    validate_mobile():
        Validate the provided mobile number format. The mobile number
        should be exactly 10 digits long, consisting only of numbers, and
        starting with either '04' or '03'.
    register_customer():
        Save the information of the new customer into the data/users.txt file.
    update_profile():
        Update the given customer object’s attribute value. According to
        different attributes, it is necessary to perform the validations to
        control the input value. If the input value is invalid, return false. If it is
        a valid input, the changes should be written into the data/users.txt
        file immediately.
    delete_customer():
        Delete the customer from the data/users.txt file based on the
        provided customer_id.
    get_customer_list():
        Retrieve one page of customers from the data/users.txt. One page
        contains a maximum of 10 customers.
    delete_all_customers():
        Removes all the customers from the data/users.txt file.

    """
    def validate_email(self, user_email):
        """
        Validate the provided email address format. An email address
        consists of four parts
        :param user_email: str
            user provided email
        :return: Boolean True/False
            return True if the email is validated, else return False
        """
        # email address re expression
        # The pattern is to match x@y.z
        email_re = re.compile(r'^[0-9a-zA-Z_]+@.+\..+$')
        return email_re.match(user_email) is not None

    def validate_mobile(self, user_mobile):
        """
        Validate the provided mobile number format. The mobile number
        should be exactly 10 digits long, consisting only of numbers, and
        starting with either '04' or '03'.
        :param user_mobile: str
            user provided mobile number
        :return: Boolean True/False
            return True if the mobile number format is validated, else return False
        """
        # mobile phone number re expression
        # start with '04' or '03', following by 8 digits
        mobile_re = re.compile(r'^0[34]\d{8}$')
        return mobile_re.match(user_mobile) is not None

    def register_customer(self, user_name, user_password, user_email, user_mobile):
        """
        Save the information of the new customer into the data/users.txt file.
        Need to apply validations in this method to make sure all the values
            are valid. If not, return false
        If the user_name exists in the database, return False
        A unique user id is required when registering a new user.
        Register time can be obtained by using the time library
        If the user registers successfully, return true and write the customer
            info into the database (the data/users.txt file) in the same format as
            the str() method of the customer class.

        :param user_name: str
            user's provided name
        :param user_password: str
            user's provided password
        :param user_email: str
            user's provided email
        :param user_mobile: str
            user's provided mobile
        :return: Boolean True/False
            return True if the registration success, if failure, return False
        """
        user_operation = UserOperation()
        if not user_operation.validate_username(user_name) or user_operation.check_username_exist(user_name):
            raise ValueError("Invalid username or the username exists!")
        if not user_operation.validate_password(user_password):
            raise ValueError("Invalid password!")
        if not self.validate_email(user_email):
            raise ValueError("Invalid email!")
        if not self.validate_mobile(user_mobile):
            raise ValueError("Invalid mobile!")
        user_password = user_operation.encrypt_password(user_password)
        user_id = user_operation.generate_unique_user_id()
        # if user_id return None -> reach the max of customer
        if user_id is None:
            raise ValueError("The customer capacity is reached!")
        user_register_time = time.strftime("%d-%m-%Y_%H:%M:%S", time.localtime(time.time()))
        new_customer = Customer(user_id, user_name, user_password, user_register_time, 'customer', user_email,
                                user_mobile)
        with open('./data/users.txt', 'a', encoding='utf-8') as f:
            f.write(str(new_customer) + '\n')
        return True

    def update_profile(self, attribute_name, value, customer_object):
        """
        Update the given customer object’s attribute value. According to
        different attributes, it is necessary to perform the validations to
        control the input value. If the input value is invalid, return false. If it is
        a valid input, the changes should be written into the data/users.txt
        file immediately.

        :param attribute_name: str
            customer name
        :param value: str
            customer object's attribute value
        :param customer_object: customer object
        :return: True/False
            return True when update success, if failed, return False
        """
        user_operation = UserOperation()
        # The lambda expression is equivalent to defining a function
        #   named check_username to check user_name
        check_username = lambda x: user_operation.validate_username(x) and not user_operation.check_username_exist(x)
        # Define a dictionary, each key corresponds to a function name corresponding to the validation process
        attribute_names_check_function_dict = {
            'user_name': check_username,
            'user_password': user_operation.validate_password,
            'user_email': self.validate_email,
            'user_mobile': self.validate_mobile
        }
        # if not in 'user_name', 'user_password', 'user_email', 'user_mobile'
        if attribute_name not in attribute_names_check_function_dict.keys():
            return False
        # Call the corresponding method to check:
        #   whether the value to be modified is ok
        if not attribute_names_check_function_dict[attribute_name](value):
            raise ValueError(f"Invalid {attribute_name}!")
        # if changing password, encryption is required
        if attribute_name == 'user_password':
            value = user_operation.encrypt_password(value)
        # setattr assigns values to object attributes
        setattr(customer_object, attribute_name, value)
        with open('./data/users.txt', 'r', encoding='utf-8') as f:
            lines = f.readlines()
        for i, line in enumerate(lines):
            if eval(line.replace('\n', ''))['user_id'] == customer_object.user_id:
                lines[i] = str(customer_object) + '\n'
        with open('./data/users.txt', 'w', encoding='utf-8') as f:
            f.writelines(lines)
        return True

    def delete_customer(self, customer_id):
        """
        Delete the customer from the data/users.txt file based on the
        provided customer_id.

        :param customer_id: str
            provided id
        :return: Boolean True/False
            return True if deleted, if failed, return False
        """
        with open('./data/users.txt', 'r', encoding='utf-8') as f:
            lines = f.readlines()
        for line in lines:
            user_dict = eval(line.replace('\n', ''))
            if user_dict['user_id'] == customer_id:
                # cannot delete admin account (only one admin is set)
                if user_dict['user_role'] == 'admin':
                    raise ValueError("Admin accounts cannot be deleted!")
                lines.remove(line)
                with open('./data/users.txt', 'w', encoding='utf-8') as f:
                    f.writelines(lines)
                return True
        return False

    def get_customer_list(self, page_number):
        """
        Retrieve one page of customers from the data/users.txt. One page
        contains a maximum of 10 customers.

        :param page_number: int
            page number
        :return: tuple
            a tuple including a list of customers objects
            and the total number of pages. For example,
            ([Customer1, Customer2,...., Customer10],
            page_number, total_page).
        """
        user_operation = UserOperation()
        with open('./data/users.txt', 'r', encoding='utf-8') as f:
            lines = f.readlines()
        customers = []
        # Extract customer
        for line in lines:
            user_dict = eval(line.replace('\n', ''))
            if user_dict['user_role'] == 'customer':
                customers.append(user_operation.parse_user_from_userinfo_dict(user_dict))
        total_num = len(customers)
        customers = customers[(page_number - 1) * 10: min(page_number * 10, total_num)]
        # Return the ceiling of x as an Integral.
        # This is the smallest integer >= x
        return customers, page_number, math.ceil(total_num / 10)

    def delete_all_customers(self):
        """
        Removes all the customers from the data/users.txt file.
        :return: None
        """
        with open('./data/users.txt', 'r', encoding='utf-8') as f:
            lines = f.readlines()
        # Filter out rows that are not customers
        lines = [line for line in lines if eval(line.replace('\n', ''))['user_role'] != 'customer']
        with open('./data/users.txt', 'w', encoding='utf-8') as f:
            f.writelines(lines)

