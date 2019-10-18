# 顺时针打印矩阵
# 题目：输入一个矩阵，按照从外向里以顺时针的顺序依次打印出每一个数字


from numpy import *

test = array([[1, 2, 3],  # test.T 和 test.transpose()都可以完成转置的操作
              [4, 5, 6],
              [7, 8, 9]])

result = []
while test.any():
    result += list(test[0])
    test = delete(test, 0, axis=0)
    test = test.T[::-1]  # 先转置再从最后一行开始输出


print(result)

