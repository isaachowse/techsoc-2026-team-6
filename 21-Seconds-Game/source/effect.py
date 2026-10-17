from abc import ABC
from .card import Card

class EffectDec(Card):
  _card: Card

  def __init__(self, card: Card) -> None:
    self._card = card

  def applyEffect(self) -> None:
    return self._card.applyEffect()

class EffectA(EffectDec):
  def applyEffect(self) -> None:
    super().applyEffect()
    print("Effect A applied!")
