### System Design

### Classes

- Card
  a. Rank: int
  b. suit: int
  c. to_str():str
- Deck
  a. cards: List<Card>
  b. shuffle()
- HandEvaluator
  a. rank_hand()
  b. compare_hands(): Player --> return winner
- Action
  a. Fold
  b. Check
  c. Call
  d. Bet
  e. Raise
  f. All in
- Player
  a. id: int
  b. stack: int
  c. hole: List<Card>
- Dealer
  a. deal_preflop(List<Player>)
  b. deal_flop()
- Main
  a. select_players()
  b. play_round()
