from card import Card, CardError

import unittest

class TestCardCreation (unittest.TestCase):
    def setUp(self):
        self.suits = 'HCDS '
        self.ranks = 'A23456789TJQKX'
        
        self.suit_names = ['Hearts', 'Clubs', 'Diamonds', 'Spades', None]

        self.rank_names = ['Ace', 'Two', 'Three', 'Four', 'Five', \
                'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', \
                'Queen', 'King', 'Joker']

    def test_invalid_code(self):
        with self.assertRaises(CardError):
            Card('Ab')

    def test_create_all_standard(self):
        # Exclude jokers for now
        for i in range(4):
            for j in range(13):
                card = Card(self.suits[i] + self.ranks[j])
                self.assertTrue(card.__str__() == (self.rank_names[j] + ' of ' + self.suit_names[i]), msg='actual string is "' + card.__str__() +'"')
        
    def test_create_jokers(self):
        card = Card(' X')
        self.assertTrue(card.__str__() == 'Joker', msg='actual string is "' + card.__str__() +'"')
        
    def test_suited_jokers(self):
        with self.assertRaises(CardError):
            card1 = Card('HX')
        with self.assertRaises(CardError):
            card2 = Card('DX')
        with self.assertRaises(CardError):
            card3 = Card('SX')
        with self.assertRaises(CardError):
            card4 = Card('CX')

if __name__ == '__main__':
	unittest.main()
