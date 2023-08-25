import math
import random
import time
from model_order import Order
from operation_customer import CustomerOperation
from opreation_product import ProductOperation
import matplotlib.pyplot as plt
class OrderOperation:
    # 和user一样
    def generate_unique_order_id(self):
        with open('./data/orders.txt', 'r', encoding='utf-8') as f:
            order_ids = [eval(line.replace('\n', '')).get('order_id') for line in f.readlines()]
        while True:
            o_id = f'o_{random.randint(0, 99999):05d}'
            if o_id not in order_ids:
                return o_id

    def create_an_order(self, customer_id, product_id, create_time=None):
        if create_time is None:
            create_time = time.strftime("%d-%m-%Y_%H:%M:%S", time.localtime(time.time()))
        order = Order(self.generate_unique_order_id(), customer_id, product_id, create_time)
        with open('./data/orders.txt', 'a', encoding='utf-8') as f:
            f.write(str(order) + '\n')
            return True

    def delete_order(self, order_id):
        with open('./data/orders.txt', 'r', encoding='utf-8') as f:
            lines = f.readlines()
        for line in lines:
            if eval(line.replace('\n', '')).get('order_id') == order_id:
                lines.remove(line)
                with open('./data/orders.txt', 'w', encoding='utf-8') as f:
                    f.writelines(lines)
                return True
        return False

    # 通过字典提取Order对象
    def parse_order_from_dict(self, order_dict):
        return Order(order_dict['order_id'], order_dict['user_id'], order_dict['pro_id'], order_dict['order_time'])

    def get_order_list(self, customer_id, page_number):
        orders = []
        with open('./data/orders.txt', 'r', encoding='utf-8') as f:
            for line in f:
                order_dict = eval(line.replace('\n', ''))
                if order_dict['user_id'] == customer_id:
                    orders.append(self.parse_order_from_dict(order_dict))
        total_num = len(orders)
        return orders[(page_number - 1) * 10: min(page_number * 10, total_num)], page_number, math.ceil(total_num / 10)

    def generate_test_order_data(self):
        customer_operation = CustomerOperation()
        product_operation = ProductOperation()
        with open('./data/users.txt', 'w', encoding='utf-8') as uf, open('./data/orders.txt', 'w', encoding='utf-8') as of:
            pass
        # 生成10个用户
        # userA userA111 xxx0@gmail.com 0300000000
        # userB userB111 xxx1@gmail.com 0300000001
        # ...
        for i in range(10):
            user_name = "user" + chr(ord('A') + i)
            customer_operation.register_customer(user_name, user_name + '111', f'xxx{i}@gmail.com', f'030000000{i}')
        # 一页10个，正好能全提出来
        users, _, _ = customer_operation.get_customer_list(1)
        product_ids = product_operation.get_all_product_id()
        # 1~12月 天数
        days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
        for user in users:
            order_nums = random.randint(50, 200)
            for i in range(order_nums):
                month = random.randint(1, 12)
                day = random.randint(1, days[month - 1])
                create_time = f'{day:02d}-{month:02d}-2023_{random.randint(0, 23):02d}:{random.randint(0, 59):02d}:{random.randint(0, 59):02d}'
                self.create_an_order(user.user_id, random.choice(product_ids), create_time)

    def generate_single_customer_consumption_figure(self, customer_id):
        product_operation = ProductOperation()
        orders = []
        orders_pro_ids = []
        orders_products = []
        # 12个月消费全部初始化为0
        month_prices = [0] * 12
        # 先提取出来订单中需要用到的商品id
        with open('./data/orders.txt', 'r', encoding='utf-8') as of:
            for line in of:
                order = self.parse_order_from_dict(eval(line.replace('\n', '')))
                if order.user_id == customer_id:
                    orders.append(order)
                    orders_pro_ids.append(order.pro_id)
        # 由于商品太多，为了降低查询代价，先把需要的商品提取出来，防止每次都需要在所有商品中查找
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
        # 字典，最终存储的key是product_id， value是出现个数
        products_count = {}
        with open('./data/orders.txt', 'r', encoding='utf-8') as f:
            for line in f:
                order = self.parse_order_from_dict(eval(line.replace('\n', '')))
                if order.pro_id in products_count.keys():
                    products_count[order.pro_id] += 1
                else:
                    products_count[order.pro_id] = 1
        # 按照字典value值由高到低排序，并取前十个
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
        # 以'w'模式打开就会自动清空了
        with open('./data/orders.txt', 'w', encoding='utf-8') as f:
            pass










if __name__ == '__main__':
    operation = OrderOperation()
    # operation.generate_test_order_data()
    # operation.generate_single_customer_consumption_figure('u_9126657332')
    # operation.generate_single_customer_consumption_figure('u_3867557741')
    # operation.generate_all_customers_consumption_figure()
    operation.generate_all_top_10_best_sellers_figure()