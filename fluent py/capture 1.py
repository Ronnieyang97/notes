import collections
import random


card = collections.namedtuple('card', ['rank', 'suit'])  # 利用collection构建一个简单的类，只有属性没有方法
testcard = card('7', 'diamonds')  # 构建方块7


class FrenchDeck:
    # 构建花色和点数
    ranks = [str(n) for n in range(2, 11)] + list('JQKA')
    suits = 'spades diamonds clubs hearts'.split()

    def __init__(self):
        self._cards = [card(rank, suit) for suit in self.suits for rank in self.ranks]

    def __len__(self):
        return len(self._cards)

    def __getitem__(self, item):
        # 此处将[]操作交给了self._cards列表，使FreanchDeck可以支持切片操作，并且可以迭代
        return self._cards[item]


deck = FrenchDeck()
print(len(deck))
print(random.choice(deck))  # 随机抽取
suit_values = dict(spades=3, hearts=2, diamonds=1, clubs=0)


def spades_high(card):
    rank_value = FrenchDeck.ranks.index(card.rank)  # 将点数转换为数字大小
    return rank_value * len(suit_values) + suit_values[card.suit]  # 点数优先于花色


print(sorted(deck, key=spades_high))  # 将其按照花色大小排序，sorted和key的组合使用


class Vector:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def __repr__(self):  # 定义后使得对象能以字符串的形式返回,区别于
        return 'vector({},{})'.format(self.x, self.y)

    def __abs__(self):
        return bool(self.x or self.y)

    def __bool__(self):
        return bool(abs(self))

    def __add__(self, other):
        return Vector(self.x + other.x, self.y + other.y)

