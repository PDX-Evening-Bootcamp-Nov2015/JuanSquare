from BlackJackModel import Player, Deck, Card

class Game():
    def __init__(self):
#TODO Delete this evan list it should be a blank list
        self.player_name_list = ["evan"]
        self.current_player = 0
        self.player_object_list = []
        self.deck = Deck(6) # create the deck object
        self.deck.create_deck() # call method to populate deck with cards


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
        '''
        tests function to set a player's hand
        player: is a player object
        cards: a list of card objects
        '''
        for card in cards:
            player.current_hand.append(card)

    def set_hand_val(self, player):
        pass

    def hit_deal(self):
        pass

    def player_turn(self):
        """ next_turn method. Gives each player their turns. selects player turns by going through playerobjectlist."""
        if self.current_player < len(self.player_object_list)-1:
            self.current_player += 1
        else:
            self.current_player = 0
