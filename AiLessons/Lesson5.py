'''
1. Add on to Lesson 3

2. A regret_table for [] with regrest for "study" and "party"
3. A function regret_matching(regret_table, info_set) that:
    * Uses positive regrets to build a strategy
    * Returns a probability distribution over actions
'''

# Set of all histories
H = [
    [],  # h0
    ["study"],  # h1
    ["party"],  # h2
    ["study", "A"],  # h3
    ["study", "B"],  # h4
    ["party", "pass"],  # h5
    ["party", "fail"],  # h6
]

# Terminal histories (no actions after these)
Z = [
    ("study", "A"),
    ("study", "B"),
    ("party", "pass"),
    ("party", "fail"),
]

I = [
    [], # Skip player 0 (doesn't exist)
    [[]], # Player 1 (no information set; root)
    [   # Player 2
        [["study", "A"], ["party", "pass"]], #Look the same to Player 2
        [["study", "B"], ["party", "fail"]]
    ] 
]

strategy_player1 = {
    (): { # Player 1's information set is root ([]) --> empty
        "study": 0.6, # Player 1 studies 60% 
        "party":0.4 # Player 1 parties 40%
    }
}

chance_strategy = {
    ("study"):{ # Player 1 chose to study
        "A": 0.5,
        "B": 0.5
    },
    ("party"):{ # Player 1 chose to party
        "pass": 0.3,
        "fail": 0.7
    }
}

U = {
    ("study", "A"): 10,
    ("study", "B"): 4,
    ("party", "pass"): 7,
    ("party", "fail"): -3
}

regret_table = {
    (): {
        "study": 22,
        "party": 3
    }
}

def expected_value(p1_strat, c_strat, U):
    expected_value = 0
    for terminal_hist in Z:
       probability = p1_strat[()][terminal_hist[0]] * chance_strategy[terminal_hist[0]][terminal_hist[1]]
       expected_value += U[terminal_hist] * probability # Reward * Probability of getting reward given strategy

    return expected_value
        
def get_info_set(player, history):
    for info_set in I[player]:
        if history in info_set:
            return info_set
        
    return None # history not in players info set


def A(h):
    if h == []:
        return ["study", "party"]
    elif h == ["study"]:
        return ["A", "B"]
    elif h == ["party"]:
        return ["pass", "fail"]
    else:
        return None
    

def P(h):
    if h == []:
        return "Player 1"
    elif h in [["study"],["party"]]:
        return "Chance"
    else:
        return None

# input: regret table, and information set
# output: distribution of actions for that information set (strategy for I)
def regret_matching(regret_table, info_set):
    rand_proportion = 1/len(regret_table[info_set].keys())
    updated_strat = { action: rand_proportion for action in regret_table[info_set]} # assign even proportion to each key in regret_table[I] {'study': 0.5, 'party': 0.5}

    regret_sum = sum(max(0,regret) for action,regret in regret_table[info_set].items()) # sum all of the POSITIVE regrets
    if regret_sum > 0:
        for action, regret in regret_table[info_set].items():
            updated_strat[action] = max(0,regret)/regret_sum # update the strategy based on the proportion of regret (IF POSITIVE)


    return updated_strat
    
# Optional: Print out tree
def print_game_tree():
    for h in H:
        print(f"History: {h} | Player to act: {P(h)} | Available actions: {A(h)}")

def main():
    expected_u = expected_value(strategy_player1, chance_strategy, U)
    
    print(regret_matching(regret_table, ()))
    '''print_game_tree()
    print("\nTesting info set lookup:")
    test_histories = [["study", "A"], ["party", "fail"], ["study", "B"], ["party", "pass"]]
    for h in test_histories:
        info = get_info_set(2, h)
        print(f"History {h} is in info set: {info}")'''


if __name__ == "__main__":
    main()