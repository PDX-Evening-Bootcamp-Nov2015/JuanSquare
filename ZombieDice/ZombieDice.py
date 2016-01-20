from random import randint
from sys import exit
from blessings import Terminal
from time import sleep

t = Terminal()

# Die class
class Die():
    '''
    defines random outcome generator cube simulators for the game
    '''
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
        '''
        picks a random side from the possible sides
        '''
        self.current_side = self.sides[randint(0,len(self.sides)) - 1]


# Player class
class Player():
    '''
    A unique butterfly (person), used to store data for the course of a game
    '''
    def __init__(self, name):
        self.name = name
        self.brains = 0 # running score variable for the player
        self.win_cond = False # gets set to true when the player has > 13 brains
    def add_brains(self, num):
        '''
        adds brains from the table to player's score at turn end and checks
        if the player has 13 brains
        '''
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
            'lineBreak': t.bright_red_on_black('==========================================')
        }
        # fill the dice_cup with the appropriate mix of die objects
        for color in self.start_dice:
                new_die = Die(color)
                self.dice_cup.append(new_die)

    def new_game_setup(self):
        '''
        obtains and sets up the initial starting conditions for the game:
        number of players
        player names
        '''
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
        print('Lets get ready to ambllllllllle...')
        self.current_player = self.players[0]
        self.player_start_turn()

    def player_start_turn(self):
        '''
        starts out each player's turn,
        begins the dice rolling portion
        '''
        while True:
            try:
                self.print_line_delay(1,0.5)
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
        self.get_dice(3) # gets 3 dice out of the cup to start things off

    def cup_empty(self):
        '''
        takes all dice from the table and hand except for shotguns and puts Them
        back in the cup
        for use when cup is empty
        '''
        # get dice from hand
        temp_dice_hand = self.dice_in_hand[:]
        for dice in self.dice_in_hand:
            self.dice_cup.append(dice)
            temp_dice_hand.remove(dice)
        self.dice_in_hand = temp_dice_hand[:]
        # get dice from table
        temp_dice_table = self.dice_on_table[:]
        for dice in self.dice_on_table:
            if dice.current_side != 'shotgun':
                # ignore shotguns
                self.dice_cup.append(dice)
                temp_dice_table.remove(dice)
        self.dice_on_table = temp_dice_table[:]

    def get_dice(self, num):
        '''
        gets a number of dice out of the cup and puts them in the player hand
            - num must be an integer
        '''
        # check to make sure there are enough dice left in the cup
        if len(self.dice_cup) < num:
            self.cup_empty() # get some more dice if it is
        for i in range(num):
            # select a random die from dice_cup
            current_die = self.dice_cup[randint(1, len(self.dice_cup)) - 1]
            # put selected die into dice_in_hand
            self.dice_in_hand.append(current_die)
            # remove selected from dice_cup
            self.dice_cup.remove(current_die)
        print (self.image_map['lineBreak'], '\n' + str(len(self.dice_cup)), \
        'dice left in the cup.')
        self.roll_dice() # roll the dice you just got

    def roll_dice(self):
        '''
        calls the roll function for each die
        '''
        for die in self.dice_in_hand:
            # get a new random side for the die
            die.roll()
            # print the colored graphic for the die that was rolled
            print_string = self.current_player.name + ' rolled a ' + '{t.' + die.color + '}' + \
            self.image_map[die.current_side] + t.normal
            print(print_string.format(t=t))
            # move die from the hand to the table
            self.dice_on_table.append(die)
        # the hand should be empty now, good job
        self.dice_in_hand = []
        self.eval_dice() # check the results of that roll

    def player_choice(self):
        '''
        displays and validates an input for the player to decide if they want
        to roll again
        '''
        while True:
            # use while loop to keep asking if the player fails to give a
            # coherent answer
            try:
                self.print_line_delay(1,0.5) # give some visual space
                player_move = input('Would you like to roll again? Y/N ')
                if player_move.lower() == 'y':
                    return True
                elif player_move.lower() == 'n':
                    return False
                elif player_move.lower() == 'exit':
                    exit()
                else:
                    # validation
                    raise ValueError()
            except ValueError:
                print('Please enter Y/N')

    def count_dice(self):
        '''
        used in eval_dice step to get a count of each type of die rolled
        '''
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
        '''
        checks the value of all rolled dice and determines game state
        '''
        blasts, brains, feet = self.count_dice() # dice are counted here
        self.display_dice() # show the player their dice
        # are there 3 blasts?
        if blasts >= 3:
            # if so mandatory turn end
            print('You are dead...er.')
            self.end_turn(brains)
            return
        # create player_choice variable
        player_continue = self.player_choice()
        # check if the player wants to roll again
        if player_continue:
            # roll again
            self.get_dice(3 - feet)
        else:
            # player does not roll again
            self.end_turn(brains) # perform end turn evaluation

    def end_turn(self, brains):
        '''
        performs end of turn bookeeping, checks for endgame conditions
        '''
        # take temporary brains and make them PERMANENT
        self.current_player.add_brains(brains)
        self.print_line_delay(1,0.5)
        # show the player their shiny new brains
        print(self.image_map['lineBreak'], '\nYou have:', \
        self.current_player.brains, 'brain(s)', self.current_player.name + \
        '. Nom nom nom...')
        # check if the player has 13 brains
        if self.current_player.win_cond:
            self.last_round = True
        # check if it is currently the last round
        if self.last_round:
            if self.players.index(self.current_player) == len(self.players) - 1:
                self.final_score() # tally everything up
                return
        # put all dice from hand back in cup
        temp_dice_hand = self.dice_in_hand[:]
        for dice in self.dice_in_hand:
            self.dice_cup.append(dice)
            temp_dice_hand.remove(dice)
        self.dice_in_hand = temp_dice_hand[:]
        # put all dice from table back in cup
        temp_dice_table = self.dice_on_table[:]
        for dice in self.dice_on_table:
            self.dice_cup.append(dice)
            temp_dice_table.remove(dice)
        self.dice_on_table = temp_dice_table[:]
        self.print_line_delay(6, 0.125)
        self.next_player() # move on to the next player's turn

    def next_player(self):
        '''
        changes to the next player in the index or first player if at the end
        and starts that player's turn
        '''
        # find the index of the next player
        if self.players.index(self.current_player) == len(self.players) - 1:
            next_index = 0
        else:
            next_index = self.players.index(self.current_player) + 1
        # change players
        self.current_player = self.players[next_index]
        self.player_start_turn()

    def display_dice(self):
        '''
        Shows the current scores and dice on table.
        '''
        # initialize empty space for table dice
        display = ''
        for i in self.dice_on_table:
            # add each die graphic to the display variable
            display += '{t.' + i.color + '}' # selects proper die color
            display += self.image_map[i.current_side] # shows rolled side
        print(self.image_map['lineBreak'])
        for player in self.players:
            # show score for each player
            score = player.brains
            name = player.name
            print(name, 'has eaten', score, 'brains.')
        print(self.image_map['lineBreak'])
        print('Dice on la mesa: \n' + display.format(t=t), t.normal + '\n')

    def final_score(self):
        '''
        tallies final scores after end game conditions have been met and
        determines if a tie breaker round is needed
        '''
        winner = ""
        tie_winners = []
        highest = 0
        self.print_line_delay(6,0.125)
        # tell them the end has come
        print('Game Over', '\n' + self.image_map['lineBreak'])
        # figure out which player has the highest scored
        for player in self.players:
            sleep(0.5)
            # as long as we're looking at it, we might as well show the player
            # their score
            print (player.name, 'scored:', player.brains, 'brain(s).')
            if player.brains > highest:
                highest = player.brains
                winner = player
        # check for a tie
        for player in self.players:
            if player.brains == highest:
                tie_winners.append(player)
        if len(tie_winners) > 1:
            self.tie_round(tie_winners) # call a tie round if you find a tie
        else:
            sleep(0.5)
            # congratulate the winner if they didn't tie, good job, winner!
            print(self.image_map['lineBreak'] + '\nYou win, ' + winner.name +\
            '!!!\n' + self.image_map['lineBreak'])

    def tie_round(self, winners):
        '''
        initiates a tie round with only the tied players
        '''
        print("\nIt's a tie between:")
        # tell the players who is tied
        for player in winners:
            sleep(0.5)
            print(player.name)
        print()
        print("\nBeginning tie-breaker round... (braaaaiiins...)")
        # make sure only the winners are playing, boo losers, boooooo
        self.players = winners
        # go back to the first player (who won)
        self.current_player = self.players[0]
        self.player_start_turn() # aaaaaand GO!

    def print_line_delay(self, lines, delay):
        '''
        Prints breaking spaces with a delay
        '''
        i = 1
        while i <= lines:
            i += 1
            sleep(delay)
            print('')









# Instantiate Them Classes
new_game = Game()
new_game.new_game_setup()
