class Pair:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __repr__(self):
        return 'Pair({0.x!r}, {0.y!r})'.format(self)  # 在repr中用!r格式化self中的变量, 0.x意为self.x,0==self

    def __str__(self):
        return '({0.x!s}, {0.y!s})'.format(self)  # 在str中用!s格式化self中的变量


p = Pair(2, 4)
print(p)  # 结果为(2, 4)
print('{0}'.format(p))  # 结果为(2, 4)
print('{0!r}'.format(p))  # 结果为Pair(2, 4)

_formats = {'ymd': '{d.year}-{d.month}-{d.day}', 'mdy': '{d.month}/{d.day}/{d.year}',
            'dmy': '{d.day}/{d.month}/{d.year}'}  # 设置显示格式


#######################################################################################


class Date:
    __slots__ = ['year', 'month', 'day']  # 使用slots可以节省大量数据产生时的内存占用，但是不能添加slots以外的实例属性

    # 但是使用后实例将不再具备字典的性质，不再支持一些普通类的特性，如多继承

    def __init__(self, year, month, day):
        self.year = year
        self.month = month
        self.day = day

    def __format__(self, code):
        if code == '':
            code = 'ymd'
        fmt = _formats[code]
        return fmt.format(d=self)  # d要与_formats中的d对应


d = Date(1997, 9, 23)
print(format(d))  # 默认格式
print(format(d, 'dmy'))  # 根据关键字获取格式


###########################################################################


class Person:
    def __init__(self, name):
        self.name = name

    @property  # 使name成为属性，访问property时会自动触发getter，setter，deleter三个方法
    def name(self):
        return self._name

    @name.setter  # 给name属性添加setter方法
    def name(self, value):
        if not isinstance(value, str):
            raise TypeError('Expected a string')
        self._name = value

    @name.deleter  # 给name属性添加deleter方法
    def name(self):
        raise AttributeError("Can't delete attribute")

    # 对于已经存在的方法，可以用property整合
    def get_name(self):
        return self._name

    def set_name(self, value):
        if not isinstance(value, str):
            raise TypeError('Expected a string')
        self._name = value

    def del_name(self):
        raise AttributeError("Can't delete attribute")

    second_name = property(get_name, set_name, del_name)  # 将三个方法整合到name中，与name属性效果相同


a = Person("ronnie")
print(a.name)  # 调用了proterty
a.name = 'may'
print(a.name)  # 结果为may，成功修改属性
# a.name = 42  赋值时遇到setter拼写检查，报错
# del a.name  删除时调用deleter
###############################################################


import math


class Circle:
    def __init__(self, radius):
        self.radius = radius

    @property
    def area(self):
        return math.pi * self.radius ** 2

    @property
    def diameter(self):
        return self.radius ** 2

    @property
    def perimeter(self):
        return 2 * math.pi * self.radius


# 将几个函数都整合到property中，与直接定义的区别是peoperty中的函数不会实际储存，只有在需要的时候才会被计算出来
c = Circle(4)
print(c.area)  # 注意area后面没有()


#######################################################


class A:
    def spam(self):
        print('A.spam')


class B(A):
    def spam(self):
        super().spam()
        print('B.spam')


class C(A):
    def spam(self):
        super().spam()
        print('C.spam')


class D(B, C):
    def spam(self):
        super().spam()
        print('D.spam')


d = D()
d.spam()
print(D.__mro__)


# 上述代码成功的基础在于b,c各自继承a，然后在b.spam和c.spam中都super()了a.spam（如果不super就会报错）
# 在使用super的过程中遇到的问题还是不少的，当遇到多重继承的父类中包含同名函数（魔术方法除外）并在调用中出错，还是只能选用显式调用作为应付手段
###################################################################################

# 父类使用person类，在第五十行
class SubPerson(Person):
    @property
    def name(self):
        print('Getting name')  # 扩展了Person中name的功能
        return super().name

    @name.setter
    def name(self, value):
        print('Setting name to', value)  # 扩展了Perosn中setter的功能
        super(SubPerson, SubPerson).name.__set__(self, value)

    # 为了委托给之前定义的setter方法，需要将控制权传递给之前定义的name属性的set()方法。不过，获取这个方法的唯一途径是使用类变量而不是实例变量来访问它。

    @name.deleter
    def name(self):
        print('Deleting name')  # 扩展了Person中deleter的功能
        super(SubPerson, SubPerson).name.__delete__(self)


s = SubPerson("ronnie")
print(s.name)
s.name = 'may'


class SubPerson2(Person):
    @Person.name.getter  # 单独修改property的某一个方法
    def name(self):
        print("getting name by subperson2")
        return super().name


class Integer:  # 描述器，定义魔术方法
    def __init__(self, name):
        self.name = name

    def __get__(self, instance, cls):
        if instance is None:
            return self
        else:
            return instance.__dict__[self.name]

    def __set__(self, instance, value):
        if not isinstance(value, int):
            raise TypeError('Expected an int')
        instance.__dict__[self.name] = value

    def __delete__(self, instance):
        del instance.__dict__[self.name]


class Point:  # 使用描述器需要将这个描述器的实例作为类属性放到一个类的定义中
    x = Integer('x')  # 必须在属性中定义
    y = Integer('y')

    def __init__(self, x, y):
        self.x = x
        self.y = y


class LazyProperty:  # 定义延时属性
    # 将一个只读属性定义成一个property，并且只在访问的时候才会计算结果。一旦被访问后，结果值被缓存起来，不用每次都去计算。
    def __init__(self, func):
        self.func = func

    def __get__(self, instance, cls):
        if instance is None:
            return self
        else:
            value = self.func(instance)
            setattr(instance, self.func.__name__, value)
            return value


class Circle:
    def __init__(self, radius):
        self.radius = radius

    @LazyProperty
    def area(self):
        print('Computing area')
        return math.pi * self.radius ** 2

    @LazyProperty
    def perimeter(self):
        print('Computing perimeter')
        return 2 * math.pi * self.radius

