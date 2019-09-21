def iterator():  # 迭代器
    test = [1, 2, 3, 4]
    test = iter(test)  # 使test成为迭代器
    print(next(test))  # 结果为1
    print(next(test))  # 结果为2

    class TestIter:
        def __init__(self, value):
            self._value = value
            self._children = []

        def __repr__(self):  # TestIter的返回值，__str__则为print（TestIter）的返回值;repr面向程序员；str面向用户
            return 'test({!r})'.format(self._value)  # !r对应非转义字符串

        def add_child(self, num):
            self._children.append(num)

        def __iter__(self):
            return iter(self._children)  # 返回的必须是可迭代对象

        def depth_first(self):  # 返回自身本身，并迭代每一个子节点，并通过调用子节点的depth_first方法返回对应元素
            yield self
            for c in self:
                yield from c.depth_first()  # yield from可理解为获取c.depth_first()函数中yield的值

        '''def __str__(self):  # 返回值为string形式
            return "value__" + str(self._value)'''

    root = TestIter(0)
    root.add_child(11)  # 迭代器中的返回值为11
    root.add_child(TestIter(22))
    for ch in root:
        print(ch)  # ch即为迭代时__repr__中设定的返回值
    print(root, '\n')  # 结果为value__0

    root = TestIter(0)
    child1 = TestIter(1)
    child2 = TestIter(2)
    root.add_child(child1)
    child1.add_child(TestIter(3))
    child2.add_child(TestIter(4))
    root.add_child(child2)
    child2.add_child(TestIter(5))
    # root(0)下有两个节点child1(1), child(2);child1下有两个节点3， 4；child2下有一个节点5
    for ch in root.depth_first():
        print(ch)
    # 在循环中先迭代到root(0)打印，在depth_first函数的for循环中去获取root下的内容，即child1(1), child(2);同理可继续向下查找


def new_iterator():
    def frange(start, end, step):  # 自定义的迭代器
        x = start
        while x < end:
            yield x
        x += step

    for n in frange(0, 4, 0.5):
        print(n)
    print(list(frange(1, 3, 0.5)))


def back_iter():  # 反向迭代
    a = [1, 2, 3, 4]
    for i in reversed(a):  # reversed的参数必须为列表
        print(i)

    class Countdown:  # 自定义类反向迭代
        def __init__(self, start):
            self.start = start

        def __iter__(self):
            n = self.start
            while n > 0:
                yield n
                n -= 1

        def __reversed__(self):
            n = 1
            while n <= self.start:
                yield n
                n += 1
    for rr in reversed(Countdown(5)):  # reverse定义与iter相反，因此结果为递增
        print(rr)
    for rr in Countdown(5):  # iter定义为递减因此结果为由大到小
        print(rr)


def interaction_iter():  # 与外部数据有交互的类的iter设置
    from collections import deque

    class LineHistory:
        def __init__(self, lines, histlen=3):
            self.lines = lines
            self.history = deque(maxlen=histlen)  # 长度为3的队列

        def __iter__(self):
            for lineno, line in enumerate(self.lines, 1):  # 枚举list中的每一个元素,1表示下标从1开始
                self.history.append((lineno, line))  # 将结果以元组的形式存入history
                yield line  # 迭代下一个line

        def clear(self):
            self.history.clear()

    f = ["I love python", "python is the best language", "python is beautiful", "lisp is too complex",
         "let us use python"]
    lines = LineHistory(f)  # 在iter方法中要使用enumerate(枚举函数，返回字符串中的每一个单词的序号和单词)
    for line in lines:  # 迭代时会顺次向class中定义好的长度为3的队列中插入新的f中的元素
        if 'python' in line:  # 当迭代对象lines当前next()返回的对象符合条件，打印history
            for lineno, hline in lines.history:
                print('{}:{}'.format(lineno, hline), end='\n')


interaction_iter()
