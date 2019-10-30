# 并发编程
# threading库在单独的线程中执行任意可调用对象
from threading import Thread
import time


def countdown(n):
    for i in range(n):
        print('time-', i)
        time.sleep(1)


t = Thread(target=countdown, args=([5]))  # target为目标函数,args为目标函数的参数，该参数必须以可迭代的形式输入
t.start()  # 创建完t后只有调用start()才会执行

if t.is_alive():
    print('still running\n')
else:
    print('completed')


