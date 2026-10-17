from abc import ABC, abstractmethod
from enum import StrEnum
from typing import override


class Suit(StrEnum):
  DIAMOND = 'Diamonds'
  CLUB = 'Clubs'
  HEART = 'Hearts'
  SPADE = 'Spades'

class CardType(StrEnum):
  ONE = '1'
  TWO = '2'
  THREE = '3'
  FOUR = '4'
  FIVE = '5'
  SIX = '6'
  SEVEN = '7'
  EIGHT = '8'
  NINE = '9'
  TEN = '10'
  JACK = 'Jack'
  QUEEN = 'Queen'
  KING = 'King'
  ACE = 'Ace'

  @property
  def num_value(self) -> int:
    try:
      return int(self.value)
    except ValueError:
      return 11 if self == CardType.ACE else 10


class Card(ABC):
  @abstractmethod
  def applyEffect(self) -> None: pass

  @property
  @abstractmethod
  def type(self) -> CardType: pass

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
    return min(self._type.num_value, 10)

  def setScore(self, newVal) -> None:
    self._score = newVal

  def getScore(self):
    return self._score

  def applyEffect(self) -> None:
    return super().applyEffect()

  @property
  def type(self) -> CardType:
    return self._type

  @property
  def name(self) -> str:
    return f"{self._type.name.title()} of {self._suit.value}"

  def __str__(self) -> str:
    return self.name

  def getCard(self, suit, type) -> 'BaseCard':
    return BaseCard(suit, type)

  def getSmallImage(self) -> str:
    return f"21-Seconds-Game/assets/Cards/PNG/cards-small/card_{self._suit.name.lower()}_{self._type.value:02d}.png"

  def getMediumImage(self) -> str:
    return f"21-Seconds-Game/assets/Cards/PNG/cards-medium/card_{self._suit.name.lower()}_{self._type.value:02d}.png"

  def getLargeImage(self) -> str:
    return f"21-Seconds-Game/assets/Cards/PNG/cards-large/card_{self._suit.name.lower()}_{self._type.value:02d}.png"
