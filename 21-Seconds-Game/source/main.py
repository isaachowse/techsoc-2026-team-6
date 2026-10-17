import pygame
from blackjack import Blackjack

def start():
    (width, height) = (300, 200)
    screen = pygame.display.set_mode((width, height))
    pygame.display.flip()

    game = Blackjack()
    print(game.player, game.dealer)
    game.newHand()
    print(game.player, game.dealer)

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

if __name__ == "__main__":
    pygame.init()
    start()
