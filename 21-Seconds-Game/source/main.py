from blackjack import Blackjack
from display import Display

if __name__ == "__main__":
    game = Blackjack()
    display = Display(game)
    display.start()
