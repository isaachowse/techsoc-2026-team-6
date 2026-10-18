import pygame
from pygame.rect import Rect
from pygame.surface import Surface

class Button():
  _image: Surface
  _rect: Rect
  disabled: bool

  def __init__(self, x: int, y: int, image: Surface, scale: float):
      width = image.get_width()
      height = image.get_height()

      self._image = pygame.transform.scale(image, (int(width * scale), int(height * scale)))
      self._rect = self._image.get_rect()
      self._rect.topleft = (x, y)
      self.disabled = False

  def draw(self, surface: Surface):
      action = False
      image = self._image.copy()

      if self.disabled:
        dark = Surface((self._image.get_width(), self._image.get_height()), flags=pygame.SRCALPHA)
        dark.fill((100, 100, 100, 0))
        image.blit(dark, (0, 0), special_flags=pygame.BLEND_RGBA_SUB)

      surface.blit(image, (self._rect.x, self._rect.y))

      return action

  def set_disabled(self, disabled: bool) -> None:
    self.disabled = disabled

  def remove(self, surface: Surface):
      surface.blit(Surface((self._rect.width, self._rect.height)), (self._rect.x, self._rect.y))
