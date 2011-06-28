import stack
import card
import unittest

class TestStack (unittest.TestCase):

    def test_create_empty(self):
        a = stack.Stack()
        self.assertTrue(a._cards == [])

    def test_create_some(self):
        a = [' X', 'H2', 'S4', 'S8', 'CA']
        b = [card.Card(i) for i in a]

        st = stack.Stack(b)
        self.assertEqual(len(st._cards), len(a))

    def test_make_decks(self):
        a = stack.Stack()
        a.make_deck(decks=10)
        self.assertEqual(len(a._cards), 54*10)

    def test_shuffle(self):
        a = stack.Stack()
        a.make_deck(decks=3)
        b = a.__str__()
        a.shuffle()
        self.assertNotEqual(a,b)

    def test_deal_too_many(self):
        a = stack.Stack()
        a.make_deck(decks=1)
        a.shuffle()
        with self.assertRaises(card.CardError):
            a.deal(30, players=2)

    def test_deal_different(self):
        a = stack.Stack()
        a.make_deck(decks=1)
        a.shuffle()
        
        hands = a.deal(10, players=2)

        self.assertNotEqual(hands[0], hands[1])
        self.assertNotIn(hands[0]._cards, a._cards)
        self.assertNotIn(hands[1]._cards, a._cards)

if __name__ == '__main__':
	unittest.main()








