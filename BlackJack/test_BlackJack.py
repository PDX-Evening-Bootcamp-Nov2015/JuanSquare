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

    def test_player_creation(self):
        test_player = Player("Bob")
        self.assertEqual(test_player.name, "Bob")
        self.assertEqual(test_player.current_hand, [])
        self.assertEqual(test_player.current_hand_value, 0)
        self.assertEqual(test_player.hands_won, 0)
        self.assertEqual(test_player.dealer, False)

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
        '''
        # check adding to empty hand
        self.test_game_object.player_object_list.insert(0, Player('Bill'))
        test_player = self.test_game_object.player_object_list[0]
        cards_dealt = [Card('spades', 'five'), Card('hearts', 'king')]
        self.test_game_object.set_player_hand(test_player, cards_dealt)
        self.assertEqual(test_player.current_hand, cards_dealt)
        # check adding to existing hand
        new_card = Card('spades', 'six')
        self.test_game_object.set_player_hand(test_player, [new_card])
        cards_dealt.append(new_card)
        self.assertEqual(test_player.current_hand, cards_dealt)

    def test_set_hand_val(self):
        self.test_game_object.player_object_list.insert(0, Player('Bill'))
        test_player = self.test_game_object.player_object_list[0]
        # case 1, expect 15
        test_player.current_hand = [Card('spades', 'five'), Card('hearts', 'king')]
        self.test_game_object.set_hand_val(test_player)
        self.assertEqual(test_player.current_hand_value, 15)
        # case 2, expect 21
        test_player.current_hand = [Card('spades', 'ace'), Card('hearts', 'king')]
        self.test_game_object.set_hand_val(test_player)
        self.assertEqual(test_player.current_hand_value, 21)
        # case 3, expect 21
        test_player.current_hand = [Card('spades', 'ace'), \
        Card('hearts', 'king'), Card('hearts', 'king')]
        self.test_game_object.set_hand_val(test_player)
        self.assertEqual(test_player.current_hand_value, 21)

    def test_hit_deal(self):
        test_variable = self.test_game_object.deck.cards[0]
        test_hand = self.player_object_list[self.current_player].current_hand
        self.test_game_object.test_hit_deal()
        self.assertTrue(test_variable, test_hand)

    def test_check_deck_empty(self):
        '''
        test function to check if the deck is running low
        '''
        # backup deck to prevent side effects on other tests
        backup = self.test_game_object.deck.cards[:]
        # test case 1
        self.test_game_object.deck.cards = []
        self.assertTrue(self.test_game_object.check_deck_empty())
        # restore backup to prevent side effects on other tests
        self.test_game_object.deck.cards = backup

    def test_player_turn(self):
        self.current_player = 0
        self.test_game_object.player_object_list = [Player("evan"), Player("Evan2")]
        self.test_game_object.player_turn()
        self.assertEqual(self.current_player, 1)

    def test_check_bust(self):
        self.test_game_object.check_bust()
        self.test_game_object.current_hand_value = 22
        self.assertTrue(player.busted)

    def test_hit_deal(self):
        pass
