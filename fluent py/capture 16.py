from functools import wraps


def simple_coroutine():
    print('start')
    x = yield
    print('get', x)


my_coro = simple_coroutine()
next(my_coro)  # 调用生成器使其启动，显示start
# my_coro.send('111')  # 显示get 111；然后抛出stopiterator异常


def averager():
    total = 0
    count = 0
    average = None
    while True:
        term = yield average
        total += term
        count += 1
        average = total/count

test = averager()
next(test)
test.send(100)
test.send(50)
print(test.send(20))  # 会无限循环的产出平均值


def coroutine(func):  # 预激活装饰器，可以@coroutine,使函数在实例化时先激活，就不用单独调用next
    @wraps(func)
    def primer(*args, **kwargs):
        gen = func(*args, **kwargs)
        next(gen)
        return gen
    return primer


