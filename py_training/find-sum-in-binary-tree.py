# 二叉树中和为某一值的路径
# 输入一颗二叉树和一个整数，打印出二叉树中结点值的和为输入整数的所有路径。路径定义为从树的根结点开始往下一直到叶结点所经过的结点形成一条路径


class node:
    def __init__(self, s):
        self.s = s
        self.left = None
        self.right = None


pathout = []


def get(node, path, target):
    if target - node.s < 0:
        return 0
    elif target - node.s == 0:
        path.append(node.s)
        print(path)
    else:
        target -= node.s
        path.append(node.s)
        if node.left is not None:
            get(node.left, path, target)
        while path[-1] != node.s:  # 最为关键的回溯出栈！将path一直回溯至执行get(node.left, path, target)前的状态
            path.pop()
        if node.right is not None:
            get(node.right, path, target)
        if node.left is None and node.right is None:
            return 0


first = node(1)
second1 = node(2)
second2 = node(3)
second1.left = node(7)
second1.right = node(6)
second2.left = node(5)
second2.right = node(4)
first.right = second2
first.left = second1

get(first, pathout, 9)
