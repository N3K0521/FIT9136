"""
Creation Date: 4th June 2023
Last Modified Date: 9th June 2023

Student ID: 31552544
Student Name: Huixin Wang
"""

from model_customer import Customer
from model_product import Product
from model_admin import Admin
from model_order import Order
from io_interface import IOInterface
from operation_user import UserOperation
from operation_customer import CustomerOperation
from operation_admin import AdminOperation
from opreation_product import ProductOperation
from operation_order import OrderOperation

io = IOInterface()
user_operation = UserOperation()
customer_operation = CustomerOperation()
admin_operation = AdminOperation()
product_operation = ProductOperation()
order_operation = OrderOperation()

current_user = None

"""
This is an e-commerce system which allows customers to login to the system, 
perform some shopping operations like purchasing products, viewing
order history and showing user consumption reports. Besides, admin users need to be
created to manage the whole system, who are able to create/delete/view customers,
products and all the orders. Except for the management part, admin users can view the
statistical figures about this system. Since the whole system is executed in the command
line system, this system has a well-formatted interface and always show proper messages 
to guide users. 
"""


def login_control(need_enter=True):
    """
    This function displays the main menu for all users to login, register and quit.
    """
    if need_enter:
        io.get_user_input("Press Enter to continue...", 1)
    global current_user
    io.main_menu()
    sel, = io.get_user_input("Please select: ", 1)
    while sel not in ['1', '2', '3']:
        io.print_message("Invalid input! Please enter again!")
        sel, = io.get_user_input("Please select: ", 1)
    if sel == '1':
        user_name, = io.get_user_input("Enter username: ", 1)
        password, = io.get_user_input("Enter password: ", 1)
        # login success -> return the user, else return None
        current_user = user_operation.login(user_name, password)
        if current_user is None:
            io.print_error_message("UserOperation.login", "username or password incorrect")
            login_control()
        else:
            io.print_message(f"Welcome {current_user.user_name}!")
            # if the user type is customer, launch -> customer control
            # else admin, launch -> admin control
            if isinstance(current_user, Customer):
                customer_control()
            else:
                admin_control()
    elif sel == '2':
        user_name, = io.get_user_input("Enter username: ", 1)
        user_password, = io.get_user_input("Enter password: ", 1)
        user_email, = io.get_user_input("Enter email: ", 1)
        user_mobile, = io.get_user_input("Enter mobile: ", 1)
        try:
            state = customer_operation.register_customer(user_name, user_password, user_email, user_mobile)
            if state:
                io.print_message("Successfully register! Please login!")
        except ValueError as e:
            io.print_error_message("CustomerOperation.register_customer", str(e))
        finally:
            login_control()
    else:
        io.print_message("Successfully quit!")
        exit(0)


def customer_control():
    """
    This function handles the customer functionality by calling the customer menu written
    in the io_interface.py.
    :return: None
    """
    io.get_user_input("Press Enter to continue...", 1)
    global current_user
    io.customer_menu()
    sel, = io.get_user_input("Please select: ", 1)
    while sel not in list('1234567'):
        io.print_message("Invalid input! Please enter again!")
        sel, = io.get_user_input("Please select: ", 1)
    if sel == '1':
        io.print_object(current_user)
        customer_control()
    elif sel == '2':
        io.print_message("The attribute names include 'user_name', 'user_password', 'user_email', 'user_mobile'")
        attribute_name, = io.get_user_input("Enter the attribute name: ", 1)
        value, = io.get_user_input("Enter the updated value: ", 1)
        try:
            if customer_operation.update_profile(attribute_name, value, current_user):
                io.print_error_message("CustomerOperation.update_profile",
                                       f"Attribute names do not include '{attribute_name}'!")
            else:
                io.print_message("Successfully update profile!")
        except ValueError as e:
            io.print_error_message("CustomerOperation.update_profile", str(e))
        customer_control()
    elif sel == '3':
        index, keyword = io.get_user_input("Enter keyword: ", 2)
        if index != '3':
            io.print_message('Invalid input! Your input could be "3 keyboard" or "3"')
        elif keyword == '':
            io.print_message('Invalid input! The keyword is null!')
        else:
            searched_products = product_operation.get_product_list_by_keyword(keyword)
            if not searched_products:
                io.print_message("Nothing found. Try a different search.")
            else:
                for product in searched_products:
                    io.print_object(product)
        customer_control()
    elif sel == '4':
        while True:
            try:
                page_number, = io.get_user_input("Enter page number: ", 1)
                page_number = int(page_number)
                break
            except ValueError as e:
                io.print_message("Please enter a integer! Please enter again!")
        order_list = order_operation.get_order_list(current_user.user_id, page_number)
        io.show_list("customer", Order, order_list)
        customer_control()
    elif sel == '5':
        order_operation.generate_single_customer_consumption_figure(current_user.user_id)
        customer_control()
    elif sel == '6':
        product_id, = io.get_user_input("Enter product id: ", 1)
        product = product_operation.get_product_by_id(product_id)
        if product is None:
            io.print_error_message("ProductOperation.get_product_by_id", "No such product!")
        else:
            io.print_object(product)
        customer_control()
    else:
        current_user = None
        io.print_message("Successfully logout!")
        login_control()


def admin_control():
    """
    This function handles the admin functionality by calling the admin menu written
    in the io_interface.py.
    :return: None
    """
    io.get_user_input("Press Enter to continue...", 1)
    global current_user
    io.admin_menu()
    sel, = io.get_user_input("Please select: ", 1)
    while sel not in [str(x) for x in range(1, 12)]:
        io.print_message("Invalid input! Please enter again!")
        sel, = io.get_user_input("Please select: ", 1)
    if sel == '1':
        while True:
            try:
                page_number, = io.get_user_input("Enter page number: ", 1)
                page_number = int(page_number)
                break
            except ValueError as e:
                io.print_message("Please enter a integer! Please enter again!")
        product_list = product_operation.get_product_list(page_number)
        io.show_list("admin", Product, product_list)
        admin_control()
    elif sel == '2':
        index, username, password, email, mobile = io.get_user_input("Enter customers information: ", 5)
        if index != '2':
            io.print_message('Invalid input! Your input could be start with "2"')
        else:
            try:
                state = customer_operation.register_customer(username, password, email, mobile)
                if state:
                    io.print_message("Successfully add a new customer!")
            except ValueError as e:
                io.print_error_message("CustomerOperation.register_customer", str(e))
        admin_control()
    elif sel == '3':
        while True:
            try:
                page_number, = io.get_user_input("Enter page number: ", 1)
                page_number = int(page_number)
                break
            except ValueError as e:
                io.print_message("Please enter a integer! Please enter again!")
        customer_list = customer_operation.get_customer_list(page_number)
        io.show_list("admin", Customer, customer_list)
        admin_control()
    elif sel == '4':
        customer_id, = io.get_user_input("Enter customer id: ", 1)
        while True:
            try:
                page_number, = io.get_user_input("Enter page number: ", 1)
                page_number = int(page_number)
                break
            except ValueError as e:
                io.print_message("Please enter a integer! Please enter again!")
        order_list = order_operation.get_order_list(customer_id, page_number)
        io.show_list("admin", Order, order_list)
        admin_control()
    elif sel == '5':
        product_operation.extract_products_from_files()
        io.print_message("Finish extracting products from files!")
        order_operation.generate_test_order_data()
        io.print_message("Finish generate customers and orders!")
        admin_operation.register_admin()
        io.print_message("Finish adding admin!")
        io.print_message("Finish generating all test data!")
        admin_control()
    elif sel == '6':
        product_operation.generate_category_figure()
        io.print_message("Category figure saved!")
        product_operation.generate_discount_figure()
        io.print_message("Discount figure saved!")
        product_operation.generate_likes_count_figure()
        io.print_message("Likes count figure saved!")
        product_operation.generate_discount_likes_count_figure()
        io.print_message("Discount likes count figure saved!")
        order_operation.generate_all_customers_consumption_figure()
        io.print_message("All customers consumption figure saved!")
        order_operation.generate_all_top_10_best_sellers_figure()
        io.print_message("All top 10 best sellers figure saved!")
        io.print_message("Finish generating all statistical figures!")
        admin_control()
    elif sel == '7':
        customer_operation.delete_all_customers()
        io.print_message("Finish deleting all customers!")
        product_operation.delete_all_products()
        io.print_message("Finish deleting all products!")
        order_operation.delete_all_orders()
        io.print_message("Finish deleting all orders!")
        io.print_message("Finish deleting all data!")
        admin_control()
    elif sel == '8':
        customer_id, = io.get_user_input("Enter customer id: ", 1)
        try:
            if customer_operation.delete_customer(customer_id):
                io.print_message(f"Successfully delete customer whose id is '{customer_id}'！")
            else:
                io.print_message(f"No such customer whose id is '{customer_id}'!")
        except ValueError as e:
            io.print_error_message("CustomerOperation.delete_customer", str(e))
        admin_control()
    elif sel == '9':
        order_id, = io.get_user_input("Enter order id: ", 1)
        if order_operation.delete_order(order_id):
            io.print_message(f"Successfully delete the '{order_id}' order!")
        else:
            io.print_message(f"No such order, which id is '{order_id}'")
        admin_control()
    elif sel == '10':
        product_id, = io.get_user_input("Enter product id: ", 1)
        if product_operation.delete_product(product_id):
            io.print_message(f"Successfully delete the '{product_id}' product!")
        else:
            io.print_message(f"No such product, which id is '{product_id}'")
        admin_control()
    else:
        current_user = None
        io.print_message("Successfully logout!")
        login_control()


def main():
    """
    Examples
    --------

    >>> ******** Main Menu ********
        (1). Login
        (2). Register
        (3). Quit
        Please select: 1
        Enter username: admin
        Enter password: nimda
        Error in UserOperation.login: username or password incorrect
        Press Enter to continue...

    >>> ******** Main Menu ********
        (1). Login
        (2). Register
        (3). Quit
        Please select: 1
        Enter username: admin
        Enter password: admin
        Welcome admin!
        Press Enter to continue...
        ******** Admin Menu ********
        (1). Show products
        (2). Add customers (user input could be "2 username password email mobile")
        (3). Show customers
        (4). Show orders
        (5). Generate test data
        (6). Generate statistical figures
        (7). Delete all data
        (8). Delete customer using customer id
        (9). Delete order using order id
        (10). Delete product using product id
        (11). Logout
        Please select:

    :return: None
    """
    # register an admin account first
    admin_operation.register_admin()
    login_control(need_enter=False)


if __name__ == '__main__':
    main()
