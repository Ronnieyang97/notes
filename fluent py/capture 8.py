import copy

# 变量是标注，不是盒子
a = [1, 2, 3]
b = a
a.append(4)
print(b)  # 此时b的结果为[1, 2, 3, 4]与a同时发生了变化
print(id(a), id(b))  # 可以看到id是相同的，因此a,b都只是[1, 2, 3, 4]这个对象绑定上的标签

c = [1, 2, 3, 4]
print(c == a, a is c)  # ==比较的是值，is比较的是对象，因此a与c的值相同，但是指向的并非是同一个对象，is不可重载

new_a = [1, 2, [3, 4], (5, 6)]
new_b = list(new_a)
print(new_a == new_b, new_a is new_b)  # list创建了a的副本，将其给了d，因此而这对象不同值相同，浅复制
new_a.append(7)  # 对new_b没有影响
new_a[2].append(8)  # 对new_b有影响，因为new_a和new_b的[2]绑定的对象是同一个
new_b[3] += (9, 10)  # 对元组来说+=操作意味着创建一个新元组，因此new_a和new_b的[3]的对象不同


class Bus:
    def __init__(self, passengers):
        self.passengers = passengers

    def on(self, name):
        self.passengers.append(name)

    def off(self, name):
        self.passengers.remove(name)


bus1 = Bus(['tom', 'may'])
bus2 = copy.copy(bus1)  # 浅复制
bus3 = copy.deepcopy(bus1)  # 深复制
# bus1, bus2, bus3的id都是不同的
print(id(bus1.passengers), id(bus2.passengers), id(bus3.passengers))
# bus1和bus2的passengers属性的id相同，为同一对象，bus3的passengers属性则跟前二者不同

a = [10, 20]
b = [a, 30]
a.append(b)
print(a)  # 循环引用，如果要实现deepcopy/copy需要实现其特殊方法__copy__/__deepcopy__

# 不要使用可变值作为默认参数，接受可变参数是有风险的，因此在接受传入的可变参数时创建副本（如果要对其作改动）


