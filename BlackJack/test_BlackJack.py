import unittest
from BlackJackModel import Card, Deck, Player
from BlackJackController import Game



class BlackJackTestCase(unittest.TestCase):
    def setUp(self):
        self.test_game_object = Game()

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

    def test_player_turn(self):
        self.current_player = 0
        self.test_game_object.player_object_list = [Player("evan"), Player("Evan2")]
        self.test_game_object.player_turn()
        self.assertEqual(self.current_player, 1)
