import re

def day15():
    manhattans = dict()
    beacons = set()
    with (open('./day15.txt')) as f:
        for line in f.readlines():
            result = re.search("^Sensor at x=(\-?\d+), y=(\-?\d+): closest beacon is at x=(\-?\d+), y=(\-?\d+)", line.rstrip())
            sensor = (int(result.group(1)), int(result.group(2)))
            beacon = (int(result.group(3)), int(result.group(4)))
            manhattans[sensor] = manhattan(sensor, beacon)
            beacons.add(beacon)

    possible_locs = set()
    """
    target_y = 2000000
    for x in range(int(-5e6), int(5e6)):
        should_process_sensor = True
        for sensor in manhattans:
            test_point = (x, target_y)
            test_manhattan = manhattan(sensor, test_point)
            if test_manhattan <= manhattans[sensor]:
                should_process_sensor = False
                break
        if not should_process_sensor:
            if (x, target_y) not in beacons:
                possible_locs += 1
    """

    for x in range(0, 4000001):
        for y in range(0, 4000001):
            should_process_sensor = True
            for sensor in manhattans:
                test_point = (x, y)
                test_manhattan = manhattan(sensor, test_point)
                if test_manhattan <= manhattans[sensor]:
                    should_process_sensor = False
                    break
            if not should_process_sensor:
                if (x, y) not in beacons:
                    possible_locs.add((x, y))

    for x in range(0, 4000000):
        for y in range(0, 4000000):
            if (x, y) not in beacons and (x, y) not in possible_locs:
                print("found distress signal at {}".format((x, y)))
                print(x * 4000000 + y)


def manhattan(point1, point2):
    return abs(point1[0] - point2[0]) + abs(point1[1] - point2[1])


if __name__ == '__main__':
    day15()
