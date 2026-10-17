import pygame
import sys
from card import Suit, CardType, BaseCard

class GameGUI:
    def __init__(self, width=800, height=600):
        pygame.init()
        self.width = width
        self.height = height
        self.screen = pygame.display.set_mode((width, height))

game = GameGUI
game.run()