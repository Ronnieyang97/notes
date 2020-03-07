# 元组的意义不仅限于不可变的列表，而更应该用于对数据的记录
import os
from collections import namedtuple
import dis
import bisect
import numpy

# 拆包
info = ('tokyo', 2003, 32450, 5468)
cityname, year, *num = info  # 拆包操作中使用*符号将所有多余的数据放入num中

t = (20, 8)
print(divmod(*t))  # divmod函数用于取商和余数，需要两个变量，单输入t会被识别为是由单个变量，加上*符号后会执行拆包操作

_, filename = os.path.split('/users/ronnie/python/mltest.py')
# 常用_符号作为占位符

city = namedtuple('city', 'name country population size')
print(city._fields)  # 得到属性
info = ('tokyo', 'japan', '50000', '36000')

tokyo = city._make(info)  # 等同于city(*info)
print(tokyo._asdict())  # 将属性名和其对应的值以元组的形式返回

s = 'abcdefghijklmn'
print(s[1:9:3])  # 在1到9之间以3为间隔取值

# 对不可变对象进行重复拼接操作时会生成一个新的对象，因此效率很低，str除外，因为cpython对其作了优化

t = (1, 2, [30, 40])
# t[2] += [50, 60]  # t[2]变为了[30, 40, 50, 60],但是同时也会抛出异常，使用t[2].extend([50, 60])可以避免异常
print(dis.dis('s[a] += b'))
'''
通过dis.dis()查看字节码
不要把可变对象放在不可变对象中
+=操作不是原子操作
'''
list1 = [n * 3 for n in range(10)]
bisect.insort(list1, 34)  # 以不打乱字符串顺序的方式将34插入字符串，前提是list1是已排序对像
bisect.bisect(list1, 34)  # 二分法查找34，在长数组时替代index，更快

# array背后存的不是float对象是数字的机器翻译即字节表述
# 对于array不同类型吗对应不同的数据类型
# array不支持list.sort这种形式的就地排序

array = numpy.arange(12)
print(array)  # 此时array为一维数组
array.shape = 3, 4
print(array)  # 此时为3*4的矩阵
print(array[:, 1])  # 打印第一列
array.transpose()  # 转置矩阵
