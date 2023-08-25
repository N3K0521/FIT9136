import re
class Order:
    def __init__(self, order_id="o_00000", user_id="u_0000000000", pro_id="000000", order_time="00-00-0000_00:00:00"):
        o_id_re = re.compile(r'^o_\d{5}$')
        u_id_re = re.compile(r'^u_\d{10}$')
        o_time_re = re.compile(r'^(\d{2})-(\d{2})-(\d{4})_(\d{2}):(\d{2}):(\d{2})$')
        if not o_id_re.match(order_id):
            raise ValueError("The order_id is invalid!")
        if not u_id_re.match(user_id):
            raise ValueError("The user_id is invalid!")
        o_time_match = o_time_re.match(order_time)
        # 如果时间不匹配，就抛出异常, match方法如果匹配会返回一个match对象，如果不匹配会返回None
        # 返回的match对象中，在正则表达式中，每一个()都是一个分组
        # 可以通过match对象的group方法获取()内的内容
        if not o_time_match:
            raise ValueError("The order_time is invalid!")
        # 否则提取年月日
        else:
            self.year = int(o_time_match.group(3))
            self.month = int(o_time_match.group(2))
            self.day = int(o_time_match.group(1))
        self.order_id = order_id
        self.user_id = user_id
        self.pro_id = pro_id
        self.order_time = order_time

    def __str__(self):
        return "{" + f"'order_id':'{self.order_id}', " \
                     f"'user_id':'{self.user_id}', " \
                     f"'pro_id':'{self.pro_id}', " \
                     f"'order_time':'{self.order_time}'" + "}"

if __name__ == '__main__':
    order = Order(order_time='11-12-2018_23:30:59')
    print(order)
    print(order.year)