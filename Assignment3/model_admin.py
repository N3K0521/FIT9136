from model_user import User

class Admin(User):
    def __init__(self, user_id="u_0000000000", user_name="admin", user_password="password", user_register_time="00-00-0000_00:00:00", user_role="admin"):
        super().__init__(user_id, user_name, user_password, user_register_time, user_role)

    def __str__(self):
        return super().__str__()

if __name__ == '__main__':
    print(Admin())