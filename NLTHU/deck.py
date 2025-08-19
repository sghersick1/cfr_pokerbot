from card import Card

class Deck:
    def __init__(self):
        self.deck = Card._card_format.keys()
        print(self.deck)

    def shuffle(self):
        pass

if __name__ == "__main__":
    c = Card()
    d = Deck()