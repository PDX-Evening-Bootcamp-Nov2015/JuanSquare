class Game():
    def __init__(self):
        self.number_of_players = number_of_players

    def number_of_players_prompt(self):
        number_of_players = int(input("How many players? (Please enter a number between 1 and 5):"))
        while number_of_players <= 5 and number_of_players != 0:
            print("Sorry please enter a number between 1 and 6")
        return number_of_players
