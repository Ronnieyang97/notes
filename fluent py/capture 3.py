# 只有可散列的数据类型才可以作为映射里的键
# 对于可散列对象，在其生命周期中散列值不变，且该对象需要实现__hash__()方法和__qe__()方法。
# 原子不可变数据类型（str、bytes和数值类型）是可散列的，frozenset只能容纳可散列类型
# 对于元组只有当其包含的元素都是可散列的他才是可散列的
import collections as co
from types import MappingProxyType

# 字典的多种创建形式
dict_a = dict(one=1, two=2, three=3)
dict_b = dict(zip(['one', 'two', 'three'], [1, 2, 3]))
dict_c = dict([('one', 1), ('two', 2), ('three', 3)])

dict_a.setdefault('four', 4)  # 当字典中没有four这个key时，会自动创建'four':4
dict_a.setdefault('two', 22)  # 当字典中存在two这个key时则不会发生改变

dict_d = co.defaultdict(int)  # 通过collections中的defaultdict设置default_factory为int（list等也可）
print(dict_d['five'])  # 当查询不到five这个key时，会直接返回0，如果是list则是空列表。
# 此情况只会在getitem被调用时触发

# dict.keys()返回的是一个视图而不是一个列表，因此遍历起来很快

dict_order = co.OrderedDict(one=1, two=2, three=3)  # 有序字典
dict_counter = co.Counter('gfhhkkkcx')  # 对象可以是字符串也可以是list等
# 每更新一个键会对其进行计数，对含有多个重复的value的字典很有用，可以通过most_common(n)返回出现次数最多的
print(dict_counter)


class TestDict(co.UserDict):  # 该基类用于创造自定义映射类型，list等数据类型同理，
    # userdict的data属性是dict的实例，是其最终存储数据的地方
    pass


dict_proxy = MappingProxyType(dict_a)
# 如此设置后，dict_proxy是只读对象,而当dict_a发生改变时，dict_proxy也会改变

# set本身是不可散列的，但是其中的元素必须是散列的

