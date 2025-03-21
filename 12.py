def get_grid():
    grid = []
    with open("input/12.txt") as file:
        for line in file.readlines():
            row = []
            for char in line:
                if char != '\n':
                    row.append(char)
            grid.append(row)
    return grid


def print_grid(grid):
    grid = get_grid()
    for row in grid:
        for char in row:
            print(char, end='')
        print()


def get_neighbours(coordinate):
    return [(coordinate[0] - 1, coordinate[1]), (coordinate[0] + 1, coordinate[1]), (coordinate[0], coordinate[1] - 1),
            (coordinate[0], coordinate[1] + 1)]


def is_coordinate_valid(coordinate, grid):
    return 0 <= coordinate[0] < len(grid) and 0 <= coordinate[1] < len(grid[0])


def get_valid_neighbours(coordinate, grid):
    return [neighbour for neighbour in get_neighbours(coordinate) if is_coordinate_valid(neighbour, grid)]


def add_to_region(region, coordinate, grid, visited):
    region.append(coordinate)
    visited.add(coordinate)
    char = row[column_index]

    for neighbour in get_valid_neighbours(coordinate, grid):
        if neighbour not in visited and grid[neighbour[0]][neighbour[1]] == char:
            add_to_region(region, neighbour, grid, visited)

def get_perimeter(region, grid):
    perimeter = 0
    for coordinate in region:
        for neighbour in get_neighbours(coordinate):
            if not is_coordinate_valid(neighbour, grid) or grid[neighbour[0]][neighbour[1]] != grid[coordinate[0]][coordinate[1]]:
                perimeter += 1
    return perimeter

def count(map):
    count = 0

    for some_list in map.values():
        points = sorted(list(some_list))
        previous = None
        for point in points:
            if previous is None or point - previous != 1:
                count += 1
            previous = point

    return count

def add_to_map(map, key, value):
    if key not in map:
        map[key] = {value}
    else:
        map[key].add(value)

def get_sides_count(region, grid):
    horizontal_map = {}
    vertical_map = {}

    for coordinate in region:
        # print("coordinate", coordinate)
        for neighbour in get_neighbours(coordinate):
            neighbour_0 = neighbour[0]
            neighbour_1 = neighbour[1]
            if not is_coordinate_valid(neighbour, grid) or grid[neighbour_0][neighbour_1] != grid[coordinate[0]][coordinate[1]]:
                # print("neighbour", neighbour)
                if coordinate[0] == neighbour_0:
                    add_to_map(vertical_map, (neighbour_1, coordinate[1] - neighbour_1),  neighbour_0)
                else:
                    add_to_map(horizontal_map, (neighbour_0, coordinate[0] - neighbour_0),  neighbour_1)

    # print()
    # print("region", grid[region[0][0]][region[0][1]])
    # print("horizontal", horizontal_map)
    # print("vertical", vertical_map)

    return  count(horizontal_map) + count(vertical_map)

if __name__ == '__main__':
    grid = get_grid()
    # print_grid(grid)

    visited = set()
    regions = []
    total = len(grid) * len(grid[0])
    while len(visited) < total:
        for row_index in range(len(grid)):
            row = grid[row_index]
            for column_index in range(len(row)):
                coordinate = (row_index, column_index)
                if coordinate not in visited:
                    region = []
                    add_to_region(region, coordinate, grid, visited)
                    regions.append(region)

    # print(regions)

    result = 0
    for region in regions:
        area = len(region)
        perimeter = get_perimeter(region, grid)
        result += area * perimeter

    print("task 1: ", result)

    result = 0
    for region in regions:
        area = len(region)
        sides = get_sides_count(region, grid)
        result += area * sides

        # print("area:", area)
        # print("sides: ", sides)

    print("task 2: ", result)



