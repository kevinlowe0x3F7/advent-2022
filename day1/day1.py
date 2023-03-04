def day1():
    elves = []
    current_calories = []
    with (open('./day1.txt')) as f:
        for line in f.readlines():
            stripped_line = line.rstrip()
            if stripped_line == "":
                elves.append(current_calories)
                current_calories = []
            else:
                current_calories.append(int(stripped_line))

    if len(current_calories) > 0:
        elves.append(current_calories)

    summed_elves = []
    for elf in elves:
        summed_elves.append(sum(elf))

    summed_elves.sort(reverse=True)

    print(summed_elves[0] + summed_elves[1] + summed_elves[2])


if __name__ == '__main__':
    day1()
