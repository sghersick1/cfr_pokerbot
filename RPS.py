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
        
    def counterfactual_reward(self, a1, a2):
        c_rewards = self.truth_table[a2]
        for i in range(len(self.regrets)):
            self.regrets[i] += c_rewards[i]

        return self.truth_table[a2][a1]
        
    

# action 1 is "our" player
# action 2 is "opponent"
def pick_winner(a1, a2):
    if a1 == a2:
        return 0
    elif a1 == 'r': # rock
        if a2 =='p':
            return -1
        else: return 1
    elif a1 == 'p': # paper
        if a2 == 's':
            return -1
        else: return 1
    else: # scissors
        if a2 == 'r':
            return -1
        else: return 1
        




def main():
    bot1 = RPS_Player()
    bot2 = RPS_Player()

    # take turn
    for i in range(1000000):
        a1 = bot1.take_turn()
        a2 = bot2.take_turn()
        bot1.counterfactual_reward(a1, a2)

    print(bot1.regrets)
    
if __name__ == "__main__":
    main()
