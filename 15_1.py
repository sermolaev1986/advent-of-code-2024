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
    boxes = 1
    while boxes > 0:
        char = grid[row][column]
        if char == '.':
            grid[row][column] = 'O'
            boxes -= 1
        row += row_diff
        column += column_diff


def can_move(grid, row, column, row_diff, column_diff):
    while True:
        if grid[row][column] == '#':
            return False
        if grid[row][column] == '.':
            return True
        row += row_diff
        column += column_diff


if __name__ == '__main__':
    grid, instructions = get_input()
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
        elif grid[new_row][new_column] == 'O':
            if can_move(grid, new_row, new_column, row_diff, column_diff):
                grid[robot_row][robot_column] = '.'
                grid[new_row][new_column] = '@'
                move(grid, new_row + row_diff, new_column + column_diff, row_diff, column_diff)
                robot_row = new_row
                robot_column = new_column

    result = 0
    for row_index in range(len(grid)):
        row = grid[row_index]
        for column_index in range(len(row)):
            char = row[column_index]
            if char == 'O':
                result += row_index * 100 + column_index

    print(result)


