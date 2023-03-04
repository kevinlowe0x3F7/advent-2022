def day6():
    with (open('./day6.txt')) as f:
        for line in f.readlines():
            signal = line.rstrip()

    """ Part 1
    i = 0
    buffer = []
    while i < len(signal):
        buffer.append(signal[i])
        if len(buffer) > 4:
            buffer = buffer[1:]
        if all_chars_different(buffer) and len(buffer) == 4:
            print(i + 1)
            break
        i += 1
    """
    i = 0
    buffer = []
    while i < len(signal):
        buffer.append(signal[i])
        if len(buffer) > 14:
            buffer = buffer[1:]
        if all_chars_different(buffer) and len(buffer) == 14:
            print(i + 1)
            break
        i += 1


def all_chars_different(chars):
    return len(set(chars)) == len(chars)


if __name__ == '__main__':
    day6()
