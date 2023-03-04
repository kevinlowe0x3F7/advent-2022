def day3():
    rucksacks = []
    with (open('./day3.txt')) as f:
        for line in f.readlines():
            rucksacks.append(line.rstrip())

    elf_groups = []
    i = 0
    while i < len(rucksacks):
        elf_groups.append((rucksacks[i], rucksacks[i + 1], rucksacks[i + 2]))
        i += 3

    errors = []
    for elf_group in elf_groups:
        errors.append(find_error_in_group(elf_group))

    print(len(errors))
    print(errors)

    priorities = 0
    for error in errors:
        priorities += chr_to_priority(error)

    print(priorities)

    """
    Part 1
    split_rucksacks = []
    for rucksack in rucksacks:
        first_compartment = rucksack[0:(len(rucksack) // 2)]
        second_compartment = rucksack[len(rucksack)//2:len(rucksack)]
        split_rucksacks.append((first_compartment, second_compartment))

    errors = []
    for split_rucksack in split_rucksacks:
        errors.append(find_error(split_rucksack))

    priorities = 0
    for error in errors:
        priorities += chr_to_priority(error)

    print(priorities)
    """


def find_error(split_rucksack):
    first_compartment = split_rucksack[0]
    second_compartment = split_rucksack[1]
    for item in first_compartment:
        if item in second_compartment:
            return item

    return None


def find_error_in_group(elf_group):
    first_compartment = elf_group[0]
    second_compartment = elf_group[1]
    third_compartment = elf_group[2]
    for item in first_compartment:
        if item in second_compartment and item in third_compartment:
            return item

    return None


def chr_to_priority(chr):
    if chr in 'abcdefghijlmnopqrstuvwxyz':
        return ord(chr) - 96
    elif chr in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ':
        return ord(chr) - 38
    return 0





if __name__ == '__main__':
    day3()
