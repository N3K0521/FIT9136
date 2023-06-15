"""
Creation Date: 4th June 2023
Last Modified Date: 6th June 2023

Student Name: Huixin Wang
Student ID: 31552544
"""

import os
import pandas as pd
from model_product import Product
import math
import re
import matplotlib.pyplot as plt

class ProductOperation:
    """
    Contains all the operations related to the product.

    Methods
    -------
    extract_products_from_files():
        Extracts product information from the given product data files
    get_product_list():
        This method retrieves one page of products from the database. One
        page contains a maximum of 10 items from data/products.txt file.
    delete_product():
        This method can delete the product info from the system (i.e.,
        data/products.txt) based on the provided product_id.
    get_product_list_by_keyword():
        This method retrieves all the products whose name contains the
        keyword (case insensitive).
    get_product_by_id():
        This method returns one product object based on the given
        product_id.
    generate_category_figure():
        This method generates a bar chart that shows the total number of
        products for each category in descending order. The figure is saved
        into the data/figure folder.
    generate_discount_figure():
        This method generates a pie chart that shows the proportion of
        products that have a discount value less than 30, between 30 and 60
        inclusive, and greater than 60. The figure is saved into the data/figure
        folder.
    generate_likes_count_figure():
        This method generates a chart (you think is the most suitable)
        displaying the sum of products’ likes_count for each category in
        ascending order. The figure is saved into the data/figure folder.
    generate_discount_likes_count_figure():
        This method generates a scatter chart showing the relationship
        between likes_count and discount for all products. The figure is saved
        into the data/figure folder.
    delete_all_products():
        This method removes all the product data in the data/products.txt
        file.
    """
    def extract_products_from_files(self):
        """
        Extracts product information from the given product data files. The
        data files are csv files (in source/*.csv) which contain many
        attributes. We only retrieve the necessary data based on the Product
        class design. The data format is “{‘pro_id’:’xxx’, ‘pro_model’:’xxx’,
        ‘pro_category’:’xxx’, ‘pro_name’:’xxx’, ‘pro_current_price’:’xxx’,
        ‘pro_raw_price’:’xxx’, ‘pro_discount’:’xxx’, ‘pro_likes_count’:’xxx’}”.
        The data is saved into the data/products.txt file. The
        data/products.txt file will be used as the file storing all the product
        information.
        :return: None
        """
        products_lines = []

        # Process pandas data by row
        def parse_product_from_row(row):
            """
            Process pandas data by row
            :param row: row in the data
            :return: None
            """
            nonlocal products_lines
            # Extract product
            product = Product(row['id'], row['model'], row['category'], row['name'], row['current_price'],
                              row['raw_price'], row['discount'], row['likes_count'])
            products_lines.append(str(product) + '\n')
        product_source_dir = './data/product'
        # os.listdir - Get all file names in this directory
        for file_path in os.listdir(product_source_dir):
            # pandas - read csv files
            data = pd.read_csv(os.path.join(product_source_dir, file_path), encoding='utf-8')
            # remove duplicates since there are duplicate data in the file
            data.drop_duplicates(inplace=True)
            # do the same process to each row
            data.apply(parse_product_from_row, axis=1)
        with open('./data/products.txt', 'w', encoding='utf-8') as f:
            f.writelines(products_lines)

    def get_product_list(self, page_number):
        """
        This method retrieves one page of products from the database. One
        page contains a maximum of 10 items from data/products.txt file.
        :param page_number:
            page number
        :return: tuple
            A tuple including a list of products objects and
            the total number of pages. For example,
            ([Product1,Product2,Product3,...Product10],p
            age_number, total_page).
        """
        products = []
        with open('./data/products.txt', 'r', encoding='utf-8') as f:
            total_num = 0
            for i, line in enumerate(f):
                if (page_number - 1) * 10 <= i < page_number * 10:
                    products.append(self.parse_product_from_line(line.replace('\n', '')))
                total_num += 1
        return products, page_number, math.ceil(total_num / 10)

    def delete_product(self, product_id):
        """
        This method can delete the product info from the system (i.e.,
        data/products.txt) based on the provided product_id.
        :param product_id: str
            product_id
        :return: Boolean True/False
            return True if successfully delete, else return False
        """
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
        """
        This becomes extracting product from each row instead of dict
        Because there are single quotes in the name column of product in the data
        which causes eval() can't be used.
        Using re expression to extract product.
        """
        product_re = re.compile(r"^\{'pro_id':'(.+)', 'pro_model':'(.+)', 'pro_category':'(.+)', 'pro_name':'(.+)',"
                                r" 'pro_current_price':'(.+)', 'pro_raw_price':'(.+)', 'pro_discount':'(.+)',"
                                r" 'pro_likes_count':'(.+)'\}$")
        product_match = product_re.match(product_line)
        return Product(product_match.group(1), product_match.group(2), product_match.group(3), product_match.group(4),
                       float(product_match.group(5)), float(product_match.group(6)), int(product_match.group(7)),
                       int(product_match.group(8)))

    def get_product_list_by_keyword(self, keyword):
        """
        This method retrieves all the products whose name contains the
        keyword (case insensitive).
        :param keyword: str
            keyword inserted
        :return: list
            The return result will be a list of product
            objects. No page limitation
        """
        searched_products = []
        with open('./data/products.txt', 'r', encoding='utf-8') as f:
            for line in f:
                product = self.parse_product_from_line(line.replace('\n', ''))
                if keyword in product.pro_name:
                    searched_products.append(product)
        return searched_products

    def get_product_by_id(self, product_id):
        """
        This method returns one product object based on the given
        product_id.
        :param product_id: str
            product_id
        :return: product object/None
             A product object or None if cannot be found.
        """
        with open('./data/products.txt', 'r', encoding='utf-8') as f:
            for line in f:
                product = self.parse_product_from_line(line.replace('\n', ''))
                if product_id == product.pro_id:
                    return product
        return None

    def generate_category_figure(self):
        """
        This method generates a bar chart that shows the total number of
        products for each category in descending order. The figure is saved
        into the data/figure folder.
        :return: None
        """
        # category count dictionary key: category value: count
        category_count = {}
        with open('./data/products.txt', 'r', encoding='utf-8') as f:
            for line in f:
                product = self.parse_product_from_line(line.replace('\n', ''))
                if product.pro_category not in category_count.keys():
                    category_count[product.pro_category] = 1
                else:
                    category_count[product.pro_category] += 1
        # Sort in descending order by count value
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
        """
        This method generates a pie chart that shows the proportion of
        products that have a discount value less than 30, between 30 and 60
        inclusive, and greater than 60. The figure is saved into the data/figure
        folder.
        :return: None
        """
        # Count the nnumber of <30 30~60 >60
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
        # Calculation ratio
        discount_count = [x / total_num for x in discount_count]
        labels = ['<30', '30~60', '>60']  # Labels for the sections in the pie chart
        plt.pie(discount_count, labels=labels, autopct='%1.1f%%')
        plt.title('Discount figure')
        plt.savefig('./data/figure/generate_discount_figure.png', dpi=300)
        plt.show()

    def generate_likes_count_figure(self):
        """
        This method generates a chart (you think is the most suitable)
        displaying the sum of products’ likes_count for each category in
        ascending order. The figure is saved into the data/figure folder.
        :return: None
        """
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
        """
        This method generates a scatter chart showing the relationship
        between likes_count and discount for all products. The figure is saved
        into the data/figure folder.
        :return: None
        """
        likes_counts = []
        discounts = []
        with open('./data/products.txt', 'r', encoding='utf-8') as f:
            for line in f:
                product = self.parse_product_from_line(line.replace('\n', ''))
                likes_counts.append(product.pro_likes_count)
                discounts.append(product.pro_discount)
        plt.figure(figsize=(16, 12))
        # Draw the scatterplot
        plt.scatter(discounts, likes_counts)
        plt.title('Discount likes count figure')
        plt.xlabel('Discount')
        plt.ylabel('Likes count')
        plt.savefig('./data/figure/generate_discount_likes_count_figure.png', dpi=300)
        plt.show()

    def delete_all_products(self):
        """
        This method removes all the product data in the data/products.txt
        file.
        :return:None
        """
        # Open in w mode -> will be cleared
        with open('./data/products.txt', 'w', encoding='utf-8') as f:
            pass

    def get_all_product_id(self):
        """
        get all the product_id
        :return: list
            all product ids
        """
        product_ids = []
        product_re = re.compile(r"^\{'pro_id':'(.+)', 'pro_model':'(.+)', 'pro_category':'(.+)', 'pro_name':'(.+)',"
                                r" 'pro_current_price':'(.+)', 'pro_raw_price':'(.+)', 'pro_discount':'(.+)',"
                                r" 'pro_likes_count':'(.+)'\}$")
        with open('./data/products.txt', 'r', encoding='utf-8') as f:
            for line in f:
                product_ids.append(product_re.match(line.replace('\n', '')).group(1))
        return product_ids

