import pygame
from pygame import QUIT, KEYDOWN, K_a, K_l
import time
from button import Button
from blackjack import Blackjack
from animations import move_card, flip_card, button_animation, score_flash_animation, result_animation 
import card
import random  

class Display():

    def __init__(self, blackjack):
        self.blackjack = blackjack
        self.player = self.blackjack.player
        self.dealer = self.blackjack.dealer

    def display_card(self, card):
        return card

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
        hitButton = Button(150, 388, hitImage, 6)
        standButton = Button(550, 388, standImage, 6)

        dealerImage = pygame.image.load("21-Seconds-Game/assets/Dealer.png").convert_alpha()
        dealerImage = pygame.transform.scale(dealerImage, (int(dealerImage.get_width())*0.3, int(dealerImage.get_height())*0.3))

        hitsImage = pygame.image.load("21-Seconds-Game/assets/HitsRemaining.png").convert_alpha()
        hitsImage = pygame.transform.scale(hitsImage, (int(hitsImage.get_width())*5, int(hitsImage.get_height())*5))
        standsImage = pygame.image.load("21-Seconds-Game/assets/StandsRemaining.png").convert_alpha()
        standsImage = pygame.transform.scale(standsImage, (int(standsImage.get_width())*5, int(standsImage.get_height())*5))

        pygame.mixer.music.load("21-Seconds-Game/sounds/music/ost_home.mp3")
        pygame.mixer.music.play(-1)
        pygame.mixer.music.set_volume(0.2)

        pygame.display.flip()

        running = True
        while running:
            for event in pygame.event.get():
                if event.type == KEYDOWN:
                    if event.key == K_a:
                        if homeScreen and not playButton.disabled:
                            press_sound = pygame.mixer.Sound("21-Seconds-Game/sounds/sfx/press_1.wav")
                            press_sound.play()
                            homeScreen = False
                            pygame.mixer.music.load("21-Seconds-Game/sounds/music/ost.mp3")
                            pygame.mixer.music.play(-1)
                            pygame.mixer.music.set_volume(0.2)
                        elif not hitButton.disabled:
                            self.aKey()
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
                bigOffset = 0
                smallOffset = 0
                if len(self.blackjack.player._cards) < 5:
                    for card in self.blackjack.player._cards:
                        newCard = self.display_card(card)
                        cardImage = self.loadCardImage(newCard)
                        screen.blit(cardImage, (0 + bigOffset, 265))
                        bigOffset += 100
                else:
                    for card in self.blackjack.player._cards[: len(self.blackjack.player._cards) - 3]:
                        newCard = self.display_card(card)
                        cardImage = self.loadCardImage(newCard)
                        screen.blit(cardImage, (0 + smallOffset, 265))
                        smallOffset += 25
                        bigOffset += 25
                    for card in self.blackjack.player._cards[len(self.blackjack.player._cards) - 3:]:
                        newCard = self.display_card(card)
                        cardImage = self.loadCardImage(newCard)
                        screen.blit(cardImage, (0 + bigOffset, 265))
                        bigOffset += 100

                screen.blit(hitsImage, (0, 150))
                screen.blit(standsImage, (0, 200))
                screen.blit(self.loadNumber(self.blackjack.hits), (500, 150))
                screen.blit(self.loadNumber(self.blackjack.stands), (500, 200))
                pygame.draw.rect(screen, (112, 145, 127), pygame.Rect(0, 400, 1000, 130))
                hitButton.draw(screen)
                standButton.draw(screen)
                screen.blit(dealerImage, (400, 0))
            pygame.display.update()
        pygame.quit()

    def aKey(self):
        self.blackjack.hit(self.player)
        deal_sound = random.randint(1, 3)
        deal_sound = pygame.mixer.Sound(f"21-Seconds-Game/sounds/sfx/deal_{deal_sound}.wav")
        deal_sound.play()

    def lKey(self):
        #self.blackjack.stand(self.player)
        stand_sound = pygame.mixer.Sound(f"21-Seconds-Game/sounds/sfx/stand_1.wav")
        stand_sound.play()

    def loadCardImage(self, card):
        suit = card.suit.name.lower() + "s"
        try:
            int(card.type.value)
            type = f"{int(card.type.value):02d}"
        except ValueError:
            type = card.type.value[0].upper()
        imagePath = f"21-Seconds-Game/assets/Cards/PNG/cards-large/card_{suit}_{type}.png"
        cardImage = pygame.image.load(imagePath).convert_alpha()
        cardImage = pygame.transform.scale(cardImage, (int(cardImage.get_width())*2, int(cardImage.get_height())*2))
        return cardImage

    def loadNumber(self, number):
        imagePath = f"21-Seconds-Game/assets/Numbers/{number}.png"
        numberImage = pygame.image.load(imagePath).convert_alpha()
        numberImage = pygame.transform.scale(numberImage, (int(numberImage.get_width())*5, int(numberImage.get_height())*5))
        return numberImage
