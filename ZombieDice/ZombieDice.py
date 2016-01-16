from random import randint
from sys import exit
from blessings import Terminal

t = Terminal()

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
        self.current_side = self.sides[randint(0,len(self.sides)) - 1]


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
        self.image_map = {
            'brain': '[ B ]',
            'feet': '[ F ]',
            'shotgun': '[ S ]',
            'lineBreak': t.black_on_bright_red('==========================================')
        }
        # fill the dice_cup with the appropriate mix of die objects
        for color in self.start_dice:
                new_die = Die(color)
                self.dice_cup.append(new_die)

    def new_game_setup(self):
        while True:
            try:
                num_players = input('How many people hunger for BRAAAIINS today (players)? ')
                # validation to make sure the above is in the right range
                if num_players.lower() == 'exit':
                    exit()
                num_players = int(num_players)
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
        print('Lets get ready to ambllllllllle...\n')
        self.current_player = self.players[0]
        self.player_start_turn()

    def player_start_turn(self):
        while True:
            try:
                player_ready = input(self.current_player.name + \
                ", it's your turn, enter 'Y' to roll: ")
                if player_ready.lower() == 'exit':
                    exit()
                if player_ready.lower() != 'y':
                    raise ValueError()
                else:
                    break
            except ValueError:
                print("Please enter the letter 'Y' when you are ready.")
        self.get_dice(3)

    def cup_empty(self):
        temp_dice_hand = self.dice_in_hand[:]
        for dice in self.dice_in_hand:
            self.dice_cup.append(dice)
            temp_dice_hand.remove(dice)
        self.dice_in_hand = temp_dice_hand[:]
        temp_dice_table = self.dice_on_table[:]
        for dice in self.dice_on_table:
            if dice.current_side != 'shotgun':
                self.dice_cup.append(dice)
                temp_dice_table.remove(dice)
        self.dice_on_table = temp_dice_table[:]

    def get_dice(self, num):
        # check to make sure there are enough dice left in the cup
        if len(self.dice_cup) < num:
            self.cup_empty()
        for i in range(num):
            # select a random die from dice_cup
            current_die = self.dice_cup[randint(1, len(self.dice_cup)) - 1]
            # put selected die into dice_in_hand
            self.dice_in_hand.append(current_die)
            # remove selected from dice_cup
            self.dice_cup.remove(current_die)
        print (self.image_map['lineBreak'], '\n' + str(len(self.dice_cup)), \
        'dice left in the cup.')
        self.roll_dice()

    def roll_dice(self):
        for die in self.dice_in_hand:
            # get a new random side for each die in hand
            die.roll()
            print_string = self.current_player.name + ' rolled a ' + '{t.' + die.color + '}' + \
            self.image_map[die.current_side] + t.normal
            print(print_string.format(t=t))
            # move all dice from the hand to the table
            self.dice_on_table.append(die)
        self.dice_in_hand = []
        self.eval_dice()

    def player_choice(self):
        while True:
            try:
                player_move = input('Would you like to roll again? Y/N ')
                if player_move.lower() == 'y':
                    return True
                elif player_move.lower() == 'n':
                    return False
                elif player_move.lower() == 'exit':
                    exit()
                else:
                    raise ValueError()
            except ValueError:
                print('Please enter Y/N')

    def count_dice(self):
        # temp vars to hold current dice values
        blasts = 0
        brains = 0
        feet = 0
        # how many feet, brains, and blasts?
        temp_dice_table = self.dice_on_table[:] # prevents errors from altering inside loop
        for current in self.dice_on_table:
            if current.current_side == 'shotgun':
                blasts += 1
            elif current.current_side == 'brain':
                brains += 1
            else:
                feet += 1
                # move feet back to dice_in_hand
                self.dice_in_hand.append(current)
                temp_dice_table.remove(current)
        self.dice_on_table = temp_dice_table[:]
        return blasts, brains, feet

    def eval_dice(self):
        blasts, brains, feet = self.count_dice()
        # are there 3 blasts?
        if blasts >= 3:
            print('\nYou are dead...er.')
            self.end_turn()
            return
        self.display_dice()
        # create player_choice variable
        player_continue = self.player_choice()
        if player_continue:
            # roll again
            self.get_dice(3-feet)
        else:
            self.current_player.add_brains(brains)
            print(self.image_map['lineBreak'], '\nYou have:', \
            self.current_player.brains, 'brain(s)', self.current_player.name + \
            '. Nom nom nom...')
            # check if the player has 13 brains
            if self.current_player.win_cond:
                self.last_round = True
            self.end_turn()

    def end_turn(self):
        if self.last_round:
            if self.players.index(self.current_player) == len(self.players) - 1:
                self.final_score()
                return
        temp_dice_hand = self.dice_in_hand[:]
        for dice in self.dice_in_hand:
            self.dice_cup.append(dice)
            temp_dice_hand.remove(dice)
        temp_dice_table = self.dice_on_table[:]
        self.dice_in_hand = temp_dice_hand[:]
        for dice in self.dice_on_table:
            self.dice_cup.append(dice)
            temp_dice_table.remove(dice)
        self.dice_on_table = temp_dice_table[:]
        print('\n\n\n\n\n\n')
        self.next_player()

    def next_player(self):
        # change current player
        if self.players.index(self.current_player) == len(self.players) - 1:
            next_index = 0
        else:
            next_index = self.players.index(self.current_player) + 1
        self.current_player = self.players[next_index]
        self.player_start_turn()

    def display_dice(self):
        display = ''
        for i in self.dice_on_table:
            display += '{t.' + i.color + '}'
            display += self.image_map[i.current_side]
        print(self.image_map['lineBreak'])
        for player in self.players:
            score = player.brains
            name = player.name
            print(name, 'has eaten', score, 'brains.')
        print(self.image_map['lineBreak'])
        print('Dice on la mesa: \n' + display.format(t=t), t.normal + '\n')

    def final_score(self):
        print('\n\n\n\n\n\nGame Over', '\n' + self.image_map['lineBreak'])
        winner = ""
        tie_winners = []
        highest = 0
        for player in self.players:
            print (player.name, 'scored:', player.brains, 'brains.')
            if player.brains > highest:
                highest = player.brains
                winner = player
        for player in self.players:
            if player.brains == highest:
                tie_winners.append(player)
        if len(tie_winners) > 1:
            self.tie_round(tie_winners)
        else:
            print(self.image_map['lineBreak'] + '\nYou win, ' + winner.name +'!!!\n' \
            + self.image_map['lineBreak'])

    def tie_round(self, winners):
        print("\nIt's a tie between:")
        for player in winners:
            print(player.name)
        print("\nBeginning tie-breaker round... (braaaaiiins...)")
        self.players = winners
        self.current_player = self.players[0]
        self.player_start_turn()









# Instantiate Them Classes
new_game = Game()
new_game.new_game_setup()


# Testing
# new_game.players = [Player('Bill'), Player('Mittens'), Player('Doug')]
# new_game.players[0].brains = 14
# new_game.players[1].brains = 14
# new_game.players[2].brains = 14
# new_game.final_score()
# redDie1 = Die('red')
# print(redDie1.sides)
# redDie1.roll()
# print(redDie1.current_side)
# newGame = Game()
# print(newGame.dice_cup[0].color)
