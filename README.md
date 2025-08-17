# cfr_pokerbot

Building a poker bot using counterfactual regret minimization.

#### No Limit Texas Holdem:

- Vanilla CFR works great for a small game such as Kuhn Poker, but it is too slow/expensive for larger poker variants

- CFR+
  a. In Vallina CFR, we use uniform updating of the average strategy
  b. Beginning and ending strategy changes the same
  c. Solution 1: reset strategy half way through and just use average from better strategy. Solution 2: Update the strategy with a weighted proportion.

- Monte Carlo CFR
  a. Instead of updating regrets for both players, we alternate between both players and only update only players regrets at a time.
  b. We reduce the amount of game tree explored at each iteration, still converging to nash equilibrium
  c. Take the greedy path with some probability

- Improved Regret storage
  a. In vanilla CFR negative number are ignored when computing strategy
  b. CFR+ doesn't store any negative regrets at all
  c. Actual regrets are not stored, they are considered "regret-like" values

- Pruning
  a. We don't explore areas on the game tree that have a tiny amount of regret
  b. Only prune after a certain amount of iterations

- Abstractions:
  a. fold, check/call, pot, all-in (start small then work up from here)
  b. Use Rand-psHar everywhere to translate off-grid bets to your nearest abstract sizes A and B:​  
   fa,b(x)=
  (B−A)(1+x)
  (B−x)(1+A)
  ​
  Sample A with that probability, else B. (Least exploitable)

- Toy Game:
  Leduc Poker
  **Flop Holdem:** Exactly like texas holdem but game stops after flop (2 betting rounds)

#### Sources:

- **CFR Examples:** http://modelai.gettysburg.edu/2013/cfr/cfr.pdf
- **Original CFR Paper:** https://poker.cs.ualberta.ca/publications/NIPS07-cfr.pdf
- **AlphaHoldem Paper:** https://ojs.aaai.org/index.php/AAAI/article/view/20394
- **Ian Sullivan Youtube:** https://www.youtube.com/watch?v=xhnDel1jOdA&list=PLoQ2rCmr5jLhPkzClcgRHyz5iLldf-5l3&index=3
- **Abstractions:** https://nebula.wsimg.com/197ee65d8124f2060c45478c8080da7c?AccessKeyId=4F0E80116E133E66881C&disposition=0&alloworigin=1
