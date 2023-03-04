import json
import functools

def day13():
    all_packets = [[[2]], [[6]]]
    pairs = []
    pair = []
    with (open('./day13.txt')) as f:
        for line in f.readlines():
            if len(line.rstrip()) == 0:
                continue
            int_line = json.loads((line.rstrip()))
            all_packets.append(int_line)
            pair.append(int_line)
            if len(pair) == 2:
                pairs.append(tuple(pair))
                pair = []

    index = 1
    sum_right_order = 0
    while pairs:
        left, right = pairs.pop(0)
        result = is_right_order(left, right)
        if result != "equal" and result:
            sum_right_order += index
        index += 1
    print(sum_right_order)

    sorted_packets = sorted(all_packets, key=functools.cmp_to_key(compare))
    divider_index_1 = -1
    divider_index_2 = -1
    index = 1
    for packet in sorted_packets:
        if str(packet) == "[[2]]":
            divider_index_1 = index
        elif str(packet) == "[[6]]":
            divider_index_2 = index
        index += 1
    print(divider_index_1 * divider_index_2)


def compare(p1, p2):
    result = is_right_order(p1, p2)
    if result == "equal":
        return 0
    elif result:
        return -1
    else:
        return 1

def is_right_order(left, right):
    if len(left) == 0 and len(right) == 0:
        return "equal"
    elif len(left) == 0:
        return True
    elif len(right) == 0:
        return False

    left_value = left[0]
    right_value = right[0]
    if isinstance(left_value, int) and isinstance(right_value, int):
        if left_value < right_value:
            return True
        elif left_value > right_value:
            return False
    elif isinstance(left_value, list) and isinstance(right_value, list):
        result = is_right_order(left_value, right_value)
        if result != "equal":
            return result
    elif isinstance(left_value, list) and isinstance(right_value, int):
        result = is_right_order(left_value, [right_value])
        if result != "equal":
            return result
    elif isinstance(left_value, int) and isinstance(right_value, list):
        result = is_right_order([left_value], right_value)
        if result != "equal":
            return result
    return is_right_order(left[1:], right[1:])


if __name__ == '__main__':
    day13()
