import pygame
from pygame.rect import Rect
from pygame.surface import Surface


class Button:
    _image: Surface
    """The image to display of the button."""

    _rect: Rect

    _disabled: bool
    """Is the button disabled?"""

    def __init__(self, x: int, y: int, scale: float, path: str):
        image = pygame.image.load(path).convert_alpha()
        width = image.get_width()
        height = image.get_height()

        self._image = pygame.transform.scale(
            image, (int(width * scale), int(height * scale))
        )

        self._rect = self._image.get_rect()
        self._rect.topleft = (x, y)

        self._disabled = False

    def draw(self, surface: Surface):
        """Blit the button to the surface."""
        action = False
        image = self._image.copy()

        if self.disabled:
            dark = Surface(
                (self._image.get_width(), self._image.get_height()),
                flags=pygame.SRCALPHA,
            )
            dark.fill((100, 100, 100, 0))
            image.blit(dark, (0, 0), special_flags=pygame.BLEND_RGBA_SUB)

        surface.blit(image, (self._rect.x, self._rect.y))

        return action

    @property
    def disabled(self) -> bool:
        return self._disabled

    def setDisabled(self, disabled: bool) -> None:
        self._disabled = disabled
