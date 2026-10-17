from abc import ABC
from card import BaseCard, Card, CardType, Suit
import random

class PlayerBase(ABC):
  _hand: list[Card]

  def __init__(self) -> None:
    self._hand = []

  def addCard(self, card: Card):
    self._hand.append(card)

  def __str__(self) -> str:
    return str(list(map(str, self._hand)))

class Player(PlayerBase):
  ...

class Dealer(PlayerBase):
  _deck: list[Card]

  def __init__(self):
    super().__init__()
    self._deck = [BaseCard(suit, type) for type in CardType for suit in Suit]

  def hit(self, player: PlayerBase):
    player.addCard(self._deck.pop())

  def deal(self, player: PlayerBase):
    self.hit(player)
    self.hit(player)

  def shuffle(self):
    for i in range(len(self._deck) - 1, 0, -1):
        j = random.randint(0,i)
        self._deck[i], self._deck[j] = self._deck[j], self._deck[i]
