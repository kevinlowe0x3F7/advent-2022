def day4():
    pairs = []
    with (open('./day4.txt')) as f:
        for line in f.readlines():
            stripped_line = line.rstrip()
            [range1, range2] = stripped_line.split(",")
            pairs.append((to_ints(range1.split("-")), to_ints(range2.split("-"))))

    """ Part 1
    num_contained = 0
    for pair in pairs:
        if is_contained(pair[0], pair[1]):
            num_contained += 1

    print(num_contained)
    """
    num_overlapping = 0
    for pair in pairs:
        if not is_not_overlapping(pair[0], pair[1]):
            num_overlapping += 1

    print(num_overlapping)


def to_ints(arr):
    new_arr = []
    for str in arr:
        new_arr.append(int(str))
    return new_arr


def is_contained(range1, range2):
    return (range1[0] <= range2[0] and range1[1] >= range2[1]) or (range2[0] <= range1[0] and range2[1] >= range1[1])


def is_not_overlapping(range1, range2):
    return (range1[0] < range2[0] and range1[1] < range2[0]) or (range2[0] < range1[0] and range2[1] < range1[0])


print(is_not_overlapping([14, 28], [13, 28])) # False
print(is_not_overlapping([12, 27], [13, 28])) # False
print(is_not_overlapping([6, 28], [6, 28])) # False
print(is_not_overlapping([6, 28], [6, 6])) # False
print(is_not_overlapping([6, 28], [4, 5])) # True
print(is_not_overlapping([10, 20], [98, 99])) # True


if __name__ == '__main__':
    day4()