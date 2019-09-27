def parameter():  # 自定义函数中参数相关
    # 位置参数：就是在给函数传参数时，按照顺序，依次传值
    # 位置参数在前，默认参数在后
    # 关键字参数：允许传入0个或任意个含参数名的参数，这些关键字参数在函数内部自动组装为一个dict。在调用函数时，可以只传入必选参数
    def avg(first, *rest):  # *rest接受任意数量的位置参数,这些参数将放在一个元组中储存
        print(first / sum(rest))
        print(type(rest))

    avg(1, 2, 3, 4)

    def element(name, age, **other):  # **other接受任意数量的关键字参数,储存形式为字典
        print(name, age)
        print(other)

    element("ronnie", "22", weight=60, height=168)

    def recv(maxsize, *, block):  # block为强制关键字，放在*或带有*的参数后面，可以设置为强制关键字
        pass

    # recv(1024, True)  # TypeError
    recv(1024, block=True)  # success


def annotation(x: int, y: float) -> float:  # 函数注解，表明x为int，y为float，返回值为float
    return x + y


def anonymous():  # 匿名函数
    add = lambda x, y: x + y
    print(add(1, 2))
    x = 10
    test1 = lambda y: x + y
    x = 20
    test2 = lambda y: x + y
    print(test1(1))  # 结果为21
    print(test2(2))  # 结果为22，读取的是同一个x=20,因为匿名函数在使用时才捕获值

    x = 10
    test3 = lambda y, x=x: x + y
    x = 20
    print(test3(3))  # 结果为13，读取的是前一次x=10的值
    # 利用此原理，可应用到生成器中
    test4 = [lambda x, n=n: x + n for n in range(5)]
    for test in test4:
        print(test(10))  # 显示10到14


def simplify():  # 简化参数
    def test(a, b, c, d):
        print('a=', a, 'b=', b, 'c=', c, 'd=', d)
    from functools import partial
    simtest = partial(test, 22, d=4)
    simtest(1, 4)  # 结果为a= 22 b= 1 c= 4 d= 4
    # 此处有一个问题 ：如果partial(test, b=22, d=4)则会显示对b多次赋值


def getoutide():  # 使回调函数可以访问外部信息；暂时无法跟实际情况结合来理解
    def apply_async(func, args, *, callback):
        result = func(*args)
        callback(result)

    def add(x, y):
        return x + y

    # 使用类来完成对外部数据的访问
    class ResultHandler:
        def __init__(self):
            self.sequence = 0

        def handler(self, result):
            self.sequence += 1
            print('[{}] Got: {}'.format(self.sequence, result))

    test = ResultHandler()
    apply_async(add, ("hello ", "world"), callback=test.handler)  # 注意handler后不能加()

    # 使用一个函数闭包来访问外部数据
    def make_handler():
        sequence = 0

        def handler(result):
            nonlocal sequence  # 非局部变量声明，该变量可在内部和外部函数中使用（即hangler和make_handler），离开make_handler无法使用
            sequence += 1
            print('[{}] Got: {}'.format(sequence, result))
        return handler

    handler = make_handler()
    apply_async(add, ("hello ", "second world"), callback=handler)

    # 使用协程访问外部函数
    def make_handler2():
        sequence = 0
        while True:
            result = yield
            sequence += 1
            print('[{}] Got: {}'.format(sequence, result))

    handler = make_handler2()
    next(handler)  # 启动迭代器
    apply_async(add, ('hello ', 'third world'), callback=handler.send)  # 要使用send方法作为回调函数

# 内联回调相关；较为复杂

# 函数的闭包类似于class，外界不能直接访问，修改class内的值，但是可以通过增加一个内置的函数达到访问或修改其中的某个值的效果
# 在函数闭包中使用nonlocal来声名此闭包函数下的内部变量





getoutide()
