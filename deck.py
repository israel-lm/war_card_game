"""
Implementation of a card deck for the War card game simulator
"""
class Card():
    """ A card is represented by a tuple (value, type) """
    #Make comparison easier
    value_map ={'2': 0, '3': 1, '4': 2, '5': 3, '6': 4, '7': 5,
                '8': 6, '9': 7, '10': 8, 'J': 9, 'Q': 10, 'K': 11, 'A': 12}

    def __init__(self, value, type):
        self.card = (value, type)

    def __repr__(self):
        return f"({self.get_value()}, {self.get_type()})"

    def get_value(self):
        return self.card[0]

    def get_type(self):
        return self.card[1]

    def compare(self, card):
        """
        Compare two cards

        Parameters
        ----------
        card: card to be compared with

        Return
        ------
        0 if cards are equal
        1 if method owner card has higher value
        -1 if method owner card is lower value

        """
        if Card.value_map[self.get_value()] == Card.value_map[card.get_value()]:
            return 0
        elif Card.value_map[self.get_value()] > Card.value_map[card.get_value()]:
            return 1
        else:
            return -1


class Deck():
    """Class representing the card deck"""

    def __init__(self, cards):
        """
        Parameters
        ----------
        cards: list of objects of type Card
        """
        self.cards = cards

    def divide_deck(self):
        return (Deck(self.cards[:27]), Deck(self.cards[27:]))

    def get_cards(self):
        return self.cards

    def add_card(self, cards):
        self.cards.extend(cards)

    def pop_card(self):
        return self.cards.pop(0)

    def get_deck_size(self):
        return len(self.cards)
