import pygame
from card import BaseCard, Suit, CardType
from effect import EffectDec, BaseValueEffect, MultEffect, AddEffect

def start():
    pygame.init()
    (width, height) = (1000, 500)
    screen = pygame.display.set_mode((width, height))
    pygame.display.flip()

    deck = createDeck()
    wildDeck = createWildDeck()
    print(deck[0].getScore())
    wildCard(wildDeck,0,deck[0])
    print(deck[0].getScore())

    print(deck[1].getScore())
    wildCard(wildDeck,1,deck[1])
    print(deck[1].getScore())
    
    print(list(str(card) for card in deck))

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

if __name__ == "__main__":
    pygame.init()
    start()
