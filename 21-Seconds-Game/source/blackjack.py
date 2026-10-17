from card import BaseCard, Card, CardType, Suit
from effect import MultEffect, AddEffect
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
    total = sum(card.score for card in self._cards)
    aces = sum(1 for card in self._cards if card.type == CardType.ACE)

    while total > 21 and aces > 0:
      total -= CardType.ACE.num_value
      aces -= 1

    return total

  @property
  def is_bust(self) -> bool:
    return self.value > 21

  def __str__(self) -> str:
    return f"{list(map(str, self._cards))} ({self.value})"

class Blackjack:
  dealer: Hand
  player: Hand
  _wild: bool
  _deck: list[Card]
  _wildDeck: list[int]

  def __init__(self) -> None:
    self.dealer = Hand()
    self.player = Hand()
    self._wildDeck = self.createWildDeck()
    self.newHand()

  def newHand(self) -> None:
    self._deck = [BaseCard(suit, type) for type in CardType for suit in Suit]
    self.shuffle(self._deck)
    self._deal()

  def getWildDeck(self) -> list[int]:
    return self._wildDeck

  def getWild(self) -> bool:
    return self._wild

  def hit(self, hand: Hand) -> None:
    if self.getWild == False:
      card = self._deck.pop()
      hand.add(card)
    else:
      card = self._deck.pop()
      card = self.wildCard()

  def _deal(self) -> None:
    for hand in (self.player, self.dealer):
      hand.reset()
      self.hit(hand)
      self.hit(hand)

  def wildCard(wildDeck:list[int], wildCard:int, nextCard:BaseCard) -> None:
    if (wildCard % 2 == 0):
       return AddEffect(nextCard,wildDeck[wildCard])
    return MultEffect(nextCard,wildDeck[wildCard])

  def createWildDeck() -> list[int]:
    return [5,2,15,4,30,8,300,16,600,24,1000]

  def shuffle(deck:list[BaseCard]) -> list[BaseCard]:
    for i in range(len(deck)-1,0,-1):
        j = random.randint(0,i)
        deck[i],deck[j]=deck[j],deck[i]
    return deck

  def isNextWild():
    if random.randint(0,4) == 1:
      return True
    return False
