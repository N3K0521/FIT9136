"""
Creation Date: 27th May 2023
Last Modified Date: 3rd June 2023

Student Name: Huixin Wang
Student ID: 31552544
"""
class Product:
    """
        A model class of product.

        Attributes
        ----------
        pro_id : str
            a string to store the unique product id
        pro_model: str
            a string to store the product model
        pro_category: str
            a string to store the product category
        pro_name: str
            a string to store the product name
        pro_current_price: int
            an integer to store the current price
        pro_raw_price: int
            an integer to store the raw price
        pro_discount: int
            an integer to store the discount
        pro_likes_count: int
            an integer to store the product likes count
        Methods
        -------
        __init__():
            Constructs a product object
        __str__():
            Return the product information as a formatted string.
        """

    # All positional arguments of the constructor have default values
    def __init__(self, pro_id="000000", pro_model="Unknown", pro_category="Unknown", pro_name="Unknown",
                 pro_current_price=-1, pro_raw_price=-1, pro_discount=-1, pro_likes_count=-1):
        """
        Constructs a product object
        :param pro_id: str
            a string to store the unique product id (default value 000000)
        :param pro_model: str
            a string to store the product model (default value Unknown)
        :param pro_category: str
            a string to store the product model (default value Unknown)
        :param pro_name: str
            a string to store the product name (default value Unkown)
        :param pro_current_price: int
            an integer to store the current price (default value -1)
        :param pro_raw_price: int
            an integer to store the raw price (default value -1)
        :param pro_discount: int
            an integer to store the product discount (default value -1)
        :param pro_likes_count: int
            an integer to store the product likes count (default value -1)
        """
        self.pro_id = pro_id
        self.pro_model = pro_model
        self.pro_category = pro_category
        self.pro_name = pro_name
        self.pro_current_price = pro_current_price
        self.pro_raw_price = pro_raw_price
        self.pro_discount = pro_discount
        self.pro_likes_count = pro_likes_count

    def __str__(self):
        """
        Return the product information as a formatted string
        :return: String returned in the format of:
                “{‘pro_id’:’xxx’, ‘pro_model’:’xxx’, ‘pro_category’:’xxx’,
                ‘pro_name’:’xxx’, ‘pro_current_price’:’xxx’,
                ‘pro_raw_price’:’xxx’, ‘pro_discount’:’xxx’,
                ‘pro_likes_count’:’xxx’}
        """
        return "{" + f"'pro_id':'{self.pro_id}', " \
                     f"'pro_model':'{self.pro_model}', " \
                     f"'pro_category':'{self.pro_category}', " \
                     f"'pro_name':'{self.pro_name}', " \
                     f"'pro_current_price':'{self.pro_current_price}', " \
                     f"'pro_raw_price':'{self.pro_raw_price}', " \
                     f"'pro_discount':'{self.pro_discount}', " \
                     f"'pro_likes_count':'{self.pro_likes_count}'" + "}"
