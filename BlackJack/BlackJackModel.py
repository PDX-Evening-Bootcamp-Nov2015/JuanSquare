

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
