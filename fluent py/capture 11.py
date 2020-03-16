# 当python没有发现iter方法时会通过getitem完成迭代
import collections

Card = collections.namedtuple('Card', ['rank', 'suit'])


class FrenchDeck(collections.MutableSequence):
    # 必须实现所继承的抽象基类要求的全部方法，编译时不会检查方法是否被全部实现，实例化时才检查
    ranks = [str(n) for n in range(2, 11)] + list('JQKA')
    suits = 'spades diamonds clubs hearts'.split()

    def __init__(self):
        self._cards = [Card(rank, suit) for suit in self.suits for rank in self.ranks]

    def __len__(self):
        return len(self._cards)

    def __getitem__(self, item):  # 当只有getitem方法时，只有不可变序列协议
        return self._cards[item]

    def __setitem__(self, key, value):  # 实现该方法后才能为序列赋值
        self._cards[key] = value

    def __delitem__(self, key):
        del self._cards[key]

    def insert(self, key, value):
        self._cards.insert(key, value)


