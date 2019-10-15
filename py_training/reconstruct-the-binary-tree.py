# 重建二叉树
# 输入某二叉树的前序遍历和中序遍历的结果，请重建出该二叉树。假设输入的前序遍历和中序遍历的结果中都不含重复的数字。
# 例如输入前序遍历序列{1,2,4,7,3,5,6,8}和中序遍历序列{4,7,2,1,5,3,8,6}，则重建二叉树并返回。

class Node:
    def __init__(self, s=None, left=None, right=None):
        self.node = s
        self.left = None
        self.right = None


pre = ['a', 'b', 'd', 'e', 'h', 'i', 'c', 'f', 'g']
inorder = ['d', 'b', 'h', 'e', 'i', 'a', 'f', 'c', 'g']


def divide(pre, inorder):
    root = Node(pre[0])
    location = inorder.index(pre[0])

    root.left = divide(pre[1:], inorder[:location])
    root.right = divide(pre[2:], inorder[location + 1:])

    return root


x = divide(pre, inorder)
print(x.right)
