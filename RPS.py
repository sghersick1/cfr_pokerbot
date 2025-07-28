''' 
Author: Sam Hersick
Date: 7-24-2025
Version: 1.0
Objective: 
    1. Build a Counterfactual Regret Minimization simulation for the game Rock, Paper, Scissors
    2. Successfully converge RPS strategy to Nash Equilibrium (33.33% Rock, 33.33% Paper, 33.33% Scissors)
'''

from typing import List
import matplotlib.pyplot as plt
import random

# Utilities (Rewards for win, loss, or draw)
# Rows are Opponent, Columns are Player [R, P, S]
U = [[0, 1, -1],
     [-1, 0, 1],
     [1, -1, 0]]

class RPS_Player:
    def __init__(self, strategy=None, strategy_sum=None, regrets=None):
        self.strategy = strategy[:] if strategy else [1/3, 1/3, 1/3] # create copy or fresh list
        self.strategy_sum = strategy_sum[:] if strategy_sum else [0, 0, 0]
        self.regrets = regrets[:] if regrets else [0,0,0]
        self.T = 0
        self.average_strategy = self.strategy[:]
        self.hands = [[0,0,0],
                      [0,0,0],
                      [0,0,0]]
        self.wins = 0
        self.draws = 0
        self.losses = 0
        self.history = [] # Matplotlib chart

    def determine_action(self):
        rand = random.random()
        return 0 if rand < self.strategy[0] else 1 if rand < sum(self.strategy[:2]) else 2
    
    def regret_matching(self):
        total = sum(max(0,regret) for regret in self.regrets) # sum all positive regrets
        for i in range(3):
            if total > 0:
                self.strategy[i] = max(0, self.regrets[i])/total # only update for positive regrets (we could improve)
            else:
                self.strategy[i] = 1/3 # if total regret <= 0, set actions distribution to totally random

    def calc_average_strategy(self):
        for j in range(3):
            self.average_strategy[j] = self.strategy_sum[j]/ self.T if self.T > 0 else 1/3

    def __str__(self):
        return f"Rounds Played: {self.T}\nWins: {self.wins}({self.wins/self.T})\nDraws: {self.draws}({self.draws/self.T})\nLosses: {self.losses}({self.losses/self.T})\nAverage Strategy: {self.average_strategy}\nCurrent Strategy: {self.strategy}"

    def play_opponent(self, opponent):
        self.history.append(self.strategy[:]) # Show strategy over time for chart
        self.T += 1 # add 1 to number of rounds played

        action = self.determine_action()
        o_action = opponent.determine_action()

        self.updated_hand_stats(action, o_action)
        self.calculate_regrets(action, o_action)
        self.regret_matching() # update the strategy based off of regrets
        for i in range(3): # updated cummulative strategy
            self.strategy_sum[i] += self.strategy[i]

        #print(f"{action} vs. {o_action}\nRegrets: {self.regrets}\nStrategy: {self.strategy}\n") # Round results

    def updated_hand_stats(self, action, o_action):
        reward = U[o_action][action]

        # update the total wins/losses for a hand
        if reward == 1: # add to wins
            self.hands[action][0] +=1 
            self.wins += 1
        elif reward == 0: # add to draws
            self.hands[action][1] += 1
            self.draws += 1
        else: # add to losses
            self.hands[action][2] += 1
            self.losses += 1

    def calculate_regrets(self, p_action, o_action):
        reward = U[o_action][p_action]
        rewards = U[o_action] 

        for i in range(3):
            play_regret = rewards[i] - reward
            self.regrets[i] += play_regret # Add positive regrets
 
def run_cfr(T: int, player: RPS_Player, opponent: RPS_Player):
    for t in range(T):
        player.play_opponent(opponent) # Player learns
        opponent.play_opponent(player) # Opponent learns
    player.calc_average_strategy()
    opponent.calc_average_strategy()

import matplotlib.pyplot as plt

def plot_strategy_evolution(history, player: str, step=1):
    """
    Plots the evolution of strategy over time, sampling every `step` rounds.
    Adds dashed horizontal lines for average strategy values.
    
    Parameters:
    - history (List[List[float]]): A list of strategy vectors [R, P, S] recorded each round.
    - player (str): Label to show in the chart title.
    - step (int): Interval of rounds to plot (e.g., every 2000 rounds).
    """
    # Downsample the history and generate corresponding round numbers
    sampled_history = history[::step]
    rounds = list(range(1, len(history) + 1, step))

    # Split strategy components
    rock = [s[0] for s in sampled_history]
    paper = [s[1] for s in sampled_history]
    scissors = [s[2] for s in sampled_history]

    # Compute averages
    full_rock = [s[0] for s in history]
    full_paper = [s[1] for s in history]
    full_scissors = [s[2] for s in history]

    avg_rock = sum(full_rock) / len(full_rock)
    avg_paper = sum(full_paper) / len(full_paper)
    avg_scissors = sum(full_scissors) / len(full_scissors)

    # Plot
    plt.figure(figsize=(12, 6))
    plt.plot(rounds, rock, label="Rock", color="red", linewidth=2)
    plt.axhline(y=avg_rock, color="red", linestyle="--", linewidth=1, label="Rock Avg")

    plt.plot(rounds, paper, label="Paper", color="blue", linewidth=2)
    plt.axhline(y=avg_paper, color="blue", linestyle="--", linewidth=1, label="Paper Avg")

    plt.plot(rounds, scissors, label="Scissors", color="green", linewidth=2)
    plt.axhline(y=avg_scissors, color="green", linestyle="--", linewidth=1, label="Scissors Avg")

    plt.title(f"Strategy Evolution: {player}", fontsize=14)
    plt.xlabel("Round (t)", fontsize=12)
    plt.ylabel("Strategy Probability", fontsize=12)
    plt.ylim(0, 1)
    plt.grid(True, linestyle="--", alpha=0.5)
    plt.legend()
    plt.tight_layout()
    plt.show()

def main():
    T = 10000 # number of round (per simulation)
    for i in range(1): # number of simulations
        p1 = RPS_Player(strategy=[1/3, 1/3, 1/3])
        p2 = RPS_Player(strategy=[1/3, 1/3,1/3])
        run_cfr(T, p1, p2) # player 1 learns
        print(f"Player 1: \n{p1}\n--------------------\n")
        print(f"Player 2: \n{p2}")
        plot_strategy_evolution(p1.history, "Player 1", step=1)
        plot_strategy_evolution(p2.history, "Player 2", step=1)

if __name__ == "__main__":
    main()
