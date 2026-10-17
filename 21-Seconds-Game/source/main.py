import pygame
from card import BaseCard, Suit, CardType
from effect import MultEffect, AddEffect

#to add effect, deck[card iterator] = wildCard(wildDeck,wildDeck iterator, deck[card iterator])

def start():
    pygame.init()
    (width, height) = (1000, 500)
    screen = pygame.display.set_mode((width, height))
    pygame.display.flip()
    deck = createDeck()
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
       return AddEffect(nextCard,wildDeck[wildCard])
    return MultEffect(nextCard,wildDeck[wildCard])

def createWildDeck() -> list[int]:
   return [5,2,15,4]

if __name__ == "__main__":
    pygame.init()
    start()
