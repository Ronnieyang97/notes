# 二进制中1的个数
# 输入一个整数，输出该数二进制表示中1的个数。其中负数用补码表示。


def find(num):
    if num >= 0:
        return str(bin(num)).count('1')
    else:
        print(bin(~num))
        return str(bin(~num)).count('1')  # ~符号用于得到某个数的补码所对应的数


print(find(-4))
