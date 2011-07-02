from phase10 import *
import unittest

class TestGame (unittest.TestCase):
    def test_start_game(self):
        g = Game()
        g.start_game(['a', 'b'], decks=2)

        g2 = Game()
        g2.start_game(['a', 'b'], decks=2)

        self.assertTrue(g._deck.card_count == 87)
        self.assertTrue(g._discard.card_count == 1) 

        a = g._players[0]
        b = g._players[1]

        # There can be more than one of a card in a deck, 
        # so these tests give the wrong result
        #self.assertFalse(a._hand in g._deck) 
        #self.assertFalse(b._hand in g._deck) 

        self.assertTrue(a._set.card_count == 0) 
        self.assertTrue(b._set.card_count == 0) 

        self.assertTrue(a._hand.card_count == 10) 
        self.assertTrue(b._hand.card_count == 10) 

    def test_next(self):
        g = Game()
        g.start_game(['a', 'b'], decks=2)

        t = g.turn
        t.draw_deck()
        t.discard_at(1)
        
        a = t.player._id 

        g.next()
        
        t = g.turn
        b = t.player._id 

        self.assertTrue(a is not b, msg="'%s' == '%s'" % (a, b))

        g.next()

        t = g.turn
        c = t.player._id 

        self.assertTrue(a is c)


    def test_turn_discard_at(self):
        g = Game()
        g.start_game(['a', 'b'], decks=2)

        t = g.turn
        
        t.draw_deck()

        self.assertTrue(g._deck.card_count == 86)
        self.assertTrue(t.hand.card_count == 11)

        with self.assertRaises(CardError):
            t.discard_at(12)


