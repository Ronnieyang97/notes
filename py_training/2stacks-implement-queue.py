# 两个栈实现队列
# 用两个栈来实现一个队列，完成队列的Push和Pop操作。 队列中的元素为int类型

class myqueue:
    def __init__(self):
        self.stack1 = []
        self.stack2 = []

    def push(self, num):
        self.stack1.append(num)

    def pop(self):
        if self.stack1:
            while self.stack1:
                self.stack2.append(self.stack1.pop())
            print(self.stack2.pop())
            while self.stack2:
                self.stack1.append(self.stack2.pop())
        else:
            return None


q = myqueue()
q.push('a')
q.push('b')
q.pop()
