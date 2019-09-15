# notes for python cookbook


def decompression():  # 解压列表，字符串中的内容
    test_str = "abcdefg"
    test_list = ['a', 'b', 'c', 'd', 'e', 'f', 'g']
    part1, part2, *part3 = test_str
    print(part1, part2, part3)

    part1, *part2, part3 = test_list
    print(part1, part2, part3)

    # 当某个part为不需要的信息时，可以使用普通的废弃名称，如：_或ign
    *_, part1, part2 = test_list
    print(part1, part2)


def split():  # 依据字符串中的某个字符，对字符串进行分割
    test = "a::bc::def::gh"
    print(test.split('::'))  # 参数只有‘::’字符时，将会一直分割字符串直至结尾
    print(test.split('::', 2))  # 字符后有参数时，将会分割出n+1个字符串


def queue():  # 在test中保留有限个数据
    from collections import deque
    test = deque(maxlen=3)
    test.append('a')
    test.append('b')
    test.append('c')
    print(test)  # 此时test中的内容为'a', 'b', 'c'
    test.append('d')  # 加入第四个字符'd'
    print(test)  # 此时test中的内容为'b', 'c', 'd'
    test.appendleft('e')  # 左侧加入第五个字符'e'
    print(test)  # 此时test中的内容为'e', 'b', 'c';
    test.clear()
    test.append('a')
    test.append('b')
    test.appendleft('c')
    print(test)  # 此时test中的内容为'c', 'a', 'b'
    print(test.pop())  # 将最右移出队列
    print(test)  # 此时test的内容为'c', 'a'


def find_element():  # 查找list等数据结构中最大或最小的n个元素
    import heapq
    test = [
        {'name': 'IBM', 'shares': 100, 'price': 91.1},
        {'name': 'AAPL', 'shares': 50, 'price': 543.22},
        {'name': 'FB', 'shares': 200, 'price': 21.09},
        {'name': 'HPQ', 'shares': 35, 'price': 31.75},
        {'name': 'YHOO', 'shares': 45, 'price': 16.35},
        {'name': 'ACME', 'shares': 75, 'price': 115.65}
    ]
    cheap = heapq.nsmallest(3, test, key=lambda s: s['price'])  # 以price为标准输出最小的三项
    expensive = heapq.nlargest(3, test, key=lambda s: s['price'])  # 以price为标准输出最大的三项
    # lambda返回':'前的变量经过':'后的表达式运算后的结果（具体使用仍不贯通）
    print(cheap, expensive)

    nums = [1, 8, 2, 23, 7, -4, 18, 23, 42, 37]
    heapq.heapify(nums)  # 将nums进行了堆排序，特点时保证nums[0]一定时nums中最小的数字
    print(nums)
    print(heapq.heappop(nums))  # 将nums中的最小数出栈


def dictionary():  # 字典中的键映射多个值;字典排序
    from collections import defaultdict
    from collections import OrderedDict
    d = defaultdict(list)
    pairs = [['a', 1], ['a', 2], ['b', 1]]
    for key, value in pairs:
        d[key].append(value)
    print(d)  # d中的结果为{'a': [1, 2], 'b': [1]}

    d = OrderedDict()  # 保持数据插入时的顺序
    d['foo'] = 1
    d['bar'] = 4
    d['spam'] = 3
    d['grok'] = 2
    print(d)  # d中的结果为[('foo', 1), ('bar', 4), ('spam', 3), ('grok', 2)]

    import json
    print(json.dumps(d))  # 转换成str

    prices = {
        'ACME': 45.23,
        'AAPL': 612.78,
        'IBM': 205.55,
        'HPQ': 37.20,
        'FB': 10.75
    }

    min_price = min(zip(prices.values(), prices.keys()))  # zip()用于将字典的key和value反转(zip只能访问一次)，min找出最小值
    print(min_price)
    prices_sorted = sorted(zip(prices.values(), prices.keys()))  # 依据价格排序
    print(prices_sorted)
    print(min(prices, key=lambda k: prices[k]))  # 返回价格最小的键值


def compare_dict():  # 字典的集合运算
    a = {'x': 1,
         'y': 2,
         'z': 3
         }
    b = {'w': 10,
         'x': 11,
         'y': 2}
    print(a.keys() & b.keys())  # a和b中相同的key值
    print(a.keys() - b.keys())  # a和b中不同不同的key值
    print(a.items() & b.items())  # a和b中key，value都相同的项

    c = {key: a[key] for key in a.keys() - {'z', 'w'}}  # 字典推导，去除指定项
    print(c)


def dedupe(items, key=None):  # 删除重复数据  例如：dedupe(a, key=lambda d: (d['x'],d['y'])，
    # a = [ {'x':1, 'y':2}, {'x':1, 'y':3}, {'x':1, 'y':2}, {'x':2, 'y':4}]
    seen = set()
    for item in items:  # items为某列表，字典等
        val = item if key is None else key(item)  # 将不可哈希的（如字典）转换为可哈希的
        if val not in seen:  # 检查val是否在seen中
            yield item
            seen.add(val)


def name_slice():  # 命名切片方便记忆
    record = '....................100 .......513.25 ..........'
    shares = slice(20, 23)
    price = slice(31, 37)
    cost = int(record[shares]) * float(record[price])
    print(cost)

    test = "abcdefghijklmn"
    test_slice = slice(0, 6)  # 0为起始位置，6为终止位置，2为间隔
    print(test[test_slice])  # 从0到6的字符串为“abcdef”，间隔为2，因此结果为"ace"
    test_slice.indices(len(test))  # 防止种植位置超出test的末位


def count():  # 计算数组中的词频
    from collections import Counter
    words = [
        'look', 'into', 'my', 'eyes', 'look', 'into', 'my', 'eyes',
        'the', 'eyes', 'the', 'eyes', 'the', 'eyes', 'not', 'around', 'the',
        'eyes', "don't", 'look', 'around', 'the', 'eyes', 'look', 'into',
        'my', 'eyes', "you're", 'under'
    ]
    word_count = Counter(words)  # 可哈希对象
    print(word_count)
    print(word_count.most_common(3))  # 词频最高的三个
    morewords = ['why', 'are', 'you', 'not', 'looking', 'in', 'my', 'eyes']
    word_count.update(morewords)  # 添加计数内容
    print(word_count)
    # count的结果可以使用加减法


def sort_dict():  # 字典排序
    from operator import itemgetter, attrgetter
    rows = [
        {'fname': 'Brian', 'lname': 'Jones', 'uid': 1003},
        {'fname': 'David', 'lname': 'Beazley', 'uid': 1002},
        {'fname': 'John', 'lname': 'Cleese', 'uid': 1001},
        {'fname': 'Big', 'lname': 'Jones', 'uid': 1004}
    ]
    rows_by_fname = sorted(rows, key=itemgetter('fname'))  # itemgetter中可以有多个参数
    print(rows_by_fname)
    min(rows, key=itemgetter('uid'))  # 适用于Min和max

    # 排序自定义类
    class User:
        def __init__(self, user_id):
            self.user_id = user_id

        def __repr__(self):
            return 'User({})'.format(self.user_id)

    def sort_notcompare():
        users = [User(23), User(3), User(99)]
        print(users)
        print(sorted(users, key=attrgetter('user_id')))

    sort_notcompare()
    # 同样可用于max和min


def flite_element():  # 过滤元素
    def is_int(val):
        try:
            x = int(val)  # 过滤条件：数字
            return True
        except ValueError:
            return False

    values = ['1', '2', '-3', '-', '4', 'N/A', '5']
    ivals = list(filter(is_int, values))  # 过滤器第一个参数为过滤函数，第二个参数为过滤对象
    print(ivals)

    addresses = [
        '5412 N CLARK',
        '5148 N CLARK',
        '5800 E 58TH',
        '2122 N CLARK'
        '5645 N RAVENSWOOD',
        '1060 W ADDISON',
        '4801 N BROADWAY',
        '1039 W GRANVILLE',
    ]
    counts = [0, 3, 10, 4, 1, 7, 6, 1]

    from itertools import compress
    more5 = [n > 5 for n in counts]  # 条件，依赖的数组与待过滤数据有对应关系
    print(list[compress(addresses, more5)])  # compress的第一参数为需要过滤的数据，第二个参数为过滤条件


def tuple_clear():  # 优化元组下标显示
    from collections import namedtuple
    Stock = namedtuple('Stock', ['name', 'shares', 'price'])  # 设置了三个属性,不可直接更改，只能用.replace方法更改

    def compute_cost(records):
        total = 0.0
        for rec in records:
            s = Stock(*rec)  # *rec将records中子list读入，相当于for x, y, z in records
            total += s.shares * s.price
        return total

    test = [['a', 2, 2], ['b', 3, 3], ['c', 4, 4]]
    print(compute_cost(test))

    stock_default = Stock('', 0, 0)  # 设置stock的默认数值
    test1 = {'name': 'test1', 'shares': 10}
    test2 = {'name': 'test2', 'shares': 15, 'price': 50}

    def replace(s):
        return stock_default._replace(**s)  # **表示字典，*表示列表或元组

    print(replace(test1))
    print(replace(test2))


def tuple_search():  # 多个元组查找，chainmap使用
    from collections import ChainMap

    a = {'x': 1, 'z': 3}
    b = {'y': 2, 'z': 4}
    c = ChainMap(a, b)  # 现在a中查找，如果没找到就在b中查找
    print(c['y'])

    test = ChainMap()  # 空
    test['x'] = 1  # test == {'x':1}
    test = test.new_child()
    test['x'] = 2  # test == ({'x':1}, {'x':2})
    test = test.new_child()
    test['x'] = 3  # test == ({'x':1}, {'x':2}, {'x':3})
    print(test)
    test = test.parents
    print(test)
    test = test.parents
    print(test)

    a = {'x': 1, 'z': 3}
    b = {'y': 2, 'z': 4}
    merged = dict(b)
    merged.update(a)
    # 后来update的数据会将原有的覆盖成新的
    print(merged)  # {'y': 2, 'z': 3, 'x': 1}

    # 用chainmap不会生成新的变量，因此在a,b中改动会影响后续输出；用.update生成新的变量，改动a和b中的数据对结果不会产生影响



tuple_search()
