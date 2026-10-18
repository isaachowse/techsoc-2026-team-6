from card import BaseCard, Card, CardType, Suit
from effect import MultEffect, AddEffect
import random

class Hand:
  _cards: list[Card]

  def __init__(self) -> None:
    self._cards = []

  def add(self, card: Card) -> None:
    self._cards.append(card)

  def empty(self) -> list[Card]:
    copy = self._cards.copy()
    self._cards.clear()
    return copy

  @property
  def value(self) -> int:
    total = sum(card.score for card in self._cards)
    aces = sum(1 for card in self._cards if card.type == CardType.ACE)

    while total > 21 and aces > 0:
      total -= CardType.ACE.num_value
      aces -= 1

    return total

  def __str__(self) -> str:
    return f"{list(map(str, self._cards))} ({self.value})"

class Blackjack:
  dealer: Hand
  player: Hand
  hits: int
  stands: int
  _deck: list[Card]

  def __init__(self) -> None:
    self.dealer = Hand()
    self.player = Hand()
    self._deck = [BaseCard(suit, type) for type in CardType for suit in Suit]
    self.newHand()


  def newHand(self) -> None:
    for hand in (self.player, self.dealer):
      self._deck.extend(hand.empty())
    random.shuffle(self._deck)
    for hand in (self.player, self.dealer):
      self.hit(hand)
      self.hit(hand)

  def hit(self, hand: Hand) -> None:
    card = self._deck.pop()
    hand.add(card)

  def stand(self) -> None:
    return

  @property
  def bust_value(self) -> int:
    return 21
