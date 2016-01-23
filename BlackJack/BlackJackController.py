from BlackJackModel import Player, Deck, Card
from BlackJackView import View

class Game():
    def __init__(self):
        self.current_player = 0
        self.player_object_list = []
        self.deck = Deck(6) # create the deck object
        self.deck.create_deck() # call method to populate deck with cards
        self.view = View()

    def assign_player_objects(self):
        for name in self.player_name_list:

    def get_players(self):
        num_players = self.view.number_of_players_prompt()
        name_players = self.view.names_of_players(num_players)
        for name in name_players:
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
        '''
        sets the player's score property equal to the total score of their cards
        '''
        card_vals = []
        hand_score = 0

        def add_hands():
            '''
            helper function to add up card scores
            '''
            score = 0
            for val in card_vals:
                score += val
            return score

        def has_elevens():
            '''
            checks if the hand has aces counted as eleven
            '''
            for val in card_vals:
                if val == 11:
                    return True
            return False

        # set up the card value list to operate on
        for card in player.current_hand:
            card_vals.append(card.score)
        # add up all card values
        hand_score = add_hands()
        # change aces if they would make player bust
        while hand_score > 21 and has_elevens():
            for val in card_vals:
                if val == 11:
                    card_vals[card_vals.index(val)] = 1
                    break
            hand_score = add_hands()
        # update the player score
        player.current_hand_value = hand_score



    def hit_deal(self):
        self.player_object_list[self.current_player].current_hand.append(self.deck.cards.pop())


    def player_turn(self):
        """ next_turn method. Gives each player their turns. selects player turns by going through playerobjectlist."""
        if self.current_player < len(self.player_object_list)-1:
            self.current_player += 1
        else:
            self.current_player = 0

    def check_bust(self):
        player = self.player_object_list[self.current_player]
        if player.current_hand_value > 21:
            player.busted = True

    def dealer_decision(self):
        dealer = self.player_object_list[-1]
        if dealer.current_hand_value <= 16:
            return True
        if dealer.current_hand_value > 16:
            return False

    def check_deck_empty(self):
        if len(self.deck.cards) < 101:
            return True

    def check_end_round(self):
        if self.player_object_list[self.current_player].dealer == True:
            return True
        else:
            return False

    def deal_cards(self):
        for player in self.player_object_list:
            for i in range(2):
                player.current_hand.append(self.deck.cards[0])
                self.deck.cards.pop(0)
                if player == self.player_object_list[-1]:
                    showing_card = player.current_hand[0]
                    showing_card.showing = False
