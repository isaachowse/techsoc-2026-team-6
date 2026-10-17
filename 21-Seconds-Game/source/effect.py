from abc import ABC
from card import Card, CardType

class EffectDec(Card):
  _card: Card
  _effectVal: int

  def __init__(self, card: Card) -> None:
    self._card = card

  @property
  def score(self):
    return self._card.score

  @property
  def type(self) -> CardType:
    return self._card.type

  def __str__(self) -> str:
    return f"{self._card} ({self.__class__.__name__})"

class MultEffect(EffectDec):
  def __init__(self, card: Card, effectVal: int):
    super().__init__(card)
    self._effectVal = effectVal

  @property
  def score(self) -> int:
    return self.type.num_value * self._effectVal

class AddEffect(EffectDec):
  def __init__(self, card: Card, effectVal: int):
      super().__init__(card)
      self._effectVal = effectVal

  @property
  def score(self):
    return self._card.score * self._effectVal
