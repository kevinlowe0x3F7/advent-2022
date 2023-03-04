import re

def day7():
    dir_id = 0
    current_dir = Dir(dir_id, "/", None)
    dir_id += 1
    root_dir = current_dir
    with (open('./day7.txt')) as f:
        for line in f.readlines():
            stripped_line = line.rstrip()
            if re.fullmatch("^\$ ls$", stripped_line) is not None:
                continue
            elif re.fullmatch("^\$ cd \.\.$", stripped_line) is not None:
                current_dir = current_dir.parent

            result = re.search("^\$ cd ([\w+\.]+)$", stripped_line)
            if result is not None and len(result.groups()) == 1:
                child_dir_to_find = result.group(1)
                for child_dir in current_dir.child_dirs:
                    if child_dir.name == child_dir_to_find:
                        current_dir = child_dir

            result = re.search("^dir ([\w+\.]+)$", stripped_line)
            if result is not None and len(result.groups()) == 1:
                child_dir_name = result.group(1)
                current_dir.child_dirs.append(Dir(dir_id, child_dir_name, current_dir))
                dir_id += 1

            result = re.search("^(\d+) ([\w+\.]+)$", stripped_line)
            if result is not None and len(result.groups()) == 2:
                child_file_size = result.group(1)
                child_file_name = result.group(2)
                current_dir.child_files.append(File(child_file_name, child_file_size))

    dir_sizes = dict()
    root_dir_size = get_sizes(root_dir, dir_sizes)
    sum_sizes_under_limit = 0
    for size in dir_sizes.values():
        if size < 100000:
            sum_sizes_under_limit += size
    print(sum_sizes_under_limit)

    print(root_dir_size)
    unused_space = 70000000 - root_dir_size
    print(unused_space)
    minimum_dir_size = 30000000 - unused_space
    print(minimum_dir_size)
    minimum_dir_size_over_min = 30000000
    for size in dir_sizes.values():
        if size > minimum_dir_size and size < minimum_dir_size_over_min:
            minimum_dir_size_over_min = size

    print(minimum_dir_size_over_min)


def get_sizes(dir, dir_sizes):
    total_size = 0
    for child_file in dir.child_files:
        total_size += child_file.size
    for child_dir in dir.child_dirs:
        total_size += get_sizes(child_dir, dir_sizes)
    dir_sizes[dir.id] = total_size
    return total_size


class Dir:
    def __init__(self, id, name, parent):
        self.id = id
        self.name = name
        self.parent = parent
        self.child_dirs = []
        self.child_files = []

    def __str__(self):
        string = self.name + "\n"
        string += "children files for {0}\n".format(self.name)
        for child_file in self.child_files:
            string += child_file.__str__()
        string += "children directories for {0}\n".format(self.name)
        for child_dir in self.child_dirs:
            string += child_dir.__str__()
        return string

class File:
    def __init__(self, name, size):
        self.name = name
        self.size = int(size)

    def __str__(self):
        return "{0} {1}\n".format(self.name, self.size)


if __name__ == '__main__':
    day7()
