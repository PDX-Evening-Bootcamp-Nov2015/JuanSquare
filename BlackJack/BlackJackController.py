from BlackJackModel import Player

class Game():
    def __init__(self):
        self.number_of_players = 0
#TODO Delete this evan list it should be a blank list
        self.player_name_list = ["evan"]
        self.current_player = 0
        self.player_object_list = []

<<<<<<< HEAD
    def number_of_players_prompt():
        number_of_players = 0
        run = True
        while run:
            try:
                txt = int(input("How many players? (Please enter a number between 1 and 5):"))
                number_of_players = txt
                if txt >5 or txt < 1:
                    print("Sorry please enter a number between 1 and 5")
                else:
                    run = False
            except ValueError:
                print ("Thanks for telling us how many are playing!")
=======
    def number_of_players_prompt(self):
        number_of_players = int(input("How many players? (Please enter a number between 1 and 5):"))
        if number_of_players >= 5 and number_of_players != 0:
            print("Sorry please enter a number between 1 and 6")
>>>>>>> 26f14cb691280a431e5424f82c0fa8c3c3f8d070
        return number_of_players

    def names_of_players(self):
#TODO delete this names list
        names = ["test","testy"]
        for x in range(1, (self.number_of_players_prompt() + 1)):
            print ("Player number" + str(x))
            name = input("Please enter name:")
            self.player_name_list.append(name)
#TODO change this return to self.player_name_list.
        return names

    def assign_player_objects(self):
        for name in self.player_name_list:
            self.player_object_list.append(Player(name))

    def spawn_dealer(self):
        dealer = Player('Dealer')
        dealer.dealer = True
        self.player_object_list.append(dealer)

    def set_player_hand(self, player, cards):
        for card in cards:
            player.current_hand.append(card)

    def hit_deal(self):
        pass

    def player_turn(self):
        """ next_turn method. Gives each player their turns. selects player turns by going through playerobjectlist."""
        if self.current_player < len(self.player_object_list)-1:
            self.current_player += 1
        else:
            self.current_player = 0
