class Card:
    """Represents a single card"""
    
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
            raise CardError('Invalid suit code "' + s + '"')

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
            self._rank = 'Joker'
            self._value = 15
        else:
             raise CardError('Invalid rank code "' + r + '"')

    def __str__(self):
        if self._rank is not 'Joker':
            return self._rank + ' of ' + self._suit
        else:
            return self._rank 

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
