import pygame
from blackjack import Blackjack

def start():
    pygame.init()
    (width, height) = (1000, 500)
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
