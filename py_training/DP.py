# 使用1， 5， 11获取15
a, b, c = 1, 5, 11
target = 15


def gettarget(target):
    if target < 0:
        return 1
    else:
        return min(gettarget(target - a), gettarget(target - b), gettarget(target - c)) + 1


# DAG 最短路  S->(10)A ->(30)C ->(20)T
#                   A ->(10)D
#                   C ->(5)D
#            S->(20)B ->(20)D ->(10)T


class node:
    def __init__(self, road=None):
        self.road = road

    def findroad(self):
        result = []
        if self.road:
            for i in self.road.keys():
                result.append(i.findroad() + self.road[i])
            return min(result)
        else:
            return 0


s = node()
a = node({s: 10})
b = node({s: 20})
c = node({a: 30})
d = node({c: 5, a: 10, b: 20})
t = node({c: 20, d: 10})

# 最长上升子序列
test = [1, 5, 3, 4, 6, 9, 7, 8]
test.reverse()


def longest(loc):
    temp = []
    if loc < len(test) - 1:
        for i in range(loc + 1, len(test)):
            if test[i] < test[loc]:
                temp.append(longest(i) + 1)
            else:
                temp.append(longest(i))
        return max(temp)
    else:
        return 1

