from abc import ABC
from card import BaseCard, CardType, Suit

class BaseEffect(BaseCard):
  _card: BaseCard
  """The card wrapped by the effect."""

  _modifier: int
  """The amount applied by the effect."""

  def __init__(self, card: BaseCard) -> None:
    self._card = card

  @property
  def suit(self) -> Suit:
    return self._card.suit

  @property
  def type(self) -> CardType:
    return self._card.type

  @property
  def modifier(self) -> int:
    """The amount applied by the effect."""
    return self._modifier

  def __str__(self) -> str:
    return f"{self._card} [{self.__class__.__name__}({self.modifier}) = {self.score}]"

class MultEffect(BaseEffect):
  def __init__(self, card: BaseCard, multiplier: int):
    super().__init__(card)
    self._modifier = multiplier

  @property
  def score(self) -> int:
    return self._card.score * self.modifier

class AddEffect(BaseEffect):
  def __init__(self, card: BaseCard, toAdd: int):
      super().__init__(card)
      self._modifier = toAdd

  @property
  def score(self):
    return self._card.score + self.modifier
