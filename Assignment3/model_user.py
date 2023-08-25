import re


class User:
    def __init__(self, user_id="u_0000000000", user_name="user", user_password="password", user_register_time="00-00-0000_00:00:00",
                 user_role="customer"):
        # 正则表达式 匹配模式是u_ 后面10个数字
        u_id_re = re.compile(r'^u_\d{10}$')
        # 正则表达式，匹配模式是 00-00-0000_00:00:00
        u_time_re = re.compile(r'^\d{2}-\d{2}-\d{4}_\d{2}:\d{2}:\d{2}$')
        # 如果模式不匹配
        if not u_id_re.match(user_id):
            raise ValueError("The user_id is invalid!")
        if not u_time_re.match(user_register_time):
            raise ValueError("The user_register_time is invalid!")
        self.user_id = user_id
        self.user_name = user_name
        self.user_password = user_password
        self.user_register_time = user_register_time
        self.user_role = user_role

    def __str__(self):
        return "{" + f"'user_id':'{self.user_id}', " \
                     f"'user_name':'{self.user_name}', " \
                     f"'user_password':'{self.user_password}', " \
                     f"'user_register_time':'{self.user_register_time}', " \
                     f"'user_role':'{self.user_role}'" + "}"


if __name__ == '__main__':
    print(User())

