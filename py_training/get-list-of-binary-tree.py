# 二叉搜索树的后序遍历序列
# 输入一个整数数组，判断该数组是不是某二叉搜索树的后序遍历的结果。如果是则输出Yes,否则输出No。假设输入的数组的任意两个数字都互不相同。

class node:
    def __init__(self, s):
        self.s = s
        self.left = None
        self.right = None

    def preorder(self):  # 前序遍历
        print(self.s)
        if self.left is not None:
            self.left.preorder()
        if self.right is not None:
            self.right.preorder()

    def inorder(self):  # 中序遍历
        if self.left is not None:
            self.left.inorder()
        print(self.s)
        if self.right is not None:
            self.right.inorder()

    def postorder(self):  # 后序遍历
        if self.left is not None:
            self.left.postorder()
        if self.right is not None:
            self.right.postorder()
        print(self.s)


first = node('a')
second1 = node('b')
second2 = node('c')
second1.left = node('d')
second1.right = node('e')
second2.left = node('f')
second2.right = node('g')
first.right = second2
first.left = second1

first.preorder()
first.inorder()
first.postorder()



