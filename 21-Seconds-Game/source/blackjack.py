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


def _wildCard(card: Card, i: int) -> Card:
  wildDeck = [5,2,15,4,30,8,300,16,600,24,1000]

  if i > len(wildDeck) - 1:
    return card
  elif (i % 2 == 0):
    return AddEffect(card, wildDeck[i])
  return MultEffect(card, wildDeck[i])

class Blackjack:
  dealer: Hand
  player: Hand
  _wild: bool
  hits: int
  stands: int
  _deck: list[Card]
  _wildDeck: list[int]
  _wildcard_count: int
  _cur_WildCard: int

  def __init__(self) -> None:
    self.dealer = Hand()
    self.player = Hand()
    self.hits = 5
    self.stands = 1
    self._deck = [BaseCard(suit, type) for type in CardType for suit in Suit]
    self._wildcard_count = 0
    self.newHand()

  def newHand(self) -> None:
    for hand in (self.player, self.dealer):
      self._deck.extend(hand.empty())

    # make one a wildcard
    self.setWild(self.isNextWild())

    # shuffle and deal
    self.shuffle(self._deck)

    for hand in (self.player, self.dealer):
      self.hit(hand)
      self.hit(hand)

  def getWildDeck(self) -> list[int]:
    return self._wildDeck
  
  def hit(self, hand: Hand) -> None:
    if self.hits == 0:
      return

    card = self._deck.pop()
    hand.add(card)
    self.hits -= 1

    if self.hit == 0:
      self.hits = 5
      self.stands += 1

  def stand(self) -> None:
    if self.stands == 0:
      return

    self.stands -= 1
    self.hits += 5

  def getWild(self) -> bool:
    return self._wild

  def setWild(self, newBool) -> None:
    self._wild = newBool

  def setCurrentWildCard(self, newVal:int) -> None:
    self._cur_WildCard = newVal

  def hit(self, hand: Hand) -> None:
    self.setWild(self.isNextWild())
    if self.getWild == False:
      card = self._deck.pop()
      hand.add(card)
    else:
      card = self._deck.pop()
      card = self.wildCard(self.getWildDeck,self.getWild,card)

  def _deal(self) -> None:
    for hand in (self.player, self.dealer):
      hand.reset()
      self.hit(hand)
      self.hit(hand)

  def wildCard(self, wildDeck:list[int], wildCard:int, nextCard:BaseCard) -> None:
    if (wildCard % 2 == 0):
       return AddEffect(nextCard,wildDeck[wildCard])
    return MultEffect(nextCard,wildDeck[wildCard])

  def createWildDeck(self) -> list[int]:
    return [5,2,15,4,30,8,300,16,600,24,1000]

  def shuffle(self, deck:list[BaseCard]) -> list[BaseCard]:
    for i in range(len(deck)-1,0,-1):
        j = random.randint(0,i)
        deck[i],deck[j]=deck[j],deck[i]
    return deck

  def isNextWild(self) -> bool:
    if random.randint(0,4) == 1:
      self.setCurrentWildCard(random.randint(0,11))
      return True
    return False
  
  @property
  def bust_value(self) -> int:
    return 21 + (sum(wild.modifier for wild in self._deck if issubclass(wild.__class__, AddEffect)) * (1 + sum(wild.modifier for wild in self._deck if issubclass(wild.__class__, MultEffect)))) # type: ignore
