from abc import ABC, abstractmethod
from enum import Enum


class Suit(Enum):
  DIAMOND = 0
  CLUB = 1
  HEART = 2
  SPADE = 3

class CardType(Enum):
  ACE = 1
  TWO = 2
  THREE = 3
  FOUR = 4
  FIVE = 5
  SIX = 6
  SEVEN = 7
  EIGHT = 8
  NINE = 9
  TEN = 10
  JACK = 11
  QUEEN = 12
  KING = 13

class Card(ABC):
  @abstractmethod
  def applyEffect(self) -> None:
    pass

  @abstractmethod
  def getValue(self) -> int:
    pass

  @abstractmethod
  def setScore(self, newVal) -> None:
    pass

  @abstractmethod
  def getScore(self, newVal) -> int:
    pass

class BaseCard(Card):
  _suit: Suit
  _type: CardType
  _score: int

  def __init__(self, suit: Suit, type: CardType) -> None:
    self._suit = suit
    self._type = type
    self._score = self.setScore(self.getValue())

  def changeCard(self, type: CardType):
    self._type = type

  def getValue(self) -> int:
    return min(self._type.value,10)

  def setScore(self, newVal) -> None:
    self._score = newVal

  def getScore(self):
    return self._score

  def applyEffect(self) -> None:
    self.setScore(self.getValue())

  def __str__(self) -> str:
    return f"{self._type} of {self._suit}"
