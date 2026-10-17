import pygame
from blackjack import Blackjack
from card import BaseCard, Suit, CardType
from effect import EffectDec, MultEffect, AddEffect

def start():
    pygame.init()
    (width, height) = (1000, 500)
    screen = pygame.display.set_mode((width, height))
    pygame.display.flip()

    game = Blackjack()
    print(game.dealer, game.player)

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

if __name__ == "__main__":
    pygame.init()
    start()
