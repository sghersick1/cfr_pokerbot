class Card:
    # Class-level mapping (built once for all card instances)
    _card_format = {}
    rank_list = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
    suit_list = ['C', 'D', 'H', 'S']

    @classmethod
    def _init_mapping(cls):
        if cls._card_format:  # already built
            return
        for s_idx, suit in enumerate(cls.suit_list):
            for r_idx, rank in enumerate(cls.rank_list):
                cls._card_format[(r_idx, s_idx)] = f'{rank}{suit}'

    # rank: 2, 3, 4, 5, 6, 7, 8, 9, 10, J, Q, K, A (0...12)
    # suit: C, D, H, S (0...3)
    def __init__(self, rank: int = 0, suit: int = 0):
        self.rank = rank
        self.suit = suit

    def __str__(self):
        return f'{Card._card_format[(self.rank, self.suit)]}'
    
# built at import time
Card._init_mapping()