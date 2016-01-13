from random import randint

# Die class
class Die():
    def __init__(self, color):
        self.color = color
        self.current_side = ''
        self.possible_sides = {
            'red': ['brain', 'feet', 'feet', 'shotgun', 'shotgun', 'shotgun'],
            'yellow': ['brain', 'brain', 'feet', 'feet', 'shotgun', 'shotgun'],
            'green': ['brain', 'brain', 'brain', 'feet', 'feet', 'shotgun']
        }
        self.sides = self.possible_sides[color]
    def roll(self):
        self.current_side = self.sides[randint(0,len(self.sides)) - 1]


# Player class
class Player():
    def __init__(self, name):
        self.name = name
        self.brains = 0


# Game class
class Game():
    def __init__(self):
        self.start_dice = ['red', 'red', 'red', 'yellow', 'yellow', 'yellow',\
        'yellow', 'green', 'green', 'green', 'green', 'green', 'green']
        self.dice_cup = []
        for color in self.start_dice:
                new_die = Die(color)
                self.dice_cup.append(new_die)
        self.dice_in_hand = []
        self.dice_on_table = []
        self.players = []
        # current_player will be a player object
        self.current_player = None
        self.winner = None
        # phantom_brains keeps track of brains on the table when brains are
        # put back in the cup for rerolling
        self.phantom_brains = 0
        self.last_round = False
    def new_game_setup(self):
        while True:
            try:
                num_players = int(input('How many people hunger for BRAAAIINS today (players)? '))
                # validation to make sure the above is in the right range
                if (num_players < 1) or (num_players > 6):
                    raise ValueError()
                else:
                    break
            except ValueError:
                print('Please enter a number between 1 and 6.')
        for players in range(0, num_players):
            new_player_name = input('What is your name, player ' + str(players + 1) + '? ')
            new_player = Player(new_player_name)
            self.players.append(new_player)




# Instantiate Them Classes

# Do stuff
redDie1 = Die('red')
print(redDie1.sides)
redDie1.roll()
print(redDie1.current_side)
newGame = Game()
print(newGame.dice_cup[0].color)
