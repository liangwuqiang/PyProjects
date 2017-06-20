class Restaurant():
    """"餐馆"""
    def __init__(self,restaurant_name,cuidione_type):
        """"构造函数"""
        self.restaurant_name = restaurant_name
        self.cuidione_type = cuidione_type

    def describe_restaurant(self):
        """餐馆的描述"""
        print("餐馆的名字是：" + self.restaurant_name)
        print("餐馆的风格是" + self.cuidione_type)

    def open_restaurant(self):
        """餐馆正在营业"""
        print("餐馆正在营业")

restaurant = Restaurant()
restaurant.describe_restaurant()
restaurant.open_restaurant()
