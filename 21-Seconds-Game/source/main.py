import pygame
from card import BaseCard, Suit, CardType

def start():
    (width, height) = (300, 200)
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

if __name__ == "__main__":
    pygame.init()
    start()
