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
    
    def test_take_at(self):
        stk = stack.Stack()
        stk.make_deck(decks=1)
        a = stk._cards[10]
        b = stk.take_at(10)
        self.assertEqual(a,b)

    def test_take_at_outofbounds(self):
        stk = stack.Stack()
        stk.make_deck(decks=1)
        with self.assertRaises(card.CardError):
            stk.take_at(60)
        with self.assertRaises(card.CardError):
            stk.take_at(-1)

    def test_iadd_stacks(self):
        stk1 = stack.Stack()
        stk1.make_deck(decks=1)

        self.assertEqual(len(stk1._cards), 54)

        stk2 = stack.Stack()
        stk2.make_deck(decks=1)

        self.assertEqual(len(stk2._cards), 54)

        stk1 += stk2

        self.assertEqual(len(stk1._cards), 54*2)
        self.assertEqual(len(stk2._cards), 0)

    def test_get_score(self):
        a = [' X', 'HK', 'SK', 'SJ', 'ST', 'SA', 'C2']
        cards = [card.Card(i) for i in a]
        
        b = 0
        for i in cards:
            b += i.val()

        self.assertEqual(b, stack.Stack(cards).get_score()) 
        
if __name__ == '__main__':
	unittest.main()








