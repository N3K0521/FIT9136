import random
from model_customer import Customer
from model_admin import Admin

class UserOperation:
    def generate_unique_user_id(self):
        # 存储的是字典格式 eval可以将字符串变成字典从而提取user_id
        with open('./data/users.txt', 'r', encoding='utf-8') as f:
            user_ids = [eval(line.replace('\n', '')).get('user_id') for line in f.readlines()]
        # 设置最多用户数量为16，包括一个管理员，所以最多可以15个customer
        if len(user_ids) >= 16:
            return None
        while True:
            # 随机数，保证10位，前面补0
            u_id = f'u_{random.randint(0, 9999999999):010d}'
            if u_id not in user_ids:
                return u_id

    def encrypt_password(self, user_password):
        # 得到所有可以用来加密的字符
        characters = 'abcdefghijklmnopqrstuvwxyz'
        characters += characters.upper() + '0123456789'
        # random.choices可以随机选出长度为k的列表(可重复)，用join连接成字符串
        random_string = ''.join(random.choices(characters, k=len(user_password) * 2))
        encrypted_password = ''
        # 每个字符前面加两个加密字符
        for i in range(len(user_password)):
            encrypted_password += (random_string[2 * i: 2 * (i + 1)] + user_password[i])
        return '^^' + encrypted_password + '$$'

    def decrypt_password(self, encrypted_password):
        # 去掉加密密码的 ^^ $$
        encrypted_password = encrypted_password[2: -2]
        user_provided_password = ''
        # 每三位提取一个字符
        for i in range(len(encrypted_password) // 3):
            user_provided_password += encrypted_password[3 * i + 2]
        return user_provided_password

    def check_username_exist(self, user_name):
        with open('./data/users.txt', 'r', encoding='utf-8') as f:
            # for line in f等同于for line in f.readlines()，for line in f更高效
            for line in f:
                # 变成字典获取键值
                user_dict = eval(line.replace('\n', ''))
                if user_name == user_dict.get('user_name'):
                    return True
            return False

    def validate_username(self, user_name):
        if len(user_name) < 5:
            return False
        for c in user_name:
            if not c.isalpha() and c != '_':
                return False
        return True

    def validate_password(self, user_password):
        if len(user_password) < 5:
            return False
        has_letter = False
        has_number = False
        for c in user_password:
            if c.isalpha():
                has_letter = True
            if c.isdigit():
                has_number = True
            if has_letter and has_number:
                return True
        return False

    def login(self, user_name, user_password):
        with open('./data/users.txt', 'r', encoding='utf-8') as f:
            for line in f:
                user_dict = eval(line.replace('\n', ''))
                if user_dict['user_name'] == user_name and self.decrypt_password(user_dict['user_password']) == user_password:
                    return self.parse_user_from_userinfo_dict(user_dict)
            return None

    # 把字典对象转化为对应的User对象
    def parse_user_from_userinfo_dict(self, user_dict):
        if user_dict['user_role'] == 'admin':
            return Admin(user_dict['user_id'], user_dict['user_name'], user_dict['user_password'],
                         user_dict['user_register_time'], user_dict['user_role'])
        elif user_dict['user_role'] == 'customer':
            return Customer(user_dict['user_id'], user_dict['user_name'], user_dict['user_password'],
                            user_dict['user_register_time'], user_dict['user_role'], user_dict['user_email'],
                            user_dict['user_mobile'])
        return None

# 下面是测试方法的代码 不需要可以删
if __name__ == '__main__':
    user_operation = UserOperation()
    print(user_operation.generate_unique_user_id())
    # encrypted_password = user_operation.encrypt_password('password')
    # print(encrypted_password)
    # print(user_operation.decrypt_password(encrypted_password))
    # print(user_operation.check_username_exist('user'))
    # print(user_operation.check_username_exist('user00'))
    # print('sss', user_operation.validate_username('sss'))
    # print('ssssss', user_operation.validate_username('ssssss'))
    # print('sss_ss', user_operation.validate_username('sss_ss'))
    # print('sss_s1', user_operation.validate_username('sss_s1'))
    # print('abcde', user_operation.validate_password('abcde'))
    # print('ab1de', user_operation.validate_password('ab1de'))
    # print('ab1d', user_operation.validate_password('ab1d'))
    # print(user_operation.login('admin', 'password1'))
    # print(user_operation.login('customer', 'password1'))
