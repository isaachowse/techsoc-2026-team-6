import pygame
from pygame import QUIT, KEYDOWN, K_a, K_l
from button import Button
from card import Card

def start():
    pygame.init()
    (width, height) = (1000, 500)
    screen = pygame.display.set_mode((width, height))
    backgroundColour = [53, 101, 77]

    homeScreen = True

    playImage = pygame.image.load("21-Seconds-Game/assets/Buttons/play-button.png").convert_alpha()
    exitImage = pygame.image.load("21-Seconds-Game/assets/Buttons/exit-button.png").convert_alpha()
    hitImage = pygame.image.load("21-Seconds-Game/assets/Buttons/hit-button.png").convert_alpha()
    standImage = pygame.image.load("21-Seconds-Game/assets/Buttons/stand-button.png").convert_alpha()

    playButton = Button(150, 250, playImage, 6)
    exitButton = Button(550, 250, exitImage, 6)
    hitButton = Button(150, 350, hitImage, 6)
    standButton = Button(550, 350, standImage, 6)
    buttons = [playButton, exitButton, hitButton, standButton]

    pygame.display.flip()

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == KEYDOWN:
                if event.key == K_a:
                    homeScreen = not homeScreen
                elif event.key == K_l:
                    running = False
            if event.type == QUIT:
                running = False

        screen.fill(backgroundColour)

        if homeScreen:
            playButton.draw(screen)
            exitButton.draw(screen)
        else:
            loadGameScreen(screen, buttons)
            displayCard(screen, Card)
        pygame.display.update()
    pygame.quit()

def displayCard(Screen, Card):
    print(card.type)


def loadGameScreen(screen, buttons):
    buttons[2].draw(screen)
    buttons[3].draw(screen)
    pygame.display.update()



start()
