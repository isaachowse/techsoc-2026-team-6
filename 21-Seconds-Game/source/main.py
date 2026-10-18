import pygame, random
from blackjack import Blackjack
from card import BaseCard, Suit, CardType
from effect import MultEffect, AddEffect
from display import Display

if __name__ == "__main__":
    game = Blackjack()
    print(list(map(str, game._deck)), game.bust_value)
    display = Display(game)
    display.start()
