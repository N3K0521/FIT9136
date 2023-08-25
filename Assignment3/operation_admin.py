from operation_user import UserOperation
from model_admin import Admin
import time


class AdminOperation:
    def register_admin(self):
        user_operation = UserOperation()
        # 设计的是只有一个管理员用户，如果不存在管理员则创建一个，如果存在不创建
        # 账号admin 密码admin
        if user_operation.check_username_exist("admin"):
            return
        user_password = user_operation.encrypt_password("admin")
        # 获取当前时间并转成固定格式的字符串
        user_register_time = time.strftime("%d-%m-%Y_%H:%M:%S", time.localtime(time.time()))
        admin = Admin(user_operation.generate_unique_user_id(), "admin", user_password, user_register_time, "admin")
        with open('./data/users.txt', 'a', encoding='utf-8') as f:
            f.write(str(admin) + '\n')

if __name__ == '__main__':
    admin_operation = AdminOperation()
    admin_operation.register_admin()