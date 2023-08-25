class Product:
    def __init__(self, pro_id="000000", pro_model="Unknown", pro_category="Unknown", pro_name="Unknown", pro_current_price=-1, pro_raw_price=-1, pro_discount=-1, pro_likes_count=-1):
        self.pro_id = pro_id
        self.pro_model = pro_model
        self.pro_category = pro_category
        self.pro_name = pro_name
        self.pro_current_price = pro_current_price
        self.pro_raw_price = pro_raw_price
        self.pro_discount = pro_discount
        self.pro_likes_count = pro_likes_count

    def __str__(self):
        return "{" + f"'pro_id':'{self.pro_id}', " \
                     f"'pro_model':'{self.pro_model}', " \
                     f"'pro_category':'{self.pro_category}', " \
                     f"'pro_name':'{self.pro_name}', " \
                     f"'pro_current_price':'{self.pro_current_price}', " \
                     f"'pro_raw_price':'{self.pro_raw_price}', " \
                     f"'pro_discount':'{self.pro_discount}', " \
                     f"'pro_likes_count':'{self.pro_likes_count}'" + "}"

if __name__ == '__main__':
    print(Product())
    print(eval(str(Product())))
