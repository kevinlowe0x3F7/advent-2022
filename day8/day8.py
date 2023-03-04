def day8():
    tree_heights = dict()
    row = 0
    num_cols = 0

    with (open('./day8.txt')) as f:
        for line in f.readlines():
            tree_height_line = line.rstrip()
            num_cols = len(tree_height_line)
            col = 0
            for height in tree_height_line:
                tree_heights[(row, col)] = int(height)
                col += 1
            row += 1
    num_rows = row
    print(tree_heights)
    visible = 0
    r = 0
    max_scenic_score = 0
    while r < num_rows:
        c = 0
        while c < num_cols:
            tree_coord = (r, c)
            if r == 0 or c == 0 or r == num_rows - 1 or c == num_cols - 1:
                visible += 1
            elif is_visible(tree_coord, tree_heights[tree_coord], tree_heights, num_rows, num_cols):
                visible += 1

            score = scenic_score(tree_coord, tree_heights[tree_coord], tree_heights, num_rows, num_cols)
            max_scenic_score = max(max_scenic_score, score)
            c += 1
        r += 1

    print(visible)
    print(max_scenic_score)


def is_visible(tree_coord, tree_height, tree_heights, num_rows, num_cols):
    return is_visible_from_top(tree_coord, tree_height, tree_heights) or is_visible_from_bottom(tree_coord, tree_height, tree_heights, num_rows) or is_visible_from_left(tree_coord, tree_height, tree_heights) or is_visible_from_right(tree_coord, tree_height, tree_heights, num_cols)


def is_visible_from_top(tree_coord, tree_height, tree_heights):
    check_row = tree_coord[0] - 1
    while check_row >= 0:
        if tree_heights[(check_row, tree_coord[1])] >= tree_height:
            return False
        check_row -= 1
    return True


def is_visible_from_bottom(tree_coord, tree_height, tree_heights, num_rows):
    check_row = tree_coord[0] + 1
    while check_row < num_rows:
        if tree_heights[(check_row, tree_coord[1])] >= tree_height:
            return False
        check_row += 1
    return True


def is_visible_from_left(tree_coord, tree_height, tree_heights):
    check_col = tree_coord[1] - 1
    while check_col >= 0:
        if tree_heights[(tree_coord[0], check_col)] >= tree_height:
            return False
        check_col -= 1
    return True


def is_visible_from_right(tree_coord, tree_height, tree_heights, num_cols):
    check_col = tree_coord[1] + 1
    while check_col < num_cols:
        if tree_heights[(tree_coord[0], check_col)] >= tree_height:
            return False
        check_col += 1
    return True


def scenic_score(tree_coord, tree_height, tree_heights, num_rows, num_cols):
    return viewing_score_top(tree_coord, tree_height, tree_heights) * viewing_score_bottom(tree_coord, tree_height, tree_heights, num_rows) * viewing_score_left(tree_coord, tree_height, tree_heights) * viewing_score_right(tree_coord, tree_height, tree_heights, num_cols)


def viewing_score_top(tree_coord, tree_height, tree_heights):
    check_row = tree_coord[0] - 1
    tree_count = 0
    while check_row >= 0:
        tree_count += 1
        if tree_heights[(check_row, tree_coord[1])] >= tree_height:
            break
        check_row -= 1
    return tree_count


def viewing_score_bottom(tree_coord, tree_height, tree_heights, num_rows):
    check_row = tree_coord[0] + 1
    tree_count = 0
    while check_row < num_rows:
        tree_count += 1
        if tree_heights[(check_row, tree_coord[1])] >= tree_height:
            break
        check_row += 1
    return tree_count


def viewing_score_left(tree_coord, tree_height, tree_heights):
    check_col = tree_coord[1] - 1
    tree_count = 0
    while check_col >= 0:
        tree_count += 1
        if tree_heights[(tree_coord[0], check_col)] >= tree_height:
            break
        check_col -= 1
    return tree_count


def viewing_score_right(tree_coord, tree_height, tree_heights, num_cols):
    check_col = tree_coord[1] + 1
    tree_count = 0
    while check_col < num_cols:
        tree_count += 1
        if tree_heights[(tree_coord[0], check_col)] >= tree_height:
            break
        check_col += 1
    return tree_count


if __name__ == '__main__':
    day8()
