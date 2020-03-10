import datetime
class Vector:
    def __init__(self, x, y):
        self._x = x
        self._y = y

    @property  # 标记为特性
    def x(self):
        return self._x

    @property
    def y(self):
        return self._y

    def __repr__(self):
        return 'vector({}{})'.format(self.x, self.y)

    def __str__(self):
        return str((self.x, self.y))

    @classmethod  # 直接将自定义函数绑定成类方法
    def method(cls):
        return 'class method'

    def __eq__(self, other):
        return tuple(self) == tuple(other)

    def __iter__(self):
        return (i for i in self)

    # 使该对象可散列，需要hash和eq
    def __hash__(self):
        return hash(self.x) ^ hash(self.y)


ve = Vector(3, 4)
print(ve)  # 此时调用的是str方法
# 当在控制台中直接调用ve，而非print时，会使用repr方法


