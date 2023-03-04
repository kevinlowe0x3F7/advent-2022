import re

def day5():
    crates = [
        ["B", "V", "S", "N", "T", "C", "H", "Q"],
        ["W", "D", "B", "G"],
        ["F", "W", "R", "T", "S", "Q", "B"],
        ["L", "G", "W", "S", "Z", "J", "D", "N"],
        ["M", "P", "D", "V", "F"],
        ["F", "W", "J"],
        ["L", "N", "Q", "B", "J", "V"],
        ["G", "T", "R", "C", "J", "Q", "S", "N"],
        ["J", "S", "Q", "C", "W", "D", "M"]
    ]

    instructions = []
    with (open('./day5moves.txt')) as f:
        for line in f.readlines():
            stripped_line = line.rstrip()
            result = re.search("^move (\\d+) from (\\d+) to (\\d+)$", stripped_line)
            groups = result.groups();
            instructions.append((int(groups[0]), int(groups[1]), int(groups[2])))

    for instruction in instructions:
        num_moves = instruction[0]
        source_crate = crates[instruction_to_crate_index(instruction[1])]
        dest_crate = crates[instruction_to_crate_index(instruction[2])]
        boxes_to_add = []
        for _ in range(num_moves):
            boxes_to_add.insert(0, source_crate.pop())
        dest_crate.extend(boxes_to_add)

    top_boxes = ""
    for crate in crates:
        top_boxes += crate[-1]

    print(top_boxes)





def instruction_to_crate_index(instruction):
    return instruction - 1


if __name__ == '__main__':
    day5()
