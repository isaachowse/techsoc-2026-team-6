import pygame
from cards import Card

def start():
    (width, height) = (300, 200)
    screen = pygame.display.set_mode((width, height))
    pygame.display.flip()

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

def initialiseCards():
    cards = []
    for type in  ["Clubs", "Diamonds", "Hearts", "Spades"]:
        for i in range(1, 14):
            card = Card(type, i)
            cards.append(card)
    return cards

def main():
    pygame.init()
    start()
    cards = initialiseCards()
