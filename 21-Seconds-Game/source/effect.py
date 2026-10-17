from abc import ABC
from card import Card, CardType

class EffectDec(Card):
  _card: Card
  _modifier: int

  def __init__(self, card: Card) -> None:
    self._card = card

  @property
  def suit(self) -> Suit:
    return self._card.suit

  @property
  def type(self) -> CardType:
    return self._card.type

  def __str__(self) -> str:
    return f"{self._card} [{self.__class__.__name__}({self._modifier})]"

class MultEffect(EffectDec):
  def __init__(self, card: Card, multiplier: int):
    super().__init__(card)
    self._modifier = multiplier

  @property
  def score(self) -> int:
    return self.type.num_value * self._modifier

class AddEffect(EffectDec):
  def __init__(self, card: Card, toAdd: int):
      super().__init__(card)
      self._modifier = toAdd

  @property
  def score(self):
    return self._card.score * self._modifier
