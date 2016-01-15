from random import random.randint

# Die class
class Die():
    def __init__(self, color):
        # color variable used to select die sides
        self.color = color
        # variable below for use in roll function and game evaluation
        self.current_side = ''
        self.possible_sides = {
            'red': ['brain', 'feet', 'feet', 'shotgun', 'shotgun', 'shotgun'],
            'yellow': ['brain', 'brain', 'feet', 'feet', 'shotgun', 'shotgun'],
            'green': ['brain', 'brain', 'brain', 'feet', 'feet', 'shotgun']
        }
        # set possible sides based on what is appropriate for this color
        self.sides = self.possible_sides[color]
    def roll(self):
        # pick a random side from the possible sides
        self.current_side = self.sides[random.randint(0,len(self.sides)) - 1]


# Player class
class Player():
    # A unique butterfly (person), used to store data for the course of a game
    def __init__(self, name):
        self.name = name
        # brains is the running score variable for the player
        self.brains = 0
        self.win_cond = False
    def add_brains(self, num):
        self.brains += num
        if self.brains >= 13:
            self.win_cond = True
        else:
            self.win_cond = False



# Game class
class Game():
    def __init__(self):
        # define the initial set of dice the game uses
        self.start_dice = ['red', 'red', 'red', 'yellow', 'yellow', 'yellow',\
        'yellow', 'green', 'green', 'green', 'green', 'green', 'green']
        # dice_cup, dice_in_hand, dice_on_table are staging areas for die objects
        self.dice_cup = []
        self.dice_in_hand = []
        self.dice_on_table = []
        # list of player objects
        self.players = []
        # current_player and winner will be player objects
        self.current_player = None
        self.winner = None
        # phantom_brains keeps track of brains on the table when brains are
        # put back in the cup for rerolling
        self.phantom_brains = 0
        # game-progression functions look for last_round to decide on continuing
        self.last_round = False
        # fill the dice_cup with the appropriate mix of die objects
        for color in self.start_dice:
                new_die = Die(color)
                self.dice_cup.append(new_die)
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
            # ask for a name for each player
            new_player_name = input('What is your name, player ' + str(players + 1) + '? ')
            new_player = Player(new_player_name)
            # add that player to our players list
            self.players.append(new_player)
    def get_dice(self, num):
        # check to make sure there are enough dice left in the cup
        if len(self.dice_cup) < num:
            # call cup_empty
        for die in range(0, num):
            # select a random die from dice_cup
            current_die = self.dice_cup[random.randint(1, len(self.dice_cup)) - 1]
            # put selected die into dice_in_hand
            self.dice_in_hand.append(current_die)
            # remove selected from dice_cup
            self.dice_cup.remove(current_die)
        self.roll_dice()
    def roll_dice(self):
        for die in self.dice_in_hand:
            # get a new random side for each die in hand
            die.roll()
            # move all dice from the hand to the table
            self.dice_on_table.append(die)
            self.dice_in_hand.remove(die)
        self.eval_dice()
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
    def count_dice(self):
        # temp vars to hold current dice values
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
        return blasts, brains, feet
    def eval_dice(self):
        blasts, brains, feet = count_dice()
        # are there 3 blasts?
        if blasts == 3:
            print('You are dead...er.')
            self.end_turn()
        # call display_dice
        # create player_choice variable
        player_continue = self.player_choice()
        if player_continue:
            # roll again
            self.get_dice(3-feet)
        else:
            current_player.add_brains(brains)
            print('You have: ' + current_player.brains)
            # check if the player has 13 brains
            if current_player.win_cond:
                self.last_round = True
            self.end_turn()
    def end_turn(self):
        if self.last_round:
            if index(current_player) == len(self.players) - 1:
                print('Game Over')
                winner = ""
                highest = 0
                for player in self.players:
                    if player.brains > highest:
                        highest = player.brains
                        winner = player
                print('You win, ' + winner.name)
                return
        for dice in dice_in_hand:
            self.dice_cup.append(dice)
            self.dice_in_hand.remove(dice)
        for dice in dice_on_table:
            self.dice_cup.append(dice)
            self.dice_on_table.remove(dice)
        self.next_player()
    def next_player(self):
        # change current player
        if index(current_player) == len(self.players) - 1:
            next_index = 0
        else:
            next_index = index(current_player) + 1
        self.current_player = self.players[next_index]
        self.get_dice(3)
    def display_dice(self):
        image_map = {
            'brain': '[ B ]',
            'feet': '[ F ]',
            'shotgun': '[ S ]'
        }
        display = ''
        for i in dice_on_table:
            display += image_map[i.current_side]
        print('Dice on la mesa: \n' + display)






# Instantiate Them Classes

# Do stuff
redDie1 = Die('red')
print(redDie1.sides)
redDie1.roll()
print(redDie1.current_side)
newGame = Game()
print(newGame.dice_cup[0].color)
