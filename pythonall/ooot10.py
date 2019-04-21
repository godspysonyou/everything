class FranchDeck:
    ranks = [str(n) for n in range(2,11)] + list('JQKA')
    suits = ['红心','方块','梅花','黑桃']

    def __init__(self):
        self._cards = [(rank, suit) for rank in FranchDeck.ranks for suit in FranchDeck.suits]


    def __len__(self):
        return len(self._cards)

    def __getitem__(self, item):
        return self._cards[item]

deck = FranchDeck()
print(deck[0])
from random import choice
print(choice(deck))
print(choice(deck))