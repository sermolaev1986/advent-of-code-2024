import heapq


def print_grid(grid):
    for row in grid:
        for char in row:
            print(char, end='')
        print()


def is_valid_coordinate(row, column, grid):
    return 0 <= row < len(grid) and 0 <= column < len(grid[0])


def get_neighbours(row, column, grid):
    neighbours = [(row, column - 1), (row, column + 1), (row - 1, column), (row + 1, column)]
    return [neighbour for neighbour in neighbours if is_valid_coordinate(neighbour[0], neighbour[1], grid)]


def get_grid(failed):
    dimension = 70
    # dimension = 6

    grid = []
    for row_index in range(dimension + 1):
        row = []
        for column in range(dimension + 1):
            if (row_index, column) in failed:
                row.append('#')
            else:
                row.append('.')
        grid.append(row)

    # print_grid(grid)

    return grid


def parse_failed():
    failed = []
    with open("input/18.txt") as file:
        for line in file.readlines():
            array = line.strip().split(',')
            failed.append((int(array[1]), int(array[0])))
    return failed


def dijkstra(end_row, end_column, grid):
    priority_queue = []
    visited = set()
    heapq.heappush(priority_queue, (0, (0, 0)))

    while priority_queue:
        distance, (row, column) = heapq.heappop(priority_queue)

        if (row, column) in visited:
            continue

        visited.add((row, column))

        if row == end_row and column == end_column:
            return distance

        for neighbour_row, neighbour_column in get_neighbours(row, column, grid):
            if grid[neighbour_row][neighbour_column] != '#':
                heapq.heappush(priority_queue, (distance + 1, (neighbour_row, neighbour_column)))


def task_1(failed):
    bytes_corrupted = 1024
    # bytes_corrupted = 12

    grid = get_grid(failed[:bytes_corrupted])
    print(dijkstra(len(grid) - 1, len(grid[0]) - 1, grid))


def task_2(failed):
    range = (0, len(failed))

    while True:
        if range[1] - range[0] == 1:
            # two items left, one of them must be the answer
            grid = get_grid(failed[:range[0]])
            left = dijkstra(len(grid) - 1, len(grid[0]) - 1, grid)

            if left is None:
                index = range[0] - 1
            else:
                index = range[1] - 1

            print("{},{}".format(failed[index][1], failed[index][0]))
            break

        # take the middle
        middle = range[0] + (range[1] - range[0]) // 2
        grid = get_grid(failed[:middle])
        if dijkstra(len(grid) - 1, len(grid[0]) - 1, grid) == None:
            # must be on the left side
            range = (range[0], middle)
        else:
            # must be on the right side
            range = (middle, range[1])

if __name__ == '__main__':
    failed = parse_failed()

    task_1(failed)

    task_2(failed)
