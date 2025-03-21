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

    for i in range(100):
        print("{} second".format(i))
        moved_robots = move_robots(moved_robots)
        grid = create_grid()
        put_robots_on_grid(moved_robots, grid)
        print_grid(grid)

    # Split grid into two halves (horizontal and vertical)
    height = len(grid)
    width = len(grid[0])

    # Exclude middle row and middle column
    middle_row = height // 2
    middle_col = width // 2

    # Define quadrants
    top_left = [row[:middle_col] for row in grid[:middle_row]]
    top_right = [row[middle_col + 1:] for row in grid[:middle_row]]
    bottom_left = [row[:middle_col] for row in grid[middle_row + 1:]]
    bottom_right = [row[middle_col + 1:] for row in grid[middle_row + 1:]]

    # Count numbers in each quadrant
    sum_top_left = count_numbers(top_left)
    sum_top_right = count_numbers(top_right)
    sum_bottom_left = count_numbers(bottom_left)
    sum_bottom_right = count_numbers(bottom_right)

    # Multiply the sums of the four quadrants
    result = sum_top_left * sum_top_right * sum_bottom_left * sum_bottom_right

    # Print results
    print("Top Left Sum:", sum_top_left)
    print("Top Right Sum:", sum_top_right)
    print("Bottom Left Sum:", sum_bottom_left)
    print("Bottom Right Sum:", sum_bottom_right)
    print("Product of Quadrant Sums:", result)
