import unittest
from BlackJackModel import Card, Deck, Player



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

    def test_player_creation(self):
        test_player = Player('Percival')
        self.assertEqual(test_player.name, 'Percival')
        self.assertFalse(test_player.dealer)
        self.assertEqual(test_player.current_hand, [])
        self.assertEqual(test_player.hands_won, 0)

    def number_of_players_prompt(self):
