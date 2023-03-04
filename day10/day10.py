def day10():
    cycle = 0
    x = 1
    strengths = 0
    tv = [['.' for _ in range(0, 40)] for _ in range(0, 6)]
    with (open('./day10.txt')) as f:
        for line in f.readlines():
            commands = line.rstrip().split(" ")
            draw_pixel(tv, cycle, x)
            if commands[0] == "noop":
                cycle += 1
            else:
                cycle += 1
                strengths += get_relevant_strengths(cycle, x)
                draw_pixel(tv, cycle, x)
                x += int(commands[1])
                cycle += 1
    print(strengths)
    for row in tv:
        print("".join(row))


def draw_pixel(tv, cycle, x):
    if x - 1 <= cycle % 40 <= x + 1:
        tv[cycle // 40][cycle % 40] = "#"


def get_relevant_strengths(cycle, x):
    if cycle != 20 and cycle != 60 and cycle != 100 and cycle != 140 and cycle != 180 and cycle != 220:
        return 0
    return cycle * x


if __name__ == '__main__':
    day10()
