# 并发编程
# threading库在单独的线程中执行任意可调用对象
from threading import Thread, Event
import time


def countdown(n, start_evt):
    print('starting')
    start_evt.set()  # 从此处开始后续代码同时执行
    time.sleep(1)
    for i in range(n):
        print('down-', n - i)
        time.sleep(1)


def countup(n, start_evt):
    print('another count')
    start_evt.wait()  # t中的.set()会连接到此处开始执行代码，而countdown处的代码也同样在执行，因此两处代码同时在运行
    for i in range(n):
        print('up-', i)
        time.sleep(0.5)


start_evt = Event()  # event对象最好只使用一次，如果要多次使用则用condition
t = Thread(target=countdown, args=([5, start_evt]))  # target为目标函数,args为目标函数的参数，该参数必须以可迭代的形式输入
t2 = Thread(target=countup, args=([3, start_evt]))
"""t.start()  # 创建完t后只有调用start()才会执行
t2.start()"""

# 如果要使用多次event对象时，需要使用condition或信号量避免出错，涉及到控制并发

from queue import Queue, Empty, Full


def producer(out_q):
    while 1:
        evt = Event()
        print('give something')
        data = input()
        try:
            out_q.put((data, evt), block=False)  # 获取的数据被放入了队列q,evt用于控制
            evt.wait()  # 只有等到consumer中的内容执行完后才会继续下一次循环
        except Full:
            print("lt's full")


def consumer(in_q):
    while True:
        try:
            data, evt = in_q.get(timeout=5.0, block=False)  # 从队列中获取数据,timeout为超时时间
            print('this is double of what you give')
            print(data * 2)
            evt.set()
        except Empty:
            print("it's empty")


q = Queue()
t1 = Thread(target=consumer, args=(q,))
t2 = Thread(target=producer, args=(q,))
t1.start()
t2.start()

# 可以在队列中存放特殊的值一次来控制是否停止
# 向队列中添加数据项时并不会复制此数据项，线程间通信实际上是在线程间传递对象引用。
# 担心对象的共享状态，那你最好只传递不可修改的数据结构（如：整型、字符串或者元组）或者一个对象的深拷贝

# block=False用来避免当执行某些特定队列操作时发生无限阻塞的情况
# 比如，一个非阻塞的put() 方法和一个固定大小的队列一起使用，这样当队列已满时就可以执行不同的代码。比如输出一条日志信息并丢弃。

# .qsize, .full和.empty 并非线程安全，可能在使用empty时队列为空但是同时另一个线程有插入了一个值，尽量不用这些方法


from concurrent.futures import ProcessPoolExecutor  # 线程池
with ProcessPoolExecutor(N=3) as pool:
    # do work in parallel using pool
    pass
# N为系统上可用的CPU的个数
# 向pool中提交工作的方式有两种：results = pool.map(work, data)和future = pool.submit(work, arg)/result = future.result
# 前者迭代所有,后者只提交一个


# 利用生成器实现简单的并发。。。挂起



