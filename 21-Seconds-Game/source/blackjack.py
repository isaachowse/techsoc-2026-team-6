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
  def score(self) -> int:
    total = sum(card.score for card in self._cards)
    aces = sum(1 for card in self._cards if card.type == CardType.ACE)

    while total > 21 and aces > 0:
      total -= CardType.ACE.num_value
      aces -= 1

    return total - 1

  def __str__(self) -> str:
    return f"{list(map(str, self._cards))} ({self.score})"

class Blackjack:
  player: Hand
  _wild: bool
  hits: int
  stands: int
  _deck: list[Card]
  _baseDeck: list[Card]
  _wildDeck: list[int]
  _wildcard_count: int
  _cur_WildCard: int
  _roundCount: int
  _roundScore: int
  _bjVal: int

  def __init__(self) -> None:
    self.player = Hand()
    self.hits = 7
    self.stands = 1
    self._roundCount = 0
    self._roundScore = 0
    self._bjVal = 21
    self._baseDeck = [BaseCard(suit, type) for type in CardType for suit in Suit]
    self._deck = self._baseDeck.copy()
    self._wildcard_count = 0
    self._cur_WildCard = 0
    self._wildDeck = self.createWildDeck()
    self._wild = False
    self.newHand()
    

  def newHand(self) -> None:
    self.setRoundScore(0)
    self.setRoundCount(self.getRoundScore()+1)
    self._deck = self._baseDeck.copy()
    self.player.empty()

    # shuffle and deal
    self.shuffle(self._deck)

    self.hit(self.player)
    self.hit(self.player)

  def stand(self, hand:Hand) -> None:

    #check if next card should be wildcard
    self.setWild(self.isNextWild())
    self.stands -=1
    if self.stands > 0:
      if self.getWild() == True:
        localWild = self.getWildDeck()[self.getCurrentWildCard()]
        if self.getCurrentWildCard() % 2 == 0:
          self.setBJVal(self.getBJVal() + localWild)
        else:
          self.setBJVal(self.getBJVal() * localWild)
      else:    
        #check if deck is empty
        if self.checkDeck() == False:
          self.newHand()
        self._deck.pop()
      #check if next card should be wildcard
      self.setWild(self.isNextWild())
    if self.stands == 0:
        self.hits = 5
    self.winCheck()

  def hit(self, hand: Hand) -> None:
    self.hits -= 1
    if self.hits > 0:
      if self.getWild() == False:
        card = self._deck.pop()
        self.setRoundScore(self.getRoundScore()+card.score)
        print(self.getRoundScore())
        hand.add(card)
        #check if deck is empty
        if self.checkDeck() == False:
          self.newHand()
      else:
        card = self._deck[0]
        card = self.wildCard(self.getWildDeck(),self.getCurrentWildCard(),card)
      #check if next card should be wildcard
      self.setWild(self.isNextWild())
    if self.hits == 0:
      self.stands = 1
    self.winCheck()

  def getWildDeck(self) -> list[int]:
    return self._wildDeck

  def getRoundScore(self) -> int:
    return self._roundScore

  def setRoundScore(self, newVal) -> None:
    self._roundScore = newVal

  def getRoundCount(self) -> int:
    return self._roundCount

  def setRoundCount(self, newVal) -> None:
    self._roundCount = newVal

  def getBJVal(self) -> int:
      return self._bjVal
  
  def setBJVal(self, newVal) -> None:
      self._bjVal = newVal

  def getWild(self) -> bool:
    return self._wild

  def setWild(self, newBool) -> None:
    self._wild = newBool

  def getCurrentWildCard(self) -> int:
      return self._cur_WildCard

  def setCurrentWildCard(self, newVal:int) -> None:
    self._cur_WildCard = newVal

  def checkDeck(self) -> bool:
    if self._deck:
      return True
    return False

  def _deal(self) -> None:
    self.player.reset()
    self.hit(self.player)
    self.hit(self.player)

  def wildCard(self, wildDeck:list[int], wildCard:int, nextCard:BaseCard) -> None:
    if (wildCard % 2 == 0):
       return AddEffect(nextCard,wildDeck[wildCard])
    return MultEffect(nextCard,wildDeck[wildCard])

  def createWildDeck(self) -> list[int]:
    return [5,2,10,3,20,4,50,5,100,6,300,10]

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

  def winCheck(self):
    if self.getRoundScore() == self.getBJVal():
      print("win")
      return True
    return False
  
  @property
  def bust_value(self) -> int:
    return 21 + (sum(wild.modifier for wild in self._deck if issubclass(wild.__class__, AddEffect)) * (1 + sum(wild.modifier for wild in self._deck if issubclass(wild.__class__, MultEffect)))) # type: ignore
