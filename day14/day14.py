def day14():
    rocks = set()
    min_x = float("inf")
    max_x = 0
    min_y = float("inf")
    max_y = 0
    rested_sand = set()
    with (open('./day14.txt')) as f:
        for line in f.readlines():
            coordinates = [split_line.strip().split(",") for split_line in line.rstrip().split("->")]
            coordinates_tup = [(int(coord[0]), int(coord[1])) for coord in coordinates]
            for coordinate in coordinates_tup:
                min_x = min(min_x, coordinate[0])
                max_x = max(max_x, coordinate[0])
                min_y = min(min_y, coordinate[1])
                max_y = max(max_y, coordinate[1])
            rocks_for_coord = all_rocks(coordinates_tup)
            for rock in rocks_for_coord:
                rocks.add(rock)
    print("max_y: {}".format(max_y))
    abyss_y = max_y + 3
    floor_y = max_y + 2
    rocks = rocks.union([(x, floor_y) for x in range(min_x - 1000, max_x + 1000)])

    while True:
        sand_pos = (500, 0)
        new_sand_pos = drop_sand(sand_pos, rocks, rested_sand, abyss_y)
        if new_sand_pos[1] == abyss_y:
            print("hit the abyss, not valid for part 2: {}".format(new_sand_pos))
            break
        elif new_sand_pos == (500, 0):
            print("part 2 done")
            break
        rested_sand.add(new_sand_pos)

    for y in range(min(min_y, 0), max_y + 1):
        line = ""
        for x in range(min_x, max_x + 1):
            if (x, y) in rocks:
                line += "#"
            elif (x, y) in rested_sand:
                line += "s"
            else:
                line += "."
        print(line)
    print(len(rested_sand))


def drop_sand(sand_pos, rocks, rested_sand, abyss_y):
    curr_sand_pos = (sand_pos[0], sand_pos[1])
    while curr_sand_pos[1] != abyss_y:
        next_sand_pos = (curr_sand_pos[0], curr_sand_pos[1] + 1)
        if next_sand_pos not in rocks and next_sand_pos not in rested_sand:
            curr_sand_pos = next_sand_pos
        else:
            left_sand_pos = (next_sand_pos[0] - 1, next_sand_pos[1])
            if left_sand_pos not in rocks and left_sand_pos not in rested_sand:
                curr_sand_pos = left_sand_pos
                continue

            right_sand_pos = (next_sand_pos[0] + 1, next_sand_pos[1])
            if right_sand_pos not in rocks and right_sand_pos not in rested_sand:
                curr_sand_pos = right_sand_pos
                continue

            break
    return curr_sand_pos


def all_rocks(coordinates):
    rock_positions = []
    index = 0
    while index < len(coordinates) - 1:
        rock_point = coordinates[index]
        rock_positions.append(rock_point)
        next_rock_point = coordinates[index + 1]
        rock_positions.extend(rock_line(rock_point, next_rock_point))
        index += 1
    rock_positions.append(coordinates[-1])
    return rock_positions


"""
Assumes either x coordinates are the same or y coordinates are the same
"""
def rock_line(rock_point_1, rock_point_2):
    line = []
    if rock_point_1[0] == rock_point_2[0]:
        larger_y = max(rock_point_1[1], rock_point_2[1])
        smaller_y = min(rock_point_1[1], rock_point_2[1]) + 1
        while smaller_y < larger_y:
            line.append((rock_point_1[0], smaller_y))
            smaller_y += 1
    else:
        larger_x = max(rock_point_1[0], rock_point_2[0])
        smaller_x = min(rock_point_1[0], rock_point_2[0]) + 1
        while smaller_x < larger_x:
            line.append((smaller_x, rock_point_1[1]))
            smaller_x += 1
    return line


if __name__ == '__main__':
    day14()
