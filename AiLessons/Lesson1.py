''' Objective:
A History class or dictionary-like structure

A list H of all histories

A list Z of all terminal histories

A function A(h) that returns available actions at a given history

A function P(h) that returns the player (or "chance") who acts at h'''

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

if __name__ == "__main__":
    main()