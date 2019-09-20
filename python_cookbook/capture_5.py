def rounding():  # 舍入计算
    print(round(3.1415, 2))  # 简单的舍入计算
    print(round(3141592, -2))  # 参数可以为负数，作用于十位（-1），百位（-2）等
    print(format(3.1415, '0.2f'))  # 简易输出用format即可
    print('{:0.3f}'.format(3.14159))

    from decimal import Decimal, localcontext  # 精确计算
    a = Decimal('4.2')
    b = Decimal('2.3')
    print((a + b) == Decimal('6.5'))
    with localcontext() as ctx:
        ctx.prec = 4
        print(a / b)  # 控制显示的位数


def decimal():  # 进制转换
    x = 1234
    print(bin(x))  # 二进制
    print(hex(x))  # 十六进制
    print(oct(x))  # 八进制

    print(format(x, 'b'))  # 二进制（无前缀）
    print(format(x, 'h'))  # 十六进制（无前缀）
    print(format(x, 'o'))  # 八进制（无前缀）

    print(int('4d2', 16))  # 十六进制转回十进制


def fraction():  # 构造分数
    from fractions import Fraction
    test = Fraction(2, 3)
    print(test)
    test = test * Fraction(7, 17)
    print(test.limit_denominator(13))  # 将test转为分子小于等于13的分数
    test = 3.5
    print(Fraction(*test.as_integer_ratio()))  # 将test转化为分数


def array():  # 数组
    array1 = [1, 2, 3, 4]
    array2 = [5, 6, 7, 8]
    print(array1 * 2)  # 结果为[1, 2, 3, 4, 1, 2, 3, 4]
    print(array1 + array2)  # 结果为[1, 2, 3, 4, 5, 6, 7, 8]

    import numpy
    array3 = numpy.array([1, 2, 3, 4])
    array4 = numpy.array([5, 6, 7, 8])
    print(array3 * 2)  # 结果为[2, 4, 6, 8]
    print(array3 + array4)  # 结果为[ 6  8 10 12]


def random_num():  # 随机数
    import random
    nums = [1, 2, 3, 4, 5]
    print(random.choice(nums))  # 随机选择
    print(random.sample(nums, 3))  # 随机提取三个样本
    print(random.shuffle(nums))  # 随机打乱顺序
    print(random.randint(0, 10))  # 0到10中随机生成一个数
    print(random.random)  # 0到1中随机浮点数


def time():  #时间
    import datetime
    a = datetime.timedelta(days=2, hours=6)
    print(a.days, a.seconds, a.total_seconds())  # seconds属性只显示hours及以下的时间（天数不包括在内）
    print(datetime.datetime.today())  # 显示当前时间

    text = '2012-09-20'  # 转换字符串为日期
    print(datetime.datetime.strptime(text, '%Y-%m-%d'))
    text = datetime.datetime.strptime(text, '%Y-%m-%d')  # 先转换格式
    print(datetime.datetime.strftime(text, '%A %B %d, %Y'))  # 一种更棒的显示方式：Thursday September 20, 2012

    from pytz import timezone
    # 涉及转换时区可用该模块

time()


