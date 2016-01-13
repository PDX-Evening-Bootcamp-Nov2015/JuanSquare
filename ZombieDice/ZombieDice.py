from random import random.randint

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
        self.current_side = self.sides[random.randint(0,len(self.sides)) - 1]


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
    def get_dice(self, num):
        for die in range(0, num):
            # select a random die from dice_cup
            current_die = self.dice_cup[random.randint(1, len(self.dice_cup)) - 1]
            # put selected die into dice_in_hand
            self.dice_in_hand.append(current_die)
            # remove selected from dice_cup
            self.dice_cup.remove(current_die)
    def roll_dice(self):
        for die in self.dice_in_hand:
            die.roll()
            self.dice_on_table.append(die)
            self.dice_in_hand.remove(die)
    def player_choice(self):
        while True:
            try:
                player_move = input('Would you like to roll again? Y/N ')
                if player_move.lower() == 'y':
                    return True
                elif player_move.lower() == 'n':
                    return False
                else:
                    raise ValueError()
            except:
                print('Please enter Y/N')
    def eval_dice(self):
        blasts = 0
        brains = 0
        feet = 0
        # how many feet, brains, and blasts?
        for i in self.dice_on_table:
            current = self.dice_on_table[i]
            if current.current_side == 'shotgun':
                blasts += 1
            elif current.current_side == 'brain':
                brains += 1
            else:
                feet += 1
                # move feet back to dice_in_hand
                self.dice_in_hand.append(self.dice_on_table[i])
                self.dice_on_table.remove(current)
        # are there 3 blasts?
        if blasts == 3:
            print('You are dead...er.')
            # call next_player
        # call display_dice
        # create player_choice variable
        player_continue = player_choice()
        print(dice_on_table)



# Instantiate Them Classes

# Do stuff
redDie1 = Die('red')
print(redDie1.sides)
redDie1.roll()
print(redDie1.current_side)
newGame = Game()
print(newGame.dice_cup[0].color)
