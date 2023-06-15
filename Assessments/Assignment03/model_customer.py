"""
Creation Date: 28th May 2023
Last Modified Date: 3rd June 2023

Student Name: Huixin Wang
Student ID: 31552544
"""

from model_user import User
class Customer(User):
    """
    A class used to represent a customer type user. The customer class inherits form the user class

    Attributes
    ----------
    user_id : str
        a string to store the user id in the format of u_10digits
    user_name : str
        a string to store the user's name
    user_password : str
        a string to store the user's password
    user_register_time : str
        a string to store the user's register time in the format “DD-MM-YYYY_HH:MM:SS”
    user_role : str
        a string to store the user's role
    user_email : str
        a string to store the user's email address
    user_mobile : str
        a string to store the user's mobile phone number

    Methods
    -------
    __init__():
        Constructs a customer object
    __str__():
        Return the customer information as a formatted string.
    """

    # All positional arguments of the constructor have default values
    def __init__(self, user_id="u_0000000000", user_name="customer", user_password="password",
                 user_register_time="00-00-0000_00:00:00", user_role="customer", user_email="Unknown",
                 user_mobile="Unknown"):
        """
        Constructs a customer object
        :param user_id: str
            The id of the user (default is u_0000000000)
            Format: u_10 digits
            Must be unique
        :param user_name: str
            A string ro store the user's name (default is "customer")
        :param user_password: str
            A string to store the user's password (default is "password")
        :param user_register_time: str
            A string to store the user's register time (default is 00-00-0000_00:00:00)
            Format: DD-MM-YYYY_HH:MM:SS
        :param user_role: str
            A string to store the user's role (default is "customer")
        :param user_email: str
            A string to store the user's email (default is "unknown")
        :param user_mobile: str
            A string to store the user's mobile (default is "Unknown")
        """
        super().__init__(user_id, user_name, user_password, user_register_time, user_role)
        self.user_email = user_email
        self.user_mobile = user_mobile

    def __str__(self):
        """
        Return the customer information as a formatted string
        :return: String returned in the format of:
                {‘user_id’:’u_1234567890’, ‘user_name’:’xxx’,
                ‘user_password’:’xxx’, ‘user_register_time’:’xxx’,
                ‘user_role’:’customer’,
                ‘user_email’:’xxxxxxxx@gmail.com’,
                ‘user_mobbile’:’0412345689’}
        """
        return "{" + f"'user_id':'{self.user_id}', " \
                     f"'user_name':'{self.user_name}', " \
                     f"'user_password':'{self.user_password}', " \
                     f"'user_register_time':'{self.user_register_time}', " \
                     f"'user_role':'{self.user_role}', " \
                     f"'user_email':'{self.user_email}', " \
                     f"'user_mobile':'{self.user_mobile}'" + "}"
