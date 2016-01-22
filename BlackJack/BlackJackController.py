from BlackJackModel import Player

class Game():
    def __init__(self):
        self.number_of_players = 0
        self.player_name_list = ["evan"] #TODO change to blank list
        self.player_object_list = []

    def number_of_players_prompt(self):
        number_of_players = int(input("How many players? (Please enter a number between 1 and 5):"))
        while number_of_players <= 5 and number_of_players != 0:
            print("Sorry please enter a number between 1 and 6")
        return number_of_players

    def names_of_players(self):
#TODO delete this names list
        names = ["test","testy"]
        for x in range(1, (self.number_of_players + 1)):
            print ("Player number" + str(x))
            name = input("Please enter name:")
            self.player_name_list.append(name)
#TODO change this return to self.player_name_list.
        return names

    def assign_player_objects(self):
        for name in self.player_name_list:
            self.player_object_list.append(Player(name))

    def set_player_hand(self, player, cards):
        pass

    def hit_deal(self):
        pass
