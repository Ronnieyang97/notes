class Pair:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __repr__(self):
        return 'Pair({0.x!r}, {0.y!r})'.format(self)  # 在repr中用!r格式化self中的变量

    def __str__(self):
        return '({0.x!s}, {0.y!s})'.format(self)  # 在str中用!s格式化self中的变量


print(Pair(2, 4))
