# 包含min函数的栈
# 定义栈的数据结构，请在该类型中实现一个能够得到栈最小元素的min函数。


class test:
    def __init__(self):
        self.stack = []
        self.minnum = [100000000000]

    def push(self, item):
        self.stack.append(item)
        x = self.minnum.pop()
        if item > x:
            self.minnum.append(x)
        else:
            self.minnum.append(item)


t = test()
t.push(3)
t.push(7)
t.push(2)
t.push(1)

print(t.minnum)
