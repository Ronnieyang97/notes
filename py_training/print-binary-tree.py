# 从上往下打印二叉树
# 从上往下打印出二叉树的每个节点，同层节点从左至右打印。
class node:
    def __init__(self, s):
        self.s = s
        self.left = None
        self.right = None


def getvalue(node):
    queue = []
    temp = [node]
    result = []
    while temp:
        for i in temp:
            queue.append(i)
        temp = []
        for i in queue:
            temp.append(i.s)
        result.append(temp)
        temp = []
        for i in queue:
            if i.left is not None:
                temp.append(i.left)
            if i.right is not None:
                temp.append(i.right)
        queue = []
    return result



first = node('a')
second1 = node('b')
second2 = node('c')
second1.left = node('d')
second1.right = node('e')
second2.left = node('f')
second2.right = node('g')
first.right = second2
first.left = second1

print(getvalue(first))

# 选择了按照层将节点的值归至不同的list，如果不分层则可以直接使用一个队列来迭代node
