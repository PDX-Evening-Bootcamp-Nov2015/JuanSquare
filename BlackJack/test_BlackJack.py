import unittest
from BlackJackModel import Card


class BlackJackTestCase(unittest.TestCase):

    def test_card_creation(self):
        suit, value = 'diamonds', 'ace'
        test_card = Card(suit, value)
        self.assertEqual(test_card.suit, suit)
        self.assertEqual(test_card.value, value)
        self.assertEqual(test_card.color, 'red')
        self.assertEqual(test_card.showing, True)
