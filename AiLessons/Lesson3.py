''' Objective:
1. Add on to Lesson 2
2. 
    a. Define a dict "strategy_player1" mapping Player 1s information set to a probability distribution
    b. Define a dict "chance_strategy" a dictionary mapping each history to a chance outcome distribution
    c. Define "U": terminal payoffs (reward) 
    d. Create function: expected_value(strategy_player1, chance_strategy, U)
        * enumerate over each Z
        * compute the probability of history based on:
            - Player 1s choice 
            - Chances outcome 
        * Multiply by Utility
        * Sum Everything'''


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
    
# Optional: Print out tree
def print_game_tree():
    for h in H:
        print(f"History: {h} | Player to act: {P(h)} | Available actions: {A(h)}")

def main():
    expected_u = expected_value(strategy_player1, chance_strategy, U)
    print(expected_u)
    '''print_game_tree()
    print("\nTesting info set lookup:")
    test_histories = [["study", "A"], ["party", "fail"], ["study", "B"], ["party", "pass"]]
    for h in test_histories:
        info = get_info_set(2, h)
        print(f"History {h} is in info set: {info}")'''


if __name__ == "__main__":
    main()