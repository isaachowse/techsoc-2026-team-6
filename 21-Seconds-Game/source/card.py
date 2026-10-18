from abc import ABC, abstractmethod
from enum import StrEnum


class Suit(StrEnum):
    DIAMOND = "Diamonds"
    CLUB = "Clubs"
    HEART = "Hearts"
    SPADE = "Spades"


class CardType(StrEnum):
    TWO = "2"
    THREE = "3"
    FOUR = "4"
    FIVE = "5"
    SIX = "6"
    SEVEN = "7"
    EIGHT = "8"
    NINE = "9"
    TEN = "10"
    JACK = "Jack"
    QUEEN = "Queen"
    KING = "King"
    ACE = "Ace"

    @property
    def num_value(self) -> int:
        try:
            return int(self.value)
        except ValueError:
            return 11 if self == CardType.ACE else 10


class BaseCard(ABC):
    @property
    @abstractmethod
    def suit(self) -> Suit:
        """The suit of the card."""
        pass

    @property
    @abstractmethod
    def type(self) -> CardType:
        """The type of card."""
        pass

    @property
    @abstractmethod
    def score(self) -> int:
        """The value of the card."""
        pass


class Card(BaseCard):
    _suit: Suit
    _type: CardType

    def __init__(self, suit: Suit, type: CardType) -> None:
        self._suit = suit
        self._type = type

    @property
    def suit(self) -> Suit:
        return self._suit

    @property
    def type(self) -> CardType:
        return self._type

    @property
    def score(self) -> int:
        return self._type.num_value

    @property
    def name(self) -> str:
        return f"{self._type.name.title()} of {self._suit.value}"

    def __str__(self) -> str:
        return self.name
