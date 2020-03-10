from abc import ABC, abstractmethod
from collections import namedtuple

# 策略模式：定义一系列算法，将他们一一封装，且可相互替换，因此使得算法可以独立于客户而变化
# 上下文：将一些计算委托给不同算法的客户换组件

Customer = namedtuple('Customer', 'name fidelity')  # 顾客属性


class Lineitem:  # 商品类
    def __init__(self, product, quantity, price):
        self.product = product
        self.quantity = quantity
        self.price = price

    def total(self):
        return self.price * self.quantity


class Order:  # 上下文
    def __init__(self, customer, cart, promotion=None):
        self.customer = customer
        self.cart = list(cart)
        self.promotion = promotion

    def total(self):
        if not hasattr(self, '__total'):  # 判断当前对象是否含有total属性
            self.__total = sum(item.total for item in self.cart)
        else:
            return self.__total

    def due(self):
        if self.promotion is None:
            discount = 0
        else:
            discount = self.promotion.discount(self)
        return self.total() - discount

    def __repr__(self):
        return 'order total : {} due: {}'.format(self.total(), self.due())


def apromotion(self, order):  # 积分1000+，95折
    return order.total() * 0.05 if order.customer.fidelity >= 1000 else 0


def bpromotion(self, order):  # 单品20+，9折
    discount = 0
    for item in order.cart:
        if item.quantity >= 20:
            discount += item.total() * 0.1
    return discount


def cpromotion(self, order):  # 商品种类10+ 93折
    distinct_items = {item.product for item in order.cart}
    if len(distinct_items) >= 10:
        return order.total() * 0.07
    else:
        return 0


promotions = [apromotion, bpromotion, cpromotion]


def best(order):
    return max(promotion(order) for promotion in promotions)  # 将函数作为对象传参


print([globals()[name] for name in globals() if name.endswith('promotion')])  # 找出全局中以promotion结尾的函数


# 命令模式通过把函数作为参数传递，解耦调用操作的对象和提供实现的对象
