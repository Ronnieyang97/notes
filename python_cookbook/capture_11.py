import time
from functools import wraps


def timethis(func):  # func为传入的函数
    @wraps(func)
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)  # 执行func函数
        end = time.time()
        print(func.__name__, end - start)  # 显示func函数的名字，和最终结果

    return wrapper  # 要将wrapper函数作为返回值返回


@timethis
def countdown(n):  # countdown即为传入的func函数
    while n > 0:
        n -= 1


@timethis
def countdown2(n):
    while n > 0:
        n -= 2


countdown(1000000)
# 使用装饰器后，countdown函数只需要完成计数即可，不同的countdown函数只要编写不同的计数部分即可，而相同重复的计时功能则全部在@wraps处实现
########################################################################################################
import logging


def logged(level, name=None, message=None):
    def decorate(func):
        logname = name if name else func.__module__
        log = logging.getLogger(logname)
        logmsg = message if message else func.__name__

        @wraps(func)
        def wrapper(*args, **kwargs):
            log.log(level, logmsg)
            return func(*args, **kwargs)

        return wrapper

    return decorate


@logged(logging.DEBUG)
def add(x, y):
    return x + y


@logged(logging.CRITICAL, 'example')
def spam():
    print('Spam!')


print(add(2, 4))


# 不清楚日志的相关功能如何起效或查看
#########################################
class NoInstances(type):  # 元类通常继承自type
    def __call__(cls, *args, **kwargs):
        raise TypeError("Can't instantiate directly")


# Example
class Spam(metaclass=NoInstances):  # metaclass设置的效果为可以自定义各种初始化的方式和条件
    @staticmethod
    def grok(x):
        print('Spam.grok')
        return 0


test = Spam.grok(4)


# test无法通过test = Spam()进行初始化
#####################################
class MyMeta(type):
    def __init__(cls, clsname, bases, clsdict):
        for name in clsdict:
            if 'i' in name:  # 函数名字中有i时会提示
                print('no character i in name!')
        return super().__init__(clsname, bases, clsdict)


class Root(metaclass=MyMeta):
    pass


class A(Root):
    def ihere(self):
        pass


class B(Root):
    def no_wrang(self):
        pass


###########################################################


def __init__(self, name, shares, price):  # 定义初始化
    self.name = name
    self.shares = shares
    self.price = price


def cost(self):  # 定义函数
    return self.shares * self.price


cls_dict = {
    '__init__': __init__,
    'cost': cost,
}

import types

Stock = types.new_class('Stock', (), {}, lambda ns: ns.update(cls_dict))  # 利用函数建立了类
Stock.__module__ = __name__  # 定义模块名

s = Stock('ronnie', 12, 1.2)
print(s.cost())


#########################################################################
def typed_property(name, expected_type):
    storage_name = '_' + name

    @property
    def prop(self):
        return getattr(self, storage_name)

    @prop.setter
    def prop(self, value):
        if not isinstance(value, expected_type):
            raise TypeError('{} must be a {}'.format(name, expected_type))
        setattr(self, storage_name, value)
        return prop


# Example use
class Person:
    name = typed_property('name', str)  # name执行str的类型检查
    age = typed_property('age', int)  # age执行int的类型检查

    def __init__(self, name, age):
        self.name = name
        self.age = age
######################################################
