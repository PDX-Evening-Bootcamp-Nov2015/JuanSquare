class View():
    def __init__(self):
        pass

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

    
