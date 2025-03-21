import re

pattern = re.compile(r"p=(\d+),(\d+)\sv=([-\d]+),([-\d]+)")

def create_grid():
    width = 101
    height = 103

    grid = []
    for _ in range(height):
        row = []
        for _ in range(width):
            row.append('.')
        grid.append(row)

    return grid

def print_grid(grid):
    print()
    for row in grid:
        for char in row:
            print(char, end='')
        print()

def put_robots_on_grid(robots, grid):
    for robot in robots:
        x = robot[0] % len(grid)
        y = robot[1] % len(grid[0])
        if grid[x][y] == '.':
            grid[x][y] = 1
        else:
            grid[x][y] += 1

def move_robots(robots):
    moved_robots = []
    for robot in robots:
        moved_robots.append(move_robot(robot))

    return moved_robots

def move_robot(robot):
    return robot[0] + robot[2], robot[1] + robot[3], robot[2], robot[3]

def count_numbers(quadrant):
    total = 0
    for row in quadrant:
        total += sum(num for num in row if num != '.')
    return total


def is_xmas_tree(grid):
    previous = 0
    for row in grid:
        count = 0
        for char in row:
            if char != '.':
                count += 1
        if count < previous:
            return False
        else:
            previous = count

    return True

if __name__ == '__main__':
    robots = []
    with open("input/14.txt") as file:
        for line in file.readlines():
            # p=0,4 v=3,-3
            search = pattern.search(line)
            x = search.group(1)
            y = search.group(2)
            x_velocity = search.group(3)
            y_velocity = search.group(4)

            robots.append((int(y), int(x), int(y_velocity), int(x_velocity)))

    grid = create_grid()

    put_robots_on_grid(robots, grid)
    # print_grid(grid)

    moved_robots = robots

    i = 1
    while True:
        moved_robots = move_robots(moved_robots)
        grid = create_grid()
        put_robots_on_grid(moved_robots, grid)
        if is_xmas_tree(grid):
            print_grid(grid)
            print("{} second".format(i))
            break
        i += 1
