import card
import unittest

Card = card.Card
CardError = card.CardError

class TestCardCreation (unittest.TestCase):
    def test_invalid_code(self):
        with self.assertRaises(CardError):
            Card('Ab')

    def test_create_all_standard(self):
        # Exclude jokers for now
        for i in range(4):
            for j in range(13):
                card1 = Card(card.suits[i] + card.ranks[j])
                self.assertTrue(card1.__str__() == (card.rank_names[j] + ' of ' + card.suit_names[i]), msg='actual string is "' + card1.__str__() +'"')
        
    def test_create_jokers(self):
        card1 = Card(' X')
        self.assertTrue(card1.__str__() == 'Joker', msg='actual string is "' + card1.__str__() +'"')
        
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
