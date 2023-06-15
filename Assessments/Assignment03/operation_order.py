"""
Creation Date: 4th June 2023
Last Modified Date: 9th June 2023

Student Name: Huixin Wang
Student ID: 31552544
"""

import math
import random
import time
from model_order import Order
from operation_customer import CustomerOperation
from opreation_product import ProductOperation
import matplotlib.pyplot as plt

class OrderOperation:
    """
    Contains all the operations related to the order

    Methods
    -------
    def generate_unique_order_id():
        This method is used to generate and return a 5 digit unique order id
        starting with "o_" every time when a new order is created. All the
        order information is saved inside the database. It is required to check
        this file when generating a new order id to make sure there is no
        duplicate.
    create_an_order():
        Every time creating a new order, a unique order id needs to be
        generated. Use the time library to get the current time. The order
        data is saved into the data/orders.txt file.
    delete_order():
        This method deletes the order info from the data/orders.txt file
        based on the provided order_id.
    def get_order_list():
        This method retrieves one page of orders from the database which
        belongs to the given customer. One page contains a maximum of 10
        items.
    def generate_test_order_data():
        Since manually inputting multiple order data is time-consuming, we
        use this method to automatically generate some test data. In this
        method, 10 customers will be created and 50-200 orders for each customer
        will be randomly generated. The order time for each order will be controled
        and the time will be scattered into different 12 months of the year.
        The product of each order is obtained randomly from the database.
        This function will reuse functions defined in previous tasks.
    def generate_single_customer_consumption_figure():
        Generate a graph to show the consumption (sum of order price) of
        12 different months (only consider month value, ignore yeear) for
        the given customer.
    def generate_all_customers_consumption_figure():
        Generate a graph to show the consumption (sum of order price)
        of 12 different months (only consider month value, ignore year)
        for all customers.
    def generate_all_top_10_best_sellers_figure(self):
        Generate a graph to sho the top 10 best-selling products and sort
        the result in descending order.
    delete_all_orders():
        Removes all the data in the data/orders.txt file.
    """
    def generate_unique_order_id(self):
        """
        This method is used to generate and return a 5 digit unique
        order id starting with "o_" every time when a new order is
        created. All the order information is saved inside the database.
        It is required to check this file when generating a new order id
        to make sure there is no duplicate
        :return: str
            This method returns a string result such as o_12345
        """
        with open('./data/orders.txt', 'r', encoding='utf-8') as f:
            order_ids = [eval(line.replace('\n', '')).get('order_id') for line in f.readlines()]
        while True:
            o_id = f'o_{random.randint(0, 99999):05d}'
            if o_id not in order_ids:
                return o_id

    def create_an_order(self, customer_id, product_id, create_time=None):
        """
        Every time creating a new order, a unique order id needs to be
        generated. Use the time library to get the current time. The order
        data is saved into the data/orders.txt file.
        :param customer_id: str
            customer id
        :param product_id: str
            product id
        :param create_time: time
            the current time if time is not provided
        :return: Boolean True/False
            Return true if an order is create.
        """
        if create_time is None:
            create_time = time.strftime("%d-%m-%Y_%H:%M:%S", time.localtime(time.time()))
        order = Order(self.generate_unique_order_id(), customer_id, product_id, create_time)
        with open('./data/orders.txt', 'a', encoding='utf-8') as f:
            f.write(str(order) + '\n')
            return True

    def delete_order(self, order_id):
        """
        This method deletes the order info from the data/orders.txt file
        based on the provided order_id.
        :param order_id: str
            order id
        :return: Boolean True/False
            return True if the order is deleted, else return False
        """
        with open('./data/orders.txt', 'r', encoding='utf-8') as f:
            lines = f.readlines()
        for line in lines:
            if eval(line.replace('\n', '')).get('order_id') == order_id:
                lines.remove(line)
                with open('./data/orders.txt', 'w', encoding='utf-8') as f:
                    f.writelines(lines)
                return True
        return False

    # dictionary to extract Order object
    def parse_order_from_dict(self, order_dict):
        return Order(order_dict['order_id'], order_dict['user_id'], order_dict['pro_id'], order_dict['order_time'])

    def get_order_list(self, customer_id, page_number):
        """
        This method retrieves one page of orders from the database which
        belongs to the given customer. One page contains a maximum of 10
        items.
        :param customer_id: str
            customer id
        :param page_number: int
            page number
        :return: tuple
            This function returns a tuple including a list of order objects
            and the total number of pages. For example, ([Order(), Order(),
            Order()...], page_number, total_page)
        """
        orders = []
        with open('./data/orders.txt', 'r', encoding='utf-8') as f:
            for line in f:
                order_dict = eval(line.replace('\n', ''))
                if order_dict['user_id'] == customer_id:
                    orders.append(self.parse_order_from_dict(order_dict))
        total_num = len(orders)
        return orders[(page_number - 1) * 10: min(page_number * 10, total_num)], page_number, math.ceil(total_num / 10)

    def generate_test_order_data(self):
        """
        Since manually inputting multiple order data is time-consuming, we
        use this method to automatically generate some test data. In this
        method, 10 customers will be created and 50-200 orders for each customer
        will be randomly generated. The order time for each order will be controled
        and the time will be scattered into different 12 months of the year.
        The product of each order is obtained randomly from the database.
        This function will reuse functions defined in previous tasks.
        :return: Nonw
        """
        customer_operation = CustomerOperation()
        product_operation = ProductOperation()
        with open('./data/users.txt', 'w', encoding='utf-8') as uf, open('./data/orders.txt', 'w',
                                                                         encoding='utf-8') as of:
            pass
        # Generate 10 customers
        # userA userA111 xxx0@gmail.com 0300000000
        # userB userB111 xxx1@gmail.com 0300000001
        # ...
        for i in range(10):
            user_name = "user" + chr(ord('A') + i)
            customer_operation.register_customer(user_name, user_name + '111', f'xxx{i}@gmail.com', f'030000000{i}')
        # 10 in one page -> all can be extracted
        users, _, _ = customer_operation.get_customer_list(1)
        product_ids = product_operation.get_all_product_id()
        # the number of days in January - December
        days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
        for user in users:
            order_nums = random.randint(50, 200)
            for i in range(order_nums):
                month = random.randint(1, 12)
                day = random.randint(1, days[month - 1])
                create_time = f'{day:02d}-{month:02d}-2023_{random.randint(0, 23):02d}:{random.randint(0, 59):02d}:{random.randint(0, 59):02d}'
                self.create_an_order(user.user_id, random.choice(product_ids), create_time)

    def generate_single_customer_consumption_figure(self, customer_id):
        """
        Generate a graph to show the consumption (sum of order price) of
        12 different months (only consider month value, ignore yeear) for
        the given customer.
        :param customer_id: str
            customer id
        :return: None
        """
        product_operation = ProductOperation()
        orders = []
        orders_pro_ids = []
        orders_products = []
        # 12 month prices set as default 0
        month_prices = [0] * 12
        # Extract the product id needed in the order
        with open('./data/orders.txt', 'r', encoding='utf-8') as of:
            for line in of:
                order = self.parse_order_from_dict(eval(line.replace('\n', '')))
                if order.user_id == customer_id:
                    orders.append(order)
                    orders_pro_ids.append(order.pro_id)
        # Too many products
        # For efficiency, extract only the needed products
        # -> don't have to look it up everytime
        with open('./data/products.txt', 'r', encoding='utf-8') as pf:
            for line in pf:
                product = product_operation.parse_product_from_line(line.replace('\n', ''))
                if product.pro_id in orders_pro_ids:
                    orders_products.append(product)
        for order in orders:
            for product in orders_products:
                if product.pro_id == order.pro_id:
                    month_prices[order.month - 1] += product.pro_current_price
                    break
        plt.figure(figsize=(12, 8))
        plt.bar(range(1, 13), month_prices)
        plt.title('Generate single customer consumption figure')
        plt.xlabel('month')
        plt.ylabel('price')
        plt.xticks(range(1, 13))
        plt.savefig('./data/figure/generate_single_customer_consumption_figure.png', dpi=300)
        plt.show()

    def generate_all_customers_consumption_figure(self):
        """
        Generate a graph to show the consumption (sum of order price)
        of 12 different months (only consider month value, ignore year)
        for all customers.
        :return: None
        """
        product_operation = ProductOperation()
        orders = []
        orders_pro_ids = []
        orders_products = []
        month_prices = [0] * 12
        with open('./data/orders.txt', 'r', encoding='utf-8') as of:
            for line in of:
                order = self.parse_order_from_dict(eval(line.replace('\n', '')))
                orders.append(order)
                orders_pro_ids.append(order.pro_id)
        with open('./data/products.txt', 'r', encoding='utf-8') as pf:
            for line in pf:
                product = product_operation.parse_product_from_line(line.replace('\n', ''))
                if product.pro_id in orders_pro_ids:
                    orders_products.append(product)
        for order in orders:
            for product in orders_products:
                if product.pro_id == order.pro_id:
                    month_prices[order.month - 1] += product.pro_current_price
                    break
        plt.figure(figsize=(12, 8))
        plt.bar(range(1, 13), month_prices)
        plt.title('Generate all customers consumption figure')
        plt.xlabel('month')
        plt.ylabel('price')
        plt.xticks(range(1, 13))
        plt.savefig('./data/figure/generate_all_customers_consumption_figure.png', dpi=300)
        plt.show()

    def generate_all_top_10_best_sellers_figure(self):
        """
        Generate a graph to sho the top 10 best-selling products and sort
        the result in descending order.
        :return: None
        """
        # dict -> key: product_id, value: ordered times (appear times in orders)
        products_count = {}
        with open('./data/orders.txt', 'r', encoding='utf-8') as f:
            for line in f:
                order = self.parse_order_from_dict(eval(line.replace('\n', '')))
                if order.pro_id in products_count.keys():
                    products_count[order.pro_id] += 1
                else:
                    products_count[order.pro_id] = 1
        # Sort from high -> low, only extract the first 10
        products_count_item = sorted(products_count.items(), key=lambda x: x[1], reverse=True)[0: 10]
        products_ids = [x[0] for x in products_count_item]
        counts = [x[1] for x in products_count_item]
        plt.figure(figsize=(12, 8))
        plt.bar(products_ids, counts)
        plt.title('Generate all top 10 best sellers figure')
        plt.xlabel('product-id')
        plt.ylabel('count')
        plt.savefig('./data/figure/generate_all_top_10_best_sellers_figure.png', dpi=300)
        plt.show()

    def delete_all_orders(self):
        """
        Removes all the data in the data/orders.txt file.
        :return: None
        """
        # open with "w" -> clear the file automatically
        with open('./data/orders.txt', 'w', encoding='utf-8') as f:
            pass
