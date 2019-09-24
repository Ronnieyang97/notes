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


def iter_slice():  # 迭代器切片
    import itertools

    def count(n):
        while 1:
            yield n
            n += 1

    test = count(0)
    for x in itertools.islice(test, 10, 20):  # 完成10-19的切片
        print(x)

    text = ["I love python", "python is the best language", "python is beautiful", "lisp is too complex",
            "let us use python"]
    for line in itertools.dropwhile(lambda line: 'python' in line, text):
        # dropwhile函数会从开头跳过符合lambda表达式的元素，从第一个不符合lambda的元素开始迭代，不会跳过除起始段以外符合lambda的元素
        print(line)  # 结果为lisp is too complex，let us use python


def permutation():  # 排列组合
    items1 = ['a', 'b', 'c']
    items2 = ('a', 'b', 'c')
    items3 = {'a': 1, 'b': 2}
    from itertools import permutations, combinations
    for x in permutations(items1, 2):  # 排列的对象可以是列表，元组和字典，对字典进行排列时只显示key值,第二个参数可以是限定某长度的所有结果
        print(x)
    for x in combinations(items2, 2):  # 组合
        print(x)


def serial_num():  # 标序号，追踪
    test = ['a', 'b', 'c', 'd']
    for idnum, char in enumerate(test, 1):  # 参数1意为从1开始标号
        print(idnum, char)


def multiple_iter():  # 同时迭代多个迭代器
    x = [1, 2, 3, 4, 5, 6]
    y = [11, 22, 33, 44, 55]
    z = ['a', 'b', 'c', 'd', 'e']
    for a, b in zip(x, y):  # 用zip完成同时迭代，迭代长度与最短序列保持一致
        print(a, b)
    from itertools import zip_longest
    for a, b in zip_longest(x, y):  # 用zip_longest，则迭代长度与最长序列保持一致
        print(a, b)
    print(dict(zip(y, z)))  # 将y, z打包成字典

    # zip函数只创建一个迭代器，如果要保存相关数据使用list（zip（））
    from itertools import chain
    for a in chain(x, y):  # 将x, y合并成一个集合迭代
        print(a)


def pipe_data():
    import os
    import fnmatch
    import re

    def gen_find(filepat, top):
        for path, dirlist, filelist in os.walk(top):  # os.walk从top路径下获取其下所有的文件夹名与文件，返回（root，dirs，files）
            for name in fnmatch.filter(filelist, filepat):  # fnmatch.filter匹配filelist是否符合filepat的格式
                yield os.path.join(path, name)  # os.path.join把目录和文件名合成

    def gen_opener(filenames):  # 打开文件
        for filename in filenames:
            f = open(filename, 'rt')
            yield f
            f.close()

    def gen_concatenate(iterators):
        for it in iterators:
            yield from it  # 返回一个生成器it

    def gen_grep(lines):  # 条件筛选
        for line in lines:
            if 'capture' in line:
                yield line

    lognames = gen_find('*.txt', 'C:\\Users\\Ronnie Yang\\PycharmProjects\\notes\\python_cookbook')
    files = gen_opener(lognames)
    lines = gen_concatenate(files)
    pylines = gen_grep(lines)
    for line in pylines:
        print(line)


def yield_from():  # yield from使用,其主要用于在某个生成器中想调用自身或其他生成器时使用
    from collections.abc import Iterable

    def flatten(items, ignore_types=(str, bytes)):
        for x in items:
            if isinstance(x, Iterable) and not isinstance(x, ignore_types):  # 当x可迭代并且将字符串和字符排除在可迭代对象外
                yield from flatten(x)  # 迭代x（类似递归）
            else:
                yield x  # 执行下一项
    items = [1, 2, [3, 4, ['five', 'six'], 7], 8]
    for x in flatten(items):
        print(x)


def merge():  # 在长序列中使用很有优势，因为不会直接读取所有的序列
    import heapq
    a = [1, 3, 7, 8, 13]
    b = [2, 6, 10, 11]
    for c in heapq.merge(a, b):  # a和b必须预先排序
        print(c)  # 返回值为1，2，3，6，7，8，10，11，13
    c = [6, 4, 2]
    for c in heapq.merge(a, c):
        print(c)  # 返回值为1，3，6，4，2，7，8，13



