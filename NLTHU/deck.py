from card import Card
from random import shuffle

class Deck(Card):
    def __init__(self):
        tups = list(Card._card_format.keys())
        self.deck = list(Card(t[0], t[1]) for t in tups)

    def shuffle(self):
        if len(self.deck) != 52:
            print("ERROR: deck not shuffled. Only shuffle complete deck.")
            return
        shuffle(self.deck)

    def popCard(self):
        if len(self.deck) <= 0:
            print("DECK IS EMPTY!\n")
            return None
        return self.deck.pop()
    
    def __str__(self):
        cards = [f"{card}" for card in self.deck]
        return f'Deck ({len(cards)})\n---------\n{cards}'
    
if __name__ == "__main__":
    d = Deck()
    d.shuffle()
    print(d)

