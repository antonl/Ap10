import random

class Game:
    """Class representing a phase 10 game. Should be serializable"""

    def __init__(self, state=None):
        if state is not None:
            try:
                self._deck = state['deck']
                self._discard = state['discard']
                self._hands = state['hands']
                self._players = state['players']
                self._playorder = state['playorder']
                self._turn = state['turn']
                return
            except KeyError:
                # State does not have all of the keys,
                # assume that the Game is empty
                self._deck = Stack() 
                self._discard = Stack()
                self._hands = []
                self._players = []
                self._playorder = []
                self._turn = 1

    def start_game(self, player_ids, decks=2):
        """player_ids is a list of player ids that is used to identify whose turn it is"""
        self._deck = Stack()
        self._deck.make_deck(decks)
        self._deck.shuffle()

        self._hands = self._deck.deal(10, len(player_ids))
        self._players = []

        self._turn = 1

        for i in range(len(self._hands)):
        	self._players.append(Player(pid=player_ids[i], hand=self._hands[i], pset=Stack()))

        # Randomize play order
        self._playorder = shuffle(range(len(player_ids)))

        self._discard = Stack()
        self._discard += self._deck.draw()
    
    @property
    def turn(self):
        self._turn += 1
        # return Turn
        pass

    def __repr__(self):
        return "Game({'deck' : %s, 'players' : %s, 'discard' : %s, 'hands' : %s, 'playorder' : %s, 'turn' : %s})" \
                % (repr(self._deck), repr(self._players), repr(self._discard), repr(self._hands), \
                        repr(self._playorder), repr(self._turn))

class Player:
    def __init__(self, pid, hand=None, pset=None):
        """pid is a key that will be used to identify the player with a login name
        hand is a Stack that represents the player's hand
        pset is a Stack that represents the player's current set
        """
        self._id = pid

        if hand:
            self._hand = hand 
        else:
        	self._hand = Stack()

        if pset: 
            self._set = pset
        else:
        	self._set = Stack()

    def __repr__(self):
        return "Player(pid=%s, hand=%s, pset=%s)" % (repr(self._id), repr(self._hand), repr(self._set))

class Turn:
    def __init__(self):
        pass

class Phase:
    pass
class Phase1 (Phase):
    pass
class Phase2 (Phase):
    pass
class Phase3 (Phase):
    pass
class Phase4 (Phase):
    pass
class Phase5 (Phase):
    pass
class Phase6 (Phase):
    pass
class Phase7 (Phase):
    pass
class Phase8 (Phase):
    pass
class Phase9 (Phase):
    pass
class Phase10 (Phase):
    pass

class Card:
    """Represents a single card"""
    @property
    def val(self):
        return self._value
    
    def __init__(self, code): 
        """
        Code is Suit letter (H,C,D,S) followed by rank (A,2,3,4,5,6,7,8,9,T,J,Q,K,X) 
        where T is 10 and X is joker
        """
        self._code = code    

        # Set suit
        s = code[0]
        if s == 'H':
            self._suit = 'Hearts'
        elif s == 'C':
            self._suit = 'Clubs'
        elif s == 'D':
            self._suit = 'Diamonds'
        elif s == 'S':
            self._suit = 'Spades'
        elif s == ' ': # Used for jokers
            self._suit = None
        else:
            raise CardError('Invalid suit code \'%s\'' % s)

        # Set rank
        r = code[1]

        if r == 'A':
            self._rank = 'Ace'
            self._value = 5
        elif r == '2':
            self._rank = 'Two'
            self._value = 5
        elif r == '3':
            self._rank = 'Three'
            self._value = 5
        elif r == '4':
            self._rank = 'Four'
            self._value = 5
        elif r == '5':
            self._rank = 'Five'
            self._value = 5
        elif r == '6':
            self._rank = 'Six'
            self._value = 5
        elif r == '7':
            self._rank = 'Seven'
            self._value = 5
        elif r == '8':
            self._rank = 'Eight'
            self._value = 5
        elif r == '9':
            self._rank = 'Nine'
            self._value = 5
        elif r == 'T':
            self._rank = 'Ten'
            self._value = 10 
        elif r == 'J':
            self._rank = 'Jack'
            self._value = 10 
        elif r == 'Q': 
            self._rank = 'Queen'
            self._value = 10 
        elif r == 'K':
            self._rank = 'King'
            self._value = 25 
        elif r == 'X':
            if s == ' ':
                self._rank = 'Joker'
                self._value = 15
            else:
            	raise CardError('Cannot create suited jokers \'%s\'' % code)
        else:
             raise CardError('Invalid rank code %s', r)

    def __str__(self):
        if self._rank is not 'Joker':
            return self._rank + ' of ' + self._suit
        else:
            return self._rank 

    def __repr__(self):
        return "Card(%s)" % repr(self._code)

def shuffle(items):
    if len(items) > 0:
        r = range(len(items));
        r.reverse()

        for i in r:
            j = random.randint(0, i)
            tmp = items[i]
            items[i] = items[j]
            items[j] = tmp

        return items

suits = 'HCDS '
ranks = 'A23456789TJQKX'
suit_names = ['Hearts', 'Clubs', 'Diamonds', 'Spades', None]
rank_names = ['Ace', 'Two', 'Three', 'Four', 'Five', \
                'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', \
                'Queen', 'King', 'Joker']

class CardError (Exception):
    """
    Represents an error in creation or use of card class
    """
    pass

class Stack:
    """
    Defines a collection of cards with helper methods to combine stacks, 
    shuffle cards, and create full decks
    """ 
    def __init__(self, cards=None):
        if cards is not None:
        	self._cards = cards 
        else:
        	self._cards = []

    def shuffle(self):
        """Perform the Fisher-Yates shuffle"""
        if len(self._cards) == 0: 
            raise CardError('Cannot shuffle an empty Stack') 
        
        self._cards = shuffle(self._cards)

    def take_at(self, index):
        """Take the card at specific index, removing it from stack"""
        if index not in range(len(self._cards)):
            raise CardError('index out of bounds:  %d (0 to %d possible)' % (index, len(self._cards)))

        tmp = self._cards[index]
        self._cards[index] = []
        return tmp

    @property
    def score(self):
        return sum(i.val for i in self._cards)

    def __iadd__(self, other):
        """In place addition of one stack to another stack. The second stack is emptied in this case"""
        if isinstance(other, Card):
        	self._cards.append(other)
        elif isinstance(other, Stack):
            self._cards.extend(other._cards)
            other._cards = []
        else:
        	raise CardError('Cannot add an unhandled type to Stack')

        return self

    def deal(self, cards, players = 3):
        if len(self._cards) < cards*players: 
            raise CardError('Cannot deal that many cards from Stack') 

        hands = []
        for j in range(players):
            hands.append(Stack(self._cards[:cards]))
            self._cards[:cards] = []

        return hands

    def draw(self):
        if len(self._cards) == 0: 
            raise CardError('Cannot draw from an empty Stack') 
        return self._cards.pop()

    def make_deck(self, decks=1):
        """Create a stack of one or more decks"""
        self._cards = []
        
        for n in range(decks):
            for i in range(4):
                for j in range(13):
                    self._cards.append(Card(suits[i] + ranks[j]))
            # Add two jokers
            self._cards.append(Card(' X'))
            self._cards.append(Card(' X'))

    @property
    def card_count(self):
        return len(self._cards)

    def __str__(self):
        s = ''
        for i in self._cards:
            s = s + i._code + ' '
        return s

    def __repr__(self):
        s = 'Stack(['
        for i in self._cards:
        	s += i.__repr__() + ', '
        s += '])'
        return s

# Unit tests
if __name__ == '__main__':
    import unittest
    import test_stack
    import test_card
    card_suite = unittest.TestLoader().loadTestsFromTestCase(test_card.TestCardCreation)
    stack_suite = unittest.TestLoader().loadTestsFromTestCase(test_stack.TestStack)
    unittest.TextTestRunner(verbosity=2).run(unittest.TestSuite([card_suite, stack_suite]))

