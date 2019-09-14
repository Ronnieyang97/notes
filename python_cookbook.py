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

    min_price = min(zip(prices.values(), prices.keys()))    # zip()用于将字典的key和value反转(zip只能访问一次)，min找出最小值
    print(min_price)
    prices_sorted = sorted(zip(prices.values(), prices.keys()))    # 依据价格排序
    print(prices_sorted)
    print(min(prices, key=lambda k: prices[k]))    # 返回价格最小的键值


dictionary()
