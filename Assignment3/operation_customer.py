import re
from operation_user import UserOperation
from model_customer import Customer
import time
import math


class CustomerOperation:
    def validate_email(self, user_email):
        # 电子邮件正则表达式，模式是 匹配形如aaa@bbb.ccc
        email_re = re.compile(r'^[0-9a-zA-Z_]+@.+\..+$')
        return email_re.match(user_email) is not None

    def validate_mobile(self, user_mobile):
        # 手机号正则表达式，模式是 03或04 后接8位数字
        mobile_re = re.compile(r'^0[34]\d{8}$')
        return mobile_re.match(user_mobile) is not None

    def register_customer(self, user_name, user_password, user_email, user_mobile):
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
        # 如果user_id返回None，则是customer已经满了
        if user_id is None:
            raise ValueError("The customer capacity is reached!")
        user_register_time = time.strftime("%d-%m-%Y_%H:%M:%S", time.localtime(time.time()))
        new_customer = Customer(user_id, user_name, user_password, user_register_time, 'customer', user_email,
                                user_mobile)
        with open('./data/users.txt', 'a', encoding='utf-8') as f:
            f.write(str(new_customer) + '\n')
        return True

    def update_profile(self, attribute_name, value, customer_object):
        user_operation = UserOperation()
        # lambda表达式 相当于定义了一个名为check_username的函数，检验user_name
        check_username = lambda x: user_operation.validate_username(x) and not user_operation.check_username_exist(x)
        # 定义一个字典， 每个key对应一个对应检验的函数名字
        attribute_names_check_function_dict = {
            'user_name': check_username,
            'user_password': user_operation.validate_password,
            'user_email': self.validate_email,
            'user_mobile': self.validate_mobile
        }
        # 如果不在'user_name', 'user_password', 'user_email', 'user_mobile'之中
        if attribute_name not in attribute_names_check_function_dict.keys():
            return False
        # 调用对应的方法检验要修改的值是否合法
        if not attribute_names_check_function_dict[attribute_name](value):
            raise ValueError(f"Invalid {attribute_name}!")
        # 如果修改的是密码，还需要加密
        if attribute_name == 'user_password':
            value = user_operation.encrypt_password(value)
        # setattr为对象属性赋值
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
        with open('./data/users.txt', 'r', encoding='utf-8') as f:
            lines = f.readlines()
        for line in lines:
            user_dict = eval(line.replace('\n', ''))
            if user_dict['user_id'] == customer_id:
                if user_dict['user_role'] == 'admin':
                    raise ValueError("Admin accounts cannot be deleted!")
                lines.remove(line)
                with open('./data/users.txt', 'w', encoding='utf-8') as f:
                    f.writelines(lines)
                return True
        return False

    def get_customer_list(self, page_number):
        user_operation = UserOperation()
        with open('./data/users.txt', 'r', encoding='utf-8') as f:
            lines = f.readlines()
        customers = []
        # 提取出来customer
        for line in lines:
            user_dict = eval(line.replace('\n', ''))
            if user_dict['user_role'] == 'customer':
                customers.append(user_operation.parse_user_from_userinfo_dict(user_dict))
        total_num = len(customers)
        customers = customers[(page_number - 1) * 10: min(page_number * 10, total_num)]
        return customers, page_number, math.ceil(total_num / 10)

    def delete_all_customers(self):
        with open('./data/users.txt', 'r', encoding='utf-8') as f:
            lines = f.readlines()
        # 筛选出不是customer的行
        lines = [line for line in lines if eval(line.replace('\n', ''))['user_role'] != 'customer']
        with open('./data/users.txt', 'w', encoding='utf-8') as f:
            f.writelines(lines)

if __name__ == '__main__':
    customer_operation = CustomerOperation()
    # print('check email...')
    # print(customer_operation.validate_email('xxx@gmail.com'))
    # print(customer_operation.validate_email('xxx@gmailcom'))
    # print(customer_operation.validate_email('xxx@gmailcom.'))
    # print(customer_operation.validate_email('@gmail.com'))
    # print('check mobile...')
    # print(customer_operation.validate_mobile('0412345689'))
    # print(customer_operation.validate_mobile('0312345689'))
    # print(customer_operation.validate_mobile('0212345689'))
    # print(customer_operation.validate_mobile('04123456899'))
    # print(customer_operation.validate_mobile('041234568'))
    # print(customer_operation.register_customer('userA', 'password1', 'xxx@gmail.com', '0412345689'))
    # print(customer_operation.register_customer('user1', 'password1', 'xxx@gmail.com', '0412345689'))
    # print(customer_operation.register_customer('userA', 'password', 'xxx@gmail.com', '0412345689'))
    # print(customer_operation.register_customer('userA', 'password1', '@gmail.com', '0412345689'))
    # print(customer_operation.register_customer('userA', 'password1', 'xxx@gmail.com', '04123456890'))
    # print('test update_profile...')
    # user_operation = UserOperation()
    # customer = user_operation.login('userB', 'a12345')
    # print(customer)
    # print(customer_operation.update_profile('user_name', 'user1', customer))
    # print(customer_operation.update_profile('user_password', '12345', customer))
    # print(customer_operation.update_profile('user_email', 'aaa@gmail.com', customer))
    # print(customer_operation.update_profile('user_mobile', '0312345689', customer))
    # print(customer_operation.update_profile('user_xxx', 'xxxxxx', customer))
    # print('test delete...')
    # print(customer_operation.delete_customer(customer.user_id))
    print('test get_customer_list')
    print(customer_operation.get_customer_list(2))
    customer_operation.delete_all_customers()
