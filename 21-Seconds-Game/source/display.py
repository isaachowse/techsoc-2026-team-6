import pygame
from pygame import QUIT, KEYDOWN, K_a, K_l
from button import Button
from blackjack import Blackjack
import card
from animations import move_card, flip_card, button_animation, score_flash_animation, result_animation
import random, time

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
        gameOver = False
        revealed = False

        playImage = pygame.image.load("21-Seconds-Game/assets/Buttons/play-button.png").convert_alpha()
        exitImage = pygame.image.load("21-Seconds-Game/assets/Buttons/exit-button.png").convert_alpha()
        hitImage = pygame.image.load("21-Seconds-Game/assets/Buttons/hit-button.png").convert_alpha()
        standImage = pygame.image.load("21-Seconds-Game/assets/Buttons/stand-button.png").convert_alpha()
        revealImage = pygame.image.load("21-Seconds-Game/assets/Buttons/reveal-button.png").convert_alpha()

        playButton = Button(150, 388, playImage, 6)
        exitButton = Button(550, 388, exitImage, 6)
        hitButton = Button(150, 388, hitImage, 6)
        standButton = Button(550, 388, standImage, 6)
        revealButton = Button(200, 388, revealImage, 6)

        dealerImage = pygame.image.load("21-Seconds-Game/assets/Dealer.png").convert_alpha()
        dealerImage = pygame.transform.scale(dealerImage, (int(dealerImage.get_width())*0.3, int(dealerImage.get_height())*0.3))

        team6 = pygame.image.load("21-Seconds-Game/assets/Team6.png").convert_alpha()
        team6 = pygame.transform.scale(team6, (int(team6.get_width())*10, int(team6.get_height())*10))

        hitsImage = pygame.image.load("21-Seconds-Game/assets/HitsRemaining.png").convert_alpha()
        hitsImage = pygame.transform.scale(hitsImage, (int(hitsImage.get_width())*5, int(hitsImage.get_height())*5))
        standsImage = pygame.image.load("21-Seconds-Game/assets/StandsRemaining.png").convert_alpha()
        standsImage = pygame.transform.scale(standsImage, (int(standsImage.get_width())*5, int(standsImage.get_height())*5))

        pygame.display.flip()

        running = True
        while running:
            hitButton.set_disabled(self.player.value >= self.blackjack.bust_value)

            for event in pygame.event.get():
                if event.type == KEYDOWN:
                    if event.key == K_a:
                        if homeScreen and not playButton.disabled:
                            pygame.mixer.music.load("21-Seconds-Game/sounds/sfx/press_1.wav")
                            pygame.mixer.music.play()
                            homeScreen = False
                        elif not hitButton.disabled and not gameOver:
                            self.aKey(screen)
                        elif gameOver and not revealed:
                            revealed = True
                        elif revealed:
                            self.blackjack = Blackjack()
                            self.player = self.blackjack.player
                            self.dealer = self.blackjack.dealer
                            gameOver = False
                            revealed = False
                    elif event.key == K_l:
                        if (homeScreen and not exitButton.disabled) or revealed:
                          running = False
                        elif not standButton.disabled:
                          self.lKey(screen)
                          gameOver = True
                if event.type == QUIT:
                    running = False

            screen.fill(backgroundColour)

            if homeScreen:
                screen.blit(team6, (250, 100))
                playButton.draw(screen)
                exitButton.draw(screen)
            else:
                pygame.draw.rect(screen, (112, 145, 127), pygame.Rect(0, 400, 1000, 130))
                screen.blit(dealerImage, (400, 0))
                if not gameOver:
                    hitButton.draw(screen)
                    standButton.draw(screen)
                elif not revealed:
                    revealButton.draw(screen)
                else:
                    playButton.draw(screen)
                    exitButton.draw(screen)

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

                if not revealed:
                    self.dealerCards(screen, self.blackjack.dealer._cards)
                else:
                    self.flipDealersCards(screen, self.blackjack.dealer._cards)
                    self.calculateWinner(screen, int(self.blackjack.player.value), int(self.blackjack.dealer.value))
                self.displayScore(screen, int(self.blackjack.player.value), 750, 330)
            pygame.display.update()
        pygame.quit()

    def aKey(self, screen):
        self.blackjack.hit(self.player)
        deal_sound = random.randint(1, 3)
        pygame.mixer.music.load(f"21-Seconds-Game/sounds/sfx/deal_{deal_sound}.wav")
        pygame.mixer.music.play()

    def lKey(self, screen):
        self.blackjack.stand()
        pygame.mixer.music.load(f"21-Seconds-Game/sounds/sfx/stand_1.wav")
        pygame.mixer.music.play()
        self.dealerThinks(screen)
        while self.blackjack.dealer.value < 17:
            self.blackjack.hit(self.dealer)
            deal_sound = random.randint(1, 3)
            pygame.mixer.music.load(f"21-Seconds-Game/sounds/sfx/deal_{deal_sound}.wav")
            pygame.mixer.music.play()
            self.dealerCards(screen, self.blackjack.dealer._cards)
            self.dealerThinks(screen)


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

    def loadThought(self, stage):
        imagePath = f"21-Seconds-Game/assets/Thoughts/thought{stage}.png"
        thoughtImage = pygame.image.load(imagePath).convert_alpha()
        return thoughtImage

    def dealerThinks(self, screen):
        original = screen.copy()
        for i in range(6):
            thoughtImage = self.loadThought((i%3)+1)
            screen.blit(thoughtImage, (475, -20))
            pygame.display.update()
            time.sleep(0.3)
        screen.blit(original, (0, 0))
        pygame.display.update()

    def dealerCards(self, screen, cards):
        dealerOffset = 0
        for card in cards:
            imagePath = f"21-Seconds-Game/assets/Cards/PNG/cards-large/card_back.png"
            cardImage = pygame.image.load(imagePath).convert_alpha()
            cardImage = pygame.transform.scale(cardImage, (int(cardImage.get_width()), int(cardImage.get_height())))
            screen.blit(cardImage, (500 + dealerOffset, 100))
            dealerOffset += 25

    def displayScore(self, screen, score, x, y):
        scoreImage = pygame.image.load("21-Seconds-Game/assets/Score.png").convert_alpha()
        scoreImage = pygame.transform.scale(scoreImage, (int(scoreImage.get_width())*5, int(scoreImage.get_height())*5))
        screen.blit(scoreImage, (x, y))

        scoreTen = score // 10
        scoreOne = score % 10
        if scoreTen > 0:
            screen.blit(self.loadNumber(scoreTen), (x+150, y))
            screen.blit(self.loadNumber(scoreOne), (x+175, y))
        else:
            screen.blit(self.loadNumber(score), (x+150, y))

    def flipDealersCards(self, screen, cards):
        dealerOffset = 0
        for card in cards:
            newCard = self.display_card(card)
            cardImage = self.loadCardImage(newCard)
            cardImage = pygame.transform.scale(cardImage, (int(cardImage.get_width()*0.5), int(cardImage.get_height())*0.5))
            screen.blit(cardImage, (500 + dealerOffset, 100))
            dealerOffset += 25
        self.displayScore(screen, self.blackjack.dealer.value, 750, 100)

    def calculateWinner(self, screen, playerScore, dealerScore):
        win = pygame.image.load("21-Seconds-Game/assets/Win.png").convert_alpha()
        win = pygame.transform.scale(win, (int(win.get_width())*7, int(win.get_height())*7))
        lose = pygame.image.load("21-Seconds-Game/assets/Lose.png").convert_alpha()
        lose = pygame.transform.scale(lose, (int(lose.get_width())*7, int(lose.get_height())*7))
        draw = pygame.image.load("21-Seconds-Game/assets/Draw.png").convert_alpha()
        draw = pygame.transform.scale(draw, (int(draw.get_width())*7, int(draw.get_height())*7))
        if playerScore <= 21 and (playerScore > dealerScore or dealerScore > 21):
            screen.blit(win, (0, 0))
        elif playerScore > 21 or dealerScore > playerScore:
            screen.blit(lose, (0, 0))
        else:
            screen.blit(draw, (0, 0))
