# 在二维数组中的查找
# 题目：在一个二维数组中，每一行都按照从左到右递增的顺序排序，每一列都按照从上到下递增的顺序排序。
# 请完成一个函数，输入这样的一个二维数组和一个整数，判断数组中是否含有该整数
import time
test = [[1, 2, 3, 4],
        [7, 8, 9, 10],
        [13, 14, 15, 18]]
start = time.time()
for n in range(1000000):
    x = 0
    target = 10
    for i in test:
        if target in i:
            y = i.index(target)
            break
        x += 1
end = time.time()
print((end-start))

# 执行一百万次花费时间约为0.67s左右

start = time.time()
for n in range(1000000):
    target = 10
    raw = len(test)
    col = len(test[0])
    i = 0
    j = col - 1
    while i < raw and j >= 0:
        if test[i][j] > target:
            j -= 1
        elif test[i][j] < target:
            i += 1
        else:
            break
end = time.time()
print(end-start)
# 执行100万次的时间花费约为1.2左右

# 多次测试可知方法1明显比方法2所花费的时间少，
# 如果用try:
#          test.index()
#          break
#      except:
#          continue
# 代替in语句，则可以发现两种方法所消耗的时间差不多
# 可见主要是用过in来节省时间，因为in不是通过遍历数组的方式完成的，可以尝试查阅in语句的源码来分析节省时间的原因
