import numpy as numpy
import random

class RPS_Player():
    def __init__(self):
        # rock, paper, scissors
        self.regrets = [0, 0, 0]
        self.strategy = [0.33, 0.33, 0.33]
        self.truth_table = [[0,1,-1], # columns = player 1, row = player 2
                            [-1,0,1],
                            [1,-1,0]]

    def take_turn(self):
        rand = random.random()
        if rand < self.strategy[0]:
            return 0 # rock
        elif rand < self.strategy[0] + self.strategy[1]:
            return 1 # paper
        else: 
            return 2 # scissors
        
    def counterfactual_reward(self, a2):
        a1 = self.take_turn()
        c_rewards = self.truth_table[a2] # get all hypothetical rewards
        for i in range(len(self.regrets)): # update regrets 
            self.regrets[i] += c_rewards[i]

        return self.truth_table[a2][a1]

def main():
    bot1 = RPS_Player()
    bot2 = RPS_Player()

    # bots play each other
    for i in range(10):
        bot1.counterfactual_reward(bot2.take_turn())

    print(bot1.regrets)
    
if __name__ == "__main__":
    main()
