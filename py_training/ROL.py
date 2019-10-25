# 左旋转字符串
# 汇编语言中有一种移位指令叫做循环左移（ROL），就是用字符串模拟这个指令的运算结果。
# 对于一个给定的字符序列S，请你把其循环左移K位后的序列输出。

test = 'student. a am I'


def rol(string, num):
    return string[num:] + string[:num]


print(rol(test, 2))
