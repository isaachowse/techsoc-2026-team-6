from card import Card, CardType, Suit
import random


class Hand:
    _cards: list[Card]

    def __init__(self) -> None:
        self._cards = []

    def add(self, card: Card) -> None:
        """Add a card to the hand."""
        self._cards.append(card)

    def empty(self) -> list[Card]:
        """Empty the hand, returning all cards within it."""
        copy = self._cards.copy()
        self._cards.clear()
        return copy

    @property
    def score(self) -> int:
        """Score the hand."""
        total = sum(card.score for card in self._cards)
        aces = sum(1 for card in self._cards if card.type == CardType.ACE)

        while total > 21 and aces > 0:
            total -= CardType.ACE.num_value
            aces -= 1

        return total

    def __str__(self) -> str:
        return f"{list(map(str, self._cards))} ({self.score})"


class Blackjack:
    _dealer: Hand
    """The dealer's hand."""

    _player: Hand
    """The player's hand."""

    _deck: list[Card]
    """The deck of cards."""

    def __init__(self) -> None:
        self._dealer = Hand()
        self._player = Hand()
        self._deck = [Card(suit, type) for type in CardType for suit in Suit]
        self.reset()

    def reset(self) -> None:
        """Reset the game."""
        # take back cards from hands
        for hand in (self.player, self.dealer):
            self._deck.extend(hand.empty())

        # shuffle the deck
        random.shuffle(self._deck)

        # deal new cards
        for hand in (self.player, self.dealer):
            self.hit(hand)
            self.hit(hand)

    def hit(self, hand: Hand) -> None:
        """Give a hand a card"""
        card = self._deck.pop()
        hand.add(card)

    @property
    def player(self) -> Hand:
        return self._player

    @property
    def dealer(self) -> Hand:
        return self._dealer
