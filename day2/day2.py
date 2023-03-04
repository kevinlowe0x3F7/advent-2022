def day2():
    pairs = []
    with (open('./day2.txt')) as f:
        for line in f.readlines():
            round = line.rstrip().split(' ')
            pairs.append((round[0], round[1]))
    total_score = 0
    for round in pairs:
        score, shape_played = score_and_shape_played(round)
        total_score += score + own_shape_score(shape_played)
    print(total_score)


def round_score(round):
    opponent_played = round[0]
    self_played = round[1]
    if opponent_played == 'A' and self_played == 'X':  # Rock Rock
        return 3
    elif opponent_played == 'A' and self_played == 'Y':  # Rock Paper
        return 6
    elif opponent_played == 'A' and self_played == 'Z':  # Rock Scissors
        return 0
    elif opponent_played == 'B' and self_played == 'X':  # Paper Rock
        return 0
    elif opponent_played == 'B' and self_played == 'Y':  # Paper Paper
        return 3
    elif opponent_played == 'B' and self_played == 'Z':  # Paper Scissors
        return 6
    elif opponent_played == 'C' and self_played == 'X':  # Scissors Rock
        return 6
    elif opponent_played == 'C' and self_played == 'Y':  # Scissors Paper
        return 0
    elif opponent_played == 'C' and self_played == 'Z':  # Scissors Scissors
        return 3
    return 0

def score_and_shape_played(round):
    opponent_played = round[0]
    outcome = round[1]
    if opponent_played == 'A' and outcome == 'X':  # Rock Lose -> Scissors
        return 0, 'Z'
    elif opponent_played == 'A' and outcome == 'Y':  # Rock Draw -> Rock
        return 3, 'X'
    elif opponent_played == 'A' and outcome == 'Z':  # Rock Win -> Paper
        return 6, 'Y'
    elif opponent_played == 'B' and outcome == 'X':  # Paper Lose -> Rock
        return 0, 'X'
    elif opponent_played == 'B' and outcome == 'Y':  # Paper Draw -> Paper
        return 3, 'Y'
    elif opponent_played == 'B' and outcome == 'Z':  # Paper Win -> Scissors
        return 6, 'Z'
    elif opponent_played == 'C' and outcome == 'X':  # Scissors Lose -> Paper
        return 0, 'Y'
    elif opponent_played == 'C' and outcome == 'Y':  # Scissors Draw -> Scissors
        return 3, 'Z'
    elif opponent_played == 'C' and outcome == 'Z':  # Scissors Win -> Rock
        return 6, 'X'
    return 0


def own_shape_score(played):
    if played == 'X':
        return 1
    elif played == 'Y':
        return 2
    elif played == 'Z':
        return 3
    return 0


if __name__ == '__main__':
    day2()