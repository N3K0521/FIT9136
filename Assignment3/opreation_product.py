import os
import pandas as pd
from model_product import Product
import math
import re
import matplotlib.pyplot as plt


class ProductOperation:
    def extract_products_from_files(self):
        products_lines = []

        # 对pandas的数据按行处理
        def parse_product_from_row(row):
            nonlocal products_lines
            # 提取product
            product = Product(row['id'], row['model'], row['category'], row['name'], row['current_price'],
                              row['raw_price'], row['discount'], row['likes_count'])
            products_lines.append(str(product) + '\n')
        product_source_dir = './data/product'
        # os.listdir获取该目录下所有文件名
        for file_path in os.listdir(product_source_dir):
            # pandas读取csv文件
            data = pd.read_csv(os.path.join(product_source_dir, file_path), encoding='utf-8')
            # 删掉重复行，我发现数据中有重复的
            data.drop_duplicates(inplace=True)
            # 对每一行执行该操作
            data.apply(parse_product_from_row, axis=1)
        with open('./data/products.txt', 'w', encoding='utf-8') as f:
            f.writelines(products_lines)

    def get_product_list(self, page_number):
        products = []
        with open('./data/products.txt', 'r', encoding='utf-8') as f:
            total_num = 0
            for i, line in enumerate(f):
                if (page_number - 1) * 10 <= i < page_number * 10:
                    products.append(self.parse_product_from_line(line.replace('\n', '')))
                total_num += 1
        return products, page_number, math.ceil(total_num / 10)

    def delete_product(self, product_id):
        with open('./data/products.txt', 'r', encoding='utf-8') as f:
            lines = f.readlines()
        deleted = False
        for i, line in enumerate(lines):
            if self.parse_product_from_line(line.replace('\n', '')).pro_id == product_id:
                lines.remove(line)
                deleted = True
        if deleted:
            with open('./data/products.txt', 'w', encoding='utf-8') as f:
                f.writelines(lines)
        return deleted

    def parse_product_from_line(self, product_line):
        # 这个变成了通过一行提取product而不是字典，因为数据中product的name列出现了 单引号，导致eval无法正确处理
        # 通过正则表达式提取product
        product_re = re.compile(r"^\{'pro_id':'(.+)', 'pro_model':'(.+)', 'pro_category':'(.+)', 'pro_name':'(.+)',"
                                r" 'pro_current_price':'(.+)', 'pro_raw_price':'(.+)', 'pro_discount':'(.+)',"
                                r" 'pro_likes_count':'(.+)'\}$")
        product_match = product_re.match(product_line)
        return Product(product_match.group(1), product_match.group(2), product_match.group(3), product_match.group(4),
                       float(product_match.group(5)), float(product_match.group(6)), int(product_match.group(7)),
                       int(product_match.group(8)))

    def get_product_list_by_keyword(self, keyword):
        searched_products = []
        with open('./data/products.txt', 'r', encoding='utf-8') as f:
            for line in f:
                product = self.parse_product_from_line(line.replace('\n', ''))
                if keyword in product.pro_name:
                    searched_products.append(product)
        return searched_products

    def get_product_by_id(self, product_id):
        with open('./data/products.txt', 'r', encoding='utf-8') as f:
            for line in f:
                product = self.parse_product_from_line(line.replace('\n', ''))
                if product_id == product.pro_id:
                    return product
        return None

    def generate_category_figure(self):
        # 种类计数字典 key: category value: count
        category_count = {}
        with open('./data/products.txt', 'r', encoding='utf-8') as f:
            for line in f:
                product = self.parse_product_from_line(line.replace('\n', ''))
                if product.pro_category not in category_count.keys():
                    category_count[product.pro_category] = 1
                else:
                    category_count[product.pro_category] += 1
        # 按计数值大小降序排列
        category_count_items = sorted(category_count.items(), key=lambda x: x[1], reverse=True)
        categories = [x[0] for x in category_count_items]
        counts = [x[1] for x in category_count_items]
        plt.figure(figsize=(12, 8))
        plt.bar(categories, counts)
        plt.title('Category figure')
        plt.xlabel('Category')
        plt.ylabel('Quantity')
        plt.savefig('./data/figure/generate_category_figure.png', dpi=300)
        plt.show()

    def generate_discount_figure(self):
        # 统计<30 30~60 >60的数量
        discount_count = [0, 0, 0]
        with open('./data/products.txt', 'r', encoding='utf-8') as f:
            for line in f:
                product = self.parse_product_from_line(line.replace('\n', ''))
                if product.pro_discount < 30:
                    discount_count[0] += 1
                elif product.pro_discount <= 60:
                    discount_count[1] += 1
                else:
                    discount_count[2] += 1
        total_num = sum(discount_count)
        # 计算比例
        discount_count = [x / total_num for x in discount_count]
        labels = ['<30', '30~60', '>60']  # 饼状图中各部分的标签
        plt.pie(discount_count, labels=labels, autopct='%1.1f%%')
        plt.title('Discount figure')
        plt.savefig('./data/figure/generate_discount_figure.png', dpi=300)
        plt.show()

    def generate_likes_count_figure(self):
        likes_count_count = {}
        with open('./data/products.txt', 'r', encoding='utf-8') as f:
            for line in f:
                product = self.parse_product_from_line(line.replace('\n', ''))
                if product.pro_category not in likes_count_count.keys():
                    likes_count_count[product.pro_category] = product.pro_likes_count
                else:
                    likes_count_count[product.pro_category] += product.pro_likes_count
        category_count_items = sorted(likes_count_count.items(), key=lambda x: x[1])
        categories = [x[0] for x in category_count_items]
        likes_count_counts = [x[1] for x in category_count_items]
        plt.figure(figsize=(12, 8))
        plt.bar(categories, likes_count_counts)
        plt.title('Likes count figure')
        plt.xlabel('Category')
        plt.ylabel('Likes count')
        plt.savefig('./data/figure/generate_likes_count_figure.png', dpi=300)
        plt.show()

    def generate_discount_likes_count_figure(self):
        likes_counts = []
        discounts = []
        with open('./data/products.txt', 'r', encoding='utf-8') as f:
            for line in f:
                product = self.parse_product_from_line(line.replace('\n', ''))
                likes_counts.append(product.pro_likes_count)
                discounts.append(product.pro_discount)
        plt.figure(figsize=(16, 12))
        # 绘制散点图
        plt.scatter(discounts, likes_counts)
        plt.title('Discount likes count figure')
        plt.xlabel('Discount')
        plt.ylabel('Likes count')
        plt.savefig('./data/figure/generate_discount_likes_count_figure.png', dpi=300)
        plt.show()

    def delete_all_products(self):
        # 以w模式打开，就会清空
        with open('./data/products.txt', 'w', encoding='utf-8') as f:
            pass

    def get_all_product_id(self):
        product_ids = []
        product_re = re.compile(r"^\{'pro_id':'(.+)', 'pro_model':'(.+)', 'pro_category':'(.+)', 'pro_name':'(.+)',"
                                r" 'pro_current_price':'(.+)', 'pro_raw_price':'(.+)', 'pro_discount':'(.+)',"
                                r" 'pro_likes_count':'(.+)'\}$")
        with open('./data/products.txt', 'r', encoding='utf-8') as f:
            for line in f:
                product_ids.append(product_re.match(line.replace('\n', '')).group(1))
        return product_ids


if __name__ == '__main__':
    product_operation = ProductOperation()
    product_operation.extract_products_from_files()
    # for product in product_operation.get_product_list(7500)[0]:
    #     print(product)
    # product_operation.delete_product('1094579')
    # product_operation.generate_category_figure()
    # product_operation.generate_discount_figure()
    # product_operation.generate_likes_count_figure()
    # product_operation.generate_discount_likes_count_figure()
    # product_operation.delete_all_products()