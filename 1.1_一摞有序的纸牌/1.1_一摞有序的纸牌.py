"""
展示如何实现__getitem__和__len__这两个特殊的方法
作者：AugustFan
邮箱：FanY_logic@outlook.com
"""
import collections

# 使用collections.namedtuple构建了一个简单的类来表示一张纸牌。
# namedtuple用以构建只有少数属性但是没有方法的对象，比如数据库条目
Card = collections.namedtuple('Card', ['rank', 'suit'])


class FrenchDeck:
    ranks = [str(n) for n in range(2, 11)] + list('JQKA')
    suits = 'spades diamonds clubs hearts'.split()

    def __init__(self):
        self._cards = [Card(rank, suit) for suit in self.suits
                                        for rank in self.ranks]
    def __len__(self):
        return len(self._cards)

    def __getitem__(self, position):
        return self._cards[position]


def main():
    beer_card = Card('7', 'diamonds')
    print(beer_card)

    deck = FrenchDeck()
    print(len(deck))
    print(deck[0])
    print(deck[-1])

    from random import choice
    print(choice(deck))
    print(choice(deck))
    print(choice(deck))

    print(deck[:3])
    print(deck[12::13])

    for card in deck:
        print(card)

    for card in reversed(deck):
        print(card)

    print(Card('Q', 'hearts') in deck)
    print(Card('7', 'beasts') in deck)

    suit_values = dict(spades=3, hearts=2, diamonds=1, clubs=0)
    def spades_high(card):
        rank_value = FrenchDeck.ranks.index(card.rank)
        return rank_value * len(suit_values) + suit_values[card.suit]

    for card in sorted(deck, key=spades_high):
        print(card)

if __name__ == '__main__':
    main()
