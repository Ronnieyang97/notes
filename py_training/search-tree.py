# 树的子结构
# 输入两棵二叉树A，B，判断B是不是A的子结构。

class node:
    def __init__(self, s):
        self.s = s
        self.left = None
        self.right = None

    def search(self, target):
        if self.s == target.s:
            if (target.right is None) & (target.left is None):
                return 1
            elif target.left is None:
                return self.right.search(target.right)
            elif target.right is None:
                return self.left.search(target.left)
            else:
                return self.right.search(target.right) & self.left.search(target.left)
        elif (self.left is None) & (self.right is None):
            return 0
        elif (self.left is not None) & (self.right is not None):
            return self.left.search(target) | self.right.search(target)
        elif self.left is None:
            return self.right.search(target)
        elif self.right is None:
            return self.left.search(target)
        else:
            return 0


first = node('a')
second1 = node('b')
second2 = node('c')
second1.left = node('d')
second1.right = node('e')
second2.left = node('f')
second2.right = node('g')
first.right = second2
first.left = second1

test = node('c')
test.right = node('g')
test.left = node('f')
print(first.search(test))
