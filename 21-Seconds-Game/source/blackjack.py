from card import BaseCard, Card, CardType, Suit
import random

class Hand:
  _cards: list[Card]

  def __init__(self) -> None:
    self._cards = []

  def add(self, card: Card) -> None:
    self._cards.append(card)

  def reset(self) -> None:
    self._cards.clear()

  @property
  def value(self) -> int:
    total = sum(card.value for card in self._cards)
    ace_count = sum(1 for card in self._cards if card.type == CardType.ACE)

    while total > 21 and ace_count > 0:
      total -= CardType.ACE.num_value
      ace_count -= 1

    return total

  @property
  def is_bust(self) -> bool:
    return self.value > 21

  def __str__(self) -> str:
    return str(list(map(str, self._cards)))

class Blackjack:
  dealer: Hand
  player: Hand

  _deck: list[Card]

  def __init__(self) -> None:
    self.dealer = Hand()
    self.player = Hand()
    self.newHand()

  def newHand(self) -> None:
    self._deck = [BaseCard(suit, type) for type in CardType for suit in Suit]
    random.shuffle(self._deck)
    self._deal()

  def hit(self, hand: Hand) -> None:
    card = self._deck.pop()
    hand.add(card)

  def _deal(self) -> None:
    for hand in (self.player, self.dealer):
      hand.reset()
      self.hit(hand)
      self.hit(hand)
