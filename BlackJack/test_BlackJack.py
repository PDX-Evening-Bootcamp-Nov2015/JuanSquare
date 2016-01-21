import unittest
from BlackJackModel import Card, Deck
from BlackJackController import Game



class BlackJackTestCase(unittest.TestCase):

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
        test_game_object = Game()
        names = ["test","testy"]
        self.assertEqual(names, test_game_object.names_of_players())

    def test_assign_player_objects(self):
        pass
