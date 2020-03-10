import functools


def decorate(func):
    def inner():
        print('run inner')

    return inner


@decorate
def target():
    print('target function')


print(target)  # 被执行的对象是inner函数
# 装饰器是语法糖，能把被装饰的函数替换成其他函数；并且在加载模块时立即执行即被被装饰的函数定义时

registery = []


def register(func):
    print('rigister', func)
    registery.append(func)
    return func


@register
def func1():
    print('func1')


@register
def func2():
    print('func2')


func1()
func2()
print(registery)
# register中包含func1和func2，因为register返回的是原函数func因此，func1和func2被执行了

# 使用装饰器可以改进capture 6中的a,b,cpromotion
promos = []


def promotion(func):
    promos.append(func)
    return func


@promotion
def apromotion():
    pass


@promotion
def bpromotion():
    pass


# 由此在promos中会包含所有promotion相关的函数，而且函数不需要特殊的名称，只要将装饰器去掉就能禁用，可以在其它模块中使用

# python在编译函数的定义体时默认变量为局部变量，当函数体内找不到该变量的定义时则会尝试全局变量，
# 如果在自定义函数内先调用某个后续函数体会定义的变量，会报错

def make_avg():  # 闭包
    nums = []  # 该变量为自由变量，指未在本地作用域中绑定的变量

    def avg(value):
        nums.append(value)
        return sum(nums) / len(nums)

    return avg


test_avg = make_avg()
print(test_avg(10), test_avg(11), test_avg(12))  # 将10，11，12成功的存到了make_avg中的nums


def make_avgnew():
    count = 0
    total = 0

    def avg(value):
        nonlocal count, total  # 将count和total定义为自由变量，避免被默认赋值为局部变量，完成闭包操作
        count += 1
        total += value
        return total / count

    return avg


test_avg2 = make_avgnew()
print(test_avg2(5), test_avg2(7), test_avg2(9))


def good_func(func):
    @functools.wraps(func)  # warp使得develop可以用于装饰一些带有关键词参数信息的被装饰函数
    def develop(*args, **kwargs):
        pass

    return develop


@functools.lru_cache()  # 注意括号，其中可以加入关键字maxsize和typed
def fibonacci(n):
    if n < 2:
        return n
    else:
        return fibonacci(n - 2) + fibonacci(n - 1)
# 使用functools.lru_cache()后，如果多次调用该‘递归’函数，将可以避免一些重复计算

# singledispatch可以在系统任何地方任何模块注册专门函数，并且为不是自己写的或者不能修改的类添加自定义函数

@decorate
@register
def muti_func():  # 效果等同于decorate(register(muti_func()))
    pass


