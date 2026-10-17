from abc import ABC
from card import Card

class EffectDec(Card):
  _card: Card
  _effectVal: int

  def __init__(self, card: Card) -> None:
    self._card = card

  def applyEffect(self) -> None:
    return self._card.applyEffect()

  def getEffectVal(self) -> int:
      return self._effectVal

  def setEffectVal(self, newVal) -> None:
      self._effectVal = newVal

  def getValue(self) -> int:
    return self._card.getValue()

  def setScore(self, newVal) -> None:
    self._card.setScore(newVal)

  def getScore(self) -> None:
    return self._card.getScore()

class MultEffect(EffectDec):

  def __init__(self, card, newVal:int):
    super().__init__(card)
    self.setEffectVal(newVal)

  def applyEffect(self) -> None:
    super().applyEffect()
    self.setScore(self.getScore() * self.getEffectVal())
    

class AddEffect(EffectDec):

  def __init__(self, card, newVal:int):
      super().__init__(card)
      self.setEffectVal(newVal)

  def applyEffect(self) -> None:
    super().applyEffect()
    self.setScore(self.getScore() + self.getEffectVal())
