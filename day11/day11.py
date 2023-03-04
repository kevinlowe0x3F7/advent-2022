def day11():
    monkeys = dict()
    monkeys[0] = Monkey([85, 77, 77], lambda old: old * 7, 19, 6, 7)
    monkeys[1] = Monkey([80, 99], lambda old: old * 11, 3, 3, 5)
    monkeys[2] = Monkey([74, 60, 74, 63, 86, 92, 80], lambda old: old + 8, 13, 0, 6)
    monkeys[3] = Monkey([71, 58, 93, 65, 80, 68, 54, 71], lambda old: old + 7, 7, 2, 4)
    monkeys[4] = Monkey([97, 56, 79, 65, 58], lambda old: old + 5, 5, 2, 0)
    monkeys[5] = Monkey([77], lambda old: old + 4, 11, 4, 3)
    monkeys[6] = Monkey([99, 90, 84, 50], lambda old: old * old, 17, 7, 1)
    monkeys[7] = Monkey([50, 66, 61, 92, 64, 78], lambda old: old + 3, 2, 5, 1)
    """
    monkeys[0] = Monkey([79, 98], lambda old: old * 19, 23, 2, 3)
    monkeys[1] = Monkey([54, 65, 75, 74], lambda old: old + 6, 19, 2, 0)
    monkeys[2] = Monkey([79, 60, 97], lambda old: old * old, 13, 1, 3)
    monkeys[3] = Monkey([74], lambda old: old + 3, 17, 0, 1)
    """

    modulus = 1
    for monkey_idx in range(0, len(monkeys)):
        modulus *= monkeys[monkey_idx].divisible

    for round in range(0, 10000):
        for monkey_idx in range(0, len(monkeys)):
            monkey = monkeys[monkey_idx]
            while len(monkey.items) > 0:
                item = monkey.items.pop(0)
                monkey.inspections = monkey.inspections + 1
                worry_level = monkey.operation(item)
                worry_level = worry_level % modulus
                if worry_level % monkey.divisible == 0:
                    monkeys[monkey.throw_if_true].items.append(worry_level)
                else:
                    monkeys[monkey.throw_if_false].items.append(worry_level)

    inspections = []
    for monkey_idx in range(0, len(monkeys)):
        print("monkey {}: {}, inspections: {}".format(monkey_idx, monkeys[monkey_idx].items, monkeys[monkey_idx].inspections))
        inspections.append(monkeys[monkey_idx].inspections)

    inspections.sort()
    print(inspections)
    print(inspections[-1] * inspections[-2])

class Monkey:
    def __init__(self, items, operation, divisible, throw_if_true, throw_if_false):
        self.items = items
        self.operation = operation
        self.divisible = divisible
        self.throw_if_true = throw_if_true
        self.throw_if_false = throw_if_false
        self.inspections = 0


if __name__ == '__main__':
    day11()
