from BlackJackModel import Player, Deck, Card
from BlackJackView import View
from sys import exit

class Game():
    def __init__(self):
        self.current_player = 0
        self.player_object_list = []
        self.deck = Deck(6) # create the deck object
        self.deck.create_deck() # call method to populate deck with cards
        self.view = View()


    def turn_loop(self):
        '''
        main turn logic, encompasses one entire turn
        '''
        players = self.player_object_list
        playing_player = self.player_object_list[self.current_player]
        turn_over = False
        while self.view.new_hand_prompt():
            self.deck.shuffle()
            self.deal_cards()
            for player in players:
                self.set_hand_val(player)
            self.view.show_table(players)
            turn_over = False
            while not turn_over:
                print(playing_player.name)
                while not playing_player.busted:
                    if playing_player.dealer:
                        if self.dealer_decision():
                            print('dealer decision HIT')
                            self.hit_deal()
                        else:
                            print('dealer decision NOHIT')
                            player.current_hand[0].showing = True
                            turn_over = True
                            self.view.show_table(players)
                            break
                    elif self.hit_prompt(self.view.hit_ask(playing_player)):
                        self.hit_deal()
                    else:
                        self.view.show_table(players)
                        break
                    self.view.show_table(players)
                    self.check_bust()
                    if playing_player.busted:
                        if playing_player.dealer:
                            turn_over = True
                        self.view.alert_bust(self.view.bust_string(playing_player))
                        break
                self.player_turn()
                playing_player = self.player_object_list[self.current_player]
            winners = self.check_round_winner()
            self.discard_cards()
            self.view.show_round_winners(winners, players)






    def hit_prompt(self, prompt_output):
        '''
        interprets player decision about hitting
        '''
        if prompt_output == 'y':
            return True
        elif prompt_output == 'n':
            return False
        elif prompt_output == 'exit':
            exit()
        else:
            raise ValueError()

    def get_players(self, name_players):
        for name in name_players:
            self.player_object_list.append(Player(name))

    def spawn_dealer(self):
        dealer = Player('Dealer')
        dealer.dealer = True
        self.player_object_list.append(dealer)

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
        self.set_hand_val(self.player_object_list[self.current_player])

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
        if self.player_object_list[self.current_player].dealer:
            return True
        else:
            return False


    def discard_cards(self):
        for player in self.player_object_list:
            for card in player.current_hand:
                self.deck.cards.append(card)
            player.current_hand = []


    def deal_cards(self):
        for player in self.player_object_list:
            for i in range(2):
                player.current_hand.append(self.deck.cards[0])
                self.deck.cards.pop(0)
                if player.dealer:
                    showing_card = player.current_hand[0]
                    showing_card.showing = False
            self.set_hand_val(player)

    def check_round_winner(self):
        dealer = self.player_object_list[-1]
        winner_list = []
        if dealer.current_hand_value == 21:
            dealer.hands_won += 1
            winner_list.append(dealer)
            return winner_list
        else:
            for player in self.player_object_list:
                if player.current_hand_value > dealer.current_hand_value and not player.busted:
                    player.hands_won += 1
                    winner_list.append(player)
            return winner_list
