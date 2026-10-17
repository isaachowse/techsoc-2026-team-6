import pygame

pygame.init()

(width, height) = (500, 400)
screen = pygame.display.set_mode((width, height))
clubs = pygame.image.load("21-Seconds-Game/assets/Cards/PNG/cards-medium/card_clubs_02.png").convert_alpha()
screen.blit(clubs, (0, 0))
pygame.display.flip()

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

