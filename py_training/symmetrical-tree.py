class node:
    def __init__(self, s):
        self.s = s
        self.left = None
        self.right = None


def reverse(nodee):
    if nodee is None:
        return None
    else:
        result = node(nodee.s)
        result.left = reverse(nodee.right)
        result.right = reverse(nodee.left)
        return result


def check(node1, node2):
    if node1 is None and node2 is None:
        return True
    elif node1 is None or node2 is None:
        return False
    elif node1.s != node2.s:
        return False
    else:
        return check(node1.left, node2.left) and check(node1.right, node2.right)


first = node('a')
second1 = node('b')
second2 = node('b')
second1.left = node('d')
second1.right = node('e')
second2.left = node('e')
second2.right = node('d')
first.right = second2
first.left = second1
print(check(first, reverse(first)))
