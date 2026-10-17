import pygame, random
from blackjack import Blackjack
from card import BaseCard, Suit, CardType
from effect import MultEffect, AddEffect
from display import Display

def shuffle(deck:list[BaseCard]) -> list[BaseCard]:
    for i in range(len(deck)-1,0,-1):
        j = random.randint(0,i)
        deck[i],deck[j]=deck[j],deck[i]
    return deck

def wildCard(wildDeck:list[int], wildCard:int, nextCard:BaseCard) -> None:
    if (wildCard % 2 == 0):
       return AddEffect(nextCard,wildDeck[wildCard])
    return MultEffect(nextCard,wildDeck[wildCard])

def createWildDeck() -> list[int]:
   return [5,2,15,4]

def shuffle(deck:list[BaseCard]) -> list[BaseCard]:
    for i in range(len(deck)-1,0,-1):
        j = random.randint(0,i)
        deck[i],deck[j]=deck[j],deck[i]
    return deck

if __name__ == "__main__":
    game = Blackjack()
    print(game.dealer, game.player)
    display = Display(game)
    display.start()