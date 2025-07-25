'''
1. Add on to Lesson 5

2. build a run_cfr function: run_cfr(T, chance_strategy, U)
    - T: number of iterations
    - chance_strategy: strategy of chance
    - U: Utility

3. Code preparation/plan:
    - initiliaze values of regret_table and strategy_sum to 0
    - for t=1 to T
        * Get current strategy from regret_matching
        * update strategy_sum with teh current strategy 
        * compute u_mixed, u_study, u_party (mixed strategy, always choose study, always choose party)
        * update regrets
    - average strategies (after loop)

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
        "study": 0.5, # Player 1 studies 50% 
        "party":0.5 # Player 1 parties 50%
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
        "study": 0.0,
        "party": 0.0
    }
}

strategy_sum = { # All of the strategies across T added together
    "study": 0.0,
    "party": 0.0
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
    

# Run CFR on the game
def run_cfr(T, chance_strategy, U):
    regret = regret_table

    for i in range(T): # run game T times
        # Expected Values (mixed strategy vs set strategy)
        u_mixed = 0
        u_single_action = {action: 0 for action in strategy_player1[()]} # ev for fixed actions

        current_strat = strategy_player1[()] # default strategy for round 0

        # Get strategy from regret matching
        if T >= 1:
            current_strat = regret_matching(regret, ())

        for p1_action in current_strat: # each of player 1's choices
            for c_action in chance_strategy[(p1_action)]: # each choice of Chance
                u_mixed +=  current_strat[p1_action] * chance_strategy[(p1_action)][c_action] * U[(p1_action, c_action)] # mixed strat ev
                u_single_action[p1_action] += chance_strategy[(p1_action)][c_action] * U[(p1_action, c_action)] # always taken this specific action ("study", "part") ev
        
        # update regrets overtime
        regret[()]["study"] += u_single_action["study"] - u_mixed
        regret[()]["party"] += u_single_action["party"] - u_mixed

        # update strategy with regret matching
        updated_strat = regret_matching(regret, ())
        for action, strat in updated_strat.items():
            strategy_sum[action] += strat

    avg_strategy = {
        a: strategy_sum[a] / T for a in strategy_sum
    }

    return avg_strategy

        

# Optional: Print out tree
def print_game_tree():
    for h in H:
        print(f"History: {h} | Player to act: {P(h)} | Available actions: {A(h)}")

def main():
    print(run_cfr(1000, chance_strategy, U))


if __name__ == "__main__":
    main()