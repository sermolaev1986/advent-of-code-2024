def print_grid(grid):
    print()

    for row in grid:
        for char in row:
            print(char, end='')
        print()

    print()


def get_robot(grid):
    for row_index in range(len(grid)):
        row = grid[row_index]
        for column_index in range(len(row)):
            char = row[column_index]
            if char == '@':
                return row_index, column_index


def transform_grid(grid):
    new_grid = []
    for row in grid:
        new_row = []
        for char in row:
            if char in ['.', '#']:
                new_row.append(char)
                new_row.append(char)
            elif char == 'O':
                new_row.append('[')
                new_row.append(']')
            elif char == '@':
                new_row.append('@')
                new_row.append('.')
        new_grid.append(new_row)

    return new_grid


def get_input():
    grid = []
    instructions = []

    with open("input/15.txt") as file:
        lines = file.readlines()

    is_instruction = False

    for row_index in range(len(lines)):
        line = lines[row_index].strip()
        if len(line) == 0:
            is_instruction = True
            continue

        if is_instruction:
            for char in line:
                instructions.append(char)
            continue
        else:
            row = []
            for column_index in range(len(line)):
                char = line[column_index]
                row.append(char)
            grid.append(row)

    return grid, instructions


def move(grid, row, column, row_diff, column_diff):
    char = grid[row][column]

    grid[row - row_diff][column - column_diff] = '.'
    grid[row][column] = '@'

    do_move(grid, row + row_diff, column + column_diff, row_diff, column_diff, [char])

    if row_diff != 0:
        if char == '[':
            grid[row][column + 1] = '.'
            do_move(grid, row + row_diff, column + 1 + column_diff, row_diff, column_diff, [']'])
        elif char == ']':
            grid[row][column - 1] = '.'
            do_move(grid, row + row_diff, column - 1 + column_diff, row_diff, column_diff, ['['])


def do_move(grid, row, column, row_diff, column_diff, stack):
    if not stack:
        return

    char = grid[row][column]
    if char == '#':
        print("Can't move any further, current stack ", stack)
        return

    grid[row][column] = stack.pop()

    if char in ['[', ']']:
        stack.append(char)

    do_move(grid, row + row_diff, column + column_diff, row_diff, column_diff, stack)

    if row_diff != 0:
        if char == '[':
            grid[row][column + 1] = '.'
            do_move(grid, row + row_diff, column + 1 + column_diff, row_diff, column_diff, [']'])
        elif char == ']':
            grid[row][column - 1] = '.'
            do_move(grid, row + row_diff, column - 1 + column_diff, row_diff, column_diff, ['['])


def can_move(grid, row, column, row_diff, column_diff):
    char = grid[row][column]
    if char == '#':
        return False
    if char == '.':
        return True

    if row_diff == 0:
        return can_move(grid, row + row_diff, column + column_diff, row_diff, column_diff)
    elif char == '[':
        return can_move(grid, row + row_diff, column + column_diff, row_diff, column_diff) and can_move(grid, row + row_diff, column + 1 + column_diff, row_diff, column_diff)
    elif char == ']':
        return can_move(grid, row + row_diff, column + column_diff, row_diff, column_diff) and can_move(grid, row + row_diff, column - 1 + column_diff, row_diff, column_diff)


if __name__ == '__main__':
    grid, instructions = get_input()
    # print_grid(grid)
    grid = transform_grid(grid)
    # print_grid(grid)
    # print(instructions)

    robot_row, robot_column = get_robot(grid)

    symbol_to_diff = {'<': (0, -1), '>': (0, 1), '^': (-1, 0), 'v': (1, 0)}
    for instruction in instructions:
        row_diff, column_diff = symbol_to_diff[instruction]
        new_row = robot_row + row_diff
        new_column = robot_column + column_diff
        if grid[new_row][new_column] == '.':
            grid[robot_row][robot_column] = '.'
            grid[new_row][new_column] = '@'
            robot_row = new_row
            robot_column = new_column
        elif grid[new_row][new_column] in ['[', ']']:
            if can_move(grid, new_row, new_column, row_diff, column_diff):
                move(grid, new_row, new_column, row_diff, column_diff)
                robot_row = new_row
                robot_column = new_column

        # print("Move {}:".format(instruction))
        # print_grid(grid)

    # print_grid(grid)

    result = 0
    for row_index in range(len(grid)):
        row = grid[row_index]
        for column_index in range(len(row)):
            char = row[column_index]
            if char == '[':
                result += row_index * 100 + column_index

    print(result)
