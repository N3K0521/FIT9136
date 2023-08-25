from model_order import Order
from model_product import Product
from model_customer import Customer


class IOInterface:

    def get_user_input(self, message, num_of_args):
        args = input(message).split(' ')
        # 长度不足num_of_args则添加空字符串
        while len(args) <= num_of_args:
            args.append("")
        # 返回前num_of_args个
        return args[0: num_of_args]

    def main_menu(self):
        print("******** Main Menu ********")
        print("(1). Login")
        print("(2). Register")
        print("(3). Quit")

    def admin_menu(self):
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
        print("******** Customer Menu ********")
        print("(1). Show profile")
        print('(2). Update profile')
        print('(3). Show products (user input could be "3 keyboard" or "3")')
        print("(4). Show history orders")
        print("(5). Generate all consumption figures")
        print("(6). Get product using product id")
        print("(7). Logout")

    def show_list(self, user_role, list_type, object_list):
        if user_role not in ["admin", "customer"]:
            raise ValueError()
        if list_type not in [Customer, Product, Order]:
            raise ValueError()
        # customer没有权限查看其他customer
        if user_role == "customer" and list_type == Customer:
            raise ValueError()
        objects, page_number, total_page_number = object_list
        if objects and not isinstance(objects[0], list_type):
            raise ValueError()
        print(f"Current page: {page_number}, Total page: {total_page_number}")
        for i, o in enumerate(objects):
            print(f"{i + 1}.{str(o)}")

    def print_error_message(self, error_source, error_message):
        print(f"Error in {error_source}: {error_message}")

    def print_message(self, message):
        print(message)

    def print_object(self, target_object):
        print(str(target_object))


if __name__ == '__main__':
    io_interface = IOInterface()
    print(io_interface.get_user_input("args1 args2 args3", 4))
    print(io_interface.get_user_input("args1 args2 args3", 3))
    print(io_interface.get_user_input("args1 args2 args3", 2))
    io_interface.main_menu()
    io_interface.admin_menu()
    io_interface.customer_menu()
    # from opreation_product import ProductOperation
    # product_operation = ProductOperation()
    # product_list = product_operation.get_product_list(1)
    # io_interface.show_list("admin", Customer, product_list)
    io_interface.print_error_message("User.login", "incorrect")
    io_interface.print_message("ok")
    io_interface.print_object(Customer())
