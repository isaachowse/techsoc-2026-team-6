import pygame
from card import BaseCard, Suit, CardType
from effect import EffectDec, BaseValueEffect, MultEffect, AddEffect

def start():
    (width, height) = (300, 200)
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

def createDeck() -> list[BaseCard]:
  deck = []

  for suit in Suit:
    for type in CardType:
      deck.append(BaseCard(suit, type))

  return deck

def wildCard(wildDeck:list[int], wildCard:int, nextCard:BaseCard) -> None:
    if (wildCard % 2 == 0):
       nextCard = AddEffect(nextCard,wildDeck[wildCard]).applyEffect()
    else:
       nextCard = MultEffect(nextCard,wildDeck[wildCard]).applyEffect()

def createWildDeck() -> list[int]:
   return [5,2,15,4]

if __name__ == "__main__":
    pygame.init()
    start()
