from phase10 import *
import unittest

class TestCardCreation (unittest.TestCase):
    def test_invalid_code(self):
        with self.assertRaises(CardError):
            Card('Ab')

    def test_create_all_standard(self):
        # Exclude jokers for now
        for i in range(4):
            for j in range(13):
                card1 = Card(suits[i] + ranks[j])
                self.assertTrue(str(card1) == (rank_names[j] + ' of ' + suit_names[i]), \
                        msg='actual string is \'%s\'' % str(card1))
        
    def test_create_jokers(self):
        card1 = Card(' X')
        self.assertTrue(str(card1) == 'Joker', msg='actual string is \'%s\'' % str(card1))
        
    def test_compare(self):
        a = Card(' X')
        b = Card(' X')
        c = Card('HA')

        self.assertTrue(a == b)
        self.assertFalse(a != b)
        self.assertTrue(a != c)
        self.assertFalse(b == c)

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
