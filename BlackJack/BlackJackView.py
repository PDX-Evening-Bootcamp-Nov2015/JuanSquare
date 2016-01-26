class View():
    IMAGE_MAP = {
        'diamonds': "\u2662",
        'spade': "\u2664",
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
        'gameover': "The game is over, {} you are the winner!",
        'gameover_dealer': "The game is over, the dealer won!",
        'playerscore': "{}, your score is now {}",
        'noshowcard': "XX"
    }

    def __init__(self):
        pass

    def show_table(self, player_object_list):
        print (self.IMAGE_MAP[linebreak])
        for player in player_object_list:
            print (player.name)
            for card in player.current_hand:
                if card.showing == True:
                    print (self.IMAGE_MAP[card.value], self.IMAGE_MAP[card.suit])
                elif card.showing == False:
                    print ("XX")
        print (self.IMAGE_MAP[linebreak])


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

    def new_hand_prompt():
        run = 0
        while run == 0:
            txt = input("Do you want to play another round? Type yes or no.")
            if txt.lower() == "yes":
                return True
                run = 1
            elif txt.lower() == "no":
                return False
                run = 1
            else:
                continue
