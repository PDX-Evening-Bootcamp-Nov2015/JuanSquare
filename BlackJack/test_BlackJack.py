import unittest
from BlackJackModel import Card, Deck, Player
from BlackJackController import Game



class BlackJackTestCase(unittest.TestCase):
    def setUp(self):
        self.test_game_object = Game()
        self.test_game_object.deck = Deck(6)

    def tearDown(self):
        del self.test_game_object

    def test_card_creation(self):
        suit, value = 'diamonds', 'ace'
        test_card = Card(suit, value)
        self.assertEqual(test_card.suit, suit)
        self.assertEqual(test_card.value, value)
        self.assertEqual(test_card.color, 'red')
        self.assertEqual(test_card.showing, True)

    def test_create_deck(self):
        test_rootdeck = Deck(6)
        test_rootdeck.create_deck()
        self.assertEqual(len(test_rootdeck.cards), 312)

    def test_number_of_players_prompt(self):
        pass

    def test_names_of_players(self):
        names = ["test","testy"]
        self.assertEqual(names, test_game_object.names_of_players())

    def test_assign_player_objects(self):
        test_game_object.assign_player_objects()
        self.assertEqual(self.test_game_object.player_name_list[0], test_game_object.player_object_list[0].name)

    def test_spawn_dealer(self):
        self.test_game_object.spawn_dealer()
        self.assertTrue(self.test_game_object.player_object_list[-1].dealer)

    def test_set_player_hand(self):
        '''
        tests function to set a player's hand
        player: is a player object
        cards: a list of card objects
        '''
        # check adding to empty hand
        self.test_game_object.player_object_list.append(Player('Bill'))
        test_player = self.test_game_object.player_object_list[0]
        cards_dealt = [Card('spades', 'five'), Card('hearts', 'king')]
        self.test_game_object.set_player_hand(test_player, cards_dealt)
        self.assertEqual(test_player.current_hand, cards_dealt)
        # check adding to existing hand
        new_card = Card('spades', 'six')
        self.test_game_object.set_player_hand(test_player, [new_card])
        cards_dealt.append(new_card)
        self.assertEqual(test_player.current_hand, cards_dealt)

    def test_hit_deal(self):
        pass

    def test_player_turn(self):
        self.current_player = 0
        self.test_game_object.player_object_list = [Player("evan"), Player("Evan2")]
        self.test_game_object.player_turn()
        self.assertEqual(self.current_player, 1)

    def test_check_bust(self):
        self.test_game_object.player_object_list = [Player("evan"), Player("Evan2")]
        player = self.test_game_object.player_object_list[self.test_game_object.current_player]
        player.current_hand_value = 22
        self.test_game_object.check_bust()
        self.assertTrue(player.busted)

    def test_dealer_decision(self):
        self.test_game_object.player_object_list = [Player("evan"), Player("Evan2")]
        dealer = self.test_game_object.player_object_list[-1]
        dealer.current_hand_value = 18
        self.assertFalse(self.test_game_object.dealer_decision())
