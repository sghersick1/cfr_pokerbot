''' Objective:
1. Add on to Lesson 1
2. 
    a.Create an information_sets dictionary that maps each player to a list of sets of indistinguishable histories.
    b. Write a function get_info_set(player, history) that returns the matching info set.
    assumption:
        Only Player 2 has an information set: they must act after ["study", "A"] or ["party", "pass"] — but can’t tell which.'''

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
    ["study", "A"],
    ["study", "B"],
    ["party", "pass"],
    ["party", "fail"],
]

I = [
    [], # Skip player 0 (doesn't exist)
    [[]], # Player 1 (no information set; root)
    [   #Player 2
        [["Study", "A"], ["party", "pass"]], #Look the same to user two
        [["Study", "B"], ["party", "fail"]]
    ] 
]
        
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
    print_game_tree()
    print("\nTesting info set lookup:")
    test_histories = [["study", "A"], ["party", "fail"], ["study", "B"], ["party", "pass"]]
    for h in test_histories:
        info = get_info_set(2, h)
        print(f"History {h} is in info set: {info}")


if __name__ == "__main__":
    main()