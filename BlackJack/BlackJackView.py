class View():
    IMAGE_MAP = {
        'diamonds': "\u2662",
        'spades': "\u2664",
        'clubs': "\u2667",
        'hearts': "\u2661",
        'two': 2,
        'three': 3,
        'four': 4,
        'five': 5,
        'six': 6,
        'seven': 7,
        'eight': 8,
        'nine': 9,
        'ten': 10,
        'jack': 'Jack',
        'queen': 'Queen',
        'king': 'King',
        'ace': 'Ace',
        'linebreak': ('=========================================='),
        'turnchange': "{} it is now your turn!",
        'gameover': "The game is over, {} you are a winner!",
        'gameover_dealer': "The game is over, the dealer won!",
        'playerscore': "{}, your score is now {}",
        'noshowcard': "XX"
    }

    def __init__(self):
        pass

    def show_table(self, player_object_list):
        print (self.IMAGE_MAP['linebreak'])
        for player in player_object_list:
            print (player.name)
            for card in player.current_hand:
                if card.showing == True:
                    print (self.IMAGE_MAP[card.value], self.IMAGE_MAP[card.suit])
                elif card.showing == False:
                    print ("XX")
            print('')
        print (self.IMAGE_MAP['linebreak'])


    def number_of_players_prompt(self):
        run = True
        while run:
            try:
                txt = int(input("How many players? (Please enter a number between 1 and 5):"))
                if txt >5 or txt < 1:
                    print("Sorry please enter a number between 1 and 5")
                else:
                    run = False
            except ValueError:
                continue
        return txt

    def names_of_players(self,number_players):
        player_names = []
        for x in range(1, (number_players + 1)):
            print ("Player number" + str(x))
            name = input("Please enter name:")
            player_names.append(name)
        return player_names

    def hit_ask(self, player):
        '''
        prompts the player for whether they would like to hit or stay
        '''
        while True:
            try:
                answer = input("Would you like to hit {} ? (Y/N)".format(player.name)).lower()
                if answer not in ['y', 'n', 'exit']:
                    raise ValueError("Sorry, we didn't understand your answer.")
                else:
                    return answer
            except ValueError:
                print("Please enter either Y, N or exit...")

    def show_round_winners(self, winners, player_object_list):
        for player in winners:
            if player.dealer == True:
                print(self.IMAGE_MAP['gameover_dealer'])
            else:
                print(self.IMAGE_MAP['gameover'].format(player.name))

        for player in player_object_list:
            print('...................................\n', '{} total hands won: {}'.format(player.name, player.hands_won))

    def bust_string(self, player):
        return '{}, you busted!'.format(player.name)

    def alert_bust(self, bust_string):
        print(bust_string)

    def new_hand_prompt(self):
        run = 0
        while run == 0:
            txt = input("Start a new round of Blackjack? (Y/N)")
            if txt.lower() == "y":
                return True
                run = 1
            elif txt.lower() == "n":
                return False
                run = 1
            elif txt.lower() == "exit":
                exit()
            else:
                continue
