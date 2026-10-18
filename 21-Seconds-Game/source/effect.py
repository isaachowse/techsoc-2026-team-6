from abc import ABC
from card import Card, CardType, Suit

class BaseEffect(Card):
  _card: Card
  modifier: int

  def __init__(self, card: Card) -> None:
    self._card = card

  @property
  def suit(self) -> Suit:
    return self._card.suit

  @property
  def type(self) -> CardType:
    return self._card.type

  def __str__(self) -> str:
    return f"{self._card} [{self.__class__.__name__}({self.modifier}) = {self.score}]"

class MultEffect(BaseEffect):
  def __init__(self, card: Card, multiplier: int):
    super().__init__(card)
    self.modifier = multiplier

  @property
  def score(self) -> int:
    return self._card.score * self.modifier

class AddEffect(BaseEffect):
  def __init__(self, card: Card, toAdd: int):
      super().__init__(card)
      self.modifier = toAdd

  @property
  def score(self):
    return self._card.score + self.modifier
