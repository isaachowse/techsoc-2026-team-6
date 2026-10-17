import pygame
from pygame import QUIT, KEYDOWN, K_a, K_l
from button import Button
from blackjack import Blackjack

class Display():

    def __init__(self, blackjack):
        self.blackjack = blackjack

    def start(self):
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
        hitButton = Button(150, 250, hitImage, 6)
        standButton = Button(550, 250, standImage, 6)
        buttons = [playButton, exitButton, hitButton, standButton]

        pygame.display.flip()

        running = True
        while running:
            for event in pygame.event.get():
                if event.type == KEYDOWN:
                    if event.key == K_a:
                        if homeScreen and not playButton.disabled:
                            homeScreen = False
                        elif not hitButton.disabled:
                            aKey()
                    elif event.key == K_l:
                        if homeScreen and not exitButton.disabled:
                          running = False
                        elif not standButton.disabled:
                          ...
                if event.type == QUIT:
                    running = False

            screen.fill(backgroundColour)

            if homeScreen:
                playButton.draw(screen)
                exitButton.draw(screen)
            else:
                hitButton.draw(screen)
                standButton.draw(screen)
            pygame.display.update()
        pygame.quit()

    def aKey(self):
        pass
