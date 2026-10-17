import pygame
from player import Dealer, Player

def start():
    (width, height) = (300, 200)
    screen = pygame.display.set_mode((width, height))
    pygame.display.flip()

    dealer = Dealer()
    player = Player()

    dealer.deal(dealer)
    dealer.deal(player)

    print(player)
    dealer.hit(player)
    print(player)

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

if __name__ == "__main__":
    pygame.init()
    start()
