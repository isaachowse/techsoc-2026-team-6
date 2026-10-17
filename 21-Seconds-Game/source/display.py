import pygame
from pygame import QUIT, KEYDOWN, K_a, K_l
from button import Button
from blackjack import Blackjack
import card

class Display():

    def __init__(self, blackjack):
        self.blackjack = blackjack

    def display_card(self, card: card.BaseCard):
        print(card.name)

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
                        if homeScreen:
                            homeScreen = False
                        else:
                            aKey()
                    elif event.key == K_l:
                        running = False
                if event.type == QUIT:
                    running = False

            screen.fill(backgroundColour)

            if homeScreen:
                playButton.draw(screen)
                exitButton.draw(screen)
            else:
                self.display_card(self, card.BaseCard(suit=card.Suit.HEART, type=card.CardType.ONE))
                hitButton.draw(screen)
                standButton.draw(screen)

            pygame.display.update()
        pygame.quit()

    def aKey(self):
        pass
