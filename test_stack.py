from phase10 import *
import unittest

class TestStack (unittest.TestCase):

    def test_str(self):
        a = Stack()

        self.assertTrue(str(a) == 'Empty')

        a += Card('HA')

        self.assertTrue('HA' in str(a))

    def test_create_empty(self):
        a = Stack()
        self.assertTrue(a.card_count == 0) 
        b = Stack()
        self.assertTrue(b.card_count == 0)

        c = Card('D3')
        b += c

        self.assertFalse(a.card_count == 1)
        self.assertTrue(b.card_count == 1)


    def test_card_count(self):
        a = Stack()
        self.assertTrue(a.card_count == 0)

    def test_create_some(self):
        a = [' X', 'H2', 'S4', 'S8', 'CA']
        b = [Card(i) for i in a]

        st = Stack(b)
        self.assertEqual(st.card_count, len(a))

    def test_make_decks(self):
        a = Stack()
        a.make_deck(decks=10)
        self.assertEqual(a.card_count, 54*10)

    def test_shuffle(self):
        a = Stack()
        a.make_deck(decks=3)
        b = str(a)
        a.shuffle()
        self.assertNotEqual(a,b)

    def test_deal_too_many(self):
        a = Stack()
        a.make_deck(decks=1)
        a.shuffle()
        with self.assertRaises(CardError):
            a.deal(30, players=2)

    def test_deal_different(self):
        a = Stack()
        a.make_deck(decks=1)
        a.shuffle()
        
        hands = a.deal(10, players=5)

        self.assertNotEqual(hands[0], hands[1])
        self.assertNotIn(hands[0]._cards, a._cards)
        self.assertNotIn(hands[1]._cards, a._cards)
        self.assertNotIn(hands[2]._cards, a._cards)
        self.assertNotIn(hands[3]._cards, a._cards)
        self.assertNotIn(hands[4]._cards, a._cards)

        self.assertTrue(a.card_count, 4)
    
    def test_take_at(self):
        stk = Stack()
        stk.make_deck(decks=1)
        a = stk._cards[10]
        b = stk.take_at(10)
        self.assertEqual(a,b)

    def test_take_at_outofbounds(self):
        stk = Stack()
        stk.make_deck(decks=1)
        with self.assertRaises(CardError):
            stk.take_at(60)
        with self.assertRaises(CardError):
            stk.take_at(-1)

    def test_iadd_stacks(self):
        stk1 = Stack()
        stk1.make_deck(decks=1)

        self.assertEqual(stk1.card_count, 54)

        stk2 = Stack()
        stk2.make_deck(decks=1)

        self.assertEqual(stk2.card_count, 54)

        stk1 += stk2

        self.assertEqual(stk1.card_count, 54*2)
        self.assertEqual(stk2.card_count, 0)

    def test_iadd_card(self):
        a = Stack()
        b = Card(' J')
        
        self.assertTrue(a.card_count == 0)
        a += b

        self.assertTrue(a.card_count == 1)
        self.assertTrue(b in a._cards)

    def test_get_score(self):
        a = [' X', 'HK', 'SK', 'SJ', 'ST', 'SA', 'C2']
        cards = [Card(i) for i in a]
        
        b = 0
        for i in cards:
            b += i.val

        self.assertEqual(b, Stack(cards).score) 
        
if __name__ == '__main__':
	unittest.main()

