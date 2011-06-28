#import uuid
import random
import card

class Stack:
    """
    Defines a collection of cards with helper methods to combine stacks, 
    shuffle cards, and create full decks
    """ 
    def __init__(self, cards = []):
        #self._id = uuid.uuid4()
        self._cards = cards 

    def shuffle(self):
        """Perform the Fisher-Yates shuffle"""
        if len(self._cards) == 0: 
            raise card.CardError('Cannot shuffle an empty Stack') 
        
        r = range(len(self._cards));
        r.reverse()

        for i in r:
            j = random.randint(0, i)
            tmp = self._cards[i]
            self._cards[i] = self._cards[j]
            self._cards[j] = tmp

    def take_at(self, index):
        """Take the card at specific index, removing it from stack"""
        if index not in range(len(self._cards)):
            raise card.CardError('index out of bounds:  %d (0 to %d possible)' % (index, len(self._cards))

        tmp = self._cards[index]
        self._cards.delete(index)
        return tmp

    def deal(self, cards, players = 3):
        if len(self._cards) < cards*players: 
            raise card.CardError('Cannot deal that many cards from Stack') 

        hands = []
        for j in range(players):
            hands.append(Stack(self._cards[:cards]))
            self._cards[:cards] = []

        return hands

    def draw(self):
        if len(self._cards) == 0: 
            raise card.CardError('Cannot draw from an empty Stack') 
        return self._cards.pop()

    def make_deck(self, decks=1):
        """Create a stack of one or more decks"""
        self._cards = []
        
        for n in range(decks):
            for i in range(4):
                for j in range(13):
                    self._cards.append(card.Card(card.suits[i] + card.ranks[j]))
            # Add two jokers
            self._cards.append(card.Card(' X'))
            self._cards.append(card.Card(' X'))

    def card_count(self):
        return len(self._cards)

    def __str__(self):
        s = ''
        for i in self._cards:
            s = s + i._code + ' '
        return s

if __name__ == '__main__':
    a = Stack()
    a.make_deck(decks=2)
    print a
    a.shuffle()
    print a
    print('Total cards: ' + str(a.card_count()))
    for i in range(20):
    	print a.draw()

    b = Stack()
    b.make_deck(decks=3)
    b.shuffle()
    hand = b.deal(10, players=3)
    for i in hand:
    	print i 

