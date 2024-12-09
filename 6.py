from enum import IntEnum


def get_grid(file_name):
    grid = []
    with open(file_name) as file:
        lines = file.readlines()

    guard_position = None
    for row_index in range(len(lines)):
        line = lines[row_index]
        line = line.replace("\n", "")
        row = []
        for column_index in range(len(line)):
            char = line[column_index]
            if char == '^':
                guard_position = (row_index, column_index)
                print("guard position: {}".format(guard_position))
            row.append(char)
        grid.append(row)

    return grid, guard_position

class Direction(IntEnum):
    UP = 0
    RIGHT = 1
    DOWN = 2
    LEFT = 3

def calculate_next_position(guard_position, direction):
    next_position = None
    if direction == Direction.UP:
        next_position = (guard_position[0] - 1, guard_position[1])
    elif direction == Direction.DOWN:
        next_position = (guard_position[0] + 1, guard_position[1])
    elif direction == Direction.LEFT:
        next_position = (guard_position[0], guard_position[1] - 1)
    elif direction == Direction.RIGHT:
        next_position = (guard_position[0], guard_position[1] + 1)

    return next_position

def calculate_previous_position(next_position, direction):
    previous_position = None
    if direction == Direction.UP:
        previous_position = (next_position[0] + 1, next_position[1])
    elif direction == Direction.DOWN:
        previous_position = (next_position[0] - 1, next_position[1])
    elif direction == Direction.LEFT:
        previous_position = (next_position[0], next_position[1] + 1)
    elif direction == Direction.RIGHT:
        previous_position = (next_position[0], next_position[1] - 1)

    return previous_position

def print_grid(grid):
    for row in grid:
        for char in row:
            print(char, end="")
        print()

def mark_x(position, grid):
    grid[position[0]][position[1]] = 'X'


def task1(file_name):
    grid, position = get_grid(file_name)
    direction = Direction.UP
    next_position = calculate_next_position(position, direction)
    mark_x(position, grid)

    while 0 <= next_position[0] < len(grid) and 0 <= next_position[1] < len(grid[0]):
        if grid[next_position[0]][next_position[1]] == "#":
            # obstacle
            direction = Direction((int(direction) + 1) % 4)
        else:
            position = next_position

        mark_x(position, grid)

        next_position = calculate_next_position(position, direction)

    # print_grid(grid)

    result = 0
    for row in grid:
        for char in row:
            if char == 'X':
                result += 1
    print("RESULT: {}".format(result))

def mark_direction(position, grid, direction):
    if grid[position[0]][position[1]] == '.':
        grid[position[0]][position[1]] = int(direction)


def make_obstacle(position, grid):
    grid[position[0]][position[1]] = '#'

def remove_obstacle(position, grid, direction):
    grid[position[0]][position[1]] = direction

def is_loop_detected(grid, position, direction):
    visited_count = {}

    result = False
    next_position = position
    position = calculate_previous_position(position, direction)
    make_obstacle(next_position, grid)

    print("printing grid with obstacle on {} and direction {}".format(next_position, direction))
    # print_grid(grid)

    original_position = next_position
    original_direction = direction

    while 0 <= next_position[0] < len(grid) and 0 <= next_position[1] < len(grid[0]):
        if next_position in visited_count:
            if visited_count[next_position] > 5:
                print("loop detected")
                result = True
                break
            else:
                visited_count[next_position] += 1
        else:
            visited_count[next_position] = 1

        if grid[next_position[0]][next_position[1]] == "#":
            direction = Direction((int(direction) + 1) % 4)
        else:
            position = next_position

        if grid[next_position[0]][next_position[1]] in [".", "|", "-"]:
            if direction in [Direction.UP , Direction.DOWN]:
                if grid[next_position[0]][next_position[1]] == '.':
                    grid[next_position[0]][next_position[1]] = '|'
                elif grid[next_position[0]][next_position[1]] == '-':
                    grid[next_position[0]][next_position[1]] = '+'
            elif direction in [Direction.LEFT, Direction.RIGHT]:
                if grid[next_position[0]][next_position[1]] == '.':
                    grid[next_position[0]][next_position[1]] = '-'
                elif grid[next_position[0]][next_position[1]] == '|':
                    grid[next_position[0]][next_position[1]] = '+'
        # mark_x(position, grid)

        next_position = calculate_next_position(position, direction)

    print("printing path with obstacle on {} and result {}".format(original_position, result))
    # print_grid(grid)

    remove_obstacle(original_position, grid, original_direction)

    return result

def task2(file_name):
    grid, position = get_grid(file_name)
    direction = Direction.UP
    next_position = calculate_next_position(position, direction)
    mark_direction(position, grid, direction)

    while 0 <= next_position[0] < len(grid) and 0 <= next_position[1] < len(grid[0]):
        if grid[next_position[0]][next_position[1]] == "#":
            # obstacle
            direction = Direction((int(direction) + 1) % 4)
        else:
            position = next_position

        mark_direction(position, grid, direction)

        next_position = calculate_next_position(position, direction)

    # print_grid(grid)

    potential_obstacles = []
    for row in range(len(grid)):
        for column in range(len(grid[0])):
            char = grid[row][column]
            if char in [0, 1, 2, 3]:
                potential_obstacles.append((row,column,char))

    result = 0
    # grid, position = get_grid(file_name)
    # is_loop_detected(grid, (7, 6), Direction.DOWN)

    for potential_obstacle in potential_obstacles:
        grid, position = get_grid(file_name)
        if is_loop_detected(grid, (potential_obstacle[0], potential_obstacle[1]), potential_obstacle[2]):
            result += 1

    print("RESULT: {}".format(result))


if __name__ == '__main__':
    # print("-----TASK 1-------")
    #
    # print("test set")
    # task1("input/6_test.txt")
    #
    # print()
    #
    # print("real set")
    # task1("input/6.txt")
    #
    print("-----TASK 2-------")

    print("test set")
    task2("input/6_test.txt")

    print()

    print("real set")
    task2("input/6.txt")
