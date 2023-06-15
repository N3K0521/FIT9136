"""
Creation Date: 4th June 2023
Last Modified Date: 9th June 2023

Student Name: Huixin Wang
Student ID: 31552544
"""

from model_order import Order
from model_product import Product
from model_customer import Customer
class IOInterface:
    """
    This Class handles all the I/O operations. All the input(get data from
    users)/output(print out info) should be defined in this class. No
    constructor and __str__methods in this class.

    Methods
    -------
    get_user_input():
        Accept user input.
    main_menu():
        Display the login menu, which includes three options:
        (1) Login
        (2) Register
        (3) Quit
        The admin account cannot be registered.
    admin_menu():
        Display the admin menu, which includes seven options:
        (1). Show products
        (2). Add customers
        (3). Show customers
        (4). Show orders
        (5). Generate test data
        (6). Generate all statistical figures
        (7). Delete all data
        (8). Logout
    customer_menu():
        Display the customer menu, which includes six options:
        (1). Show profile
        (2). Update profile
        (3). Show products (user input could be “3 keyword” or “3”)
        (4). Show history orders
        (5). Generate all consumption figures
        (6). Logout
    show_list():
        Prints out the different types of list. In this system, there are three
        types of lists - “Customer”, “Product” and “Order”. If user_role is
        “customer”, only product list and order list can be displayed. If
        user_role is “admin”, all types of list can be displayed. The output list
        should also show the row number, the page number and the total
        page number.
    print_error_message():
        Prints out an error message and shows where the error occurred. For
        example, when the login has an error, you can call this function
        print_error_message(“UserOperation.login”, “username or password
        incorrect”).
    print_message():
        Print out the given message.
    print_object():
        Print out the object using the str() function.
    """
    def get_user_input(self, message, num_of_args):
        """
        Accept user input.

        *Notes:
        The message is used for the input() function.
        The user inputs have only one format with all the arguments
            connected by a whitespace “ ”. For example, the input could be “arg1
            arg2 arg3…”.
        The num_of_args determines how many arguments can be accepted
            and used. If users input more than num_of_args arguments into the
            system, ignore the others and only use the num_of_args arguments.
            For instance, the num_of_args=3, but user input is “arg1 arg2 arg3
            arg4”. Only use the first 3 args and ignore the last one.

        :param message:str
            input message
        :param num_of_args: int
            the number of user’s input arguments
        :return: list
            The return result is [“arg1”, “arg2”, “arg3”]. If
            the number of user’s input arguments is less
            than the num_of_args, return the rest as
            empty str “”. For example, the
            num_of_args=3, but user input is “arg1 arg2”.
            The return result will be [“arg1”, “arg2”, “”].
        """
        args = input(message).split(' ')
        # Add an empty string if the length is less than num_of_args
        while len(args) <= num_of_args:
            args.append("")
        # see *Notes
        return args[0: num_of_args]

    def main_menu(self):
        """
        Display the login menu, which includes three options: (1) Login, (2)
        Register, and (3) Quit. The admin account cannot be registered.

        :return: None
        """
        print("******** Main Menu ********")
        print("(1). Login")
        print("(2). Register")
        print("(3). Quit")

    def admin_menu(self):
        """
        Display the admin menu, which includes seven options:
        (1). Show products
        (2). Add customers
        (3). Show customers
        (4). Show orders
        (5). Generate test data
        (6). Generate all statistical figures
        (7). Delete all data
        (8). Logout
        :return: None
        """
        print("******** Admin Menu ********")
        print("(1). Show products")
        print('(2). Add customers (user input could be "2 username password email mobile")')
        print("(3). Show customers")
        print("(4). Show orders")
        print("(5). Generate test data")
        print("(6). Generate statistical figures")
        print("(7). Delete all data")
        print("(8). Delete customer using customer id")
        print("(9). Delete order using order id")
        print("(10). Delete product using product id")
        print("(11). Logout")

    def customer_menu(self):
        """
        Display the customer menu, which includes six options:
        (1). Show profile
        (2). Update profile
        (3). Show products (user input could be “3 keyword” or “3”)
        (4). Show history orders
        (5). Generate all consumption figures
        (6). Logout
        :return: None
        """
        print("******** Customer Menu ********")
        print("(1). Show profile")
        print('(2). Update profile')
        print('(3). Show products (user input could be "3 keyboard" or "3")')
        print("(4). Show history orders")
        print("(5). Generate all consumption figures")
        print("(6). Get product using product id")
        print("(7). Logout")

    def show_list(self, user_role, list_type, object_list):
        """
        Prints out the different types of list. In this system, there are three
        types of lists - “Customer”, “Product” and “Order”. If user_role is
        “customer”, only product list and order list can be displayed. If
        user_role is “admin”, all types of list can be displayed. The output list
        should also show the row number, the page number and the total
        page number.
        :param user_role: str
            User role
        :param list_type: str
            type of list (customer, produce and order)
        :param object_list: list
            object_list (the format is [[Customer1,
            Customer2, …Customer10], page_number,
            total_page]. For product and order, the format
            is similar)
        :return: None
        """
        if user_role not in ["admin", "customer"]:
            raise ValueError()
        if list_type not in [Customer, Product, Order]:
            raise ValueError()
        # customer can't check other customer
        if user_role == "customer" and list_type == Customer:
            raise ValueError()
        objects, page_number, total_page_number = object_list
        if objects and not isinstance(objects[0], list_type):
            raise ValueError()
        print(f"Current page: {page_number}, Total page: {total_page_number}")
        for i, o in enumerate(objects):
            print(f"{i + 1}.{str(o)}")

    def print_error_message(self, error_source, error_message):
        """
        Prints out an error message and shows where the error occurred. For
        example, when the login has an error, you can call this function
        print_error_message(“UserOperation.login”, “username or password
        incorrect”).
        :return: None
        """
        print(f"Error in {error_source}: {error_message}")

    def print_message(self, message):
        """
        Print out the given message.
        :return: None
        """
        print(message)

    def print_object(self, target_object):
        """
        Print out the object using the str() function.
        :return: None
        """
        print(str(target_object))

