from random import shuffle

class Card():
    def __init__(self, suit, value):
        self.suit = suit
        self.value = value
        self.showing = True
        if self.suit in ['diamonds', 'hearts']:
            self.color = 'red'
        elif self.suit in ['spades', 'clubs']:
            self.color = 'black'
        else:
            raise ValueError('Invalid Suit')

class Deck():
    default_deck = ["two", "three", "four", "five", "six", "seven", "eight", "nine", "ten", "jack", "queen", "king", "ace"]
    default_suit = ["hearts", "clubs", "spades", "diamonds"]

    def __init__(self,num_decks):
        self.num_decks = num_decks
        self.cards = []

    def create_deck(self):
        for suit in self.default_suit:
            for value in self.default_deck:
                for decks in range(self.num_decks):
                    new_card = Card(suit, value)
                    self.cards.append(new_card)

    def shuffle(self):
        shuffle(self.cards)

class Player():
    def __init__(self, name):
        self.name = name
        self.current_hand = []
        self.current_hand_value = 0
        self.hands_won = 0
        self.dealer = False
        self.busted =  False
