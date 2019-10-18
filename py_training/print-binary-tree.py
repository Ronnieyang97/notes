# 从上往下打印二叉树
# 从上往下打印出二叉树的每个节点，同层节点从左至右打印。

class node:
    def __init__(self, s):
        self.s = s
        self.left = None
        self.right = None

    def print_tree(self):
        print(self.s)
        if self.left is not None:
            self.left.print_tree()
        if self.right is not None:
            self.right.print_tree()


first = node('a')
second1 = node('b')
second2 = node('c')
second1.left = node('d')
second1.right = node('e')
second2.left = node('f')
second2.right = node('g')
first.right = second2
first.left = second1


first.print_tree()
