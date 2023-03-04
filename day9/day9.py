import copy


def day9():
    rope = [(0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0)]
    seen_tail_pos = set()
    with (open('./day9.txt')) as f:
        for line in f.readlines():
            move = line.rstrip().split(" ")
            direction = move[0]
            steps = int(move[1])
            for _ in range(0, steps):
                new_rope = copy.deepcopy(rope)
                new_rope[0] = move_head(new_rope[0], direction)
                i = 1
                while i < len(new_rope):
                    new_rope[i] = move_closer(new_rope[i - 1], new_rope[i])
                    i += 1
                rope = new_rope
                seen_tail_pos.add(rope[-1])

    print(len(seen_tail_pos))


# Returns the new tail_pos
def move_closer(head_pos, tail_pos):
    # Same x coord but too far away in y
    if head_pos[0] == tail_pos[0] and abs(tail_pos[1] - head_pos[1]) >= 2:
        if tail_pos[1] > head_pos[1]:
            return tail_pos[0], tail_pos[1] - 1
        else: # tail_pos[1] < head_pos[1]
            return tail_pos[0], tail_pos[1] + 1
    elif head_pos[1] == tail_pos[1] and abs(tail_pos[0] - head_pos[0]) >= 2:
        if tail_pos[0] > head_pos[0]:
            return tail_pos[0] - 1, tail_pos[1]
        else:  # tail_pos[0] < head_pos[0]
            return tail_pos[0] + 1, tail_pos[1]
    elif 1 <= abs(head_pos[0] - tail_pos[0]) <= 2 and abs(tail_pos[1] - head_pos[1]) >= 2:
        if tail_pos[0] < head_pos[0] and tail_pos[1] > head_pos[1]:
            return tail_pos[0] + 1, tail_pos[1] - 1
        elif tail_pos[0] < head_pos[0] and tail_pos[1] < head_pos[1]:
            return tail_pos[0] + 1, tail_pos[1] + 1
        elif tail_pos[0] > head_pos[0] and tail_pos[1] > head_pos[1]:
            return tail_pos[0] - 1, tail_pos[1] - 1
        else:
            return tail_pos[0] - 1, tail_pos[1] + 1
    elif 1 <= abs(head_pos[1] - tail_pos[1]) <= 2 and abs(tail_pos[0] - head_pos[0]) >= 2:
        if tail_pos[0] < head_pos[0] and tail_pos[1] > head_pos[1]:
            return tail_pos[0] + 1, tail_pos[1] - 1
        elif tail_pos[0] < head_pos[0] and tail_pos[1] < head_pos[1]:
            return tail_pos[0] + 1, tail_pos[1] + 1
        elif tail_pos[0] > head_pos[0] and tail_pos[1] > head_pos[1]:
            return tail_pos[0] - 1, tail_pos[1] - 1
        else:
            return tail_pos[0] - 1, tail_pos[1] + 1
    else:
        return tail_pos


def move_head(pos, direction):
    if direction == "U":
        return pos[0], pos[1] + 1
    elif direction == "D":
        return pos[0], pos[1] - 1
    elif direction == "R":
        return pos[0] + 1, pos[1]
    elif direction == "L":
        return pos[0] - 1, pos[1]
    else:
        print("Unknown dir: {}".format(direction))
        return pos

"""
print(move_closer((2, 0), (0, 0)))
print(move_closer((-2, 0), (0, 0)))
print(move_closer((0, 2), (0, 0)))
print(move_closer((0, -2), (0, 0)))
print(move_closer((1, 0), (0, 0)))
print(move_closer((-1, 0), (0, 0)))
print(move_closer((0, 1), (0, 0)))
print(move_closer((0, -1), (0, 0)))
print(move_closer((1, 2), (0, 0))) # (1, 1)
print(move_closer((1, -2), (0, 0))) # (1, -1)
print(move_closer((-1, 2), (0, 0))) # (-1, 1)
print(move_closer((-1, -2), (0, 0))) # (-1, -1)
print(move_closer((2, 1), (0, 0))) # (1, 1)
print(move_closer((2, -1), (0, 0))) # (1, -1)
print(move_closer((-2, 1), (0, 0))) # (-1, 1)
print(move_closer((-2, -1), (0, 0))) # (-1, -1)
"""


if __name__ == '__main__':
    day9()