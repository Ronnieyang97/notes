# 二叉树的镜像
# 返回输入的二叉树的镜像二叉树

class node:
    def __init__(self, s):
        self.s = s
        self.right = None
        self.left = None


first = node('a')
second1 = node('b')
second2 = node('c')
second1.left = node('d')
second1.right = node('e')
second2.left = node('f')
second2.right = node('g')
first.right = second2
first.left = second1


def reverse(nodee):
    if nodee is None:
        return None
    else:
        result = node(nodee.s)
        result.left = reverse(nodee.right)
        result.right = reverse(nodee.left)
        return result


print(reverse(first).left.s)

