"""
This is an implementation of a simulator of the War card game
"""
import random
import time
import os
from deck import Card, Deck

class Game():


    def __init__(self):
        self.deck = None
        self.deck_player1 = None
        self.deck_player2 = None
        self.winner_pile = []


    def display_board(self, card1, card2, winner):
        """Print the board with current marks"""
        os.system('clear')
        board = """
            Player      | 1             |  2
            --------------------------------
            deck size   | {}            | {}
            --------------------------------
            top card    | {}   | {}
            ---------------------------------
            {} takes cards
            """.format(self.deck_player1.get_deck_size(),\
              self.deck_player2.get_deck_size(), card1, card2, winner)
        print(board)
        time.sleep(2)

    def generate_deck_cards(self):
        cards = [0]*52

        for type in ["hearts", "diamonds", "spades", "clubs"]:
            for value in ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'A', 'J', 'Q', 'K']:
                while True:
                    pos = random.randint(0, 51)
                    if cards[pos] == 0:
                        cards[pos] = Card(value, type)
                        break
        return Deck(cards)

    def compare_and_take(self, card1, card2):

        self.winner_pile.append(card1)
        self.winner_pile.append(card2)
        winner = ""

        if card1.compare(card2) == 0:
            return False
        elif card1.compare(card2) > 0:
            winner = "Player1"
            self.deck_player1.add_card(self.winner_pile)
        else:
            winner = "Player2"
            self.deck_player2.add_card(self.winner_pile)

        self.display_board(card1, card2, winner)
        return True

    def start_war(self):
        print("Starting War!")
        while True:
            for i in [1, 2, 3]:
                try:
                    print("Player1 takes from deck")
                    self.winner_pile.append(self.deck_player1.pop_card())
                    print("Player2 takes from deck")
                    self.winner_pile.append(self.deck_player2.pop_card())
                except IndexError:
                    break
            try:
                card1 = self.deck_player1.pop_card()
                card2 = self.deck_player1.pop_card()
            except IndexError:
                break

            if self.compare_and_take(card1, card2):
                break

    def play(self):
        self.deck = self.generate_deck_cards()
        self.deck_player1, self.deck_player2 = self.deck.divide_deck()

        while self.deck_player1.get_deck_size() != 0 and \
              self.deck_player2.get_deck_size() != 0:

            self.winner_pile.clear()
            try:
                card_p1 = self.deck_player1.pop_card()
                card_p2 = self.deck_player2.pop_card()
            except IndexError:
                break

            if not self.compare_and_take(card_p1, card_p2):
                self.start_war()

        if self.deck_player1.get_deck_size() == 0:
            print("Player 2 won!")
        else:
            print("Player 1 won!")

if __name__ == "__main__":
    game = Game()
    game.play()