class node:
    def __init__(self, s):
        self.s = s
        self.left = None
        self.right = None


def getdepth(node):
    if node is None:
        return 0
    else:
        return max(getdepth(node.left), getdepth(node.right))+1


first = node('a')
second1 = node('b')
second2 = node('c')
second1.left = node('d')
second1.right = node('e')
second1.right.right = node('h')
second2.left = node('f')
second2.right = node('g')
first.right = second2
first.left = second1


print(getdepth(first))
