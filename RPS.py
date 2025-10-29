import random

def player(prev_play, opponent_history=[]):
    if prev_play:
        opponent_history.append(prev_play)

    guess = "R"  # Default first move

    if len(opponent_history) > 3:
        # Look for patterns in the last 3 moves
        last3 = "".join(opponent_history[-3:])
        possible_patterns = {}

        for i in range(len(opponent_history) - 3):
            pattern = "".join(opponent_history[i:i+3])
            next_move = opponent_history[i+3] if i+3 < len(opponent_history) else None
            if pattern not in possible_patterns:
                possible_patterns[pattern] = {"R": 0, "P": 0, "S": 0}
            if next_move:
                possible_patterns[pattern][next_move] += 1

        if last3 in possible_patterns:
            prediction = max(possible_patterns[last3], key=possible_patterns[last3].get)
        else:
            prediction = random.choice(["R", "P", "S"])
    else:
        prediction = random.choice(["R", "P", "S"])

    # Choose the move that beats the predicted move
    counter_moves = {"R": "P", "P": "S", "S": "R"}
    guess = counter_moves[prediction]

    return guess
