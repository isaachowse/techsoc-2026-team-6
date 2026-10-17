from abc import ABC, abstractmethod
from enum import Enum


class Suit(Enum):
  DIAMOND = 0
  CLUB = 1
  HEART = 2
  SPADE = 3

class CardType(Enum):
  ONE = 1
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

class BaseCard(Card):
  _suit: Suit
  _type: CardType

  def __init__(self, suit: Suit, type: CardType) -> None:
    self._suit = suit
    self._type = type

  def changeCard(self, type: CardType):
    self._type = type

  def applyEffect(self) -> None:
    return super().applyEffect()

  @property
  def name(self) -> str:
    return self._type.name.title()

  @property
  def value(self) -> int:
    return self._type.value

  @property
  def suit_name(self) -> str:
    return self._suit.name.title()

  def __str__(self) -> str:
    return f"{self._type} of {self._suit}"

  def getCard(self, suit, type) -> 'BaseCard':
    return BaseCard(suit, type)

  def getSmallImage(self) -> str:
    return f"21-Seconds-Game/assets/Cards/PNG/cards-small/card_{self._suit.name.lower()}_{self._type.value:02d}.png"

  def getMediumImage(self) -> str:
    return f"21-Seconds-Game/assets/Cards/PNG/cards-medium/card_{self._suit.name.lower()}_{self._type.value:02d}.png"

  def getLargeImage(self) -> str:
    return f"21-Seconds-Game/assets/Cards/PNG/cards-large/card_{self._suit.name.lower()}_{self._type.value:02d}.png"
  
