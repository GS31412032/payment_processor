class Card:
    
    def __init__(self, value, suit):
        self.value = value
        self.suit = suit
    
    def card_print(self):
        print(f"The {self.value} of {self.suit}'s.")

    def face_card(self):
        face_cards = ['jack', 'king', 'queen']
        value = self.value.lower()
        return value in face_cards


class Deck:
    def __init__(self):
        self.cards = []
        suits = ['spade', 'heart', 'club', 'diamond']
        values = ['two', 'three', 'four', 'five', 'six', 
                  'seven', 'eight', 'nine', 'ten', 
                  'jack', 'queen', 'king', 'ace']
        
        for suit in suits:
            for value in values:
                card = Card(value, suit)
                self.cards.append(card)

    def draw(self):
        return self.cards.pop()


# Testing
deck = Deck()
print(len(deck.cards))  # 52
card = deck.draw()
card.card_print()
print(len(deck.cards))  # 51

class ClownDeck(Deck):
    def __init__(self):
        super().__init__()
    
    def draw_clown_card(self):
        if len( self.cards) > 0:
            card = self.cards.pop()
            face_cards = ['jack', 'king', 'queen']
            if card.value == 'jack':
                    print('Bozo The Clown')
            elif card.value == 'queen':
                    print('Sunshine Clown')
            elif card.value == 'king':
                    print('Weary Willie')
            else:
                print('Not a Clown Face Card')
        else:
            print('Out of Cards')

deck = ClownDeck()
for card in range(53):
    deck.draw_clown_card()



