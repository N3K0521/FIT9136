from model_user import User

class Customer(User):
    def __init__(self, user_id="u_0000000000", user_name="customer", user_password="password", user_register_time="00-00-0000_00:00:00", user_role="customer", user_email="Unknown", user_mobile="Unknown"):
        super().__init__(user_id, user_name, user_password, user_register_time, user_role)
        self.user_email = user_email
        self.user_mobile = user_mobile

    def __str__(self):
        return "{" + f"'user_id':'{self.user_id}', " \
                     f"'user_name':'{self.user_name}', " \
                     f"'user_password':'{self.user_password}', " \
                     f"'user_register_time':'{self.user_register_time}', " \
                     f"'user_role':'{self.user_role}', " \
                     f"'user_email':'{self.user_email}', " \
                     f"'user_mobile':'{self.user_mobile}'" + "}"

if __name__ == '__main__':
    print(Customer())