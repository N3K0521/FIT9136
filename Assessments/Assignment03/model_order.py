"""
Creation Date: 27th May 2023
Last Modified Date: 3rd June 2023

Student Name: Huixin Wang
Student ID: 31552544
"""

import re
class Order:
    """
    A model class of oder.

    Attributes
    ----------
    order_id : str
        a string to store the order id in the format of o_5digits
    user_id : str
        a string to store the user's id
    pro_id : str
        a string to store the product id
    order_time : str
        a string to store the place time of the order in the format “DD-MM-YYYY_HH:MM:SS”

    Methods
    -------
    __init__():
        Constructs a unit object
    __str__():
        Return the order information as a formatted string.
    """

    # All positional arguments of the constructor have default values
    def __init__(self, order_id="o_00000", user_id="u_0000000000", pro_id="000000", order_time="00-00-0000_00:00:00"):
        """
        Constructs a unit object
        :param order_id: str
            a string to store the order id
            Must be a unique integer (the default value is 0_00000)
            Format: o_5digits
        :param user_id: str
            a string to store the user's id of the order (the default value is u_0000000000)
        :param pro_id:
            s string to store the product's id in the order (the default value is 000000)
        :param order_time:
            a string to store the order's placement time (the default value is 00-00-0000_00:00:00)
            Format: DD-MM-YYYY_HH:MM:SS
        """
        o_id_re = re.compile(r'^o_\d{5}$')
        u_id_re = re.compile(r'^u_\d{10}$')
        o_time_re = re.compile(r'^(\d{2})-(\d{2})-(\d{4})_(\d{2}):(\d{2}):(\d{2})$')
        if not o_id_re.match(order_id):
            raise ValueError("The order_id is invalid!")
        if not u_id_re.match(user_id):
            raise ValueError("The user_id is invalid!")
        o_time_match = o_time_re.match(order_time)
        # If the time doesn't match -> error prompt
        # The match method will return a matched object if matched, else will return None
        # Each() will be a group in the returned match object in the re expression
        # using the group method of the match object to get the content of ()
        if not o_time_match:
            raise ValueError("The order_time is invalid!")
        # else get the year month and day
        else:
            self.year = int(o_time_match.group(3))
            self.month = int(o_time_match.group(2))
            self.day = int(o_time_match.group(1))
        self.order_id = order_id
        self.user_id = user_id
        self.pro_id = pro_id
        self.order_time = order_time

    def __str__(self):
        """
        Return the order information as a formatted string
        :return: String returned in the format of:
                {‘order_id’:’xxx’, ‘user_id’:’xxx’, ‘pro_id’:’xxx’,
                ‘order_time’:’xxx’}
        """
        return "{" + f"'order_id':'{self.order_id}', " \
                     f"'user_id':'{self.user_id}', " \
                     f"'pro_id':'{self.pro_id}', " \
                     f"'order_time':'{self.order_time}'" + "}"

